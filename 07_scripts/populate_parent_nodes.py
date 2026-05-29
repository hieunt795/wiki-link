"""populate_parent_nodes.py — One-time batch script.

Reads all wiki nodes, selects the highest-priority hierarchical relation from
the `related:` field, and writes `parent_node:` into the frontmatter.

Priority: parent_framework > parent_mechanism > component_of > part_of
Excludes: extends, implements (peer-level)

Run locally (no GPU needed):
    python 07_scripts/populate_parent_nodes.py --dry-run
    python 07_scripts/populate_parent_nodes.py
"""

from __future__ import annotations

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_ROOT = ROOT / "03_wiki"

PRIORITY = ["parent_framework", "parent_mechanism", "component_of", "part_of"]


def _pick_parent(related: list) -> str | None:
    """Return wikilink string of the highest-priority parent, or None."""
    candidates: dict[int, str] = {}
    for rel in related:
        if not isinstance(rel, dict):
            continue
        relation_str = str(rel.get("relation", "")).strip()
        node_str = rel.get("node", "")
        if not node_str:
            continue
        for rank, keyword in enumerate(PRIORITY):
            if keyword in relation_str:
                if rank not in candidates:
                    candidates[rank] = node_str
                break
    if not candidates:
        return None
    return candidates[min(candidates.keys())]


def process_file(md_file: Path, dry_run: bool) -> str:
    """Returns: 'set' | 'null' | 'already_set' | 'skip' | 'error'"""
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

    # Skip if already explicitly set (not None/null)
    existing = fm.get("parent_node")
    if existing is not None and "parent_node" in (yaml.safe_load(parts[1]) or {}):
        # Field exists and is not None → already populated
        if existing is not None:
            return "already_set"

    body = parts[2]
    related = fm.get("related", [])
    parent = _pick_parent(related if isinstance(related, list) else [])

    # Build new frontmatter preserving insertion order
    items = list(fm.items())
    # Remove any existing parent_node key
    items = [(k, v) for k, v in items if k != "parent_node"]
    # Insert parent_node before 'related'
    related_idx = next((i for i, (k, _) in enumerate(items) if k == "related"), len(items))
    items.insert(related_idx, ("parent_node", parent))
    new_fm = dict(items)

    new_fm_str = yaml.dump(new_fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = f"---\n{new_fm_str}---{body}"

    if dry_run:
        action = "SET " if parent else "NULL"
        print(f"[DRY] {action}: {md_file.name}  ->  {parent!r}")
    else:
        md_file.write_text(new_content, encoding="utf-8")

    return "set" if parent else "null"


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("[populate_parent_nodes] DRY RUN — no files will be written.\n")

    stats: dict[str, int] = {"set": 0, "null": 0, "already_set": 0, "skip": 0, "error": 0}
    set_examples: list[tuple[str, str]] = []

    for md_file in sorted(WIKI_ROOT.rglob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        result = process_file(md_file, dry_run)
        stats[result] += 1
        if result == "set" and not dry_run:
            # Re-read to confirm
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            parts = text.split("---", 2)
            fm = yaml.safe_load(parts[1]) if len(parts) >= 3 else {}
            set_examples.append((md_file.name, str(fm.get("parent_node", ""))))

    print(f"\n[populate_parent_nodes] Done.")
    print(f"  parent_node SET    : {stats['set']}")
    print(f"  parent_node null   : {stats['null']}")
    print(f"  already_set        : {stats['already_set']}")
    print(f"  skipped (no id)    : {stats['skip']}")
    print(f"  errors             : {stats['error']}")

    if set_examples:
        print(f"\nSample nodes with parent_node set (first 10):")
        for name, parent in set_examples[:10]:
            print(f"  {name}  ->  {parent}")


if __name__ == "__main__":
    main()
