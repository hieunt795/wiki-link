"""Coverage-aware search: probe first, then route to the right search layer.

Coverage probe classifies a query into one of three states:
  INGESTED  — topic is well-represented in the wiki → search wiki first
  PENDING   — topic exists in raw sources but not yet wiki → search raw
  TRUE_GAP  — topic not in corpus at all → STOP, log gap

This probe costs ~120ms and prevents wasted search effort on TRUE_GAP queries.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from models import Probe, SearchResult
from bge_m3_daemon import query_daemon
from sparse_index import FTSIndex
from search_pipeline import run_pipeline
from vi_en import is_vietnamese, vi_augment

GAP_QUEUE = Path(__file__).parent.parent / ".cache" / "gap_queue.jsonl"
_fts = FTSIndex()

# ── Probe thresholds (calibrate after first 50 research queries) ───────────────
INGESTED_DENSE_THRESHOLD  = 0.65
INGESTED_LABEL_MIN_HITS   = 1
INGESTED_PHRASE_MIN_HITS  = 3
INGESTED_LABEL_COV_MIN    = 0.60
PENDING_DENSE_THRESHOLD   = 0.55
PENDING_PHRASE_MIN_HITS   = 2


def probe(query: str, topic: str = "") -> Probe:
    """Run coverage probe and return Probe with state classification.

    Runs 4 checks in parallel (conceptually):
      A. BGE-M3 dense → wiki
      B. BGE-M3 dense → raw sources
      C. FTS5 → wiki (phrase hits + label hits + label coverage)
      D. FTS5 → raw (phrase hits)
    """
    t0 = time.time()

    # Augment VI queries for FTS5
    fts_query = vi_augment(query) if is_vietnamese(query) else query

    # A & B: dense search
    wiki_dense = query_daemon(query, mode="dense", top_k=5, wiki_only=True)
    raw_dense  = query_daemon(query, mode="dense", top_k=5, raw_only=True)

    wiki_dense_results = wiki_dense.get("dense_results", []) if isinstance(wiki_dense, dict) else wiki_dense
    raw_dense_results  = raw_dense.get("dense_results",  []) if isinstance(raw_dense,  dict) else raw_dense

    wiki_sem = wiki_dense_results[0]["score"] if wiki_dense_results else 0.0
    raw_sem  = raw_dense_results[0]["score"]  if raw_dense_results  else 0.0

    # C: FTS5 wiki probing
    wiki_phrase_hits  = _fts.phrase_hit_count(fts_query, source="wiki")
    wiki_label_hits   = _fts.label_hits(fts_query, source="wiki")
    wiki_label_cov    = _fts.label_token_coverage(fts_query, source="wiki")

    # D: FTS5 raw probing
    raw_phrase_hits = _fts.phrase_hit_count(fts_query, source="raw")

    # State classification (evaluated in priority order — first match wins)
    if (
        (wiki_sem > INGESTED_DENSE_THRESHOLD and wiki_label_hits >= INGESTED_LABEL_MIN_HITS)
        or (wiki_phrase_hits >= INGESTED_PHRASE_MIN_HITS and wiki_label_cov >= INGESTED_LABEL_COV_MIN)
    ):
        state = "INGESTED"
    elif raw_sem > PENDING_DENSE_THRESHOLD or raw_phrase_hits >= PENDING_PHRASE_MIN_HITS:
        state = "PENDING"
    else:
        state = "TRUE_GAP"
        _log_gap(query, topic, wiki_sem, raw_sem)

    elapsed = int((time.time() - t0) * 1000)
    return Probe(
        state=state,
        wiki_sem=wiki_sem,
        wiki_fts=float(wiki_phrase_hits),
        raw_sem=raw_sem,
        raw_fts=float(raw_phrase_hits),
        phrase_wiki=wiki_phrase_hits,
        phrase_raw=raw_phrase_hits,
        label_hits=wiki_label_hits,
        label_cov=wiki_label_cov,
        elapsed_ms=elapsed,
    )


def synthesis_search(
    query: str,
    top: int = 10,
    topic: str = "",
    verbose: bool = False,
) -> tuple[Probe, list[SearchResult]]:
    """Coverage-aware search. Returns (probe_result, results).

    Routing:
      INGESTED → search_pipeline(wiki_only=True)
      PENDING  → search_pipeline(raw_only=True)
      TRUE_GAP → return empty results + log gap
    """
    p = probe(query, topic=topic)

    if verbose:
        print(f"[synth] state={p.state} wiki_sem={p.wiki_sem:.3f} raw_sem={p.raw_sem:.3f} "
              f"label_hits={p.label_hits} phrase_wiki={p.phrase_wiki} ({p.elapsed_ms}ms)")

    if p.state == "INGESTED":
        results = run_pipeline(query, top=top, wiki_only=True)
    elif p.state == "PENDING":
        results = run_pipeline(query, top=top, raw_only=False)  # search both, wiki supplement
    else:  # TRUE_GAP
        _print_gap_message(query)
        results = []

    return p, results


def _log_gap(query: str, topic: str, wiki_sem: float, raw_sem: float):
    GAP_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "query":     query,
        "state":     "TRUE_GAP",
        "topic":     topic,
        "wiki_sem":  round(wiki_sem, 3),
        "raw_sem":   round(raw_sem, 3),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    with open(GAP_QUEUE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _print_gap_message(query: str):
    msg = (
        f'[TRUE_GAP] "{query}"\n'
        "  -> No relevant sources found in wiki or raw corpus.\n"
        "  -> Gap logged to .cache/gap_queue.jsonl\n"
        "  -> Add this to RESEARCH.yaml gaps[] with type: TRUE_GAP\n"
        "  -> Suggested source types:\n"
        "      Monetary:  BIS WP, Fed FEDS notes, ECB WP, IMF WP\n"
        "      Basel:     BCBS consultative papers, BIS Quarterly Review, FSB reports\n"
        "      Markets:   ISDA, SIFMA, Federal Reserve FEDS notes, NY Fed SR\n"
        "      Macro:     IMF WEO, BIS Annual Report, NBER working papers"
    )
    print(msg.encode("ascii", errors="replace").decode("ascii"))


def get_gap_queue() -> list[dict]:
    """Read all logged gaps from gap_queue.jsonl."""
    if not GAP_QUEUE.exists():
        return []
    gaps = []
    with open(GAP_QUEUE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    gaps.append(json.loads(line))
                except Exception:
                    pass
    return gaps
