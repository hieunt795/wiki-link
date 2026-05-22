# Wiki Link — Search Architecture

A hybrid search system for a bilingual (Vietnamese/English) macroeconomics knowledge base.
Built to handle a **partially-ingested corpus**: ~11% of raw sources have been converted
into structured wiki nodes; the remaining 89% exists only as raw book extracts.

---

## Contents

| File | Role |
|------|------|
| `fts_index.py` | SQLite FTS5 index builder — indexes wiki nodes + raw sources |
| `semantic_daemon.py` | Persistent E5-Base embedding server + Centroid PRF |
| `search_pipeline.py` | Core 4-phase search engine (KG²RAG) |
| `synthesis_search.py` | Coverage-aware 3-state/3-layer search |
| `agentic_search.py` | Multi-round agentic search with query reformulation |
| `deepdive_search.py` | Thin-node detection + draft generation for maintenance |
| `graph_rag.py` | Knowledge graph traversal, BFS expansion, path finding |

---

## System Overview

```text
User query
    │
    ▼
┌──────────────────────────────────────────────────────────────┐
│  synthesis_search  (coverage probe — run first)              │
│  probe(query) → INGESTED / PENDING / TRUE_GAP                │
│  Routes to correct search layer before any retrieval         │
└──────────────────────────────────────────────────────────────┘
                 │
    ┌────────────┼──────────────┬──────────────┐
    ▼            ▼              ▼
 INGESTED     PENDING       TRUE_GAP
    │            │             │
search_pipeline  search_pipeline  stop
 (wiki_only)    (raw_only)
    │            │
    └──────┬──────┘
           ▼
┌──────────────────────────────────────────────────────────────┐
│  search_pipeline  (4-phase KG²RAG)                           │
│                                                              │
│  Phase 1 SEED    FTS5 + Semantic → RRF merge                │
│  Phase 2 EXPAND  KG graph 1-hop neighbors                   │
│  Phase 3 CHAIN   Bridge between seed clusters               │
│  Phase 4 RERANK  BM25 field-boost + confidence score        │
└──────────────────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────────────────────────┐
│  agentic_search  (optional — when results are thin)         │
│  5 analytical lenses → parallel search_pipeline             │
│  Coverage eval → reformulate queries (max 2 rounds)         │
└──────────────────────────────────────────────────────────────┘
```

---

## Component Deep-Dive

### 1. FTS Index (`fts_index.py`)

SQLite FTS5 index over two corpus layers:

- **Wiki layer** (`03_wiki/**/*.md`): Structured atomic nodes with frontmatter fields
  `title`, `thesis`, `body`, `aliases`, `type`, `confidence`, `tags`, `source_refs`.
  Field boosting on query: `title^5 · thesis^4 · body^1`.

- **Raw layer** (`02_sources/**/*.md`): Extracted book/report markdown. Indexed as
  flat text chunks. No structured fields — body only.

Both layers share one FTS5 table (`wiki_fts`) with a `source` discriminator column
(`wiki` | `raw`). This allows a single query to search both simultaneously and filter
by source at query time.

**Why SQLite FTS5 over Elasticsearch/Typesense:**
No infrastructure dependency. The entire index is a single `.cache/wiki_fts.db` file
that rebuilds in ~2s on `librarian.py sync`. Works offline, no server process needed.

---

### 2. Semantic Daemon (`semantic_daemon.py`)

**Model:** `intfloat/multilingual-e5-base` (559M params, 768-dim, supports EN+VI).

**Architecture:** Persistent TCP server (port 7432). Loads model once at first query,
serves subsequent queries over a socket. Eliminates the 15s cold-start penalty that
would otherwise hit every search call.

**Centroid PRF (Pseudo-Relevance Feedback):**

Standard query → top-k results → compute centroid of result vectors + query vector →
re-search with centroid. This shifts the query vector toward the cluster of relevant
documents in embedding space.

```python
# centroid = mean(query_vec, result_vec_1, ..., result_vec_k)
all_vecs = np.vstack([query_vec, seed_vecs])
centroid = np.mean(all_vecs, axis=0, keepdims=True)
centroid /= np.linalg.norm(centroid)   # re-normalise for cosine similarity
```

**Why Centroid PRF instead of HyDE:**
HyDE (Hypothetical Document Embeddings) requires an LLM API call per query to generate
a fake document. Centroid PRF achieves similar vocabulary expansion using only the
existing FAISS index — no API key, no latency spike, no cost per query.

**Limitation:** Centroid PRF only expands toward concepts already in the index.
For TRUE_GAP queries (concept not in corpus) it adds noise rather than signal.
`synthesis_search.py` detects this case and skips the expansion step.

---

### 3. Search Pipeline (`search_pipeline.py`)

4-phase KG²RAG pipeline inspired by HippoRAG and KG²RAG patterns.

#### Phase 1 — SEED (FTS5 + Semantic → RRF)

Runs FTS5 BM25 and semantic search in parallel, merges with Reciprocal Rank Fusion:

```text
RRF score(d) = Σ  1 / (k + rank_i(d))   where k=3
```

**Why RRF over score normalisation:**
BM25 and cosine similarity live on incompatible scales. RRF uses rank position only,
making fusion scale-invariant. k=3 (vs the typical k=60) because the corpus is small
(~3,000 nodes) — a lower k gives more weight to top ranks.

**Speculative skip:** If FTS5 returns a confident result (phrase match + confidence ≥ 4),
semantic search is skipped. This saves 80ms for common queries that hit exact labels.

#### Phase 2 — EXPAND (KG Graph 1-hop)

For each seed node, load its graph neighbors from `graph.json` (built by Obsidian
Graphify / `_build_wiki_graph.py`). Score neighbors using convergence:

```text
convergence_score(n) = number of distinct seed nodes that are neighbors of n
```

Nodes that appear as neighbors of multiple seeds score higher — this surfaces
"hub" concepts that tie together the query's components.

#### Phase 3 — CHAIN (Bridge Nodes)

Uses BFS on the graph (`graph_rag.py`) to find shortest paths between seed node
clusters that are semantically related but not directly connected. Bridge nodes
on those paths are injected into the result set.

#### Phase 4 — RERANK

```text
final_score = rrf_score
            × field_boost          (title match > thesis match > body match)
            × confidence_factor    (conf 5 → 1.5×, conf 1 → 0.5×)
            × community_factor     (same Louvain community as top-1 seed → 1.2×)
```

---

### 4. Synthesis Search (`synthesis_search.py`)

**Problem it solves:** With only 11% of raw sources ingested, a standard search that
only queries wiki nodes will fail on most topics — not because the knowledge base
doesn't have the information, but because it hasn't been ingested yet. This is the
normal state of the system, not an edge case.

**3-state probe (runs in ~80-150ms before any search):**

```text
INGESTED   → wiki has a dedicated node for this concept
PENDING    → concept exists in raw sources but no wiki node yet
TRUE_GAP   → concept is not in the corpus at all
```

**3-layer result structure:**

```text
L1 PROCESSED   Wiki nodes directly matching the query  (search_pipeline wiki_only)
L2 ADJACENT    Graph neighbors + phrase mentions in wiki body
L3 UNPROCESSED Raw source chunks (search_pipeline raw_only)
```

---

### 5. Agentic Search (`agentic_search.py`)

Multi-round search for complex, broad, or ambiguous queries.

**Round 0 — Perspective decomposition:**

Five fixed analytical lenses:

```text
Policy    → ["policy", "regulation", "regime"]
Macro     → ["inflation", "growth", "macro"]
Plumbing  → ["liquidity", "mechanism", "transmission"]
Treasury  → ["yield", "market", "pricing"]
Timing    → ["historical", "cycle", "evolution"]
```

**Round 1 — Coverage evaluation**

If sufficient → output. If not → Round 2.

**Round 2 — Reformulation**

Two strategies:
1. Acronym expansion using wiki aliases
2. Neighbor drilling using labels of top Round 1 hits

---

### 6. DeepDive Search (`deepdive_search.py`)

**Purpose:** wiki maintenance, not research.

**Pipeline:**

```text
Stage 1  DETECT   search_pipeline wiki_only → classify each hit as THIN or SOLID
Stage 2  DRILL    search_pipeline raw_only + heatmap → find source evidence for thin nodes
Stage 3  DRAFT    save structured expansion proposal to 04_outputs/drafts/
```

---

## Performance

| Operation | Typical latency | Notes |
|-----------|----------------|-------|
| FTS5 query | ~5ms | SQLite BM25 |
| Semantic query (warm daemon) | ~30ms | FAISS flat search |
| Semantic query (cold start) | ~15s | Model load, first call only |
| Centroid PRF | +20ms | Two FAISS searches |
| Full `search_pipeline` | ~400-600ms | All 4 phases |
| `synth` probe | ~80-150ms | FTS5 only if daemon warm |
| `agentic` (1 round) | ~1-3s | 6 parallel pipeline calls |

---

## Design Principles

1. No API key required for core search.
2. Partial ingest is the normal state, not a degraded state.
3. Coverage state before search.
4. Trust signals from the ingest process.
5. Corpus-bootstrapped query expansion.

