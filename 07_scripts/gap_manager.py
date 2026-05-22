"""gap_manager.py — Gap queue, contradiction management, template insight lifecycle.

Gap queue (.cache/gap_queue.jsonl):
  - Logged by synthesis_search when state=TRUE_GAP
  - Closed when source is acquired and ingested

Contradiction nodes (03_wiki/contradictions/):
  - Created by agent during research
  - Lifecycle: open → context_dependent → resolved

Template insights (06_templates/_insights/pending/*.yaml):
  - Flagged by agent during research
  - Applied by user via librarian template-apply
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

ROOT      = Path(__file__).parent.parent
GAP_QUEUE = ROOT / ".cache" / "gap_queue.jsonl"
WIKI_ROOT = ROOT / "03_wiki"
INSIGHTS  = ROOT / "06_templates" / "_insights"
TODAY = date.today().isoformat()


# ── Gap Queue ──────────────────────────────────────────────────────────────────

def list_gaps() -> list[dict]:
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


def close_gap(query: str):
    """Remove a gap entry from the queue (source has been acquired)."""
    if not GAP_QUEUE.exists():
        print(f"[gaps] Gap queue is empty.")
        return
    gaps = list_gaps()
    remaining = [g for g in gaps if g.get("query", "").lower() != query.lower()]
    removed = len(gaps) - len(remaining)
    _rewrite_gap_queue(remaining)
    print(f"[gaps] Closed {removed} gap(s) matching '{query}'.")


def _rewrite_gap_queue(gaps: list[dict]):
    GAP_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    with open(GAP_QUEUE, "w", encoding="utf-8") as f:
        for g in gaps:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")


def suggest_sources(query: str, topic: str = ""):
    """Print source suggestions for a TRUE_GAP query based on keyword heuristics."""
    q = query.lower()
    suggestions: list[str] = []

    if any(k in q for k in ["monetary", "central bank", "fed", "ecb", "boj", "rate", "qe", "qt"]):
        suggestions += [
            "BIS Working Papers (bis.org/publ/work.htm)",
            "Fed FEDS Notes (federalreserve.gov/econres/feds)",
            "ECB Working Papers (ecb.europa.eu/pub/research)",
            "IMF Working Papers (imf.org/en/Publications/WP)",
        ]
    if any(k in q for k in ["basel", "capital", "cet1", "lcr", "nsfr", "rwa", "g-sib"]):
        suggestions += [
            "BCBS Consultative Papers (bis.org/bcbs/publ)",
            "BIS Quarterly Review",
            "FSB Reports (fsb.org/publications)",
        ]
    if any(k in q for k in ["yield", "repo", "swap", "duration", "dv01", "sofr", "fx", "collateral"]):
        suggestions += [
            "ISDA Research (isda.org/research)",
            "SIFMA Research (sifma.org/resources/research)",
            "NY Fed Staff Reports (newyorkfed.org/research)",
        ]
    if any(k in q for k in ["gdp", "cpi", "fiscal", "output gap", "current account", "imf"]):
        suggestions += [
            "IMF World Economic Outlook",
            "BIS Annual Report",
            "NBER Working Papers (nber.org/papers)",
        ]

    if not suggestions:
        suggestions = ["BIS Working Papers", "IMF Working Papers", "Central bank staff notes"]

    print(f"\n[gap] Suggested sources for: '{query}'")
    for s in suggestions:
        print(f"  → {s}")


# ── Contradiction Nodes ────────────────────────────────────────────────────────

def create_contradiction(
    topic: str,
    claim_a: dict,
    claim_b: dict,
    affects_nodes: list[str] | None = None,
) -> Path:
    """Write a contradiction wiki node.

    claim_a / claim_b: {statement, sources, confidence, stance}
    """
    slug = re.sub(r"[^a-z0-9]+", "_", topic.lower()).strip("_")
    contra_dir = WIKI_ROOT / "contradictions"
    contra_dir.mkdir(parents=True, exist_ok=True)

    # Find next counter
    existing = list(contra_dir.glob(f"contra_{slug}_*.md"))
    counter = len(existing) + 1
    node_id = f"contra_{slug}_{counter:03d}"
    filename = f"Contra_{slug.replace('_', ' ').title().replace(' ', '_')}_{counter:03d}.md"
    out_path = contra_dir / filename

    fm = {
        "node_id":           node_id,
        "type":              "contradiction",
        "title":             f"Contradiction: {topic}",
        "aliases":           [],
        "domain":            {"primary": "monetary_policy"},
        "tags":              ["contradiction", slug],
        "confidence":        2,
        "stability":         "contested",
        "thesis":            f"[LLM] Contradiction between two sources on: {topic}",
        "claim_a":           claim_a,
        "claim_b":           claim_b,
        "resolution_status": "open",
        "resolution_note":   "",
        "affects_nodes":     affects_nodes or [],
        "source_refs":       [],
        "related":           [],
        "date_created":      TODAY,
        "date_updated":      TODAY,
    }

    fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    content = f"---\n{fm_str}---\n\n[LLM] Contradiction detected during research. Review and resolve.\n"
    out_path.write_text(content, encoding="utf-8")
    print(f"[gap] Created contradiction node: {out_path.name}")
    return out_path


def resolve_contradiction(node_id: str, resolution: str, status: str = "resolved"):
    """Update contradiction node resolution status."""
    for md_file in (WIKI_ROOT / "contradictions").glob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        if f"node_id: {node_id}" in text:
            text = re.sub(r"resolution_status: \w+", f"resolution_status: {status}", text)
            text = re.sub(r"resolution_note: .*", f"resolution_note: {resolution!r}", text)
            text = text.replace(f"date_updated: {text}", f"date_updated: {TODAY}")
            md_file.write_text(text, encoding="utf-8")
            print(f"[gap] Updated contradiction {node_id} → {status}")
            return
    print(f"[gap] Contradiction node '{node_id}' not found.")


# ── Template Insights ──────────────────────────────────────────────────────────

def log_template_insight(
    insight_id: str,
    target_template: str,
    observation: str,
    proposed_change: str,
    priority: str = "medium",
    evidence: str = "",
    session: str = "",
):
    """Save a new template insight to pending queue."""
    pending_dir = INSIGHTS / "pending"
    pending_dir.mkdir(parents=True, exist_ok=True)

    data = {
        "id":               insight_id,
        "target_template":  target_template,
        "observation":      observation,
        "proposed_change":  proposed_change,
        "evidence":         evidence,
        "priority":         priority,
        "status":           "pending",
        "session":          session,
        "date_logged":      TODAY,
    }
    out = pending_dir / f"{insight_id}.yaml"
    out.write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False), encoding="utf-8")
    print(f"[template] Logged insight: {insight_id} ({priority}) → {target_template}")


def apply_template_insight(insight_id: str):
    """Apply a pending insight: append change note to target template and move to accepted/."""
    pending_dir = INSIGHTS / "pending"
    accepted_dir = INSIGHTS / "accepted"
    accepted_dir.mkdir(parents=True, exist_ok=True)

    insight_file = pending_dir / f"{insight_id}.yaml"
    if not insight_file.exists():
        print(f"[template] Insight '{insight_id}' not found in pending/")
        return

    data = yaml.safe_load(insight_file.read_text(encoding="utf-8"))
    target = ROOT / data["target_template"]

    if not target.exists():
        print(f"[template] Target template not found: {target}")
        return

    # Append change note to template file
    template_text = target.read_text(encoding="utf-8")

    # Add version_history block if YAML, or append as comment if .md
    if target.suffix in (".yaml", ".yml"):
        try:
            tdata = yaml.safe_load(template_text) or {}
        except Exception:
            tdata = {}
        version = tdata.get("version", 1) + 1
        tdata["version"] = version
        history = tdata.setdefault("version_history", [])
        history.append({
            "version": version,
            "date": TODAY,
            "changes": data.get("proposed_change", ""),
            "session_source": data.get("session", ""),
            "insight_id": insight_id,
        })
        target.write_text(
            yaml.dump(tdata, allow_unicode=True, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )
        _update_template_changelog(target, version, data)
    else:
        # .md template — append a comment block
        note = (f"\n\n<!-- INSIGHT APPLIED {TODAY} [{insight_id}]\n"
                f"Change: {data.get('proposed_change', '')}\n"
                f"Evidence: {data.get('evidence', '')}\n-->\n")
        with open(target, "a", encoding="utf-8") as f:
            f.write(note)

    # Move insight to accepted
    shutil.move(str(insight_file), str(accepted_dir / insight_file.name))
    data["status"] = "accepted"
    data["date_applied"] = TODAY
    (accepted_dir / insight_file.name).write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False), encoding="utf-8"
    )
    print(f"[template] Applied insight '{insight_id}' → {target.name} (v{tdata.get('version', '?')})")


def reject_template_insight(insight_id: str, reason: str = ""):
    """Move a pending insight to rejected/ with reason."""
    pending_dir = INSIGHTS / "pending"
    rejected_dir = INSIGHTS / "rejected"
    rejected_dir.mkdir(parents=True, exist_ok=True)

    insight_file = pending_dir / f"{insight_id}.yaml"
    if not insight_file.exists():
        print(f"[template] Insight '{insight_id}' not found.")
        return

    data = yaml.safe_load(insight_file.read_text(encoding="utf-8"))
    data["status"] = "rejected"
    data["rejection_reason"] = reason
    data["date_rejected"] = TODAY

    shutil.move(str(insight_file), str(rejected_dir / insight_file.name))
    (rejected_dir / insight_file.name).write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False), encoding="utf-8"
    )
    print(f"[template] Rejected insight '{insight_id}'.")


def _update_template_changelog(template_path: Path, version: int, insight: dict):
    """Append entry to _changelog.md alongside the template file."""
    changelog = template_path.parent / "_changelog.md"
    if not changelog.exists():
        changelog.write_text(f"# {template_path.stem} — Changelog\n\n", encoding="utf-8")
    entry = (f"\n## v{version} ({TODAY})\n"
             f"- {insight.get('proposed_change', '')}\n"
             f"  - Source: session `{insight.get('session', 'unknown')}`, insight `{insight.get('id', '')}`\n"
             f"  - Evidence: {insight.get('evidence', 'N/A')}\n")
    with open(changelog, "a", encoding="utf-8") as f:
        f.write(entry)


def summarize_session_insights(topic_slug: str):
    """Scan 04_research/{topic_slug}/findings/ for TEMPLATE_INSIGHTs and print summary."""
    research_dir = ROOT / "04_research" / topic_slug / "findings"
    if not research_dir.exists():
        print(f"[session] No findings dir for topic '{topic_slug}'")
        return

    all_insights: list[dict] = []
    for f in research_dir.glob("*.md"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        fm_match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not fm_match:
            continue
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except Exception:
            continue
        for ins in fm.get("template_insights", []):
            ins["_source_file"] = f.name
            all_insights.append(ins)

    if not all_insights:
        print(f"[session] No template insights found in session '{topic_slug}'.")
        return

    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    all_insights.sort(key=lambda x: priority_order.get(x.get("priority", "low"), 3))

    print(f"\nTemplate Insight Summary — Session: {topic_slug}")
    print("─" * 60)
    for ins in all_insights:
        p = ins.get("priority", "?").upper()
        tid = ins.get("id", "?")
        target = ins.get("target_template", "?")
        obs = ins.get("observation", "")[:120]
        print(f"[{p}]  {tid}")
        print(f"       target: {target}")
        print(f"       {obs}")
        print()

    print("Commands:")
    print(f"  python librarian.py template-apply <insight_id>")
    print(f"  python librarian.py template-reject <insight_id> --reason '...'")
    print(f"  python librarian.py template-apply --priority high")

    # Auto-log pending insights from findings
    for ins in all_insights:
        if ins.get("status") == "pending":
            log_template_insight(
                insight_id=ins.get("id", f"insight_{topic_slug}"),
                target_template=ins.get("target_template", ""),
                observation=ins.get("observation", ""),
                proposed_change=ins.get("proposed_change", ""),
                priority=ins.get("priority", "medium"),
                evidence=ins.get("evidence", ""),
                session=topic_slug,
            )
