"""maintain_wiki.py — Rebuild Index and Knowledge Graph.

Automates:
1. Rebuilding 03_wiki/index.md from all existing nodes.
2. Rebuilding graphify-out/wiki_graph_data.json for the visualization.
"""

import re
import json
import yaml
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent.parent
WIKI_ROOT = ROOT / "03_wiki"
GRAPH_DATA_PATH = ROOT / "graphify-out" / "wiki_graph_data.json"
INDEX_PATH = ROOT / "03_wiki" / "index.md"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")

NODE_TYPES = [
    "concept", "mechanism", "framework", "entity", "policy", "indicator",
    "relationship", "contradiction", "synthesis", "regulation"
]

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

def get_all_nodes():
    nodes = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = split_frontmatter(text)
        if not fm.get("node_id"):
            continue
        
        domain_field = fm.get("domain", {})
        domain = domain_field.get("primary", "monetary_policy") if isinstance(domain_field, dict) else str(domain_field)
        
        nodes.append({
            "id": fm["node_id"],
            "path": md_file,
            "title": fm.get("title", md_file.stem),
            "type": fm.get("type", "concept"),
            "domain": domain,
            "confidence": int(fm.get("confidence", 1)),
            "tags": fm.get("tags", []),
            "thesis": fm.get("thesis", "").strip(),
            "stability": fm.get("stability", "stable"),
            "date_updated": str(fm.get("date_updated", date.today().isoformat())),
            "body": body
        })
    return nodes

def rebuild_index(nodes):
    print(f"[maintain] Rebuilding {INDEX_PATH}...")
    
    # Sort by type then title
    nodes.sort(key=lambda x: (x["type"], x["title"]))
    
    type_counts = {t: 0 for t in NODE_TYPES}
    for n in nodes:
        if n["type"] in type_counts:
            type_counts[n["type"]] += 1
            
    header = f"# Wiki Index\n\n**Total nodes:** {len(nodes)}  |  **Last updated:** {date.today().isoformat()}\n\n---\n\n"
    
    sections = []
    for ntype in NODE_TYPES:
        count = type_counts[ntype]
        if count == 0:
            continue
            
        section = f"## {ntype.capitalize()}s ({count})\n\n"
        for n in [x for x in nodes if x["type"] == ntype]:
            stars = "★" * n["confidence"] + "☆" * (5 - n["confidence"])
            thesis_short = n["thesis"][:150] + ("..." if len(n["thesis"]) > 150 else "")
            # Ensure links are correctly formatted for the index
            section += f"- **[[{n['title']}]]**  {stars}\n  {thesis_short}\n"
        sections.append(section)
        
    content = header + "\n".join(sections)
    INDEX_PATH.write_text(content, encoding="utf-8")
    print(f"[maintain] Done: {len(nodes)} nodes indexed.")

def rebuild_graph(nodes):
    print(f"[maintain] Rebuilding {GRAPH_DATA_PATH}...")
    
    # Map title/slug/id to node_id for edge resolution
    lookup = {}
    for n in nodes:
        lookup[n["id"].lower()] = n["id"]
        lookup[n["title"].lower()] = n["id"]
        # Also handle filenames/slugs
        lookup[n["path"].stem.lower()] = n["id"]
    
    graph_nodes = []
    edges = []
    seen_edges = set()
    
    def add_edge(src, target_raw, relation="related"):
        target_raw = target_raw.strip("[]").split("|")[0].split("#")[0].strip()
        target_id = lookup.get(target_raw.lower())
        if not target_id:
            # Try underscore conversion for CamelCase links
            underscore = re.sub(r'([A-Z])', r'_\1', target_raw).lstrip('_').lower()
            target_id = lookup.get(underscore)
            
        if target_id and target_id != src:
            edge_key = tuple(sorted((src, target_id)))
            if edge_key not in seen_edges:
                edges.append({
                    "source": src,
                    "target": target_id,
                    "relation": relation
                })
                seen_edges.add(edge_key)

    for n in nodes:
        graph_nodes.append({
            "id": n["id"],
            "title": n["title"],
            "type": n["type"],
            "domain": n["domain"],
            "confidence": n["confidence"],
            "tags": n["tags"],
            "thesis": n["thesis"],
            "stability": n["stability"],
            "date_updated": n["date_updated"]
        })
        
        # 1. Frontmatter 'related' section
        text = n["path"].read_text(encoding="utf-8", errors="ignore")
        fm, body = split_frontmatter(text)
        related = fm.get("related", [])
        if isinstance(related, list):
            for rel in related:
                if isinstance(rel, dict) and "node" in rel:
                    add_edge(n["id"], rel["node"], rel.get("relation", "related"))
                elif isinstance(rel, str):
                    add_edge(n["id"], rel)

        # 2. Body links
        links = WIKILINK_RE.findall(body)
        for link in links:
            add_edge(n["id"], link)
                    
    graph_data = {"nodes": graph_nodes, "edges": edges}
    GRAPH_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    GRAPH_DATA_PATH.write_text(json.dumps(graph_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[maintain] Done: {len(graph_nodes)} nodes, {len(edges)} edges.")

if __name__ == "__main__":
    all_nodes = get_all_nodes()
    rebuild_index(all_nodes)
    rebuild_graph(all_nodes)
