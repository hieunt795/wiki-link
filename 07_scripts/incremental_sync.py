"""incremental_sync.py — Encode only wiki nodes not yet in the dense index.

Appends new vectors to existing FAISS index and upserts into sparse/FTS SQLite.
Run from repo root: python 07_scripts/incremental_sync.py
"""

import json
import re
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

DENSE_INDEX_PATH = ROOT / ".cache" / "bge_m3_dense.index"
DENSE_META_PATH  = ROOT / ".cache" / "bge_m3_dense_meta.json"
WIKI_ROOT        = ROOT / "03_wiki"

IGNORED_FILES = {"index.md", "log.md"}


def read_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields we need (regex, no yaml dep required)."""
    import yaml
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def collect_new_wiki_nodes(existing_ids: set) -> list[dict]:
    """Collect wiki nodes whose node_id is not yet in the index."""
    docs = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in IGNORED_FILES:
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm = read_frontmatter(text)
        node_id = fm.get("node_id")
        if not node_id or node_id in existing_ids:
            continue

        # Extract body (after frontmatter)
        body_match = re.match(r"^---\s*\n.*?\n---\s*\n(.*)", text, re.DOTALL)
        body = body_match.group(1).strip() if body_match else ""

        # Build chunk_text: thesis + body (truncated)
        thesis = fm.get("thesis", "")
        if isinstance(thesis, dict):
            thesis = str(thesis)
        chunk_text = f"{fm.get('title', '')}. {thesis} {body}"[:2000]

        # Tags normalised to list of strings
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        tags = [str(t) for t in (tags or [])]

        # Domain normalised
        domain = fm.get("domain", {})
        if isinstance(domain, dict):
            domain_str = domain.get("primary", "general")
        else:
            domain_str = str(domain) if domain else "general"

        docs.append({
            "node_id":    node_id,
            "stem":       md_file.stem,
            "label":      str(fm.get("title", md_file.stem)),
            "source":     "wiki",
            "source_file": str(md_file.relative_to(ROOT)),
            "confidence": str(fm.get("confidence", 1)),
            "thesis":     str(thesis)[:500],
            "tags":       tags,
            "domain":     domain_str,
            "chunk_text": chunk_text,
            "text":       chunk_text,
        })
    return docs


def append_to_dense(docs: list[dict], encode_fn) -> None:
    import faiss

    print(f"[incr] Loading existing FAISS index from {DENSE_INDEX_PATH} ...")
    index = faiss.read_index(str(DENSE_INDEX_PATH))
    print(f"[incr] Existing vectors: {index.ntotal}")

    # Load existing meta
    meta = json.loads(DENSE_META_PATH.read_text("utf-8"))

    # Encode new docs
    print(f"[incr] Encoding {len(docs)} new docs ...")
    texts = [d["chunk_text"] for d in docs]
    result = encode_fn(texts)
    vecs = np.array(result["dense_vecs"], dtype="float32")

    # Append to FAISS
    index.add(vecs)
    faiss.write_index(index, str(DENSE_INDEX_PATH))
    print(f"[incr] FAISS now has {index.ntotal} vectors.")

    # Append to meta
    for d in docs:
        meta.append({
            "node_id":    d["node_id"],
            "stem":       d["stem"],
            "label":      d["label"],
            "source":     d["source"],
            "source_file": d["source_file"],
            "confidence": d["confidence"],
            "thesis":     d["thesis"],
            "tags":       d["tags"],
            "domain":     d["domain"],
        })
    DENSE_META_PATH.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    print(f"[incr] Meta updated: {len(meta)} entries.")


def upsert_sparse_fts(docs: list[dict], encode_fn) -> None:
    from sparse_index import SparseIndex, FTSIndex

    sparse_idx = SparseIndex()
    fts_idx    = FTSIndex()
    sparse_idx.create_tables()
    fts_idx.create_tables()

    print(f"[incr] Upserting {len(docs)} docs into sparse + FTS5 ...")
    batch_size = 8
    for i in range(0, len(docs), batch_size):
        batch = docs[i:i + batch_size]
        texts = [d["chunk_text"] for d in batch]
        resp  = encode_fn(texts)
        sparse_weights = resp.get("sparse_weights", [{} for _ in texts])

        for doc, svec in zip(batch, sparse_weights):
            meta = {k: doc[k] for k in ("stem", "label", "source", "source_file",
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
        print(f"[incr] Sparse/FTS {min(i + batch_size, len(docs))}/{len(docs)}", end="\r")
    print()


def main():
    from bge_m3_daemon import _ensure_running, _send

    print("[incr] Starting BGE-M3 daemon ...")
    _ensure_running()
    time.sleep(2)

    # Load existing index node_ids
    if not DENSE_META_PATH.exists():
        print("[incr] No existing dense meta — run full sync instead.")
        sys.exit(1)

    existing_meta = json.loads(DENSE_META_PATH.read_text("utf-8"))
    existing_ids  = {m.get("node_id") for m in existing_meta}
    print(f"[incr] Existing indexed nodes: {len(existing_ids)}")

    # Collect new nodes
    new_docs = collect_new_wiki_nodes(existing_ids)
    if not new_docs:
        print("[incr] No new nodes to encode. Index is up to date.")
        return

    print(f"[incr] New nodes to encode: {len(new_docs)}")
    for d in new_docs:
        print(f"  + {d['node_id']}")

    # Single encode_fn wrapper
    def encode_fn(texts: list[str]) -> dict:
        resp = _send({"mode": "encode_batch", "texts": texts})
        if "error" in resp:
            raise RuntimeError(f"Daemon error: {resp['error']}")
        vecs = np.array(resp["dense_vecs"], dtype="float32")
        return {"dense_vecs": vecs, "sparse_weights": resp.get("sparse_weights", [])}

    # Phase 1: dense
    append_to_dense(new_docs, encode_fn)

    # Phase 2: sparse + FTS5
    upsert_sparse_fts(new_docs, encode_fn)

    print(f"\n[incr] Done. {len(new_docs)} new nodes added to all indexes.")


if __name__ == "__main__":
    main()
