"""fix_tags_dicts.py — Fix nodes where related: entries ended up in tags:.

Some nodes have tags like:
    tags:
      - node: '[[IRRBB]]'
        relation: related_to

These dict entries belong in related:, not tags:.
This script:
  1. Moves dict items from tags: -> related: (if not already present)
  2. Keeps only string items in tags:

Run locally (no GPU):
    python 07_scripts/fix_tags_dicts.py --dry-run
    python 07_scripts/fix_tags_dicts.py
"""

from __future__ import annotations

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_ROOT = ROOT / "03_wiki"


def fix_file(md_file: Path, dry_run: bool) -> str:
    """Returns: 'fixed' | 'ok' | 'skip' | 'error'"""
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return "skip"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "skip"
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return "error"
    if not fm.get("node_id"):
        return "skip"

    tags = fm.get("tags", [])
    if not isinstance(tags, list):
        return "ok"

    # Separate string tags from dict tags
    str_tags = [t for t in tags if isinstance(t, str)]
    dict_tags = [t for t in tags if isinstance(t, dict)]

    if not dict_tags:
        return "ok"

    # Move dict_tags into related:
    related = fm.get("related", [])
    if not isinstance(related, list):
        related = []

    # Build set of existing related node refs to avoid duplicates
    existing_nodes = set()
    for r in related:
        if isinstance(r, dict) and "node" in r:
            existing_nodes.add(r["node"])

    added = 0
    for d in dict_tags:
        node_ref = d.get("node", "")
        if node_ref and node_ref not in existing_nodes:
            related.append({"node": node_ref, "relation": d.get("relation", "related_to")})
            existing_nodes.add(node_ref)
            added += 1

    if dry_run:
        print(f"[DRY] {md_file.name}: remove {len(dict_tags)} dict tag(s), add {added} to related:")
        for d in dict_tags:
            print(f"       tag dict: {d}")
        return "fixed"

    # Write back
    fm["tags"] = str_tags
    fm["related"] = related

    items = list(fm.items())
    new_fm_str = yaml.dump(dict(items), allow_unicode=True, default_flow_style=False, sort_keys=False)
    body = parts[2]
    new_content = f"---\n{new_fm_str}---{body}"
    md_file.write_text(new_content, encoding="utf-8")
    return "fixed"


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("[fix_tags_dicts] DRY RUN\n")

    stats = {"fixed": 0, "ok": 0, "skip": 0, "error": 0}
    for md_file in sorted(WIKI_ROOT.rglob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        result = fix_file(md_file, dry_run)
        stats[result] += 1

    print(f"\n[fix_tags_dicts] Done.")
    print(f"  fixed  : {stats['fixed']}")
    print(f"  ok     : {stats['ok']}")
    print(f"  skipped: {stats['skip']}")
    print(f"  errors : {stats['error']}")


if __name__ == "__main__":
    main()
