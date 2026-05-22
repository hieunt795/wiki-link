"""FAISS dense vector index management for BGE-M3 1024-dim vectors.

Index type: IndexFlatIP (inner product) — BGE-M3 outputs L2-normalized vectors,
so inner product == cosine similarity.

Dimensions: 1024 (BGE-M3 dense output, up from 768 with E5-Base).
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import numpy as np

INDEX_PATH = Path(__file__).parent.parent / ".cache" / "bge_m3_dense.index"
META_PATH  = Path(__file__).parent.parent / ".cache" / "bge_m3_dense_meta.json"
DIM = 1024


class DenseIndex:
    def __init__(self, index_path: Path = INDEX_PATH, meta_path: Path = META_PATH):
        self.index_path = index_path
        self.meta_path = meta_path
        self._index = None
        self._meta: list[dict] = []
        self._loaded = False

    def _ensure_loaded(self):
        if self._loaded:
            return
        if not self.index_path.exists() or not self.meta_path.exists():
            raise FileNotFoundError(
                "Dense index not built yet. Run: python librarian.py sync"
            )
        import faiss
        self._index = faiss.read_index(str(self.index_path))
        self._meta = json.loads(self.meta_path.read_text("utf-8"))
        self._loaded = True

    def search(
        self,
        query_vec: np.ndarray,
        top_k: int = 10,
        threshold: float = 0.30,
        wiki_only: bool = False,
        raw_only: bool = False,
    ) -> list[dict]:
        """Search FAISS index. Returns list of result dicts."""
        self._ensure_loaded()

        q = np.array([query_vec], dtype="float32")
        scores, indices = self._index.search(q, min(top_k * 3, len(self._meta)))

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            if score < threshold:
                break
            meta = self._meta[idx]
            src = meta.get("source", "")
            if wiki_only and src != "wiki":
                continue
            if raw_only and src != "raw":
                continue
            results.append({
                "node_id":   meta.get("node_id", ""),
                "stem":      meta.get("stem", ""),
                "label":     meta.get("label", ""),
                "source":    src,
                "source_file": meta.get("source_file", ""),
                "confidence": meta.get("confidence", ""),
                "thesis":    meta.get("thesis", ""),
                "tags":      meta.get("tags", []),
                "domain":    meta.get("domain", ""),
                "score":     float(score),
                "faiss_idx": int(idx),
            })
            if len(results) >= top_k:
                break

        return results

    def reconstruct(self, faiss_idx: int) -> np.ndarray:
        """Reconstruct a stored vector for centroid PRF."""
        self._ensure_loaded()
        vec = np.zeros(DIM, dtype="float32")
        self._index.reconstruct(faiss_idx, vec)
        return vec

    @staticmethod
    def build(docs: list[dict], encode_fn, index_path: Path = INDEX_PATH, meta_path: Path = META_PATH, batch_size: int = 16):
        """Build FAISS index from document chunks.

        Args:
            docs: list of dicts with keys: node_id, stem, label, source, source_file,
                  confidence, thesis, tags, domain, chunk_text
            encode_fn: callable(texts: list[str]) → dict with "dense_vecs"
        """
        import faiss

        index_path.parent.mkdir(parents=True, exist_ok=True)

        if not docs:
            print("[dense_index] No documents to index.")
            return

        print(f"[dense_index] Encoding {len(docs)} chunks ...")
        t0 = time.time()

        texts = [d["chunk_text"] for d in docs]
        # Encode in batches (smaller = less JSON per round-trip)
        all_vecs = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            enc = encode_fn(batch)
            all_vecs.append(enc["dense_vecs"])
            print(f"  {i + len(batch)}/{len(texts)} ...", end="\r", flush=True)

        vecs = np.vstack(all_vecs).astype("float32")
        print(f"\n[dense_index] Encoded in {time.time()-t0:.1f}s. Building FAISS index ...")

        index = faiss.IndexFlatIP(DIM)
        index.add(vecs)
        faiss.write_index(index, str(index_path))

        # Write metadata (parallel to index entries)
        meta = []
        for d in docs:
            meta.append({
                "node_id":    d.get("node_id", ""),
                "stem":       d.get("stem", ""),
                "label":      d.get("label", ""),
                "source":     d.get("source", ""),
                "source_file": d.get("source_file", ""),
                "confidence": d.get("confidence", ""),
                "thesis":     d.get("thesis", ""),
                "tags":       d.get("tags", []),
                "domain":     d.get("domain", ""),
            })
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"[dense_index] Built: {index.ntotal} vectors → {index_path}")

    def status(self) -> dict:
        if not self.index_path.exists():
            return {"built": False}
        self._ensure_loaded()
        return {
            "built": True,
            "total_vectors": self._index.ntotal,
            "dimensions": DIM,
            "index_path": str(self.index_path),
            "meta_count": len(self._meta),
        }
