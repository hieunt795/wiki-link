"""link_enhancer.py — Semantically link isolated wiki nodes.

For each isolated node, use semantic search to find the most relevant existing nodes
and add them to the 'related' section if they are high-confidence matches.
"""

import sys
import yaml
from pathlib import Path
import subprocess
import json
import re

ROOT = Path(__file__).parent.parent
WIKI_ROOT = ROOT / "03_wiki"
LIBRARIAN = ROOT / "07_scripts" / "librarian.py"

def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1])
        return fm or {}, parts[2]
    except:
        return {}, text

def get_node_id_to_title():
    mapping = {}
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = split_frontmatter(text)
        if fm.get("node_id"):
            mapping[fm["node_id"]] = fm.get("title", md_file.stem)
    return mapping

def get_isolated_nodes():
    # Use the logic from find_isolated.py
    graph_path = ROOT / "graphify-out" / "wiki_graph_data.json"
    if not graph_path.exists():
        return []
    data = json.loads(graph_path.read_text("utf-8"))
    nodes = data["nodes"]
    edges = data["edges"]
    degree = {n["id"]: 0 for n in nodes}
    for e in edges:
        degree[e["source"]] = degree.get(e["source"], 0) + 1
        degree[e["target"]] = degree.get(e["target"], 0) + 1
    return [n["id"] for n in nodes if degree[n["id"]] == 0]

def find_related_nodes(query, exclude_id):
    # Call librarian search via subprocess
    try:
        cmd = ["py", "-3.12", str(LIBRARIAN), "search", query, "--top", "10"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        # Parse output to find node paths/ids
        # Expected output format from librarian search includes node paths
        # This is a bit hacky as we have to parse text output
        matches = re.findall(r"03_wiki/[^/]+/([^/]+\.md)", result.stdout)
        # Convert filenames to potential IDs/titles
        return [m.replace(".md", "") for m in matches if exclude_id not in m]
    except Exception as e:
        print(f"Error searching: {e}")
        return []

def add_links_to_node(node_id, related_titles):
    # Find the file
    target_file = None
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, _ = split_frontmatter(text)
        if fm.get("node_id") == node_id:
            target_file = md_file
            break
    
    if not target_file:
        return

    text = target_file.read_text(encoding="utf-8", errors="ignore")
    fm, body = split_frontmatter(text)
    
    current_related = fm.get("related", [])
    if not isinstance(current_related, list):
        current_related = []
    
    existing_nodes = set()
    for r in current_related:
        if isinstance(r, dict):
            existing_nodes.add(r["node"].strip("[]"))
        else:
            existing_nodes.add(r.strip("[]"))
            
    added = 0
    for title in related_titles[:3]: # Limit to top 3
        if title not in existing_nodes:
            current_related.append({"node": f"[[{title}]]", "relation": "related"})
            added += 1
    
    if added > 0:
        fm["related"] = current_related
        new_fm_str = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
        new_text = f"---\n{new_fm_str}\n---\n{body}"
        target_file.write_text(new_text, encoding="utf-8")
        print(f"[enhance] Added {added} links to {node_id}")

def main():
    print("[enhance] Starting connectivity enhancement...")
    isolated = get_isolated_nodes()
    id_to_title = get_node_id_to_title()
    
    if not isolated:
        print("[enhance] No isolated nodes found.")
        return

    print(f"[enhance] Found {len(isolated)} isolated nodes.")
    
    for nid in isolated:
        title = id_to_title.get(nid)
        if not title: continue
        
        print(f"[enhance] Processing: {title}")
        related = find_related_nodes(title, nid)
        if related:
            add_links_to_node(nid, related)

if __name__ == "__main__":
    main()
