"""4-phase KG²RAG search pipeline.

Phase 1 SEED:   3-way RRF fusion (BGE-M3 dense + BGE-M3 sparse + FTS5)
Phase 2 EXPAND: KG 1-hop neighbor expansion + convergence scoring
Phase 3 CHAIN:  BFS bridge nodes between seed clusters
Phase 4 RERANK: bge-reranker-v2-m3 cross-encoder on top-20 candidates
"""

from __future__ import annotations

import json
import time
from collections import defaultdict
from pathlib import Path

from models import SearchResult
from bge_m3_daemon import query_daemon
from sparse_index import FTSIndex
from reranker import CrossEncoderReranker
from vi_en import is_vietnamese, vi_augment

GRAPH_PATH = Path(__file__).parent.parent / "graphify-out" / "graph.json"
GAP_QUEUE  = Path(__file__).parent.parent / ".cache" / "gap_queue.jsonl"

_fts = FTSIndex()
_reranker = CrossEncoderReranker()

# ── Graph cache ────────────────────────────────────────────────────────────────

class _GraphCache:
    def __init__(self):
        self._adj: dict[str, list[str]] = {}
        self._loaded = False

    def _load(self):
        if self._loaded:
            return
        if not GRAPH_PATH.exists():
            self._adj = {}
            self._loaded = True
            return
        try:
            data = json.loads(GRAPH_PATH.read_text("utf-8"))
            for edge in data.get("edges", []):
                src = edge.get("source", "")
                tgt = edge.get("target", "")
                if src and tgt:
                    self._adj.setdefault(src, []).append(tgt)
                    self._adj.setdefault(tgt, []).append(src)  # undirected
        except Exception:
            pass
        self._loaded = True

    def neighbors(self, node_id: str) -> list[str]:
        self._load()
        return self._adj.get(node_id, [])

    def path_exists(self, a: str, b: str, max_hops: int = 3) -> list[str]:
        """BFS shortest path between two nodes. Returns path or []."""
        self._load()
        if a == b:
            return [a]
        visited = {a}
        queue = [[a]]
        for _ in range(max_hops):
            next_queue = []
            for path in queue:
                for nb in self.neighbors(path[-1]):
                    if nb == b:
                        return path + [nb]
                    if nb not in visited:
                        visited.add(nb)
                        next_queue.append(path + [nb])
            queue = next_queue
        return []


_graph = _GraphCache()


# ── Phase 1: SEED ─────────────────────────────────────────────────────────────

def phase1_seed(
    query: str,
    top: int = 50,
    wiki_only: bool = False,
    raw_only: bool = False,
) -> list[dict]:
    """3-way retrieval → RRF fusion.

    1. BGE-M3 dense search (via daemon)
    2. BGE-M3 sparse search (via daemon)
    3. FTS5 phrase/label match (local SQLite)
    4. RRF fusion k=60
    """
    # Augment VI queries for FTS5
    fts_query = vi_augment(query) if is_vietnamese(query) else query

    # Parallel retrieval (all three methods)
    dense_res  = query_daemon(query, mode="dense",  top_k=top * 2, wiki_only=wiki_only, raw_only=raw_only)
    sparse_res = query_daemon(query, mode="sparse", top_k=top * 2, wiki_only=wiki_only, raw_only=raw_only)
    fts_res    = _fts.query_fts(fts_query, top_k=top * 2, wiki_only=wiki_only, raw_only=raw_only)

    # Speculative skip: if sparse returns exact label match with score > 0.8
    # skip dense (saves ~20ms). Less aggressive than v1 FTS5 skip.
    _sparse_list = sparse_res.get("sparse_results", sparse_res) if isinstance(sparse_res, dict) else sparse_res
    if _sparse_list and _sparse_list[0]["score"] > 0.8:
        label = _sparse_list[0]["label"].lower()
        if any(tok in label for tok in query.lower().split()):
            dense_res = []  # speculative skip

    # RRF fusion
    K = 60
    rrf_scores: dict[str, float] = defaultdict(float)
    node_data: dict[str, dict] = {}

    for rank_i, r in enumerate(dense_res.get("dense_results", dense_res) if isinstance(dense_res, dict) else dense_res):
        nid = r.get("node_id") or r.get("stem", "")
        rrf_scores[nid] += 1.0 / (K + rank_i + 1)
        node_data.setdefault(nid, r)
        node_data[nid]["found_by"] = "dense"

    for rank_i, r in enumerate(sparse_res.get("sparse_results", sparse_res) if isinstance(sparse_res, dict) else sparse_res):
        nid = r.get("node_id") or r.get("stem", "")
        rrf_scores[nid] += 1.0 / (K + rank_i + 1)
        node_data.setdefault(nid, r)
        if node_data[nid].get("found_by") == "dense":
            node_data[nid]["found_by"] = "dense+sparse"
        else:
            node_data[nid]["found_by"] = "sparse"

    for rank_i, r in enumerate(fts_res):
        nid = r.get("node_id") or r.get("stem", "")
        rrf_scores[nid] += 1.0 / (K + rank_i + 1)
        node_data.setdefault(nid, r)
        existing = node_data[nid].get("found_by", "")
        if "fts" not in existing:
            node_data[nid]["found_by"] = (existing + "+fts").lstrip("+")

    # Merge and sort
    merged = []
    for nid, rrf_score in sorted(rrf_scores.items(), key=lambda x: -x[1]):
        d = dict(node_data[nid])
        d["score"] = rrf_score
        merged.append(d)

    return merged[:top]


def _to_search_result(d: dict, found_by: str = "") -> SearchResult:
    return SearchResult(
        node_id=d.get("node_id", d.get("stem", "")),
        stem=d.get("stem", ""),
        label=d.get("label", ""),
        source_file=d.get("source_file", ""),
        source=d.get("source", ""),
        confidence=str(d.get("confidence", "")),
        thesis=d.get("thesis", ""),
        tags=d.get("tags", []),
        score=float(d.get("score", 0.0)),
        found_by=found_by or d.get("found_by", ""),
        domain=d.get("domain", ""),
    )


# ── Phase 2: EXPAND ───────────────────────────────────────────────────────────

def phase2_expand(seeds: list[dict], top: int = 30) -> list[SearchResult]:
    """KG 1-hop neighbor expansion with convergence scoring."""
    seed_ids = {s.get("node_id", s.get("stem", "")) for s in seeds[:10]}
    neighbor_scores: dict[str, float] = defaultdict(float)

    for seed in seeds[:10]:
        nid = seed.get("node_id", seed.get("stem", ""))
        seed_score = seed.get("score", 0.0)
        for nb in _graph.neighbors(nid):
            if nb not in seed_ids:
                neighbor_scores[nb] += seed_score * 0.5  # decay factor

    expanded = []
    for nid, nb_score in sorted(neighbor_scores.items(), key=lambda x: -x[1])[:top]:
        expanded.append(SearchResult(
            node_id=nid, stem=nid, label=nid,
            source_file="", source="wiki",
            confidence="", thesis="", tags=[],
            score=nb_score,
            found_by=f"kg_expand",
        ))

    return expanded


# ── Phase 3: CHAIN ────────────────────────────────────────────────────────────

def phase3_chain(seeds: list[dict], top: int = 10) -> list[SearchResult]:
    """BFS bridge nodes between seed clusters."""
    if len(seeds) < 2:
        return []

    seed_ids = [s.get("node_id", s.get("stem", "")) for s in seeds[:5]]
    bridge_scores: dict[str, float] = defaultdict(float)

    for i, a in enumerate(seed_ids):
        for b in seed_ids[i+1:]:
            path = _graph.path_exists(a, b, max_hops=3)
            if len(path) > 2:
                for bridge in path[1:-1]:
                    bridge_scores[bridge] += 1.0 / len(path)

    chains = []
    for nid, score in sorted(bridge_scores.items(), key=lambda x: -x[1])[:top]:
        chains.append(SearchResult(
            node_id=nid, stem=nid, label=nid,
            source_file="", source="wiki",
            confidence="", thesis="", tags=[],
            score=score,
            found_by="chain",
        ))

    return chains


# ── Phase 4: RERANK ────────────────────────────────────────────────────────────

def phase4_rerank(
    query: str,
    seeds: list[dict],
    expanded: list[SearchResult],
    chains: list[SearchResult],
    top: int = 10,
) -> list[SearchResult]:
    """Merge all candidates, dedup, cross-encoder rerank top-20."""
    seed_results = [_to_search_result(s) for s in seeds]

    seen: dict[str, SearchResult] = {}
    for r in seed_results + expanded + chains:
        nid = r.node_id
        if nid not in seen or r.score > seen[nid].score:
            seen[nid] = r

    candidates = sorted(seen.values(), key=lambda x: -x.score)
    return _reranker.rerank(query, candidates, top_k=top)


# ── Gap detection ─────────────────────────────────────────────────────────────

def _gap_score(results: list) -> float:
    """Returns 0-1: how much of the result set is low-quality (gap indicator)."""
    if not results:
        return 1.0
    scores = [r.score if isinstance(r, SearchResult) else r.get("score", 0) for r in results[:5]]
    avg = sum(scores) / len(scores)
    return max(0.0, 1.0 - avg * 2)


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run_pipeline(
    query: str,
    top: int = 10,
    wiki_only: bool = False,
    raw_only: bool = False,
) -> list[SearchResult]:
    """Run the full 4-phase KG²RAG pipeline."""
    t0 = time.time()

    # Phase 1
    seeds = phase1_seed(query, top=50, wiki_only=wiki_only, raw_only=raw_only)

    # Gap check + centroid PRF fallback
    if _gap_score(seeds) > 0.40 and seeds:
        extra = query_daemon(query, mode="dense", top_k=20, centroid_expand=True,
                             centroid_k=3, wiki_only=wiki_only, raw_only=raw_only)
        extra_list = extra.get("dense_results", []) if isinstance(extra, dict) else extra
        seen_ids = {s.get("node_id") for s in seeds}
        for r in extra_list:
            if r.get("node_id") not in seen_ids:
                seeds.append(r)

    # Phase 2 & 3
    expanded = phase2_expand(seeds)
    chains   = phase3_chain(seeds)

    # Phase 4
    results = phase4_rerank(query, seeds, expanded, chains, top=top)

    elapsed = int((time.time() - t0) * 1000)
    if results:
        results[0].heatmap_ctx = f"[pipeline {elapsed}ms]"

    return results
