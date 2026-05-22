"""agentic_search.py — 5-lens multi-perspective search for T_MODE_DEEP.

Runs 5 parallel query variants (lenses) through the pipeline:
  Policy    — regulatory, CB decision-making angle
  Macro     — regime, output gap, fiscal stance angle
  Plumbing  — reserve flows, balance sheet, repo, collateral angle
  Treasury  — desk positioning, duration, DV01, curve angle
  Timing    — historical precedent, cycle timing angle

Each lens queries synthesis_search independently.
Results are merged, deduped, and ranked by aggregate score.

Used by research_agent.py for deep-dive sessions.
"""

from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from models import SearchResult, Probe
from synthesis_search import synthesis_search


@dataclass
class LensResult:
    lens: str
    probe: Probe
    results: list[SearchResult]


@dataclass
class AgenticSearchResult:
    query: str
    lenses: list[LensResult] = field(default_factory=list)
    merged: list[SearchResult] = field(default_factory=list)
    gap_lenses: list[str] = field(default_factory=list)
    elapsed_ms: int = 0


# ── Lens query builders ────────────────────────────────────────────────────────

LENS_TEMPLATES = {
    "policy": [
        "{query} policy framework",
        "{query} regulatory",
        "{query} central bank decision",
    ],
    "macro": [
        "{query} macro regime",
        "{query} output gap inflation",
        "{query} fiscal monetary interaction",
    ],
    "plumbing": [
        "{query} reserve flow balance sheet",
        "{query} repo collateral liquidity",
        "{query} transmission mechanism",
    ],
    "treasury": [
        "{query} yield curve duration positioning",
        "{query} DV01 spread hedge",
        "{query} market structure pricing",
    ],
    "timing": [
        "{query} historical precedent cycle",
        "{query} timing phase transition",
        "{query} past present future trajectory",
    ],
}


def _build_lens_query(lens: str, base_query: str, variant: int = 0) -> str:
    templates = LENS_TEMPLATES.get(lens, ["{query}"])
    tmpl = templates[variant % len(templates)]
    return tmpl.format(query=base_query)


# ── Main agentic search ────────────────────────────────────────────────────────

def agentic_search(
    query: str,
    top_per_lens: int = 6,
    top_merged: int = 15,
    topic: str = "",
    verbose: bool = False,
) -> AgenticSearchResult:
    """Run 5-lens search and merge results.

    For each lens, uses the primary template variant. Lenses that return
    TRUE_GAP are noted in gap_lenses.
    """
    t0 = time.time()
    result = AgenticSearchResult(query=query)

    for lens in LENS_TEMPLATES:
        lens_query = _build_lens_query(lens, query, variant=0)
        probe, results = synthesis_search(
            lens_query, top=top_per_lens, topic=topic, verbose=False
        )
        lr = LensResult(lens=lens, probe=probe, results=results)
        result.lenses.append(lr)
        if probe.state == "TRUE_GAP":
            result.gap_lenses.append(lens)
        if verbose:
            print(f"  [{lens:8s}] state={probe.state:8s} results={len(results)}")

    # Merge and dedup by node_id, keeping highest per-lens score
    merged_scores: dict[str, float] = defaultdict(float)
    merged_data: dict[str, SearchResult] = {}

    for lr in result.lenses:
        for r in lr.results:
            nid = r.node_id
            # Add fractional score weighted by lens importance
            merged_scores[nid] += r.score
            if nid not in merged_data or r.score > merged_data[nid].score:
                merged_data[nid] = r

    result.merged = sorted(
        merged_data.values(),
        key=lambda r: -merged_scores[r.node_id]
    )[:top_merged]

    result.elapsed_ms = int((time.time() - t0) * 1000)

    if verbose:
        print(f"\n[agentic] {len(result.merged)} merged results in {result.elapsed_ms}ms")
        if result.gap_lenses:
            print(f"[agentic] TRUE_GAP lenses: {result.gap_lenses}")

    return result


def agentic_search_deep(
    query: str,
    topic: str = "",
    verbose: bool = False,
) -> AgenticSearchResult:
    """Extended search: runs 2 variants per lens for broader coverage.

    Use for T_MODE_DEEP analysis sessions.
    """
    t0 = time.time()
    result = AgenticSearchResult(query=query)

    for lens in LENS_TEMPLATES:
        for variant in range(2):
            lens_query = _build_lens_query(lens, query, variant=variant)
            probe, results = synthesis_search(
                lens_query, top=8, topic=topic, verbose=False
            )
            lr = LensResult(lens=f"{lens}_v{variant}", probe=probe, results=results)
            result.lenses.append(lr)
            if probe.state == "TRUE_GAP" and variant == 0:
                result.gap_lenses.append(lens)

    # Merge
    merged_scores: dict[str, float] = defaultdict(float)
    merged_data: dict[str, SearchResult] = {}
    for lr in result.lenses:
        for r in lr.results:
            nid = r.node_id
            merged_scores[nid] += r.score * 0.9 ** int(lr.lens[-1])  # decay variant 1
            if nid not in merged_data or r.score > merged_data[nid].score:
                merged_data[nid] = r

    result.merged = sorted(
        merged_data.values(),
        key=lambda r: -merged_scores[r.node_id]
    )[:20]
    result.elapsed_ms = int((time.time() - t0) * 1000)

    if verbose:
        print(f"[agentic_deep] {len(result.merged)} merged, {result.elapsed_ms}ms")

    return result


def format_lens_summary(result: AgenticSearchResult) -> str:
    """Format a compact lens summary for inclusion in analysis context."""
    lines = [f"Agentic search: '{result.query}'  ({result.elapsed_ms}ms)"]
    lines.append(f"{'Lens':10s} {'State':10s} {'Hits':>5s}  Top result")
    lines.append("-" * 70)
    for lr in result.lenses:
        top_label = lr.results[0].label[:40] if lr.results else "(none)"
        state = lr.probe.state
        lines.append(f"{lr.lens:10s} {state:10s} {len(lr.results):5d}  {top_label}")
    if result.gap_lenses:
        lines.append(f"\nGAP lenses: {', '.join(result.gap_lenses)}")
    return "\n".join(lines)
