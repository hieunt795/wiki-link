# Wiki Link v2 — Architecture Specification

> **Purpose**: This document is a complete build spec for Claude Code (or any coding agent).
> It describes the full repo structure, every module, data flow, and migration plan
> to rebuild the Wiki Link search system with BGE-M3 as the retrieval backbone.
>
> **Origin**: Merges three systems:
> - **QMD** (tobi/qmd) — retrieval engine patterns (RRF fusion, smart chunking, MCP)
> - **LLM Wiki** (karpathy) — knowledge management pattern (persistent wiki, ingest-query-lint)
> - **Wiki Link v1** (current) — coverage-aware KG²RAG pipeline, bilingual VI/EN
>
> **Target**: 100% local, zero LLM tokens per query, bilingual Vietnamese/English.

---

## 1. Repo structure

```
wiki-link/
├── CLAUDE.md                          ← Agent schema (LLM Wiki pattern)
├── README.md                          ← This spec (human + agent readable)
├── pyproject.toml                     ← Python package config
├── requirements.txt                   ← Pinned dependencies
│
├── 01_schema/                         ← LLM Wiki schema layer
│   ├── frontmatter.md                 ← Frontmatter convention reference
│   ├── node_types.md                  ← Node type definitions
│   └── vi_en_dictionary.yml           ← Vietnamese ↔ English domain terms
│
├── 02_sources/                        ← Raw source documents (IMMUTABLE)
│   ├── books/                         ← Extracted book markdown
│   ├── papers/                        ← Research papers
│   └── reports/                       ← Policy reports, transcripts
│
├── 03_wiki/                           ← LLM-maintained wiki (MUTABLE)
│   ├── concepts/                      ← Atomic concept nodes
│   ├── mechanisms/                    ← Process/mechanism nodes
│   ├── entities/                      ← Institution/person nodes
│   ├── relationships/                 ← Cross-concept relationship nodes
│   ├── contradictions/                ← Contradiction tracking nodes
│   ├── index.md                       ← Master index (LLM Wiki pattern)
│   └── log.md                         ← Chronological operation log
│
├── 04_outputs/                        ← Generated outputs
│   ├── drafts/                        ← DeepDive expansion proposals
│   └── exports/                       ← Agent-consumable exports
│
├── 05_scripts/                        ← All Python modules
│   ├── __init__.py
│   │
│   │   # — RETRIEVAL LAYER (BGE-M3) —
│   ├── bge_m3_daemon.py               ← Persistent BGE-M3 server (TCP 7432)
│   ├── sparse_index.py                ← BGE-M3 sparse vector index (replaces fts_index.py)
│   ├── dense_index.py                 ← FAISS index management for dense vectors
│   ├── reranker.py                    ← bge-reranker-v2-m3 cross-encoder
│   │
│   │   # — INTELLIGENCE LAYER (kept from v1) —
│   ├── search_pipeline.py             ← 4-phase KG²RAG pipeline (adapted)
│   ├── synthesis_search.py            ← Coverage probe + 3-layer search
│   ├── agentic_search.py              ← Multi-round perspective search
│   ├── graph_rag.py                   ← Knowledge graph traversal
│   ├── deepdive_search.py             ← Thin-node detection + draft gen
│   │
│   │   # — KNOWLEDGE LAYER (new, LLM Wiki pattern) —
│   ├── librarian.py                   ← CLI entry point for all operations
│   ├── ingest.py                      ← Source → wiki node pipeline
│   ├── linker.py                      ← Cross-reference maintenance
│   ├── linter.py                      ← Wiki health check
│   │
│   │   # — SHARED —
│   ├── vi_en.py                       ← Bilingual dictionary + augmentation
│   ├── chunker.py                     ← Smart markdown chunker
│   └── models.py                      ← Shared dataclasses
│
├── graphify-out/                      ← Knowledge graph (built by Obsidian Graphify)
│   └── graph.json                     ← Nodes + edges JSON
│
├── .cache/                            ← All indexes (gitignored, rebuildable)
│   ├── bge_m3_dense.index             ← FAISS flat index (1024-dim)
│   ├── bge_m3_dense_meta.json         ← Metadata per vector
│   ├── bge_m3_sparse.db              ← SQLite sparse vector store
│   ├── wiki_fts.db                    ← FTS5 index (kept as fallback/phrase search)
│   ├── reranker_cache.db              ← LRU cache for reranker scores
│   ├── gap_queue.jsonl                ← Logged coverage gaps
│   └── daemon.pid                     ← BGE-M3 daemon PID
│
└── tests/
    ├── test_search_pipeline.py
    ├── test_synthesis.py
    ├── test_bge_m3.py
    ├── benchmark_queries.py           ← 10+ domain queries for regression
    └── fixtures/
```

---

## 2. Dependencies

```
# requirements.txt
FlagEmbedding>=1.2.11        # BGE-M3 + bge-reranker-v2-m3
sentence-transformers>=2.7   # Fallback / utilities
faiss-cpu>=1.7.4             # Dense vector index
numpy>=1.26
PyYAML>=6.0
torch>=2.1                   # BGE-M3 backend (CPU or CUDA)

# Optional (improves but not required)
# faiss-gpu                  # GPU-accelerated FAISS
# onnxruntime                # ONNX inference for faster embedding
```

**Python**: ≥ 3.11 (for `dict | None` syntax, `match` statements).

**Hardware floor**: 4GB RAM minimum (BGE-M3 fp16 ~1.2GB + reranker ~1.2GB + FAISS overhead).
Recommended: 8GB RAM or any GPU with ≥ 4GB VRAM.

---

## 3. Model inventory

| Model | Role | Size (disk) | VRAM (fp16) | Output |
|-------|------|-------------|-------------|--------|
| `BAAI/bge-m3` | Embed + sparse + ColBERT | ~1.1GB (fp16) / 635MB (Q8 GGUF) | ~1.2GB | 1024-dim dense, sparse lexical weights, multi-vec |
| `BAAI/bge-reranker-v2-m3` | Cross-encoder reranker | ~1.1GB (fp16) / 635MB (Q8 GGUF) | ~1.6GB | Sigmoid relevance score [0, 1] |

**Total**: ~2.2GB fp16 / ~1.3GB quantized.
**LLM tokens per query**: zero. All inference is local embedding/classification.

**Loading strategy**: Lazy load on first query. BGE-M3 stays resident in daemon.
Reranker loads only when Phase 4 activates (top-20 candidates). Auto-unloads after
5 minutes idle to free VRAM.

---

## 4. Module specifications

### 4.1 `bge_m3_daemon.py` — Replaces `semantic_daemon.py`

**Architecture**: Persistent TCP server on `127.0.0.1:7432`. Identical lifecycle
to current `semantic_daemon.py` (PID file, anchor monitoring, auto-start on first query).

**Model loading**:
```python
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
```

**Encode protocol** (JSONL over TCP):
```json
// Request:
{
  "query": "federal funds rate",
  "mode": "all",           // "dense" | "sparse" | "colbert" | "all"
  "top_k": 10,
  "threshold": 0.30,
  "wiki_only": false,
  "raw_only": false,
  "centroid_expand": false,
  "centroid_k": 3
}

// Response:
{
  "dense_results": [...],   // FAISS search results
  "sparse_results": [...],  // Sparse dot-product results
  "colbert_score": null      // Optional, only if mode includes colbert
}
```

**Key changes from v1 `semantic_daemon.py`**:
- Model: `BGEM3FlagModel` replaces `SentenceTransformer("intfloat/multilingual-e5-base")`
- Encode call returns dict with `dense_vecs` + `lexical_weights` (+ optionally `colbert_vecs`)
- Dense vectors are 1024-dim (was 768-dim with E5-Base)
- Sparse weights from `lexical_weights` output replace FTS5 BM25 for semantic-aware lexical matching
- Centroid PRF logic remains identical — just operates on 1024-dim vectors now
- Vietnamese queries: NO `"query: "` prefix needed (BGE-M3 does not use instruction prefixes
  for encoding; E5-Base required `"query: "` prefix)

**Daemon lifecycle** — keep identical to v1:
- `cmd_start()`: subprocess with `DAEMON_ANCHOR_PID` env
- `_monitor_anchor()`: thread checks parent shell alive every 5s
- `query_daemon()`: auto-start with `_start_lock` threading

### 4.2 `sparse_index.py` — Replaces `fts_index.py` BM25 role

**Purpose**: Store and query BGE-M3's learned sparse lexical weights.
These are NOT traditional BM25 — they are neural-learned token weights that
capture semantic importance, produced alongside dense vectors in the same forward pass.

**Storage**: SQLite table with inverted index structure.

```sql
CREATE TABLE sparse_postings (
    token_id   INTEGER,          -- BGE-M3 vocabulary token ID
    doc_id     TEXT,             -- node_id (same as FAISS metadata)
    weight     REAL,             -- BGE-M3 lexical weight for this token in this doc
    source     TEXT,             -- 'wiki' | 'raw'
    PRIMARY KEY (token_id, doc_id)
);
CREATE INDEX idx_sparse_token ON sparse_postings(token_id);
CREATE INDEX idx_sparse_doc ON sparse_postings(doc_id);

CREATE TABLE sparse_meta (
    doc_id      TEXT PRIMARY KEY,
    stem        TEXT,
    label       TEXT,
    source      TEXT,
    source_file TEXT,
    confidence  TEXT,
    tags        TEXT,
    thesis      TEXT
);
```

**Build** (`build()`):
1. Iterate all docs from `03_wiki/` and `02_sources/`
2. Encode each chunk via BGE-M3 daemon with `mode="sparse"`
3. Extract non-zero entries from `lexical_weights` dict
4. Insert into `sparse_postings` table

**Query** (`query_sparse(query, top_k, wiki_only, raw_only)`):
1. Encode query via daemon with `mode="sparse"`
2. For each non-zero query token, lookup matching docs in `sparse_postings`
3. Score = dot product of query sparse vector × doc sparse vector
4. Sort by score descending, return top_k

**Why keep FTS5 alongside**:
FTS5 (`wiki_fts.db`) is still needed for:
- Exact phrase matching (`synthesis_search.probe()` uses `MATCH '"yield curve"'`)
- Label column matching for INGESTED/PENDING classification
- Fast `_label_hits()` and `_label_token_coverage()` checks
- These are string operations that sparse vectors don't handle well

So `fts_index.py` is NOT deleted — it is demoted from "primary retrieval" to
"phrase matching + coverage probe utility". Its BM25 ranking role is replaced
by BGE-M3 sparse.

### 4.3 `dense_index.py` — FAISS index management

**Extracted from `semantic_daemon.py`** into standalone module.

```python
import faiss
import numpy as np
import json

class DenseIndex:
    def __init__(self, index_path, meta_path):
        self.index = faiss.read_index(str(index_path))
        self.meta = json.loads(meta_path.read_text("utf-8"))

    def search(self, query_vec, top_k=10, threshold=0.30,
               wiki_only=False, raw_only=False):
        """Search FAISS index. Returns list of (score, meta_dict)."""
        ...

    def reconstruct(self, idx):
        """Reconstruct vector for centroid PRF."""
        return self.index.reconstruct(int(idx))

    @staticmethod
    def build(docs: list[dict], model, index_path, meta_path):
        """Build FAISS flat index from document list.
        Uses model.encode() with return_dense=True."""
        ...
```

**Index type**: `faiss.IndexFlatIP` (inner product, since BGE-M3 outputs L2-normalized vectors).
**Dimensions**: 1024 (BGE-M3 dense output).
**Migration note**: Rebuild required — old 768-dim E5-Base index is incompatible.

### 4.4 `reranker.py` — Replaces handcrafted Phase 4 scoring

```python
from FlagEmbedding import FlagReranker

class CrossEncoderReranker:
    def __init__(self, model_name="BAAI/bge-reranker-v2-m3", use_fp16=True):
        self._reranker = None    # lazy load
        self._model_name = model_name
        self._use_fp16 = use_fp16

    def _ensure_loaded(self):
        if self._reranker is None:
            self._reranker = FlagReranker(self._model_name, use_fp16=self._use_fp16)

    def rerank(self, query: str, candidates: list[SearchResult],
               top_k: int = 10) -> list[SearchResult]:
        """
        Cross-encoder rerank. Scores each (query, candidate.body) pair.
        Returns candidates sorted by reranker score.
        Applies confidence multiplier AFTER reranker score (trust hierarchy preserved).
        """
        self._ensure_loaded()
        pairs = [[query, c.body[:512] or c.thesis[:512] or c.label]
                 for c in candidates]
        scores = self._reranker.compute_score(pairs, normalize=True)

        for c, score in zip(candidates, scores):
            # Confidence multiplier (from v1 Phase 4)
            try:
                conf = int(c.confidence) if c.confidence else 0
            except ValueError:
                conf = 0
            conf_mult = 1.0 + conf * 0.05  # conf=5 → 1.25×

            # [LLM] penalty (from v1)
            if "[LLM]" in c.thesis or "[LLM]" in (c.body[:200] if c.body else ""):
                conf_mult *= 0.4

            c.score = score * conf_mult

        candidates.sort(key=lambda x: -x.score)
        return candidates[:top_k]
```

**Caching**: Store `(query_hash, doc_hash) → score` in `reranker_cache.db` (SQLite).
Cache hit rate expected ~30-50% for repeated queries on static corpus.
TTL: clear on `librarian.py sync` (corpus changed).

### 4.5 `search_pipeline.py` — Adapted Phase 1, kept Phases 2-3-4

**Phase 1 SEED** — rewritten to use BGE-M3 daemon:

```python
def phase1_seed(query, top=50, wiki_only=False, raw_only=False):
    """
    3-way retrieval → RRF merge.

    1. BGE-M3 dense search (via daemon, mode="dense") → rank list
    2. BGE-M3 sparse search (via daemon, mode="sparse") → rank list
    3. FTS5 phrase/label (via fts_index, kept for exact match) → rank list
    4. RRF fusion with k=60 across all 3 lists
    """
    dense_results = daemon.query(query, mode="dense", top_k=top*2, ...)
    sparse_results = daemon.query(query, mode="sparse", top_k=top*2, ...)
    fts_results = fts_index.query_fts(query, top=top*2, ...)

    # RRF merge (3-way)
    K = 60
    scores = defaultdict(float)
    for rank_i, (stem, r) in enumerate(dense_results):
        scores[stem] += 1.0 / (K + rank_i + 1)
    for rank_i, (stem, r) in enumerate(sparse_results):
        scores[stem] += 1.0 / (K + rank_i + 1)
    for rank_i, (stem, r) in enumerate(fts_results):
        scores[stem] += 1.0 / (K + rank_i + 1)

    # ... merge node_data, return top-N SearchResult list
```

**Speculative skip** (adapted):
- If sparse search returns top-1 with score > 0.8 AND the stem matches
  a wiki label exactly → skip dense search (saves ~20ms).
- Much less aggressive than v1 FTS5 skip because sparse is already semantic-aware.

**Phase 2 EXPAND** — no changes. Operates on SearchResult objects regardless of
how Phase 1 produced them. Graph adjacency, convergence scoring, all identical.

**Phase 3 CHAIN** — no changes. BFS path finding on graph.json, bridge node scoring.

**Phase 4 RERANK** — replaced by `reranker.py`:
```python
def phase4_rerank(query, seeds, expanded, chains, top=10):
    # Merge all candidates, dedup by stem
    candidates = _merge_dedup(seeds, expanded, chains)

    # Cross-encoder rerank (top-20 only, cost control)
    reranker = CrossEncoderReranker()
    return reranker.rerank(query, candidates[:20], top_k=top)
```

**Gap detection + centroid fallback** — kept from v1. `_gap_score()` unchanged.
Centroid PRF now uses 1024-dim vectors from BGE-M3 dense output.

### 4.6 `synthesis_search.py` — Minimal changes

**`probe()`** — identical logic, different backends:
- `query_daemon()` now calls BGE-M3 daemon (dense mode) instead of E5-Base daemon
- `query_fts()` unchanged (still FTS5 for phrase counts + label matching)
- State classifier logic (INGESTED/PENDING/TRUE_GAP) unchanged

**`expand()`** — `_semantic_anchors()` uses BGE-M3 daemon instead of E5-Base.

**All layers (L1/L2/L3)** — call updated `search_pipeline` which internally uses BGE-M3.
No changes to layer logic.

### 4.7 `agentic_search.py` — No changes

- `plan_perspectives()`: unchanged (5 fixed lenses)
- `_batch_pipeline()`: ThreadPoolExecutor calls to `search_pipeline`
- `evaluate_coverage()`: unchanged thresholds
- `reformulate_queries()`: unchanged (acronym expansion, neighbor drilling)

All changes are internal to `search_pipeline.py` which agentic_search calls.

### 4.8 `vi_en.py` — Extracted from search_pipeline.py

Extract the Vietnamese-English bilingual logic into standalone module:

```python
# vi_en.py — Bilingual Vietnamese ↔ English domain dictionary

_VI_EN: dict[str, list[str]] = { ... }   # ~40 term pairs from v1
_VI_TOKEN_MAP: dict[str, list[str]] = {}  # reverse map
_VI_CHARS = set("àáâã...ỹ")              # tone-marked chars

def is_vietnamese(text: str) -> bool: ...
def vi_augment(query: str) -> str: ...
def load_dictionary(path: Path) -> None: ...  # load from 01_schema/vi_en_dictionary.yml
```

**Dictionary file** (`01_schema/vi_en_dictionary.yml`):
```yaml
# Vietnamese → English domain term mapping
# Used by synthesis_search probe + search_pipeline query augmentation
terms:
  "lãi suất": ["interest rate"]
```

This makes the dictionary maintainable outside code.

### 4.9 `chunker.py` — Smart markdown chunker (new, inspired by QMD)

Extract chunking logic from `fts_index.py` `_iter_documents()` and enhance
with QMD's smart boundary detection:

```python
def chunk_markdown(text: str, target_tokens: int = 900,
                   overlap_pct: float = 0.15) -> list[dict]:
    """
    Smart chunk markdown with QMD-style break point scoring.

    Break scores:
      # H1 = 100, ## H2 = 90, ### H3 = 80, #### = 70
      ``` code fence = 80
      --- / *** horizontal rule = 60
      blank line = 20
      - list item = 5
      line break = 1

    Algorithm:
      1. Scan for all break points with scores
      2. At 900-token target, search 200-token window before cutoff
      3. Score = baseScore × (1 - (distance/window)^2 × 0.7)
      4. Cut at highest-scoring break point

    Code fence protection: break points inside code blocks are ignored.

    Returns list of {text, heading, position, token_count}.
    """
```

### 4.10 `models.py` — Shared dataclasses

```python
from dataclasses import dataclass

@dataclass
class SearchResult:
    node_id:     str
    stem:        str
    label:       str
    source_file: str
    source:      str          # "wiki" | "raw"
    confidence:  str
    thesis:      str
    tags:        list
    score:       float
    found_by:    str          # "dense", "sparse", "fts", "kg_expand:X", "chain:A→B"
    body:        str = ""
    heatmap_ctx: str = ""

@dataclass
class Probe:
    state:        str         # INGESTED | PENDING | TRUE_GAP
    wiki_sem:     float
    wiki_fts:     float
    raw_sem:      float
    raw_fts:      float
    phrase_wiki:  int
    phrase_raw:   int
    label_hits:   int
    label_cov:    float
    elapsed_ms:   int
```

### 4.11 `librarian.py` — CLI entry point

```
Usage:
  python librarian.py sync              # Rebuild FTS5 + sparse + dense indexes
  python librarian.py embed             # Build FAISS dense index only
  python librarian.py search "query"    # search_pipeline (default)
  python librarian.py synth "query"     # synthesis_search with coverage probe
  python librarian.py agentic "query"   # Multi-round agentic search
  python librarian.py deep "query"      # DeepDive thin-node detection
  python librarian.py ingest <file>     # Ingest raw source → wiki node
  python librarian.py lint              # Wiki health check
  python librarian.py status            # Index status + daemon status
  python librarian.py daemon start|stop|status
```

### 4.12 Knowledge layer modules (LLM Wiki pattern)

**`ingest.py`** — Source → wiki node pipeline:
- Read raw source from `02_sources/`
- Extract frontmatter, split into chunks
- (Optional, requires LLM) Generate wiki node draft with thesis, source_refs
- Write to `03_wiki/concepts/{slug}.md` with frontmatter
- Update `03_wiki/index.md`
- Append to `03_wiki/log.md`
- Trigger `librarian.py sync` to rebuild indexes

**`linker.py`** — Cross-reference maintenance:
- Scan all wiki nodes for `[[wikilink]]` syntax
- Detect broken links (target doesn't exist)
- Suggest missing links (semantic similarity > threshold between unlinked nodes)
- Update graph.json (or trigger Graphify rebuild)

**`linter.py`** — Wiki health check:
- Thin nodes: confidence ≤ 2, body contains `[LLM]`, no `source_refs`
- Orphan pages: no inbound links from other wiki pages
- Stale claims: `source_refs` point to files no longer in `02_sources/`
- Missing pages: concepts mentioned in body but no dedicated node
- Contradiction candidates: nodes with conflicting thesis on same topic

---

## 5. Data flow

### 5.1 Search flow (zero tokens)

```
User query (VI or EN)
    │
    ├─► vi_en.vi_augment() if Vietnamese detected
    │
    ▼
synthesis_search.probe()        ← ~80ms, FTS5 + BGE-M3 dense
    │
    ├─ INGESTED → search_pipeline(wiki_only=True)
    ├─ PENDING  → search_pipeline(raw_only=True)
    └─ TRUE_GAP → stop, log to gap_queue.jsonl
         │
         ▼
search_pipeline()               ← ~400-600ms total
    │
    ├─ Phase 1: SEED
    │   ├─ BGE-M3 dense search (daemon, 1024-dim FAISS)
    │   ├─ BGE-M3 sparse search (daemon, inverted index)
    │   ├─ FTS5 phrase/label match (sqlite, exact match)
    │   └─ RRF fusion (k=60, 3-way merge)
    │
    ├─ Phase 2: EXPAND
    │   └─ KG 1-hop neighbors, convergence scoring
    │
    ├─ Phase 3: CHAIN
    │   └─ BFS bridge nodes between seed clusters
    │
    └─ Phase 4: RERANK
        ├─ bge-reranker-v2-m3 cross-encoder (top-20)
        ├─ × confidence multiplier (1-5 → 1.05-1.25×)
        ├─ × [LLM] penalty (0.4×)
        └─ → final ranked results

    [If gap_score > 0.40]
        └─ Centroid PRF: re-search with centroid vector
```

### 5.2 Index build flow

```
librarian.py sync
    │
    ├─ 1. Scan 03_wiki/**/*.md + 02_sources/**/*.md
    ├─ 2. chunker.chunk_markdown() each file (900 tokens, smart breaks)
    ├─ 3. BGE-M3 encode all chunks (mode="all")
    │      ├─ dense_vecs  → FAISS IndexFlatIP → .cache/bge_m3_dense.index
    │      ├─ sparse_wts  → SQLite inverted   → .cache/bge_m3_sparse.db
    │      └─ metadata    → JSON              → .cache/bge_m3_dense_meta.json
    ├─ 4. FTS5 index rebuild                  → .cache/wiki_fts.db
    └─ 5. Clear reranker cache                → .cache/reranker_cache.db
```

### 5.3 Ingest flow (LLM Wiki pattern — uses LLM tokens)

```
librarian.py ingest <raw_source.md>
    │
    ├─ 1. Read raw source, extract key information
    ├─ 2. [LLM] Generate wiki node draft (thesis, body, source_refs)
    ├─ 3. Write 03_wiki/concepts/{slug}.md with frontmatter:
    │      ---
    │      type: concept
    │      confidence: 3          ← based on source quality
    │      aliases: [QE, LSAP]
    │      tags: [monetary-policy, unconventional]
    │      source_refs:
    │        - 02_sources/books/bernanke_ch4.md
    │      ---
    ├─ 4. Update 03_wiki/index.md (add entry)
    ├─ 5. Append to 03_wiki/log.md
    ├─ 6. [LLM] Update related wiki nodes (cross-references)
    └─ 7. Trigger librarian.py sync
```

---

## 6. Wiki node frontmatter convention

```yaml
---
type: concept                    # concept | mechanism | definition | entity |
                                 # relationship | contradiction | synthesis |
                                 # convention | perspective | glossary | domain
confidence: 4                   # 1-5 trust scale:
                                 #   5 = multiple primary textbooks
                                 #   4 = single primary textbook
                                 #   3 = reliable secondary source
                                 #   2 = LLM synthesis with some source backing
                                 #   1 = LLM stub, no source verification
title: Quantitative Easing
aliases: [QE, LSAP, large-scale asset purchases]
tags: [monetary-policy, unconventional, central-bank]
thesis: >
  QE expands the central bank's balance sheet by purchasing long-term
  securities, lowering long-term yields and easing financial conditions.
source_refs:
  - 02_sources/books/bernanke_monetary_policy_ch4.md
  - 02_sources/papers/borio_2019_unconventional.md
related:
  - [[Interest_Rate_Channel]]
  - [[Portfolio_Balance_Effect]]
  - [[Reserve_Requirements]]
date_created: 2025-01-15
date_updated: 2025-03-22
---
```

---

## 7. CLAUDE.md — Agent schema

Place at repo root. This is what the coding agent / LLM reads to understand
how to operate the wiki.

```markdown
# Wiki Link — Agent Operating Manual

## What this is
A bilingual (Vietnamese/English) macroeconomics knowledge base with hybrid search.
You maintain this wiki. The search system is fully local (BGE-M3, no API keys).

## Directory layout
- `02_sources/` — Raw source documents. NEVER modify these.
- `03_wiki/` — Wiki nodes you maintain. Create, update, cross-reference here.
- `04_outputs/drafts/` — DeepDive expansion proposals. Review and action these.
- `05_scripts/` — Search and maintenance scripts. Do not modify without review.

## Frontmatter rules
Every wiki node MUST have: type, confidence (1-5), title, aliases, tags, thesis, source_refs.
See 01_schema/frontmatter.md for full specification.

## Operations

### Search (read-only, zero tokens)
- `python librarian.py search "query"` — 4-phase KG²RAG search
- `python librarian.py synth "query"` — Coverage-aware search (probe first)
- `python librarian.py agentic "query"` — Multi-round perspective search

### Ingest (creates wiki nodes)
1. Drop source file into `02_sources/`
2. Run `python librarian.py ingest 02_sources/path/to/file.md`
3. Review generated node in `03_wiki/`
4. Adjust confidence, verify source_refs
5. Run `python librarian.py sync` to rebuild indexes

### Maintenance
- `python librarian.py lint` — Find thin nodes, orphans, broken links
- `python librarian.py deep "topic"` — Deep dive: find what needs ingesting
- After any wiki changes: `python librarian.py sync`

## Rules
1. NEVER modify files in `02_sources/` — they are immutable raw sources.
2. Every wiki node MUST cite at least one source_ref.
3. Set confidence honestly: 1 if you generated it without source verification.
4. Keep aliases up to date — search quality depends on them.
5. After creating/updating nodes, always run `librarian.py sync`.
6. When you find contradictions between sources, create a contradiction node.
```

---

## 8. Migration checklist

### Phase A: Extract and restructure (no functional change)

- [ ] Create repo structure as specified in §1
- [ ] Extract `_VI_EN` dict from `search_pipeline.py` → `vi_en.py` + `01_schema/vi_en_dictionary.yml`
- [ ] Extract `SearchResult` + `Probe` dataclasses → `models.py`
- [ ] Extract `_GraphCache` class → keep in `search_pipeline.py` or move to `graph_rag.py`
- [ ] Create `chunker.py` from `fts_index.py:_iter_documents()` + QMD smart break logic
- [ ] Write `CLAUDE.md` agent schema
- [ ] Write `01_schema/frontmatter.md` and `01_schema/node_types.md`
- [ ] All existing tests must still pass

### Phase B: BGE-M3 integration (core swap)

- [ ] Implement `bge_m3_daemon.py` (copy lifecycle from `semantic_daemon.py`, swap model)
- [ ] Implement `dense_index.py` (extract FAISS logic from `semantic_daemon.py`)
- [ ] Implement `sparse_index.py` (new, BGE-M3 lexical weights → SQLite inverted index)
- [ ] Implement `reranker.py` (bge-reranker-v2-m3 with confidence multiplier)
- [ ] Update `search_pipeline.py` Phase 1: 3-way RRF (dense + sparse + FTS5)
- [ ] Update `search_pipeline.py` Phase 4: call `reranker.py` instead of handcrafted scoring
- [ ] Update `synthesis_search.py` probe: use BGE-M3 daemon
- [ ] Update `librarian.py sync`: rebuild sparse + dense + FTS5
- [ ] Rebuild all indexes: `librarian.py sync`
- [ ] Run benchmark: `python search_pipeline.py --benchmark`
- [ ] Verify latency targets: Phase 1 < 100ms warm, full pipeline < 600ms

### Phase C: Knowledge layer (LLM Wiki pattern)

- [ ] Create `03_wiki/index.md` master index
- [ ] Create `03_wiki/log.md` operation log
- [ ] Implement `ingest.py` (source → wiki node)
- [ ] Implement `linker.py` (cross-reference maintenance)
- [ ] Implement `linter.py` (wiki health check)
- [ ] Wire into `librarian.py` CLI
- [ ] Test full ingest cycle: raw source → wiki node → index rebuild → search verifies

### Phase D: Quality and polish

- [ ] Write `tests/test_bge_m3.py` — daemon start/stop, encode, search
- [ ] Write `tests/test_search_pipeline.py` — 10 benchmark queries regression
- [ ] Write `tests/test_synthesis.py` — probe state classification accuracy
- [ ] Add `--json` output to all search commands
- [ ] Add `librarian.py status` showing index freshness, daemon status, coverage stats
- [ ] Write README.md for public consumption

---

## 9. Performance targets

| Operation | Target | Notes |
|-----------|--------|-------|
| BGE-M3 encode (warm) | < 50ms per query | Single query, fp16 |
| Sparse search | < 10ms | SQLite inverted index |
| Dense search (FAISS flat) | < 5ms | 1024-dim, ~3000 vectors |
| FTS5 phrase match | < 5ms | Kept for exact matching |
| Phase 1 SEED (3-way RRF) | < 100ms | Warm daemon |
| Phase 2 EXPAND | < 20ms | In-memory graph traversal |
| Phase 3 CHAIN | < 30ms | BFS on adjacency list |
| Phase 4 RERANK | < 200ms | Cross-encoder on top-20 |
| Full pipeline | < 500ms | All 4 phases |
| Synthesis probe | < 120ms | FTS5 + dense only |
| Agentic (1 round) | < 3s | 6 parallel pipeline calls |
| Cold start (first query) | < 30s | BGE-M3 model load |
| Index rebuild | < 60s | ~3000 documents |

---

## 10. Design principles (inherited + new)

1. **Zero LLM tokens for search.** All retrieval is local: BGE-M3 (dense + sparse),
   FAISS, FTS5, graph traversal, cross-encoder reranker. No API key needed.

2. **Partial ingest is the normal state.** System designed around ~11% wiki coverage.
   Raw sources are a peer retrieval layer, not a fallback.

3. **Coverage state before search.** `synthesis_search.probe()` costs ~120ms and
   prevents wasted search effort on TRUE_GAP queries.

4. **Trust signals from ingest.** Confidence (1-5) encodes source quality.
   Reranker applies confidence multiplier. Agents inherit this trust hierarchy.

5. **One model, three retrieval modes.** BGE-M3 produces dense + sparse + ColBERT
   in a single forward pass. No separate BM25 engine, no separate embedding model.

6. **Knowledge compounds.** LLM Wiki pattern: wiki nodes accumulate and interlink.
   Each ingest enriches the graph. Search quality improves with coverage.

7. **Bilingual native.** BGE-M3 supports 100+ languages natively. VI→EN dictionary
   augments FTS5 exact matching. No translation API needed.

8. **Corpus-bootstrapped expansion.** Centroid PRF, KG neighbor drilling, and
   agentic lenses all use the existing corpus — no external API.
