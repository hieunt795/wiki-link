"""graph_rag.py — Knowledge graph traversal utilities.

Builds on the _GraphCache in search_pipeline.py.
Provides higher-level graph operations for research_agent:
  - Multi-hop path finding between concept clusters
  - Subgraph extraction for a topic
  - Centrality scoring (identify hub nodes)
  - Community detection (simple label propagation)
"""

from __future__ import annotations

import json
from collections import defaultdict, deque
from pathlib import Path

GRAPH_PATH = Path(__file__).parent.parent / "graphify-out" / "graph.json"


class KnowledgeGraph:
    def __init__(self, graph_path: Path = GRAPH_PATH):
        self._path = graph_path
        self._adj: dict[str, list[str]] = {}
        self._node_meta: dict[str, dict] = {}
        self._loaded = False

    def _load(self):
        if self._loaded:
            return
        self._adj = {}
        self._node_meta = {}
        if not self._path.exists():
            self._loaded = True
            return
        try:
            data = json.loads(self._path.read_text("utf-8"))
            for node in data.get("nodes", []):
                nid = node.get("id", "")
                self._node_meta[nid] = node
            for edge in data.get("edges", []):
                src = edge.get("source", "")
                tgt = edge.get("target", "")
                w = float(edge.get("weight", 1.0))
                if src and tgt:
                    self._adj.setdefault(src, []).append(tgt)
                    self._adj.setdefault(tgt, []).append(src)
        except Exception:
            pass
        self._loaded = True

    @property
    def node_count(self) -> int:
        self._load()
        return len(self._node_meta)

    @property
    def edge_count(self) -> int:
        self._load()
        return sum(len(v) for v in self._adj.values()) // 2

    def neighbors(self, node_id: str) -> list[str]:
        self._load()
        return self._adj.get(node_id, [])

    def meta(self, node_id: str) -> dict:
        self._load()
        return self._node_meta.get(node_id, {})

    def shortest_path(self, src: str, dst: str, max_hops: int = 5) -> list[str]:
        """BFS shortest path. Returns [] if not found within max_hops."""
        self._load()
        if src == dst:
            return [src]
        visited = {src}
        queue: deque[list[str]] = deque([[src]])
        for _ in range(max_hops):
            if not queue:
                break
            next_queue: deque[list[str]] = deque()
            while queue:
                path = queue.popleft()
                for nb in self.neighbors(path[-1]):
                    if nb == dst:
                        return path + [nb]
                    if nb not in visited:
                        visited.add(nb)
                        next_queue.append(path + [nb])
            queue = next_queue
        return []

    def subgraph(self, seed_nodes: list[str], hops: int = 2) -> dict[str, list[str]]:
        """Extract subgraph within `hops` of any seed node. Returns adjacency dict."""
        self._load()
        visited: set[str] = set(seed_nodes)
        frontier: set[str] = set(seed_nodes)
        for _ in range(hops):
            next_frontier: set[str] = set()
            for node in frontier:
                for nb in self.neighbors(node):
                    if nb not in visited:
                        visited.add(nb)
                        next_frontier.add(nb)
            frontier = next_frontier
        sub_adj: dict[str, list[str]] = {}
        for node in visited:
            sub_adj[node] = [nb for nb in self.neighbors(node) if nb in visited]
        return sub_adj

    def degree_centrality(self, node_ids: list[str] | None = None) -> dict[str, float]:
        """Compute degree centrality for given nodes (or all nodes)."""
        self._load()
        nodes = node_ids or list(self._node_meta.keys())
        max_degree = max((len(self._adj.get(n, [])) for n in nodes), default=1)
        if max_degree == 0:
            max_degree = 1
        return {n: len(self._adj.get(n, [])) / max_degree for n in nodes}

    def hub_nodes(self, candidate_ids: list[str], top: int = 5) -> list[tuple[str, float]]:
        """Return top hub nodes by degree centrality among candidates."""
        centrality = self.degree_centrality(candidate_ids)
        return sorted(centrality.items(), key=lambda x: -x[1])[:top]

    def bridge_nodes(self, cluster_a: list[str], cluster_b: list[str],
                     max_hops: int = 3) -> list[str]:
        """Find nodes that lie on paths between cluster_a and cluster_b."""
        self._load()
        bridges: dict[str, int] = defaultdict(int)
        for a in cluster_a[:5]:
            for b in cluster_b[:5]:
                path = self.shortest_path(a, b, max_hops=max_hops)
                if len(path) > 2:
                    for mid in path[1:-1]:
                        bridges[mid] += 1
        return [n for n, _ in sorted(bridges.items(), key=lambda x: -x[1])]

    def label_propagation(self, max_iter: int = 10) -> dict[str, str]:
        """Simple label propagation community detection.

        Returns mapping node_id → community_id.
        """
        self._load()
        nodes = list(self._node_meta.keys())
        communities = {n: n for n in nodes}  # each node is its own community initially

        for _ in range(max_iter):
            changed = False
            for node in nodes:
                nbs = self.neighbors(node)
                if not nbs:
                    continue
                # Most frequent community among neighbors
                freq: dict[str, int] = defaultdict(int)
                for nb in nbs:
                    freq[communities[nb]] += 1
                best = max(freq, key=freq.get)
                if communities[node] != best:
                    communities[node] = best
                    changed = True
            if not changed:
                break
        return communities

    def topic_subgraph_summary(self, seed_nodes: list[str]) -> str:
        """Return a compact text summary of the subgraph around seed nodes."""
        sub = self.subgraph(seed_nodes, hops=2)
        n_nodes = len(sub)
        n_edges = sum(len(v) for v in sub.values()) // 2
        hubs = self.hub_nodes(list(sub.keys()), top=3)
        hub_str = ", ".join(f"{nid} ({sc:.2f})" for nid, sc in hubs)
        return (f"Subgraph: {n_nodes} nodes, {n_edges} edges  "
                f"| Top hubs: {hub_str or 'none'}")


# Module-level singleton
_graph = KnowledgeGraph()


def get_graph() -> KnowledgeGraph:
    return _graph
