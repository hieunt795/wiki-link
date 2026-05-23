import yaml
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
WIKI_ROOT = ROOT / "03_wiki"

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

def main():
    print("[tag-link] Starting tag-based connectivity enhancement...")
    
    tag_map = defaultdict(list)
    nodes = []
    
    # Map tags to nodes
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name in ("index.md", "log.md"):
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        fm, body = split_frontmatter(text)
        if not fm.get("node_id"):
            continue
            
        node_info = {
            "id": fm["node_id"],
            "title": fm.get("title", md_file.stem),
            "path": md_file,
            "tags": fm.get("tags", []),
            "fm": fm,
            "body": body
        }
        nodes.append(node_info)
        for tag in node_info["tags"]:
            tag_map[tag.lower()].append(node_info["title"])

    # Add links based on shared tags
    links_added = 0
    for n in nodes:
        current_related = n["fm"].get("related", [])
        if not isinstance(current_related, list):
            current_related = []
            
        existing_targets = set()
        for r in current_related:
            if isinstance(r, dict):
                existing_targets.add(r["node"].strip("[]").lower())
            else:
                existing_targets.add(r.strip("[]").lower())
        
        new_links = []
        for tag in n["tags"]:
            tag_lower = tag.lower()
            # Skip generic tags
            if tag_lower in ["clippings", "monetary_policy", "financial_markets"]:
                continue
                
            peers = tag_map[tag_lower]
            for peer_title in peers:
                if peer_title.lower() != n["title"].lower() and peer_title.lower() not in existing_targets:
                    new_links.append({"node": f"[[{peer_title}]]", "relation": f"shared_tag:{tag}"})
                    existing_targets.add(peer_title.lower())
        
        if new_links:
            n["fm"]["related"] = current_related + new_links[:5] # Max 5 new tag links
            new_fm_str = yaml.dump(n["fm"], sort_keys=False, allow_unicode=True).strip()
            new_text = f"---\n{new_fm_str}\n---\n{n['body']}"
            n["path"].write_text(new_text, encoding="utf-8")
            links_added += len(new_links[:5])
            print(f"[tag-link] Added {len(new_links[:5])} tag-links to {n['id']}")

    print(f"[tag-link] Done. Added {links_added} total links.")

if __name__ == "__main__":
    main()
