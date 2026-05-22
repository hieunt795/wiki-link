"""librarian.py - Master CLI for Wiki-Agentic.

Usage:
  python librarian.py <command> [options]

Commands:
  daemon   start|stop|status           BGE-M3 daemon management
  sync     [--incremental]             Rebuild all indexes
  embed    [--incremental]             Encode wiki + raw sources -> indexes
  ingest   <source_path> [--dry-run]   Ingest source file -> wiki nodes
  sweep    [--dry-run]                 Batch ingest 02_sources/Inbox/
  search   <query> [--top N]           4-phase KG2RAG search
  synth    <query> [--top N] [--v]     Coverage-aware synthesis search
  probe    <query>                     Coverage probe only (INGESTED/PENDING/TRUE_GAP)
  agentic  <query> [--top N] [--deep]  5-lens T_MODE_DEEP multi-perspective search
  deep     <domain> [--audit]          Thin-node detection + deepdive augmentation
  lint     [--fix]                     Wiki health check
  link     [--fix]                     Cross-reference audit
  gaps     [list|suggest|close]        Gap queue management
  status                               System health overview
  session-close <topic_slug>           Summarize template insights from session
  template-show <insight_id>           Show pending template insight
  template-apply <insight_id|--priority high>  Apply approved insight
  template-reject <insight_id>         Reject insight with reason
"""

from __future__ import annotations

import argparse
import sys
import json
from pathlib import Path

# Paths
ROOT        = Path(__file__).parent.parent
WIKI_ROOT   = ROOT / "03_wiki"
SOURCES_DIR = ROOT / "02_sources"
CACHE_DIR   = ROOT / ".cache"
SCRIPTS_DIR = Path(__file__).parent


def cmd_daemon(args):
    from bge_m3_daemon import is_running, cmd_stop, _ensure_running
    if args.action == "start":
        if is_running():
            print("[daemon] Already running.")
        else:
            _ensure_running()
            print("[daemon] Started.")
    elif args.action == "stop":
        cmd_stop()
    elif args.action == "status":
        if is_running():
            pid_file = CACHE_DIR / "daemon.pid"
            pid = pid_file.read_text().strip() if pid_file.exists() else "?"
            print(f"[daemon] Running (PID {pid})")
        else:
            print("[daemon] Not running.")


def cmd_sync(args):
    """Full rebuild: encode all docs → rebuild all indexes."""
    print("[sync] Starting full index rebuild...")
    _ensure_daemon()
    _encode_all(incremental=getattr(args, "incremental", False))
    _rebuild_graph()
    from reranker import CrossEncoderReranker
    CrossEncoderReranker()._cache.clear()
    print("[sync] Done.")


def cmd_embed(args):
    """Encode documents and update indexes (no graph rebuild)."""
    _ensure_daemon()
    _encode_all(incremental=getattr(args, "incremental", False))
    print("[embed] Done.")


def _ensure_daemon():
    from bge_m3_daemon import _ensure_running
    _ensure_running()


def _encode_all(incremental: bool = False):
    """Encode wiki nodes + raw source chunks → FAISS + sparse + FTS5."""
    from bge_m3_daemon import _send
    from dense_index import DenseIndex
    from sparse_index import SparseIndex, FTSIndex
    import numpy as np

    sparse_idx = SparseIndex()
    fts_idx    = FTSIndex()
    sparse_idx.create_tables()
    fts_idx.create_tables()

    docs = []
    docs.extend(_collect_wiki_nodes())
    docs.extend(_collect_raw_chunks())

    if not docs:
        print("[embed] No documents found.")
        return

    # DenseIndex.build() expects key "chunk_text"
    for d in docs:
        d["chunk_text"] = d["text"]

    print(f"[embed] {len(docs)} docs to encode ...")

    # encode_fn passed to DenseIndex.build() — calls daemon encode_batch endpoint
    def encode_fn(texts: list[str]) -> dict:
        resp = _send({"mode": "encode_batch", "texts": texts})
        if "error" in resp:
            raise RuntimeError(f"Daemon encode error: {resp['error']}")
        vecs = np.array(resp["dense_vecs"], dtype="float32")
        return {"dense_vecs": vecs}

    # Phase 1: build FAISS dense index (handles batching internally)
    DenseIndex.build(docs, encode_fn)

    # Phase 2: build sparse + FTS5 indexes
    batch_size = 32
    total = len(docs)
    for i in range(0, total, batch_size):
        batch_docs  = docs[i:i + batch_size]
        batch_texts = [d["chunk_text"] for d in batch_docs]
        resp = _send({"mode": "encode_batch", "texts": batch_texts})
        sparse_weights = resp.get("sparse_weights", [{} for _ in batch_texts])
        for doc, svec in zip(batch_docs, sparse_weights):
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
        print(f"[embed] Sparse/FTS {min(i + batch_size, total)}/{total}", end="\r", flush=True)

    print(f"\n[embed] Done: {total} documents indexed.")


def _collect_wiki_nodes() -> list[dict]:
    """Read all wiki node .md files → list of doc dicts."""
    from chunker import _split_frontmatter
    docs = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        node_id = fm["node_id"]
        tags = fm.get("tags", [])
        domain_field = fm.get("domain", {})
        domain = domain_field.get("primary", "") if isinstance(domain_field, dict) else str(domain_field)
        docs.append({
            "node_id":    node_id,
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
    return docs


def _collect_raw_chunks() -> list[dict]:
    """Chunk all raw source .md files → list of doc dicts."""
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
            chunks = chunk_markdown(text, target_tokens=4096, source_file=str(md_file))
            for i, chunk in enumerate(chunks):
                chunk_id = f"raw__{md_file.stem}__{i:04d}"
                docs.append({
                    "node_id":    chunk_id,
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
    return docs


def _rebuild_graph():
    """Rebuild KG from wiki node [[wikilinks]] → graphify-out/graph.json."""
    import re
    graph_out = ROOT / "graphify-out"
    graph_out.mkdir(exist_ok=True)
    nodes = []
    edges = []
    seen_edges: set[tuple[str, str]] = set()

    for md_file in WIKI_ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        # Extract node_id from frontmatter
        from chunker import _split_frontmatter
        fm, body = _split_frontmatter(text)
        nid = fm.get("node_id")
        if not nid:
            continue
        nodes.append({"id": nid, "label": fm.get("title", md_file.stem),
                       "type": fm.get("type", "concept")})
        # Extract [[wikilinks]]
        links = re.findall(r"\[\[([^\]]+)\]\]", text)
        for link in links:
            target = link.split("|")[0].strip().replace(" ", "_").lower()
            key = (nid, target)
            if key not in seen_edges:
                seen_edges.add(key)
                edges.append({"source": nid, "target": target, "weight": 1.0})

    graph = {"nodes": nodes, "edges": edges}
    (graph_out / "graph.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[graph] Built graph: {len(nodes)} nodes, {len(edges)} edges.")


def cmd_ingest(args):
    from ingest import ingest_source
    ingest_source(args.source_path, dry_run=args.dry_run)


def cmd_sweep(args):
    """Batch ingest all files in 02_sources/Inbox/."""
    from ingest import ingest_source
    inbox = SOURCES_DIR / "Inbox"
    if not inbox.exists():
        print("[sweep] Inbox not found.")
        return
    files = list(inbox.rglob("*.md"))
    if not files:
        print("[sweep] No .md files in Inbox.")
        return
    print(f"[sweep] Found {len(files)} files.")
    for f in files:
        try:
            ingest_source(f, dry_run=args.dry_run)
        except Exception as e:
            print(f"[sweep] ERROR on {f.name}: {e}")


def cmd_search(args):
    from search_pipeline import run_pipeline
    _ensure_daemon()
    results = run_pipeline(args.query, top=args.top)
    _print_results(results)


def cmd_synth(args):
    from synthesis_search import synthesis_search
    _ensure_daemon()
    probe, results = synthesis_search(
        args.query, top=args.top, verbose=args.verbose
    )
    print(f"[probe] state={probe.state}  wiki_sem={probe.wiki_sem:.3f}  "
          f"raw_sem={probe.raw_sem:.3f}  label_hits={probe.label_hits}  "
          f"({probe.elapsed_ms}ms)")
    _print_results(results)


def cmd_probe(args):
    from synthesis_search import probe
    _ensure_daemon()
    p = probe(args.query)
    print(f"State:        {p.state}")
    print(f"wiki_sem:     {p.wiki_sem:.3f}")
    print(f"raw_sem:      {p.raw_sem:.3f}")
    print(f"wiki_fts:     {p.phrase_wiki} phrase hits, {p.label_hits} label hits, cov={p.label_cov:.2f}")
    print(f"raw_fts:      {p.phrase_raw} phrase hits")
    print(f"elapsed:      {p.elapsed_ms}ms")


def _print_results(results):
    if not results:
        print("[search] No results.")
        return
    for i, r in enumerate(results, 1):
        source_tag = f"[{r.source}]" if r.source else ""
        conf_tag   = f" conf={r.confidence}" if r.confidence else ""
        print(f"  {i:2}. [{r.score:.3f}] {r.label or r.stem} {source_tag}{conf_tag}")
        if r.thesis:
            print(f"       {r.thesis[:120]}")
        print(f"       found_by={r.found_by}  node_id={r.node_id}")


def cmd_agentic(args):
    """5-lens T_MODE_DEEP search across policy/macro/plumbing/treasury/timing."""
    from agentic_search import agentic_search, agentic_search_deep, format_lens_summary
    _ensure_daemon()
    if args.deep:
        result = agentic_search_deep(args.query, verbose=True)
    else:
        result = agentic_search(args.query, top_per_lens=args.top, verbose=True)
    print()
    print(format_lens_summary(result))
    print()
    print(f"Merged top-{len(result.merged)} results:")
    _print_results(result.merged)
    if result.gap_lenses:
        print(f"\n[agentic] TRUE_GAP lenses: {', '.join(result.gap_lenses)}")
        print("[agentic] Add these to RESEARCH.yaml gaps[] with type: TRUE_GAP")


def cmd_deep(args):
    """Thin-node detection and deep-dive augmentation.

    Usage:
      librarian deep <domain>            - search domain, augment thin nodes
      librarian deep <domain> --audit    - audit-only (list thin nodes, no search)
    """
    from deepdive_search import report_thin_nodes, deepdive_search
    from graph_rag import get_graph

    if args.audit:
        report_thin_nodes()
        return

    _ensure_daemon()
    query = args.domain
    results = deepdive_search(query, top=args.top, augment_thin=True)
    print(f"[deep] {len(results)} results for '{query}' (thin nodes augmented with raw chunks):\n")
    for i, r in enumerate(results, 1):
        ctx = f" {r.heatmap_ctx}" if r.heatmap_ctx else ""
        conf_tag = f" conf={r.confidence}" if r.confidence else ""
        print(f"  {i:2}. [{r.score:.3f}] {r.label or r.stem} [{r.source}]{conf_tag}{ctx}")
        if r.thesis:
            print(f"       {r.thesis[:120]}")

    # Graph subgraph summary
    g = get_graph()
    if g.node_count > 0:
        seed_ids = [r.node_id for r in results[:5] if r.source == "wiki"]
        if seed_ids:
            print(f"\n[graph] {g.topic_subgraph_summary(seed_ids)}")


def cmd_lint(args):
    from linter import run_lint
    issues = run_lint(fix=args.fix)
    n_blocking = sum(1 for i in issues if i.get("severity") == "blocking")
    n_warning  = sum(1 for i in issues if i.get("severity") == "warning")
    print(f"[lint] {len(issues)} issues ({n_blocking} blocking, {n_warning} warnings).")


def cmd_link(args):
    from linker import run_link_audit
    report = run_link_audit(fix=args.fix)
    print(f"[link] {report['broken']} broken links, {report['orphans']} orphans.")


def cmd_gaps(args):
    from gap_manager import list_gaps, suggest_sources, close_gap
    action = getattr(args, "action", "list")
    if action == "list":
        gaps = list_gaps()
        if not gaps:
            print("[gaps] No gaps logged.")
        for g in gaps:
            print(f"  [{g.get('state','?')}] {g.get('query','?')}  ({g.get('timestamp','')[:10]})")
    elif action == "suggest":
        gaps = list_gaps()
        for g in gaps:
            suggest_sources(g.get("query", ""), g.get("topic", ""))
    elif action == "close":
        if not args.query:
            print("[gaps] Provide --query to close.")
        else:
            close_gap(args.query)


def cmd_status(args):
    """System health overview."""
    from dense_index import DenseIndex
    from sparse_index import SparseIndex, FTSIndex
    from bge_m3_daemon import is_running

    dense_st  = DenseIndex().status()
    sparse_st = SparseIndex().status()
    fts_st    = FTSIndex().status()

    wiki_nodes = sum(1 for _ in WIKI_ROOT.rglob("*.md")
                     if _.name not in ("index.md", "log.md"))

    registry = ROOT / "02_sources" / "_source_registry.yaml"
    import yaml
    reg_data = yaml.safe_load(registry.read_text(encoding="utf-8")) if registry.exists() else {}
    meta = reg_data.get("meta", {})

    print("=" * 50)
    print("Wiki-Agentic System Status")
    print("=" * 50)
    print(f"Daemon:        {'Running' if is_running() else 'Stopped'}")
    print(f"Wiki nodes:    {wiki_nodes}")
    print(f"Dense index:   {'Built' if dense_st.get('built') else 'Not built'}"
          + (f" ({dense_st.get('docs', 0)} docs)" if dense_st.get("built") else ""))
    print(f"Sparse index:  {'Built' if sparse_st.get('built') else 'Not built'}"
          + (f" ({sparse_st.get('docs', 0)} docs, {sparse_st.get('postings', 0)} postings)" if sparse_st.get("built") else ""))
    print(f"FTS5 index:    {'Built' if fts_st.get('built') else 'Not built'}"
          + (f" ({fts_st.get('docs', 0)} docs)" if fts_st.get("built") else ""))
    print(f"Sources:       {meta.get('total_sources', '?')} total, "
          f"{meta.get('total_ingested', 0)} ingested "
          f"({meta.get('coverage_pct', 0)}%)")
    gap_file = CACHE_DIR / "gap_queue.jsonl"
    n_gaps = sum(1 for _ in gap_file.open(encoding="utf-8")) if gap_file.exists() else 0
    print(f"Gap queue:     {n_gaps} entries")
    print("=" * 50)


def cmd_session_close(args):
    """Summarize TEMPLATE_INSIGHTs from a completed research session."""
    from gap_manager import summarize_session_insights
    summarize_session_insights(args.topic_slug)


def cmd_template_show(args):
    insight_file = ROOT / "06_templates" / "_insights" / "pending" / f"{args.insight_id}.yaml"
    if not insight_file.exists():
        print(f"[template] Insight '{args.insight_id}' not found in pending/")
        return
    import yaml
    data = yaml.safe_load(insight_file.read_text(encoding="utf-8"))
    print(yaml.dump(data, allow_unicode=True, default_flow_style=False))


def cmd_template_apply(args):
    """Apply one or more template insights."""
    from gap_manager import apply_template_insight
    if args.priority:
        _apply_by_priority(args.priority)
    else:
        apply_template_insight(args.insight_id)


def _apply_by_priority(priority: str):
    from gap_manager import apply_template_insight
    import yaml
    pending_dir = ROOT / "06_templates" / "_insights" / "pending"
    if not pending_dir.exists():
        print("[template] No pending insights.")
        return
    for f in pending_dir.glob("*.yaml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if data.get("priority") == priority:
            apply_template_insight(f.stem)


def cmd_template_reject(args):
    from gap_manager import reject_template_insight
    reject_template_insight(args.insight_id, reason=getattr(args, "reason", ""))


# ── Argument parser ────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="librarian", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command")

    # daemon
    d = sub.add_parser("daemon")
    d.add_argument("action", choices=["start", "stop", "status"])

    # sync
    s = sub.add_parser("sync")
    s.add_argument("--incremental", action="store_true")

    # embed
    e = sub.add_parser("embed")
    e.add_argument("--incremental", action="store_true")

    # ingest
    i = sub.add_parser("ingest")
    i.add_argument("source_path")
    i.add_argument("--dry-run", action="store_true")

    # sweep
    sw = sub.add_parser("sweep")
    sw.add_argument("--dry-run", action="store_true")

    # search
    sr = sub.add_parser("search")
    sr.add_argument("query")
    sr.add_argument("--top", type=int, default=10)

    # synth
    sy = sub.add_parser("synth")
    sy.add_argument("query")
    sy.add_argument("--top", type=int, default=10)
    sy.add_argument("-v", "--verbose", action="store_true")

    # probe
    pr = sub.add_parser("probe")
    pr.add_argument("query")

    # agentic
    ag = sub.add_parser("agentic")
    ag.add_argument("query")
    ag.add_argument("--top", type=int, default=6)
    ag.add_argument("--deep", action="store_true", help="Run 2 variants per lens (T_MODE_DEEP)")

    # deep
    dp = sub.add_parser("deep")
    dp.add_argument("domain", help="Query or domain name (e.g. 'monetary_policy')")
    dp.add_argument("--top", type=int, default=10)
    dp.add_argument("--audit", action="store_true", help="Audit-only: list thin nodes")

    # lint
    lt = sub.add_parser("lint")
    lt.add_argument("--fix", action="store_true")

    # link
    lk = sub.add_parser("link")
    lk.add_argument("--fix", action="store_true")

    # gaps
    gp = sub.add_parser("gaps")
    gp.add_argument("action", choices=["list", "suggest", "close"], default="list", nargs="?")
    gp.add_argument("--query", default="")

    # status
    sub.add_parser("status")

    # session-close
    sc = sub.add_parser("session-close")
    sc.add_argument("topic_slug")

    # template-show
    ts = sub.add_parser("template-show")
    ts.add_argument("insight_id")

    # template-apply
    ta = sub.add_parser("template-apply")
    ta.add_argument("insight_id", nargs="?", default="")
    ta.add_argument("--priority", default="")

    # template-reject
    tr = sub.add_parser("template-reject")
    tr.add_argument("insight_id")
    tr.add_argument("--reason", default="")

    return p


COMMAND_MAP = {
    "daemon":          cmd_daemon,
    "sync":            cmd_sync,
    "embed":           cmd_embed,
    "ingest":          cmd_ingest,
    "sweep":           cmd_sweep,
    "search":          cmd_search,
    "synth":           cmd_synth,
    "probe":           cmd_probe,
    "agentic":         cmd_agentic,
    "deep":            cmd_deep,
    "lint":            cmd_lint,
    "link":            cmd_link,
    "gaps":            cmd_gaps,
    "status":          cmd_status,
    "session-close":   cmd_session_close,
    "template-show":   cmd_template_show,
    "template-apply":  cmd_template_apply,
    "template-reject": cmd_template_reject,
}


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    handler = COMMAND_MAP.get(args.command)
    if handler:
        handler(args)
    else:
        print(f"Unknown command: {args.command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
