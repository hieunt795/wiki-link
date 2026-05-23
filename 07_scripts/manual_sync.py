"""
manual_sync.py — Sync tất cả indexes mà không cần daemon.

Load BGE-M3 trực tiếp trong process, encode toàn bộ wiki nodes + raw chunks,
rồi build FAISS dense + SQLite sparse + FTS5.

Chạy:
    cd D:/AI/Wiki-agentic
    python 07_scripts/manual_sync.py

Yêu cầu:
    pip install FlagEmbedding faiss-cpu
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

WIKI_ROOT    = ROOT / "03_wiki"
SOURCES_DIR  = ROOT / "02_sources"
CACHE_DIR    = ROOT / ".cache"
CACHE_DIR.mkdir(exist_ok=True)

BATCH_SIZE   = 32  # T4: 32 | A100: 64
CHUNK_SIZE   = 4096


# ── Load model ────────────────────────────────────────────────────────────────

def load_model():
    print("[sync] Loading BAAI/bge-m3 ...")
    t0 = time.time()
    try:
        from FlagEmbedding import BGEM3FlagModel
        model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
        print(f"[sync] Model loaded in {time.time()-t0:.1f}s")
        return model
    except ImportError:
        print("[sync] ERROR: FlagEmbedding chưa cài.")
        print("       Chạy: pip install FlagEmbedding")
        sys.exit(1)


def encode_batch(model, texts: list[str]) -> dict:
    """Trả về dense_vecs (L2-normalized) và sparse_weights."""
    import numpy as np
    out = model.encode(
        texts,
        batch_size=BATCH_SIZE,
        max_length=512,
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=False,
    )
    dense = out["dense_vecs"]  # (N, 1024) float32

    # Normalize
    norms = np.linalg.norm(dense, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    dense = (dense / norms).astype("float32")

    # sparse_weights: list[dict[str, float]] từ FlagEmbedding
    sparse_raw = out.get("lexical_weights", [])
    # Chuyển token-id key → int
    sparse_weights = []
    for sw in sparse_raw:
        sparse_weights.append({int(k): float(v) for k, v in sw.items()})

    return {"dense_vecs": dense, "sparse_weights": sparse_weights}


# ── Collect documents ─────────────────────────────────────────────────────────

def collect_wiki_nodes() -> list[dict]:
    from chunker import _split_frontmatter
    docs = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        domain_field = fm.get("domain", {})
        domain = domain_field.get("primary", "") if isinstance(domain_field, dict) else str(domain_field)
        tags = fm.get("tags", [])
        docs.append({
            "node_id":    fm["node_id"],
            "stem":       md_file.stem,
            "label":      fm.get("title", md_file.stem),
            "source":     "wiki",
            "source_file": str(md_file.relative_to(ROOT)),
            "confidence": fm.get("confidence", 1),
            "tags":       tags if isinstance(tags, list) else [],
            "thesis":     fm.get("thesis", ""),
            "domain":     domain,
            "text":       body.strip(),
        })
    print(f"[sync] Collected {len(docs)} wiki nodes")
    return docs


def collect_raw_chunks() -> list[dict]:
    from chunker import chunk_markdown, _split_frontmatter
    from ingest import _guess_domain
    docs = []
    source_dirs = [SOURCES_DIR / d for d in
                   ("books", "academic", "Clipping", "deep-research", "Inbox")
                   if (SOURCES_DIR / d).exists()]
    for src_dir in source_dirs:
        for md_file in src_dir.rglob("*.md"):
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            fm, body = _split_frontmatter(text)
            domain = _guess_domain(md_file, fm)
            chunks = chunk_markdown(text, target_tokens=CHUNK_SIZE, source_file=str(md_file))
            for i, chunk in enumerate(chunks):
                docs.append({
                    "node_id":    f"raw__{md_file.stem}__{i:04d}",
                    "stem":       md_file.stem,
                    "label":      fm.get("title", md_file.stem),
                    "source":     "raw",
                    "source_file": str(md_file.relative_to(ROOT)),
                    "confidence": 0,
                    "tags":       fm.get("tags", []),
                    "thesis":     "",
                    "domain":     domain,
                    "text":       chunk.text,
                })
    print(f"[sync] Collected {len(docs)} raw chunks")
    return docs


# ── Build indexes ─────────────────────────────────────────────────────────────

def build_dense(docs: list[dict], model):
    import numpy as np
    import faiss
    from dense_index import INDEX_PATH, META_PATH, DIM
    import json

    print(f"\n[dense] Encoding {len(docs)} docs (batch={BATCH_SIZE})...")
    t0 = time.time()
    texts = [d["chunk_text"] for d in docs]
    all_dense = []

    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i:i + BATCH_SIZE]
        result = encode_batch(model, batch)
        all_dense.append(result["dense_vecs"])
        done = min(i + BATCH_SIZE, len(texts))
        elapsed = time.time() - t0
        rate = done / elapsed if elapsed > 0 else 0
        eta = (len(texts) - done) / rate if rate > 0 else 0
        print(f"  [dense] {done}/{len(texts)}  {rate:.1f} docs/s  ETA {eta/60:.1f}m", end="\r", flush=True)

    vecs = np.vstack(all_dense).astype("float32")
    print(f"\n[dense] Encoded in {time.time()-t0:.1f}s. Building FAISS...")

    index = faiss.IndexFlatIP(DIM)
    index.add(vecs)
    faiss.write_index(index, str(INDEX_PATH))

    meta = [{
        "node_id":    d.get("node_id", ""),
        "stem":       d.get("stem", ""),
        "label":      d.get("label", ""),
        "source":     d.get("source", ""),
        "source_file": d.get("source_file", ""),
        "confidence": d.get("confidence", ""),
        "thesis":     d.get("thesis", ""),
        "tags":       d.get("tags", []),
        "domain":     d.get("domain", ""),
    } for d in docs]
    META_PATH.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[dense] Done: {index.ntotal} vectors → {INDEX_PATH}")
    return vecs


def build_sparse_fts(docs: list[dict], model):
    from sparse_index import SparseIndex, FTSIndex

    sparse_idx = SparseIndex()
    fts_idx = FTSIndex()
    sparse_idx.create_tables()
    fts_idx.create_tables()

    print(f"\n[sparse] Building sparse + FTS5 for {len(docs)} docs...")
    t0 = time.time()

    for i in range(0, len(docs), BATCH_SIZE):
        batch_docs  = docs[i:i + BATCH_SIZE]
        batch_texts = [d["chunk_text"] for d in batch_docs]
        result = encode_batch(model, batch_texts)
        sparse_weights = result["sparse_weights"]

        for doc, svec in zip(batch_docs, sparse_weights):
            meta = {k: doc[k] for k in
                    ("stem", "label", "source", "source_file",
                     "confidence", "tags", "thesis", "domain")}
            sparse_idx.insert_doc(doc["node_id"], svec, meta)
            fts_idx.insert_doc(
                doc_id=doc["node_id"],
                label=doc["label"],
                thesis=doc["thesis"],
                body=doc["text"][:2000],
                tags=doc["tags"],
                source=doc["source"],
                source_file=doc["source_file"],
                confidence=str(doc["confidence"]),
                domain=doc["domain"],
                stem=doc.get("stem", ""),
            )

        done = min(i + BATCH_SIZE, len(docs))
        print(f"  [sparse] {done}/{len(docs)}", end="\r", flush=True)

    print(f"\n[sparse] Done in {time.time()-t0:.1f}s")


# ── Graph rebuild (lightweight, no model needed) ──────────────────────────────

def rebuild_graph():
    import re, json
    from chunker import _split_frontmatter
    graph_out = ROOT / "graphify-out"
    graph_out.mkdir(exist_ok=True)
    nodes, edges = [], []
    seen_edges: set[tuple[str, str]] = set()

    for md_file in WIKI_ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = _split_frontmatter(text)
        nid = fm.get("node_id")
        if not nid:
            continue
        nodes.append({"id": nid, "label": fm.get("title", md_file.stem),
                      "type": fm.get("type", "concept")})
        for target in re.findall(r"\[\[([^\]]+)\]\]", body):
            key = (nid, target)
            if key not in seen_edges:
                edges.append({"source": nid, "target": target})
                seen_edges.add(key)

    graph = {"nodes": nodes, "edges": edges}
    (graph_out / "graph.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[graph] {len(nodes)} nodes, {len(edges)} edges → graphify-out/graph.json")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    t_start = time.time()
    print("=" * 60)
    print("Wiki-Agentic Manual Sync")
    print("=" * 60)

    model = load_model()

    wiki_docs = collect_wiki_nodes()
    raw_docs  = collect_raw_chunks()
    all_docs  = wiki_docs + raw_docs

    if not all_docs:
        print("[sync] Không có documents nào. Dừng.")
        return

    for d in all_docs:
        d["chunk_text"] = d["text"]

    print(f"\n[sync] Tổng: {len(all_docs)} docs ({len(wiki_docs)} wiki + {len(raw_docs)} raw)")
    print(f"       Ước tính: ~{len(all_docs) * 20 / 60:.0f} phút trên CPU")

    # Phase 1: Dense
    build_dense(all_docs, model)

    # Phase 2: Sparse + FTS5 (re-encode — tận dụng model đang loaded)
    build_sparse_fts(all_docs, model)

    # Phase 3: Graph (không cần model)
    rebuild_graph()

    total = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"[sync] HOÀN THÀNH: {len(all_docs)} docs trong {total/60:.1f} phút")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
