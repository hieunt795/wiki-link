import json
from pathlib import Path

graph_path = Path("graphify-out/wiki_graph_data.json")
if not graph_path.exists():
    print("Graph data not found.")
    exit()

data = json.loads(graph_path.read_text("utf-8"))
nodes = data["nodes"]
edges = data["edges"]

degree = {n["id"]: 0 for n in nodes}
for e in edges:
    degree[e["source"]] = degree.get(e["source"], 0) + 1
    degree[e["target"]] = degree.get(e["target"], 0) + 1

isolated = [n for n in nodes if degree[n["id"]] == 0]

print(f"Total nodes: {len(nodes)}")
print(f"Total edges: {len(edges)}")
print(f"Isolated nodes: {len(isolated)}")
print("\nIsolated nodes list:")
for n in isolated:
    print(f"- {n['title']} ({n['id']})")
