"""vector_map.py — Generate a 2D semantic map of wiki nodes.

Reduces 1024-dim BGE-M3 vectors to 2D using PCA and outputs an interactive HTML map.
Note: Requires 'scikit-learn' for dimensionality reduction.
"""

import json
import sys
from pathlib import Path

import numpy as np
from dense_index import DenseIndex

ROOT = Path(__file__).parent.parent
OUTPUT_PATH = ROOT / "vector_map.html"
DATA_PATH = ROOT / "graphify-out" / "vector_data.json"

def _run_tsne(vecs_pca, total):
    """Run t-SNE 3D with best available backend: cuML > openTSNE > sklearn."""
    perp = min(30, total - 1)

    # 1. cuML (RAPIDS GPU) — fastest, Colab T4 / A100
    try:
        from cuml.manifold import TSNE as cuTSNE
        print("[vector-map] Backend: cuML (GPU)")
        tsne = cuTSNE(n_components=3, perplexity=perp, random_state=42,
                      n_iter=1000, learning_rate=200.0)
        import cupy as cp
        result = tsne.fit_transform(cp.array(vecs_pca, dtype="float32"))
        import numpy as np
        return np.array(result)
    except ImportError:
        pass

    # 2. openTSNE (FFT-BH accelerated CPU) — ~10-20x faster than sklearn
    try:
        from openTSNE import TSNE as openTSNE
        print("[vector-map] Backend: openTSNE (FFT-BH CPU)")
        tsne = openTSNE(n_components=3, perplexity=perp, random_state=42,
                        n_jobs=-1, verbose=True)
        return tsne.fit(vecs_pca)
    except ImportError:
        pass

    # 3. sklearn fallback (slow on large datasets)
    from sklearn.manifold import TSNE
    print("[vector-map] Backend: sklearn t-SNE (CPU, slow — consider: pip install opentsne)")
    tsne = TSNE(n_components=3, random_state=42, perplexity=perp,
                n_iter=1000, verbose=1)
    return tsne.fit_transform(vecs_pca)


def main():
    print("[vector-map] Generating semantic map...")
    
    try:
        from sklearn.decomposition import PCA
    except ImportError:
        print("[vector-map] Error: 'scikit-learn' is required. Install with: pip install scikit-learn")
        return

    idx = DenseIndex()
    try:
        status = idx.status()
        if not status.get("built"):
            print("[vector-map] Error: Dense index not built. Run 'librarian.py sync' first.")
            return

        total = status["total_vectors"]
        meta = idx._meta

        print(f"[vector-map] Loading {total} vectors...")
        vectors = []
        for i in range(total):
            vectors.append(idx.reconstruct(i))

        vecs_array = np.vstack(vectors)

        print("[vector-map] Reducing dimensions (PCA 1024d -> 50d)...")
        pca = PCA(n_components=min(50, total))
        vecs_pca = pca.fit_transform(vecs_array)

        print("[vector-map] Running t-SNE 3D...")
        vecs_3d = _run_tsne(vecs_pca, total)

        # Load structural edges from graph data
        graph_path = ROOT / "graphify-out" / "wiki_graph_data.json"
        graph_edges = []
        if graph_path.exists():
            graph_data = json.loads(graph_path.read_text("utf-8"))
            graph_edges = graph_data.get("edges", [])

        # Prepare data for JSON
        points = []
        id_to_idx = {}
        for i in range(total):
            m = meta[i]
            nid = m.get("node_id", f"vec_{i}")
            id_to_idx[nid] = i
            points.append({
                "x": float(vecs_3d[i, 0]),
                "y": float(vecs_3d[i, 1]),
                "z": float(vecs_3d[i, 2]),
                "id": nid,
                "title": m.get("label", m.get("stem", "Untitled")),
                "source": m.get("source", "unknown"),
                "domain": m.get("domain", "general"),
                "type": m.get("type", "concept"),
                "thesis": m.get("thesis", "")
            })
            
        # Map structural edges to coordinate indices
        valid_edges = []
        for e in graph_edges:
            src_id = e["source"]
            tgt_id = e["target"]
            if src_id in id_to_idx and tgt_id in id_to_idx:
                valid_edges.append({
                    "s": id_to_idx[src_id],
                    "t": id_to_idx[tgt_id]
                })

        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        DATA_PATH.write_text(json.dumps({"points": points, "edges": valid_edges}, indent=2), encoding="utf-8")
        
        generate_html(points, valid_edges)
        print(f"[vector-map] Map generated: {OUTPUT_PATH}")
        print(f"[vector-map] Data saved: {DATA_PATH}")

    except Exception as e:
        print(f"[vector-map] Error: {e}")
        import traceback
        traceback.print_exc()

def generate_html(points, edges):
    n_wiki = sum(1 for p in points if p["source"] == "wiki")
    n_raw = len(points) - n_wiki
    n_edges = len(edges)
    total = len(points)

    points_json = json.dumps(points)
    edges_json = json.dumps(edges)

    html = (
        """<!DOCTYPE html>
<html>
<head>
    <title>Wiki-Agentic Neural Brain Map 3D</title>
    <style>
        body { margin: 0; background: #050505; color: #00ffcc; font-family: 'Courier New', monospace; overflow: hidden; }
        .ui { position: absolute; top: 20px; left: 20px; pointer-events: none; text-shadow: 0 0 10px #00ffcc; z-index: 10; }
        .ui h1 { margin: 0 0 4px 0; font-size: 16px; }
        .ui p  { margin: 0 0 2px 0; font-size: 12px; }
        .ui small { font-size: 10px; color: #aaa; }
        .tooltip {
            position: absolute; background: rgba(0,20,20,0.92); border: 1px solid #00ffcc;
            padding: 10px; border-radius: 4px; pointer-events: none; display: none;
            font-size: 12px; box-shadow: 0 0 15px rgba(0,255,204,0.3);
            max-width: 300px; z-index: 20;
        }
        .legend { position: absolute; bottom: 20px; right: 20px; background: rgba(0,0,0,0.5); padding: 10px; border-radius: 4px; border: 1px solid #333; z-index: 10; }
        .legend-item { display: flex; align-items: center; gap: 8px; margin: 4px 0; font-size: 10px; }
        .dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
    </style>
</head>
<body>
    <div class="ui">
        <h1>NEURAL SEMANTIC MAP 3D</h1>
        <p>"""
        + f"{total:,} Nodes &nbsp;|&nbsp; {n_edges} Synapses"
        + """</p>
        <small>LEFT-DRAG: rotate &nbsp; RIGHT-DRAG: pan &nbsp; SCROLL: zoom &nbsp; HOVER: inspect</small>
    </div>
    <div id="tooltip" class="tooltip"></div>
    <div class="legend">
        <div class="legend-item"><span class="dot" style="background:#00ffcc"></span> WIKI NODE ("""
        + f"{n_wiki:,}"
        + """)</div>
        <div class="legend-item"><span class="dot" style="background:#0066ff"></span> RAW SOURCE ("""
        + f"{n_raw:,}"
        + """)</div>
        <div class="legend-item"><span class="dot" style="background:rgba(0,255,204,0.25)"></span> SYNAPSE</div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const points = """
        + points_json
        + """;
        const edges  = """
        + edges_json
        + """;

        // --- Scene ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x050505);
        scene.fog = new THREE.FogExp2(0x050505, 0.0012);

        // --- Camera ---
        const camera = new THREE.PerspectiveCamera(60, innerWidth / innerHeight, 0.5, 8000);
        camera.position.set(0, 0, 350);

        // --- Renderer ---
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setPixelRatio(devicePixelRatio);
        renderer.setSize(innerWidth, innerHeight);
        document.body.appendChild(renderer.domElement);

        // --- Controls ---
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.06;

        // --- Split wiki vs raw ---
        const wikiPts = [], rawPts = [];
        const wikiMap = [], rawMap = [];   // local-index → global-index
        points.forEach((p, i) => {
            if (p.source === 'wiki') { wikiMap.push(i); wikiPts.push(p); }
            else                     { rawMap.push(i);  rawPts.push(p); }
        });

        function makeCloud(pts, color, size) {
            const pos = new Float32Array(pts.length * 3);
            pts.forEach((p, i) => { pos[i*3]=p.x; pos[i*3+1]=p.y; pos[i*3+2]=p.z||0; });
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            const mat = new THREE.PointsMaterial({
                color, size, sizeAttenuation: true,
                transparent: true, opacity: 0.88,
                blending: THREE.AdditiveBlending, depthWrite: false
            });
            return new THREE.Points(geo, mat);
        }

        const wikiCloud = makeCloud(wikiPts, 0x00ffcc, 3.5);
        const rawCloud  = makeCloud(rawPts,  0x0066ff, 1.5);
        scene.add(wikiCloud, rawCloud);

        // --- Edges ---
        if (edges.length) {
            const epos = new Float32Array(edges.length * 6);
            edges.forEach((e, i) => {
                const s = points[e.s], t = points[e.t];
                epos[i*6]   = s.x; epos[i*6+1] = s.y; epos[i*6+2] = s.z||0;
                epos[i*6+3] = t.x; epos[i*6+4] = t.y; epos[i*6+5] = t.z||0;
            });
            const egeo = new THREE.BufferGeometry();
            egeo.setAttribute('position', new THREE.BufferAttribute(epos, 3));
            const emat = new THREE.LineBasicMaterial({
                color: 0x00ffcc, opacity: 0.12, transparent: true,
                blending: THREE.AdditiveBlending, depthWrite: false
            });
            scene.add(new THREE.LineSegments(egeo, emat));
        }

        // --- Hover tooltip via raycasting ---
        const tooltip  = document.getElementById('tooltip');
        const raycaster = new THREE.Raycaster();
        raycaster.params.Points.threshold = 3;
        const mouse = new THREE.Vector2(-9999, -9999);

        window.addEventListener('mousemove', e => {
            mouse.x =  (e.clientX / innerWidth)  * 2 - 1;
            mouse.y = -(e.clientY / innerHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);
            const wHits = raycaster.intersectObject(wikiCloud);
            const rHits = raycaster.intersectObject(rawCloud);

            let found = null;
            if (wHits.length)       found = wikiPts[wHits[0].index];
            else if (rHits.length)  found = rawPts[rHits[0].index];

            if (found) {
                tooltip.style.display = 'block';
                tooltip.style.left = (e.clientX + 16) + 'px';
                tooltip.style.top  = (e.clientY + 16) + 'px';
                tooltip.innerHTML  =
                    '<strong>' + found.title + '</strong>' +
                    '<br><small>' + found.source.toUpperCase() + ' &nbsp;|&nbsp; ' + found.type + '</small>' +
                    (found.thesis ? '<p style="margin:6px 0 0;font-size:10px;color:#aaa">' + found.thesis + '</p>' : '');
            } else {
                tooltip.style.display = 'none';
            }
        });

        // --- Resize ---
        window.addEventListener('resize', () => {
            camera.aspect = innerWidth / innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(innerWidth, innerHeight);
        });

        // --- Loop ---
        (function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        })();
    </script>
</body>
</html>"""
    )
    OUTPUT_PATH.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
