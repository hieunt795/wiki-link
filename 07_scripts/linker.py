"""linker.py — Cross-reference audit for wiki nodes.

Responsibilities:
  1. Scan all [[wikilinks]] in 03_wiki/
  2. Identify broken links (target node_id does not exist)
  3. Identify orphan nodes (no incoming links + no source_refs)
  4. Optionally write a report; --fix adds stub nodes for broken links

run_link_audit() is called by `librarian link`.
"""

from __future__ import annotations

import re
from pathlib import Path
from datetime import date

from chunker import _split_frontmatter

WIKI_ROOT = Path(__file__).parent.parent / "03_wiki"
TODAY = date.today().isoformat()

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def run_link_audit(fix: bool = False) -> dict:
    """Scan wiki for broken links and orphan nodes.

    Returns:
        {"broken": int, "orphans": int, "details": [...]}
    """
    node_map = _build_node_map()       # node_id → Path
    label_map = _build_label_map()     # lower(title) → node_id
    incoming: dict[str, list[str]] = {nid: [] for nid in node_map}
    broken_links: list[dict] = []
    orphans: list[str] = []

    for node_id, node_path in node_map.items():
        text = node_path.read_text(encoding="utf-8", errors="ignore")
        links = WIKILINK_RE.findall(text)
        for raw_link in links:
            target = _resolve_link(raw_link, node_map, label_map)
            if target:
                incoming.setdefault(target, []).append(node_id)
            else:
                broken_links.append({
                    "source": node_id,
                    "raw_link": raw_link,
                    "file": str(node_path.relative_to(WIKI_ROOT.parent)),
                })

    # Orphans: nodes with no incoming links and no source_refs
    for node_id, node_path in node_map.items():
        if incoming.get(node_id):
            continue
        text = node_path.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        source_refs = fm.get("source_refs", [])
        if not source_refs:
            orphans.append(node_id)

    # Report
    print(f"\n[link] {len(broken_links)} broken links, {len(orphans)} orphans")
    if broken_links:
        print("\nBroken links:")
        for b in broken_links[:20]:
            print(f"  {b['source']} → [[{b['raw_link']}]]  ({b['file']})")
        if len(broken_links) > 20:
            print(f"  ... and {len(broken_links) - 20} more")

    if orphans:
        print("\nOrphan nodes (no incoming links, no source_refs):")
        for o in orphans[:20]:
            print(f"  {o}")

    if fix and broken_links:
        _fix_broken_links(broken_links, node_map)

    return {
        "broken": len(broken_links),
        "orphans": len(orphans),
        "details": broken_links,
    }


def _build_node_map() -> dict[str, Path]:
    """Map node_id → file path for all wiki nodes."""
    node_map: dict[str, Path] = {}
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        nid = fm.get("node_id")
        if nid:
            node_map[nid] = md_file
        # Also index by stem for [[filename]] links
        node_map[md_file.stem.lower()] = md_file
    return node_map


def _build_label_map() -> dict[str, str]:
    """Map lower(title) → node_id for fuzzy link resolution."""
    label_map: dict[str, str] = {}
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = _split_frontmatter(text)
        nid = fm.get("node_id")
        title = fm.get("title", "")
        if nid and title:
            label_map[title.lower()] = nid
            # Also map aliases
            for alias in fm.get("aliases", []):
                label_map[alias.lower()] = nid
    return label_map


def _resolve_link(raw_link: str, node_map: dict, label_map: dict) -> str | None:
    """Try to resolve a wikilink text to a node_id. Returns None if not found."""
    slug = raw_link.strip()
    # Direct node_id match
    if slug in node_map:
        return slug
    # Lowercase stem match
    if slug.lower() in node_map:
        return slug.lower()
    # Title/alias match
    if slug.lower() in label_map:
        return label_map[slug.lower()]
    # CamelCase slug → underscore
    underscore = re.sub(r"([A-Z])", r"_\1", slug).lstrip("_").lower()
    if underscore in node_map:
        return underscore
    return None


def _fix_broken_links(broken_links: list[dict], node_map: dict):
    """Create stub nodes for unique broken link targets."""
    seen: set[str] = set()
    stubs_created = 0
    for b in broken_links:
        target = b["raw_link"]
        if target in seen:
            continue
        seen.add(target)
        # Create stub only if target looks like a proper node name
        if len(target) < 3 or target.startswith("http"):
            continue
        stub_path = WIKI_ROOT / "concepts" / f"{target.replace(' ', '_')}.md"
        if not stub_path.exists():
            stub_path.parent.mkdir(parents=True, exist_ok=True)
            slug = re.sub(r"[^a-z0-9]+", "_", target.lower()).strip("_")
            content = f"""---
node_id: {slug}_001
type: concept
title: {target}
aliases: []
domain:
  primary: monetary_policy
tags: []
confidence: 1
stability: evolving
thesis: '[LLM] Auto-generated stub — broken link target. Review and expand.'
source_refs: []
related: []
date_created: {TODAY}
date_updated: {TODAY}
---

[LLM] Stub created by linker --fix. Review and fill content.
"""
            stub_path.write_text(content, encoding="utf-8")
            stubs_created += 1
            print(f"[link] Created stub: {stub_path.name}")
    print(f"[link] Created {stubs_created} stub nodes.")
