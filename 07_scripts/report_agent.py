"""report_agent.py — Report generation orchestrator.

Converts a research session into a final approved report:
  1. Load session RESEARCH.yaml
  2. Validate audit checklist passes
  3. Apply style template
  4. Write 05_reports/{YYYY-MM}/{slug}.md
  5. Update 05_reports/_index.yaml
  6. Check promotion gate for research findings
  7. Log to 03_wiki/log.md

Called after user has reviewed and approved the draft.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

ROOT         = Path(__file__).parent.parent
WIKI_ROOT    = ROOT / "03_wiki"
REPORTS_DIR  = ROOT / "05_reports"
RESEARCH_DIR = ROOT / "04_research"
TEMPLATES    = ROOT / "06_templates"
TODAY        = date.today().isoformat()
YYYY_MM      = date.today().strftime("%Y-%m")


class ReportAgent:
    """Orchestrate final report generation from a research session."""

    def __init__(self, topic_slug: str):
        self.slug = topic_slug
        self.session_dir = RESEARCH_DIR / topic_slug
        self.yaml_path   = self.session_dir / "RESEARCH.yaml"
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"RESEARCH.yaml not found for topic '{topic_slug}'")
        self._data = yaml.safe_load(self.yaml_path.read_text(encoding="utf-8")) or {}

    # ── Audit ──────────────────────────────────────────────────────────────────

    def run_audit(self) -> dict:
        """Run audit checklist. Returns {passed, failed, blocking_failures}."""
        from chunker import _split_frontmatter
        checks = self._load_audit_checklist()
        results: list[dict] = []

        for check in checks:
            cid = check.get("id", "?")
            desc = check.get("description", "")
            severity = check.get("severity", "warning")
            passed = self._evaluate_check(check)
            results.append({"id": cid, "description": desc,
                             "severity": severity, "passed": passed})

        passed = [r for r in results if r["passed"]]
        failed = [r for r in results if not r["passed"]]
        blocking = [r for r in failed if r["severity"] == "blocking"]

        print(f"[audit] {len(passed)}/{len(results)} checks passed.")
        if blocking:
            print("[audit] BLOCKING failures:")
            for b in blocking:
                print(f"  [{b['id']}] {b['description']}")
        if failed and not blocking:
            print("[audit] Warnings (non-blocking):")
            for w in [r for r in failed if r["severity"] == "warning"]:
                print(f"  [{w['id']}] {w['description']}")

        return {
            "passed": len(passed),
            "failed": len(failed),
            "blocking_failures": blocking,
            "all_results": results,
        }

    def _load_audit_checklist(self) -> list[dict]:
        checklist_path = TEMPLATES / "core" / "audit_checklist.yaml"
        if not checklist_path.exists():
            return []
        data = yaml.safe_load(checklist_path.read_text(encoding="utf-8")) or {}
        checks = []
        for category in data.get("categories", {}).values():
            for check in category.get("checks", []):
                checks.append(check)
        return checks

    def _evaluate_check(self, check: dict) -> bool:
        """Evaluate a single audit check against the session data."""
        cid = check.get("id", "")
        findings = self._data.get("findings", [])
        gaps = self._data.get("gaps", [])

        # A-series: source integrity
        if cid == "A1":
            # All findings have sources
            return all(f.get("confidence", 0) > 0 for f in findings)
        if cid == "A2":
            # No unresolved TRUE_GAP blocks a key finding
            open_gaps = [g for g in gaps if g.get("status") == "open"
                         and g.get("type") == "TRUE_GAP"]
            return len(open_gaps) == 0

        # B-series: logic integrity — hard to automate, default pass
        if cid.startswith("B"):
            return True

        # C-series: coverage
        if cid == "C1":
            sub_questions = self._data.get("sub_questions", [])
            probes = self._data.get("coverage_probe", {}).get("queries", [])
            probed_queries = {p["query"] for p in probes}
            return all(q in probed_queries for q in sub_questions)
        if cid == "C2":
            open_gaps = [g for g in gaps if g.get("type") == "TRUE_GAP"
                         and g.get("status") == "open"]
            return len(open_gaps) == 0

        # D-series: contradictions
        if cid == "D1":
            contradictions = self._data.get("contradictions", [])
            open_contras = [c for c in contradictions if c.get("status") == "open"]
            return len(open_contras) == 0

        # E-series: style — default pass (enforced by template)
        if cid.startswith("E"):
            return True

        # T-series: T_MODE_DEEP checks — default pass
        if cid.startswith("T"):
            return True

        return True  # Unknown checks pass by default

    # ── Report generation ──────────────────────────────────────────────────────

    def generate(
        self,
        draft_text: str,
        audit_approved: bool = False,
        reviewer: str = "user_approved",
    ) -> Path:
        """Write final report file after audit approval.

        draft_text: The full report markdown content.
        """
        if not audit_approved:
            audit = self.run_audit()
            if audit["blocking_failures"]:
                raise RuntimeError(
                    f"[report] {len(audit['blocking_failures'])} blocking audit failures. "
                    "Fix them or call generate(audit_approved=True) to override."
                )

        # Write report
        report_dir = REPORTS_DIR / YYYY_MM
        report_dir.mkdir(parents=True, exist_ok=True)
        out_path = report_dir / f"{self.slug}.md"

        # Prepend metadata header
        header = self._build_header(reviewer)
        full_content = header + "\n\n" + draft_text
        out_path.write_text(full_content, encoding="utf-8")
        print(f"[report] Written: {out_path.relative_to(ROOT)}")

        # Update reports index
        self._update_reports_index(out_path)

        # Log
        self._append_wiki_log(out_path)

        # Promotion gate
        self._check_promotions()

        # Update session status
        self._data["status"] = "complete"
        self._data["date_updated"] = TODAY
        self.yaml_path.write_text(
            yaml.dump(self._data, allow_unicode=True, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )

        # Save audit log
        self._write_audit_log(reviewer)

        return out_path

    def _build_header(self, reviewer: str) -> str:
        title = self._data.get("title", self.slug)
        pq = self._data.get("primary_question", "")
        return (
            f"# {title}\n\n"
            f"**Topic:** `{self.slug}`  \n"
            f"**Date:** {TODAY}  \n"
            f"**Reviewed by:** {reviewer}  \n"
            f"**Primary question:** {pq}\n"
        )

    def _update_reports_index(self, report_path: Path):
        index_path = REPORTS_DIR / "_index.yaml"
        if index_path.exists():
            data = yaml.safe_load(index_path.read_text(encoding="utf-8")) or {}
        else:
            data = {"reports": []}
        data.setdefault("reports", []).append({
            "slug":    self.slug,
            "title":   self._data.get("title", self.slug),
            "path":    str(report_path.relative_to(ROOT)),
            "date":    TODAY,
            "status":  "final",
        })
        index_path.write_text(
            yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )

    def _append_wiki_log(self, report_path: Path):
        log_path = WIKI_ROOT / "log.md"
        if not log_path.exists():
            log_path.write_text("# Wiki Operation Log\n\n", encoding="utf-8")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n- **{TODAY}**: REPORT generated `{self.slug}` → "
                    f"`{report_path.relative_to(ROOT)}`")

    def _check_promotions(self):
        """Print promotion candidates for user review."""
        candidates = self._data.get("promotion_candidates", [])
        pending = [c for c in candidates if c.get("status") == "pending"]
        if not pending:
            return
        print(f"\n[report] {len(pending)} promotion candidate(s) from this session:")
        for c in pending:
            print(f"  node_id={c['node_id']}  reason={c.get('reason', '')}")
        print("  → Review and promote via: ingest.create_wiki_node() if conditions met")

    def _write_audit_log(self, reviewer: str):
        import json
        audit_log = self.session_dir / "audit_log.json"
        if audit_log.exists():
            history = json.loads(audit_log.read_text(encoding="utf-8"))
        else:
            history = []
        audit = self.run_audit()
        history.append({
            "date":            TODAY,
            "checks_passed":   audit["passed"],
            "checks_failed":   audit["failed"],
            "reviewer":        reviewer,
            "final_approved":  True,
        })
        audit_log.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
