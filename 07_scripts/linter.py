"""linter.py — Wiki node health checker.

Checks each wiki node .md file for:
  - Required frontmatter fields present
  - Confidence in range 1-5
  - [LLM] tag on confidence=1 nodes
  - source_refs non-empty (warning if empty)
  - thesis is a claim (not starts with "This document...")
  - node_id matches slug convention
  - Stale nodes (date_updated > threshold for type)
  - Duplicate node_ids

Severity levels:
  blocking — must fix before report generation
  warning  — should fix, logged but not blocking

run_lint() is called by `librarian lint`.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path

from chunker import _split_frontmatter

WIKI_ROOT = Path(__file__).parent.parent / "03_wiki"
TODAY = date.today()

REQUIRED_FIELDS = ["node_id", "type", "title", "thesis", "confidence", "source_refs"]
VALID_TYPES = {"concept", "mechanism", "entity", "relationship", "contradiction",
               "synthesis", "policy", "framework", "indicator", "regulation"}

STALE_THRESHOLDS_DAYS = {
    "policy": 90,
    "entity": 365,
    "indicator": 90,
    "mechanism": 5 * 365,
    "concept": 5 * 365,
    "framework": 3 * 365,
    "relationship": 3 * 365,
    "contradiction": 365,
    "synthesis": 365,
    "regulation": 2 * 365,
}


def run_lint(fix: bool = False) -> list[dict]:
    """Run all lint checks across wiki nodes.

    Returns list of issue dicts:
      {file, node_id, check, severity, message}
    """
    issues: list[dict] = []
    seen_ids: dict[str, str] = {}  # node_id → first file path

    for md_file in sorted(WIKI_ROOT.rglob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = _split_frontmatter(text)
        rel = str(md_file.relative_to(WIKI_ROOT.parent))

        if not fm:
            issues.append(_issue(rel, "", "missing_frontmatter", "blocking",
                                 "No YAML frontmatter found."))
            continue

        node_id = fm.get("node_id", "")

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in fm or fm[field] is None or fm[field] == "":
                issues.append(_issue(rel, node_id, f"missing_{field}", "blocking",
                                     f"Required field '{field}' is missing or empty."))

        # Duplicate node_ids
        if node_id:
            if node_id in seen_ids:
                issues.append(_issue(rel, node_id, "duplicate_node_id", "blocking",
                                     f"node_id '{node_id}' already used in {seen_ids[node_id]}"))
            else:
                seen_ids[node_id] = rel

        # Valid type
        node_type = fm.get("type", "")
        if node_type and node_type not in VALID_TYPES:
            issues.append(_issue(rel, node_id, "invalid_type", "blocking",
                                 f"type='{node_type}' not in valid set {VALID_TYPES}"))

        # Confidence range
        conf = fm.get("confidence")
        if conf is not None:
            try:
                conf_int = int(conf)
                if not 1 <= conf_int <= 5:
                    issues.append(_issue(rel, node_id, "invalid_confidence", "blocking",
                                         f"confidence={conf} out of range 1-5"))
            except (ValueError, TypeError):
                issues.append(_issue(rel, node_id, "invalid_confidence", "blocking",
                                     f"confidence='{conf}' is not an integer"))

        # [LLM] tag required for confidence=1
        if conf == 1 or conf == "1":
            if "[LLM]" not in text:
                issues.append(_issue(rel, node_id, "missing_llm_tag", "warning",
                                     "confidence=1 node should contain [LLM] marker."))

        # Thesis not a description placeholder
        thesis = fm.get("thesis", "")
        if isinstance(thesis, str) and thesis.strip().lower().startswith("this document"):
            issues.append(_issue(rel, node_id, "bad_thesis", "warning",
                                 "thesis looks like a description, not a claim."))

        # source_refs non-empty (warning only — stubs may be empty)
        source_refs = fm.get("source_refs", [])
        if isinstance(source_refs, list) and len(source_refs) == 0:
            # Only warning if confidence > 1
            sev = "warning" if (conf == 1 or conf == "1") else "blocking"
            issues.append(_issue(rel, node_id, "empty_source_refs", sev,
                                 "source_refs is empty — every node needs at least one source."))

        # Stale check
        date_updated = fm.get("date_updated", "")
        if date_updated and node_type in STALE_THRESHOLDS_DAYS:
            try:
                updated = date.fromisoformat(str(date_updated))
                delta = (TODAY - updated).days
                threshold = STALE_THRESHOLDS_DAYS[node_type]
                if delta > threshold:
                    issues.append(_issue(rel, node_id, "stale_node", "warning",
                                         f"Last updated {delta}d ago (threshold {threshold}d for {node_type})."))
            except (ValueError, TypeError):
                pass

        # node_id slug convention: lowercase alphanumeric + underscore + _NNN suffix
        if node_id and not re.match(r"^[a-z0-9_]+_\d{3}$", node_id):
            issues.append(_issue(rel, node_id, "bad_node_id_format", "warning",
                                 f"node_id '{node_id}' doesn't match slug_NNN pattern."))

    # Print summary
    blocking = [i for i in issues if i["severity"] == "blocking"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    print(f"\n[lint] {len(issues)} issues: {len(blocking)} blocking, {len(warnings)} warnings")

    for issue in blocking:
        print(f"  BLOCK  {issue['check']:30s} {issue['file']}")
        print(f"         {issue['message']}")
    for issue in warnings:
        print(f"  WARN   {issue['check']:30s} {issue['file']}")
        print(f"         {issue['message']}")

    if fix:
        _auto_fix(issues)

    return issues


def _issue(file: str, node_id: str, check: str, severity: str, message: str) -> dict:
    return {"file": file, "node_id": node_id, "check": check,
            "severity": severity, "message": message}


def _auto_fix(issues: list[dict]):
    """Apply safe auto-fixes: add missing date fields, normalize confidence strings."""
    today_str = TODAY.isoformat()
    fixed = 0
    for issue in issues:
        if issue["check"] in ("missing_date_created", "missing_date_updated"):
            path = WIKI_ROOT.parent / issue["file"]
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            field = "date_created" if "created" in issue["check"] else "date_updated"
            if f"{field}:" not in text:
                # Inject before closing ---
                text = text.replace("---\n\n", f"---\n{field}: {today_str}\n\n", 1)
                path.write_text(text, encoding="utf-8")
                fixed += 1
    if fixed:
        print(f"[lint] Auto-fixed {fixed} issues.")
