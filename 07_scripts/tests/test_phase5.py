"""Phase 5 test suite — agentic_search, deepdive_search, graph_rag.

Tests are designed to run WITHOUT the BGE-M3 daemon (offline mode).
They test module logic, data structures, and graph operations using
mock responses and the real wiki node files on disk.

Run:
  python -m pytest 07_scripts/tests/test_phase5.py -v

Or standalone (no pytest):
  python 07_scripts/tests/test_phase5.py
"""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path
from typing import Callable

# Add scripts dir to path for imports
SCRIPTS_DIR = Path(__file__).parent.parent
ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

# ── Test runner (minimal, no pytest dep required) ─────────────────────────────

_results: list[dict] = []


def test(name: str):
    """Decorator: mark a function as a test case."""
    def decorator(fn: Callable):
        _results.append({"name": name, "fn": fn, "status": "pending", "error": ""})
        return fn
    return decorator


def run_all():
    passed = failed = skipped = 0
    for t in _results:
        try:
            t["fn"]()
            t["status"] = "PASS"
            passed += 1
        except SkipTest as e:
            t["status"] = "SKIP"
            t["error"] = str(e)
            skipped += 1
        except Exception as e:
            t["status"] = "FAIL"
            t["error"] = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}"
            failed += 1

    print(f"\n{'='*60}")
    print(f"Phase 5 Test Suite: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"{'='*60}")
    for t in _results:
        icon = {"PASS": "OK", "FAIL": "XX", "SKIP": "--"}.get(t["status"], "??")
        print(f"  {icon} {t['name']}")
        if t["status"] == "FAIL":
            for line in t["error"].splitlines()[-6:]:
                print(f"      {line}")
    print()
    return failed == 0


class SkipTest(Exception):
    pass


def assert_eq(a, b, msg=""):
    if a != b:
        raise AssertionError(f"{msg} Expected {b!r}, got {a!r}")


def assert_true(cond, msg=""):
    if not cond:
        raise AssertionError(msg or f"Expected truthy, got {cond!r}")


def assert_in(item, container, msg=""):
    if item not in container:
        raise AssertionError(msg or f"{item!r} not in {container!r}")


# ── Tests: models.py ─────────────────────────────────────────────────────────

@test("models: SearchResult dataclass fields")
def test_search_result_fields():
    from models import SearchResult
    r = SearchResult(
        node_id="test_001", stem="test_001", label="Test Node",
        source_file="03_wiki/concepts/Test.md", source="wiki",
        confidence="3", thesis="A test thesis.", tags=["test"],
        score=0.72, found_by="dense",
    )
    assert_eq(r.node_id, "test_001")
    assert_eq(r.score, 0.72)
    assert_eq(r.body, "")      # default
    assert_eq(r.domain, "")   # default


@test("models: Probe dataclass fields")
def test_probe_fields():
    from models import Probe
    p = Probe(
        state="INGESTED", wiki_sem=0.71, wiki_fts=3.0, raw_sem=0.40, raw_fts=2.0,
        phrase_wiki=3, phrase_raw=2, label_hits=2, label_cov=0.80, elapsed_ms=120,
    )
    assert_eq(p.state, "INGESTED")
    assert_eq(p.wiki_sem, 0.71)


# ── Tests: graph_rag.py ───────────────────────────────────────────────────────

@test("graph_rag: KnowledgeGraph loads (empty if no graph.json)")
def test_graph_empty_load():
    from graph_rag import KnowledgeGraph
    tmp_path = ROOT / ".cache" / "_test_graph_empty.json"
    g = KnowledgeGraph(graph_path=tmp_path)  # doesn't exist
    assert_eq(g.node_count, 0)
    assert_eq(g.edge_count, 0)
    assert_eq(g.neighbors("nonexistent"), [])


@test("graph_rag: KnowledgeGraph loads from JSON")
def test_graph_load_json():
    from graph_rag import KnowledgeGraph
    import tempfile, os
    data = {
        "nodes": [
            {"id": "node_a", "label": "Node A", "type": "concept"},
            {"id": "node_b", "label": "Node B", "type": "mechanism"},
            {"id": "node_c", "label": "Node C", "type": "framework"},
        ],
        "edges": [
            {"source": "node_a", "target": "node_b", "weight": 1.0},
            {"source": "node_b", "target": "node_c", "weight": 1.0},
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        assert_eq(g.node_count, 3)
        assert_eq(g.edge_count, 2)
        assert_in("node_b", g.neighbors("node_a"))
        assert_in("node_a", g.neighbors("node_b"))  # undirected
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: shortest_path BFS")
def test_graph_shortest_path():
    from graph_rag import KnowledgeGraph
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in "abcde"],
        "edges": [
            {"source": "a", "target": "b", "weight": 1.0},
            {"source": "b", "target": "c", "weight": 1.0},
            {"source": "c", "target": "d", "weight": 1.0},
            {"source": "d", "target": "e", "weight": 1.0},
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph_path.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        path = g.shortest_path("a", "e", max_hops=5)
        assert_eq(path, ["a", "b", "c", "d", "e"])
        # Within 2 hops — should fail
        path2 = g.shortest_path("a", "e", max_hops=2)
        assert_eq(path2, [])
        # Same node
        assert_eq(g.shortest_path("a", "a"), ["a"])
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: subgraph extraction")
def test_graph_subgraph():
    from graph_rag import KnowledgeGraph
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in ["hub", "a", "b", "c", "far"]],
        "edges": [
            {"source": "hub", "target": "a", "weight": 1.0},
            {"source": "hub", "target": "b", "weight": 1.0},
            {"source": "hub", "target": "c", "weight": 1.0},
            {"source": "far", "target": "a", "weight": 1.0},  # 2 hops from hub via a
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph_sub.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        sub = g.subgraph(["hub"], hops=1)
        assert_in("hub", sub)
        assert_in("a", sub)
        assert_in("b", sub)
        assert_in("c", sub)
        assert "far" not in sub  # 2 hops away, not in 1-hop

        sub2 = g.subgraph(["hub"], hops=2)
        assert_in("far", sub2)  # now reachable via hub→a→far
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: degree_centrality and hub_nodes")
def test_graph_centrality():
    from graph_rag import KnowledgeGraph
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in ["hub", "a", "b", "c"]],
        "edges": [
            {"source": "hub", "target": "a", "weight": 1.0},
            {"source": "hub", "target": "b", "weight": 1.0},
            {"source": "hub", "target": "c", "weight": 1.0},
            {"source": "a",   "target": "b", "weight": 1.0},
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph_cent.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        centrality = g.degree_centrality(["hub", "a", "b", "c"])
        # hub has degree 3 (highest)
        assert_true(centrality["hub"] >= centrality["c"],
                    "hub should have higher centrality than leaf c")
        hubs = g.hub_nodes(["hub", "a", "b", "c"], top=1)
        assert_eq(hubs[0][0], "hub")
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: label_propagation community detection")
def test_graph_communities():
    from graph_rag import KnowledgeGraph
    # Two clear communities: {a,b,c} and {x,y,z} connected by weak bridge
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in "abcxyz"],
        "edges": [
            {"source": "a", "target": "b", "weight": 1.0},
            {"source": "b", "target": "c", "weight": 1.0},
            {"source": "x", "target": "y", "weight": 1.0},
            {"source": "y", "target": "z", "weight": 1.0},
            {"source": "c", "target": "x", "weight": 1.0},  # bridge
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph_comm.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        communities = g.label_propagation(max_iter=20)
        assert_true(isinstance(communities, dict))
        assert_true(len(communities) == 6)
        # All nodes should have a community assigned
        for n in "abcxyz":
            assert_in(n, communities)
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: bridge_nodes between clusters")
def test_graph_bridges():
    from graph_rag import KnowledgeGraph
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in ["a", "bridge", "b"]],
        "edges": [
            {"source": "a",      "target": "bridge", "weight": 1.0},
            {"source": "bridge", "target": "b",      "weight": 1.0},
        ]
    }
    tmp = ROOT / ".cache" / "_test_graph_bridge.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        bridges = g.bridge_nodes(["a"], ["b"], max_hops=3)
        assert_in("bridge", bridges)
    finally:
        tmp.unlink(missing_ok=True)


@test("graph_rag: topic_subgraph_summary returns string")
def test_graph_summary():
    from graph_rag import KnowledgeGraph
    data = {
        "nodes": [{"id": n, "label": n, "type": "concept"} for n in ["a", "b"]],
        "edges": [{"source": "a", "target": "b", "weight": 1.0}]
    }
    tmp = ROOT / ".cache" / "_test_graph_summ.json"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(json.dumps(data), encoding="utf-8")
    try:
        g = KnowledgeGraph(graph_path=tmp)
        summary = g.topic_subgraph_summary(["a"])
        assert_true(isinstance(summary, str))
        assert_true("Subgraph:" in summary)
    finally:
        tmp.unlink(missing_ok=True)


# ── Tests: deepdive_search.py ─────────────────────────────────────────────────

@test("deepdive: is_thin_node detects [LLM] marker")
def test_deepdive_thin_llm():
    from models import SearchResult
    from deepdive_search import is_thin_node
    thin = SearchResult(
        node_id="x", stem="x", label="X", source_file="", source="wiki",
        confidence="2", thesis="[LLM] This was synthesized.", tags=[],
        score=0.5, found_by="dense",
    )
    assert_true(is_thin_node(thin))


@test("deepdive: is_thin_node detects confidence <= 1")
def test_deepdive_thin_conf():
    from models import SearchResult
    from deepdive_search import is_thin_node
    thin = SearchResult(
        node_id="y", stem="y", label="Y", source_file="", source="wiki",
        confidence="1", thesis="Sourced claim.", tags=[],
        score=0.6, found_by="dense",
    )
    assert_true(is_thin_node(thin))


@test("deepdive: is_thin_node detects short body")
def test_deepdive_thin_body():
    from models import SearchResult
    from deepdive_search import is_thin_node
    thin = SearchResult(
        node_id="z", stem="z", label="Z", source_file="", source="wiki",
        confidence="3", thesis="Good confidence.", tags=[],
        score=0.7, found_by="dense", body="Short.",
    )
    assert_true(is_thin_node(thin))


@test("deepdive: is_thin_node passes for healthy node")
def test_deepdive_not_thin():
    from models import SearchResult
    from deepdive_search import is_thin_node
    healthy = SearchResult(
        node_id="w", stem="w", label="W", source_file="", source="wiki",
        confidence="4", thesis="Well-sourced.", tags=[],
        score=0.8, found_by="dense",
        body="A" * 300,  # long enough
    )
    assert_true(not is_thin_node(healthy))


@test("deepdive: audit_thin_nodes reads real wiki files")
def test_deepdive_audit_real():
    from deepdive_search import audit_thin_nodes
    wiki_root = ROOT / "03_wiki"
    if not any(wiki_root.rglob("*.md")):
        raise SkipTest("No wiki nodes on disk — skip")
    thin = audit_thin_nodes(min_confidence=3)
    # Should return a list (possibly empty)
    assert_true(isinstance(thin, list))
    for t in thin:
        assert_in("node_id", t)
        assert_in("confidence", t)
        assert_in("reasons", t)


# ── Tests: agentic_search.py ──────────────────────────────────────────────────

@test("agentic: LENS_TEMPLATES has exactly 5 lenses")
def test_agentic_lens_count():
    from agentic_search import LENS_TEMPLATES
    assert_eq(len(LENS_TEMPLATES), 5)
    for lens in ("policy", "macro", "plumbing", "treasury", "timing"):
        assert_in(lens, LENS_TEMPLATES)


@test("agentic: _build_lens_query formats correctly")
def test_agentic_build_query():
    from agentic_search import _build_lens_query
    q = _build_lens_query("policy", "reserve scarcity", variant=0)
    assert_true("reserve scarcity" in q)
    assert_true(isinstance(q, str))
    # Variant cycling — should not raise
    for v in range(6):
        r = _build_lens_query("macro", "QT balance sheet", variant=v)
        assert_true("QT balance sheet" in r)


@test("agentic: AgenticSearchResult dataclass defaults")
def test_agentic_result_defaults():
    from agentic_search import AgenticSearchResult
    r = AgenticSearchResult(query="test query")
    assert_eq(r.query, "test query")
    assert_eq(r.lenses, [])
    assert_eq(r.merged, [])
    assert_eq(r.gap_lenses, [])
    assert_eq(r.elapsed_ms, 0)


@test("agentic: format_lens_summary renders table")
def test_agentic_format_summary():
    from agentic_search import AgenticSearchResult, LensResult, format_lens_summary
    from models import Probe, SearchResult

    probe = Probe(state="INGESTED", wiki_sem=0.7, wiki_fts=2.0, raw_sem=0.3,
                  raw_fts=1.0, phrase_wiki=2, phrase_raw=1, label_hits=1,
                  label_cov=0.6, elapsed_ms=80)
    sr = SearchResult(node_id="n1", stem="n1", label="A Long Node Label Here",
                      source_file="", source="wiki", confidence="3", thesis="T",
                      tags=[], score=0.75, found_by="dense")
    lr = LensResult(lens="policy", probe=probe, results=[sr])

    result = AgenticSearchResult(query="reserve scarcity", lenses=[lr], merged=[sr])
    summary = format_lens_summary(result)

    assert_true("policy" in summary)
    assert_true("INGESTED" in summary)
    assert_true("reserve scarcity" in summary)


@test("agentic: merge dedup logic (no real daemon)")
def test_agentic_merge_dedup():
    """Test the merge/dedup logic by constructing results manually."""
    from agentic_search import AgenticSearchResult, LensResult
    from models import Probe, SearchResult

    def make_probe(state="INGESTED"):
        return Probe(state=state, wiki_sem=0.7, wiki_fts=2.0, raw_sem=0.3, raw_fts=1.0,
                     phrase_wiki=2, phrase_raw=1, label_hits=1, label_cov=0.6, elapsed_ms=80)

    def make_sr(node_id, score):
        return SearchResult(node_id=node_id, stem=node_id, label=node_id,
                            source_file="", source="wiki", confidence="3", thesis="",
                            tags=[], score=score, found_by="dense")

    # Same node_id appears in two lenses — should be deduped, scores summed
    from collections import defaultdict

    lens1 = LensResult(lens="policy", probe=make_probe(), results=[make_sr("a", 0.8), make_sr("b", 0.6)])
    lens2 = LensResult(lens="macro",  probe=make_probe(), results=[make_sr("a", 0.7), make_sr("c", 0.5)])

    result = AgenticSearchResult(query="q", lenses=[lens1, lens2])

    # Replicate merge logic
    merged_scores = defaultdict(float)
    merged_data = {}
    for lr in result.lenses:
        for r in lr.results:
            merged_scores[r.node_id] += r.score
            if r.node_id not in merged_data or r.score > merged_data[r.node_id].score:
                merged_data[r.node_id] = r

    result.merged = sorted(merged_data.values(), key=lambda r: -merged_scores[r.node_id])

    # "a" appears in both lenses with 0.8+0.7=1.5 total — should rank first
    assert_eq(result.merged[0].node_id, "a")
    assert_eq(len(result.merged), 3)  # a, b, c — no duplicates


# ── Tests: librarian.py CLI wiring ────────────────────────────────────────────

@test("librarian: agentic command registered in COMMAND_MAP")
def test_librarian_agentic_registered():
    import importlib.util
    spec = importlib.util.spec_from_file_location("librarian", SCRIPTS_DIR / "librarian.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert_in("agentic", mod.COMMAND_MAP)
    assert_in("deep",    mod.COMMAND_MAP)


@test("librarian: agentic parser parses correctly")
def test_librarian_agentic_parser():
    import importlib.util
    spec = importlib.util.spec_from_file_location("librarian", SCRIPTS_DIR / "librarian.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    parser = mod.build_parser()
    args = parser.parse_args(["agentic", "reserve scarcity", "--top", "8"])
    assert_eq(args.query, "reserve scarcity")
    assert_eq(args.top, 8)
    assert_true(not args.deep)

    args_deep = parser.parse_args(["agentic", "reserve scarcity", "--deep"])
    assert_true(args_deep.deep)


@test("librarian: deep parser parses correctly")
def test_librarian_deep_parser():
    import importlib.util
    spec = importlib.util.spec_from_file_location("librarian", SCRIPTS_DIR / "librarian.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    parser = mod.build_parser()
    args = parser.parse_args(["deep", "monetary_policy"])
    assert_eq(args.domain, "monetary_policy")
    assert_true(not args.audit)

    args_audit = parser.parse_args(["deep", "monetary_policy", "--audit"])
    assert_true(args_audit.audit)


# ── Tests: integration — wiki files on disk ───────────────────────────────────

@test("wiki: all nodes have valid node_id in frontmatter")
def test_wiki_nodes_have_ids():
    from chunker import _split_frontmatter
    wiki_root = ROOT / "03_wiki"
    nodes_checked = 0
    for md_file in wiki_root.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        if not fm:
            continue
        assert_true(
            "node_id" in fm,
            f"Missing node_id in {md_file.relative_to(ROOT)}"
        )
        assert_true(
            fm["node_id"],
            f"Empty node_id in {md_file.relative_to(ROOT)}"
        )
        nodes_checked += 1
    assert_true(nodes_checked > 0, "No wiki nodes found — check 03_wiki/")


@test("wiki: all nodes have confidence field")
def test_wiki_nodes_have_confidence():
    from chunker import _split_frontmatter
    wiki_root = ROOT / "03_wiki"
    for md_file in wiki_root.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        assert_true(
            "confidence" in fm,
            f"Missing confidence in {md_file.relative_to(ROOT)}"
        )


@test("wiki: all nodes have thesis field (non-empty)")
def test_wiki_nodes_have_thesis():
    from chunker import _split_frontmatter
    wiki_root = ROOT / "03_wiki"
    issues = []
    for md_file in wiki_root.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        if not fm.get("thesis"):
            issues.append(str(md_file.relative_to(ROOT)))
    assert_true(
        len(issues) == 0,
        f"Nodes missing thesis: {issues}"
    )


@test("wiki: source_refs point to existing files")
def test_wiki_source_refs_exist():
    from chunker import _split_frontmatter
    wiki_root = ROOT / "03_wiki"
    broken = []
    for md_file in wiki_root.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        for ref in fm.get("source_refs", []):
            path_str = ref.get("path", "") if isinstance(ref, dict) else ""
            if path_str:
                full_path = ROOT / path_str
                if not full_path.exists():
                    broken.append(f"{md_file.name}: {path_str}")
    assert_true(
        len(broken) == 0,
        f"Broken source_refs: {broken}"
    )


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    success = run_all()
    sys.exit(0 if success else 1)
