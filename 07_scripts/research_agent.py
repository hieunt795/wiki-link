"""research_agent.py — Research session orchestrator.

Manages the lifecycle of a 04_research/{topic_slug}/ session:
  1. Initialize session from RESEARCH.yaml
  2. Run coverage probe for all sub-questions
  3. Route queries to appropriate search layer
  4. Track findings and gaps
  5. Identify promotion candidates

Called by the agent directly; not a standalone CLI (use librarian.py).
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

from models import SearchResult, Probe
from synthesis_search import synthesis_search, probe as run_probe
from agentic_search import agentic_search, format_lens_summary

ROOT        = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "04_research"
TODAY = date.today().isoformat()


class ResearchSession:
    """Wraps a 04_research/{slug}/ directory and manages its RESEARCH.yaml state."""

    def __init__(self, topic_slug: str):
        self.slug = topic_slug
        self.dir = RESEARCH_DIR / topic_slug
        self.yaml_path = self.dir / "RESEARCH.yaml"
        self._data: dict = {}
        self._load()

    def _load(self):
        if self.yaml_path.exists():
            self._data = yaml.safe_load(self.yaml_path.read_text(encoding="utf-8")) or {}
        else:
            self._data = {}

    def _save(self):
        self.yaml_path.write_text(
            yaml.dump(self._data, allow_unicode=True, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )

    @classmethod
    def create(
        cls,
        topic_slug: str,
        title: str,
        primary_question: str,
        sub_questions: list[str] | None = None,
        template: str = "",
        output_style: str = "research_memo",
    ) -> "ResearchSession":
        """Initialize a new research session from the template scaffold."""
        session_dir = RESEARCH_DIR / topic_slug
        session_dir.mkdir(parents=True, exist_ok=True)
        for subdir in ("findings", "data", "drafts", "final"):
            (session_dir / subdir).mkdir(exist_ok=True)

        data = {
            "topic_slug":       topic_slug,
            "title":            title,
            "status":           "active",
            "primary_question": primary_question,
            "sub_questions":    sub_questions or [],
            "coverage_probe":   {"queries": []},
            "sources_used":     {"wiki": [], "raw": [], "fresh_data": []},
            "findings":         [],
            "gaps":             [],
            "contradictions":   [],
            "promotion_candidates": [],
            "template":         template,
            "output_style":     output_style,
            "date_created":     TODAY,
            "date_updated":     TODAY,
        }

        session = cls.__new__(cls)
        session.slug = topic_slug
        session.dir = session_dir
        session.yaml_path = session_dir / "RESEARCH.yaml"
        session._data = data
        session._save()
        print(f"[research] Created session: {topic_slug}")
        return session

    # ── Coverage probe ─────────────────────────────────────────────────────────

    def probe_all(self, verbose: bool = False) -> list[dict]:
        """Run coverage probe for all sub-questions + primary question."""
        queries = [self._data.get("primary_question", "")]
        queries += self._data.get("sub_questions", [])
        queries = [q for q in queries if q]

        probe_results = []
        for q in queries:
            p = run_probe(q)
            entry = {
                "query":       q,
                "state":       p.state,
                "wiki_sem":    round(p.wiki_sem, 3),
                "raw_sem":     round(p.raw_sem, 3),
                "label_hits":  p.label_hits,
                "phrase_wiki": p.phrase_wiki,
                "elapsed_ms":  p.elapsed_ms,
            }
            probe_results.append(entry)
            if verbose:
                print(f"  [{p.state:8s}] {q[:80]}")

        # Update RESEARCH.yaml
        self._data["coverage_probe"]["queries"] = probe_results
        self._data["date_updated"] = TODAY
        self._save()
        return probe_results

    # ── Search ─────────────────────────────────────────────────────────────────

    def search(
        self,
        query: str,
        mode: str = "auto",
        top: int = 10,
        verbose: bool = False,
    ) -> tuple[Probe, list[SearchResult]]:
        """Search with coverage-aware routing.

        mode: 'auto' (coverage probe) | 'wiki' | 'raw' | 'agentic'
        """
        if mode == "agentic":
            agentic_result = agentic_search(query, top_per_lens=5, topic=self.slug, verbose=verbose)
            probe = agentic_result.lenses[0].probe if agentic_result.lenses else None
            return probe, agentic_result.merged

        probe, results = synthesis_search(query, top=top, topic=self.slug, verbose=verbose)
        self._track_sources(results)
        return probe, results

    def _track_sources(self, results: list[SearchResult]):
        """Add discovered nodes/sources to sources_used."""
        wiki_set  = set(self._data["sources_used"]["wiki"])
        raw_set   = set(self._data["sources_used"]["raw"])
        for r in results:
            if r.source == "wiki" and r.node_id:
                wiki_set.add(r.node_id)
            elif r.source == "raw" and r.source_file:
                raw_set.add(r.source_file)
        self._data["sources_used"]["wiki"] = sorted(wiki_set)
        self._data["sources_used"]["raw"]  = sorted(raw_set)

    # ── Findings ───────────────────────────────────────────────────────────────

    def log_finding(
        self,
        title: str,
        content: str,
        confidence: int = 2,
        sources: list[str] | None = None,
        promote: bool = False,
    ) -> Path:
        """Write a finding to findings/ and update RESEARCH.yaml."""
        from ingest import _slugify
        slug = _slugify(title)
        out_path = self.dir / "findings" / f"{slug}.md"

        fm = {
            "title":      title,
            "confidence": confidence,
            "sources":    sources or [],
            "promote":    promote,
            "status":     "draft",
            "date":       TODAY,
        }
        fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
        full_content = f"---\n{fm_str}---\n\n{content}\n"
        out_path.write_text(full_content, encoding="utf-8")

        # Track in RESEARCH.yaml
        self._data["findings"].append({
            "file":       str(out_path.relative_to(self.dir)),
            "title":      title,
            "confidence": confidence,
            "status":     "draft",
            "promote":    promote,
        })
        self._data["date_updated"] = TODAY
        self._save()
        print(f"[research] Finding saved: {out_path.name}")
        return out_path

    def log_gap(
        self,
        query: str,
        gap_type: str = "TRUE_GAP",
        note: str = "",
        action_required: str = "",
    ):
        """Log a gap to RESEARCH.yaml."""
        self._data["gaps"].append({
            "query":           query,
            "type":            gap_type,
            "gap_note":        note,
            "action_required": action_required,
            "status":          "open",
            "date":            TODAY,
        })
        self._data["date_updated"] = TODAY
        self._save()
        print(f"[research] Gap logged: {query[:60]}")

    def flag_promotion(self, node_id: str, reason: str = ""):
        """Flag a finding/wiki node as promotion candidate."""
        self._data["promotion_candidates"].append({
            "node_id": node_id,
            "reason":  reason,
            "status":  "pending",
        })
        self._data["date_updated"] = TODAY
        self._save()

    # ── Status ─────────────────────────────────────────────────────────────────

    def summary(self) -> str:
        d = self._data
        n_findings = len(d.get("findings", []))
        n_gaps     = len(d.get("gaps", []))
        n_promo    = len(d.get("promotion_candidates", []))
        probes     = d.get("coverage_probe", {}).get("queries", [])
        n_ingested = sum(1 for p in probes if p.get("state") == "INGESTED")
        n_pending  = sum(1 for p in probes if p.get("state") == "PENDING")
        n_gap_p    = sum(1 for p in probes if p.get("state") == "TRUE_GAP")

        return (
            f"Session: {d.get('topic_slug')}  [{d.get('status', '?')}]\n"
            f"  Coverage probe: {n_ingested} INGESTED, {n_pending} PENDING, {n_gap_p} TRUE_GAP\n"
            f"  Findings: {n_findings}  Gaps: {n_gaps}  Promotions: {n_promo}\n"
            f"  Last updated: {d.get('date_updated', '?')}"
        )

    def close(self, status: str = "complete"):
        """Mark session as complete and summarize template insights."""
        self._data["status"] = status
        self._data["date_updated"] = TODAY
        self._save()
        print(f"[research] Session '{self.slug}' marked {status}.")

        # Trigger template insight summary
        from gap_manager import summarize_session_insights
        summarize_session_insights(self.slug)
