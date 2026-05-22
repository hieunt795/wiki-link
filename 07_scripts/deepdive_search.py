"""deepdive_search.py — Thin-node detection and deep-dive retrieval.

A "thin" wiki node has:
  - confidence <= 1 OR marked [LLM]
  - body < 200 chars (stub)
  - Few incoming links (orphan risk)
  - No empirical evidence cited

deepdive_search() identifies thin nodes in search results and
augments them with relevant raw source chunks.
"""

from __future__ import annotations

import re
from pathlib import Path

from models import SearchResult
from chunker import _split_frontmatter
from search_pipeline import run_pipeline

WIKI_ROOT = Path(__file__).parent.parent / "03_wiki"


def is_thin_node(result: SearchResult) -> bool:
    """Heuristic thinness check for a SearchResult."""
    # LLM-generated stubs
    if "[LLM]" in (result.thesis or ""):
        return True
    # Low confidence
    try:
        if int(result.confidence or "0") <= 1:
            return True
    except (ValueError, TypeError):
        return True
    # Short body
    if len(result.body or "") < 200:
        return True
    return False


def deepdive_search(
    query: str,
    top: int = 10,
    augment_thin: bool = True,
) -> list[SearchResult]:
    """Search wiki; for thin nodes, augment with raw source results.

    Strategy:
      1. Run normal pipeline (wiki_only=False)
      2. For each thin node in top results, pull raw chunks that match
      3. Annotate with `heatmap_ctx` showing thin + augment note
    """
    results = run_pipeline(query, top=top, wiki_only=False)

    if not augment_thin:
        return results

    # Find thin nodes
    thin_nodes = [r for r in results if is_thin_node(r) and r.source == "wiki"]

    if not thin_nodes:
        return results

    # Augment: pull raw chunks for thin nodes
    # Query raw source specifically
    raw_results = run_pipeline(query, top=top, raw_only=True)

    # Build augmented list: non-thin wiki first, then raw chunks, then thin wiki
    non_thin = [r for r in results if not is_thin_node(r) or r.source != "wiki"]
    augmented_thin: list[SearchResult] = []

    for thin in thin_nodes:
        thin.heatmap_ctx = f"[THIN: conf={thin.confidence}]"
        augmented_thin.append(thin)

    for r in raw_results:
        r.heatmap_ctx = "[RAW augment]"

    # Merge: put raw results where thin nodes were
    merged: list[SearchResult] = []
    raw_inserted = False
    for r in results:
        if is_thin_node(r) and r.source == "wiki" and not raw_inserted:
            # Insert raw augmentation at the position of the first thin node
            merged.extend(raw_results[:3])
            raw_inserted = True
        merged.append(r)

    # Dedup by node_id
    seen: set[str] = set()
    deduped: list[SearchResult] = []
    for r in merged:
        if r.node_id not in seen:
            seen.add(r.node_id)
            deduped.append(r)

    return deduped[:top]


def audit_thin_nodes(min_confidence: int = 2) -> list[dict]:
    """Scan all wiki nodes and return those below min_confidence or flagged [LLM].

    Returns list of {node_id, file, confidence, reason} dicts.
    """
    thin: list[dict] = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = _split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        conf = fm.get("confidence", 0)
        try:
            conf_int = int(conf)
        except (ValueError, TypeError):
            conf_int = 0
        reasons = []
        if conf_int < min_confidence:
            reasons.append(f"confidence={conf_int}")
        if "[LLM]" in text:
            reasons.append("[LLM] marker present")
        if len(body.strip()) < 200:
            reasons.append(f"body too short ({len(body.strip())} chars)")
        if reasons:
            thin.append({
                "node_id":  fm["node_id"],
                "file":     str(md_file.relative_to(WIKI_ROOT.parent)),
                "confidence": conf_int,
                "reasons":  reasons,
            })
    return thin


def report_thin_nodes():
    """Print a summary of thin nodes needing expansion."""
    thin = audit_thin_nodes()
    print(f"\n[deepdive] {len(thin)} thin nodes requiring expansion:\n")
    for t in sorted(thin, key=lambda x: x["confidence"]):
        reasons = ", ".join(t["reasons"])
        print(f"  [{t['confidence']}] {t['node_id']}  — {reasons}")
        print(f"       {t['file']}")
