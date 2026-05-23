"""Cross-encoder reranker using bge-reranker-v2-m3.

Replaces handcrafted Phase 4 scoring from v1.
Applied to top-20 candidates only (cost control).

Scoring formula:
    final_score = cross_encoder_score × confidence_multiplier × llm_penalty

    confidence_multiplier = 1.0 + confidence × 0.05  (conf=5 → 1.25×)
    llm_penalty = 0.4 if [LLM] in thesis or body[:200], else 1.0
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from pathlib import Path

from models import SearchResult

CACHE_DB = Path(__file__).parent.parent / ".cache" / "reranker_cache.db"
RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"
IDLE_UNLOAD_SECONDS = 300


class CrossEncoderReranker:
    def __init__(self, model_name: str = RERANKER_MODEL, use_fp16: bool = True):
        self._reranker = None
        self._model_name = model_name
        self._use_fp16 = use_fp16
        self._last_used = time.time()
        self._cache = RerankerCache()

    def _ensure_loaded(self):
        self._last_used = time.time()
        if self._reranker is None:
            print(f"[reranker] Loading {self._model_name} ...", flush=True)
            try:
                from FlagEmbedding import FlagReranker
                self._reranker = FlagReranker(self._model_name, use_fp16=self._use_fp16)
                print("[reranker] Loaded.", flush=True)
            except ImportError:
                print("[reranker] FlagEmbedding not installed.", flush=True)
                self._reranker = None

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        top_k: int = 10,
    ) -> list[SearchResult]:
        """Cross-encoder rerank. Returns candidates sorted by final_score."""
        if not candidates:
            return []

        # Only rerank top-20 (cost control)
        to_rerank = candidates[:20]
        remainder = candidates[20:]

        self._ensure_loaded()

        if self._reranker is None:
            # Fallback: apply confidence multiplier only (no cross-encoder)
            for c in candidates:
                c.score = c.score * _confidence_mult(c) * _llm_penalty(c)
            candidates.sort(key=lambda x: -x.score)
            return candidates[:top_k]

        # Build pairs for cross-encoder
        pairs = []
        q = str(query) if query else ""
        for c in to_rerank:
            doc_text = str(
                (c.body[:512] if c.body else "")
                or (c.thesis[:512] if c.thesis else "")
                or c.label
                or c.stem
                or ""
            )
            pairs.append([q, doc_text])

        # Check cache
        scores = self._cache.batch_get(query, [c.node_id for c in to_rerank])
        uncached_idx = [i for i, s in enumerate(scores) if s is None]

        if uncached_idx:
            uncached_pairs = [pairs[i] for i in uncached_idx]
            try:
                raw_scores = self._reranker.compute_score(uncached_pairs, normalize=True)
                if isinstance(raw_scores, float):
                    raw_scores = [raw_scores]
                for i, score in zip(uncached_idx, raw_scores):
                    scores[i] = float(score)
                    self._cache.put(query, to_rerank[i].node_id, float(score))
            except (AttributeError, Exception) as e:
                print(f"[reranker] compute_score failed ({e}), using confidence fallback.", flush=True)
                self._reranker = None  # unload broken model
                for c in candidates:
                    c.score = c.score * _confidence_mult(c) * _llm_penalty(c)
                candidates.sort(key=lambda x: -x.score)
                return candidates[:top_k]

        # Apply multipliers
        for c, score in zip(to_rerank, scores):
            raw = score if score is not None else 0.0
            c.score = raw * _confidence_mult(c) * _llm_penalty(c)

        # Remainder gets score 0 (below all reranked)
        for c in remainder:
            c.score = 0.0

        all_candidates = to_rerank + remainder
        all_candidates.sort(key=lambda x: -x.score)
        return all_candidates[:top_k]

    def unload(self):
        """Free VRAM — called after IDLE_UNLOAD_SECONDS of inactivity."""
        if self._reranker is not None:
            del self._reranker
            self._reranker = None


def _confidence_mult(c: SearchResult) -> float:
    try:
        conf = int(c.confidence) if c.confidence else 0
    except (ValueError, TypeError):
        conf = 0
    return 1.0 + conf * 0.05


def _llm_penalty(c: SearchResult) -> float:
    check_text = (c.thesis or "") + (c.body[:200] if c.body else "")
    return 0.4 if "[LLM]" in check_text else 1.0


class RerankerCache:
    """LRU cache for reranker scores in SQLite. TTL: cleared on sync."""

    def __init__(self, db_path: Path = CACHE_DB):
        self.db_path = db_path
        self._conn: sqlite3.Connection | None = None

    def _connect(self) -> sqlite3.Connection:
        if self._conn is None:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self._conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
            self._conn.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    query_hash TEXT,
                    doc_id     TEXT,
                    score      REAL,
                    ts         INTEGER,
                    PRIMARY KEY (query_hash, doc_id)
                )
            """)
            self._conn.commit()
        return self._conn

    def _qhash(self, query: str) -> str:
        return hashlib.md5(query.encode()).hexdigest()

    def batch_get(self, query: str, doc_ids: list[str]) -> list[float | None]:
        try:
            conn = self._connect()
            qh = self._qhash(query)
            scores = {row[0]: row[1] for row in conn.execute(
                f"SELECT doc_id, score FROM scores WHERE query_hash=? AND doc_id IN ({','.join('?'*len(doc_ids))})",
                [qh] + doc_ids
            )}
            return [scores.get(d) for d in doc_ids]
        except Exception:
            return [None] * len(doc_ids)

    def put(self, query: str, doc_id: str, score: float):
        try:
            conn = self._connect()
            qh = self._qhash(query)
            conn.execute(
                "INSERT OR REPLACE INTO scores(query_hash,doc_id,score,ts) VALUES(?,?,?,?)",
                (qh, doc_id, score, int(time.time()))
            )
            conn.commit()
        except Exception:
            pass

    def clear(self):
        try:
            conn = self._connect()
            conn.execute("DELETE FROM scores")
            conn.commit()
        except Exception:
            pass
