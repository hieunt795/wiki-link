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
    import sklearn
    from sklearn.manifold import TSNE
    print("[vector-map] Backend: sklearn t-SNE (CPU, slow — consider: pip install opentsne)")
    # n_iter renamed to max_iter in sklearn 1.5
    iter_kwarg = "max_iter" if tuple(int(x) for x in sklearn.__version__.split(".")[:2]) >= (1, 5) else "n_iter"
    tsne = TSNE(n_components=3, random_state=42, perplexity=perp,
                verbose=1, **{iter_kwarg: 1000})
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
    n_raw  = len(points) - n_wiki
    n_edges = len(edges)
    total   = len(points)

    TYPE_COLORS = {
        "concept":       "#00e5cc",
        "mechanism":     "#ff6e40",
        "framework":     "#ce93d8",
        "entity":        "#ffd740",
        "policy":        "#69f0ae",
        "indicator":     "#64b5f6",
        "contradiction": "#ff5252",
        "synthesis":     "#f48fb1",
        "regulation":    "#ffab40",
        "relationship":  "#4dd0e1",
    }

    legend_items = "".join(
        f'<div class="li"><span class="ld" style="background:{c};box-shadow:0 0 6px {c}80"></span>{t}</div>\n'
        for t, c in TYPE_COLORS.items()
    ) + '<div class="li"><span class="ld" style="background:#1565c0;opacity:.7"></span>raw chunk</div>\n'

    points_json      = json.dumps(points)
    edges_json       = json.dumps(edges)
    type_colors_json = json.dumps(TYPE_COLORS)

    TMPL = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Wiki Neural Map 3D</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#030810; color:#cdd9f0; font-family:system-ui,sans-serif; overflow:hidden; }
#ui {
    position:absolute; top:22px; left:22px; pointer-events:none; z-index:10;
}
#ui h1 { font-size:12px; font-weight:700; letter-spacing:.14em; color:#00e5cc;
         text-shadow:0 0 14px #00e5cc88; margin-bottom:5px; }
#ui p  { font-size:11px; color:#4a6180; }
#ui small { display:block; margin-top:5px; font-size:10px; color:#2d4060; }
.tip {
    position:absolute; background:rgba(4,10,24,.94);
    border:1px solid #1c2d46; border-radius:10px;
    padding:13px 15px; pointer-events:none; display:none;
    font-size:12px; max-width:290px; z-index:20;
    box-shadow:0 8px 32px rgba(0,0,0,.7);
    backdrop-filter:blur(12px);
}
.tip-title { font-size:13px; font-weight:600; color:#e8f0ff; margin-bottom:6px; line-height:1.3; }
.tip-badge {
    display:inline-block; padding:2px 8px; border-radius:20px;
    font-size:10px; font-weight:700; letter-spacing:.07em;
    text-transform:uppercase; margin-bottom:7px;
}
.tip-domain { font-size:10px; color:#3a5070; margin-top:2px; }
.tip-thesis { font-size:11px; color:#6a8098; line-height:1.55; margin-top:6px;
              border-top:1px solid #1c2d46; padding-top:6px; }
#legend {
    position:absolute; bottom:22px; right:22px;
    background:rgba(4,10,24,.85); border:1px solid #1c2d46;
    border-radius:10px; padding:13px 15px; z-index:10;
    backdrop-filter:blur(10px);
}
#legend h4 { font-size:9px; color:#2d4060; letter-spacing:.12em;
             text-transform:uppercase; margin-bottom:9px; }
.li { display:flex; align-items:center; gap:9px; margin:5px 0;
      font-size:11px; color:#4a6180; }
.ld { width:7px; height:7px; border-radius:50%; flex-shrink:0; }
#stats { position:absolute; bottom:22px; left:22px;
         font-size:10px; color:#2d4060; z-index:10; line-height:2; }
</style>
</head>
<body>
<div id="ui">
  <h1>WIKI NEURAL MAP &mdash; 3D</h1>
  <p>__TOTAL__ nodes &nbsp;&middot;&nbsp; __NEDGES__ synapses</p>
  <small>drag &nbsp;&middot;&nbsp; scroll &nbsp;&middot;&nbsp; hover</small>
</div>
<div id="tooltip" class="tip"></div>
<div id="legend">
  <h4>Node Type</h4>
  __LEGEND__
</div>
<div id="stats">wiki __NWIKI__ &nbsp;&middot;&nbsp; raw __NRAW__</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script>
const points = __POINTS__;
const edges  = __EDGES__;
const TYPE_COLORS = __TYPE_COLORS__;
const DEFAULT_COLOR = '#78909c';

// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x030810);
scene.fog = new THREE.FogExp2(0x030810, 0.0007);

const camera = new THREE.PerspectiveCamera(55, innerWidth/innerHeight, 0.5, 10000);
camera.position.set(0, 0, 440);

const renderer = new THREE.WebGLRenderer({ antialias:true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.25;
controls.addEventListener('start', () => { controls.autoRotate = false; });

// Solid circle sprite
function makeSprite() {
    const sz = 64, cv = document.createElement('canvas');
    cv.width = cv.height = sz;
    const ctx = cv.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(sz/2, sz/2, sz/2 - 1, 0, Math.PI * 2);
    ctx.fill();
    return new THREE.CanvasTexture(cv);
}
const sprite = makeSprite();

// Split wiki / raw
const wikiPts = [], rawPts = [], wikiMap = [], rawMap = [];
points.forEach((p, i) => {
    if (p.source === 'wiki') { wikiMap.push(i); wikiPts.push(p); }
    else                     { rawMap.push(i);  rawPts.push(p); }
});

// Wiki cloud — vertex colors by node type
const wikiPos = new Float32Array(wikiPts.length * 3);
const wikiCol = new Float32Array(wikiPts.length * 3);
wikiPts.forEach((p, i) => {
    wikiPos[i*3]=p.x; wikiPos[i*3+1]=p.y; wikiPos[i*3+2]=p.z||0;
    const c = new THREE.Color(TYPE_COLORS[p.type] || DEFAULT_COLOR);
    wikiCol[i*3]=c.r; wikiCol[i*3+1]=c.g; wikiCol[i*3+2]=c.b;
});
const wikiGeo = new THREE.BufferGeometry();
wikiGeo.setAttribute('position', new THREE.BufferAttribute(wikiPos, 3));
wikiGeo.setAttribute('color',    new THREE.BufferAttribute(wikiCol, 3));
const wikiCloud = new THREE.Points(wikiGeo, new THREE.PointsMaterial({
    size:4, map:sprite, vertexColors:true,
    alphaTest:0.02, transparent:true,
    blending:THREE.AdditiveBlending, depthWrite:false, sizeAttenuation:false,
}));
scene.add(wikiCloud);

// Raw cloud
const rawPos = new Float32Array(rawPts.length * 3);
rawPts.forEach((p, i) => { rawPos[i*3]=p.x; rawPos[i*3+1]=p.y; rawPos[i*3+2]=p.z||0; });
const rawGeo = new THREE.BufferGeometry();
rawGeo.setAttribute('position', new THREE.BufferAttribute(rawPos, 3));
const rawCloud = new THREE.Points(rawGeo, new THREE.PointsMaterial({
    size:2, map:sprite, color:0x1565c0,
    alphaTest:0.02, transparent:true, opacity:0.4,
    blending:THREE.AdditiveBlending, depthWrite:false, sizeAttenuation:false,
}));
scene.add(rawCloud);

// Brain sphere container
(function addBrainSphere() {
    const R = 220;
    // outer shell — very faint
    const shell = new THREE.Mesh(
        new THREE.SphereGeometry(R, 48, 48),
        new THREE.MeshBasicMaterial({ color:0x00e5cc, wireframe:true, transparent:true, opacity:0.025 })
    );
    scene.add(shell);
    // inner equator ring
    const ring = new THREE.Mesh(
        new THREE.TorusGeometry(R, 0.4, 4, 96),
        new THREE.MeshBasicMaterial({ color:0x00e5cc, transparent:true, opacity:0.08 })
    );
    scene.add(ring);
    // meridian rings
    const m1 = ring.clone(); m1.rotation.x = Math.PI/2; scene.add(m1);
    const m2 = ring.clone(); m2.rotation.y = Math.PI/2; scene.add(m2);
})();

// Edges
if (edges.length) {
    const epos = new Float32Array(edges.length * 6);
    edges.forEach((e, i) => {
        const s=points[e.s], t=points[e.t];
        epos[i*6]=s.x; epos[i*6+1]=s.y; epos[i*6+2]=s.z||0;
        epos[i*6+3]=t.x; epos[i*6+4]=t.y; epos[i*6+5]=t.z||0;
    });
    const egeo = new THREE.BufferGeometry();
    egeo.setAttribute('position', new THREE.BufferAttribute(epos, 3));
    scene.add(new THREE.LineSegments(egeo, new THREE.LineBasicMaterial({
        color:0x00e5cc, opacity:0.07, transparent:true,
        blending:THREE.AdditiveBlending, depthWrite:false,
    })));
}

// Hover tooltip
const tooltip   = document.getElementById('tooltip');
const raycaster = new THREE.Raycaster();
raycaster.params.Points.threshold = 5;
const mouse = new THREE.Vector2(-9999,-9999);

window.addEventListener('mousemove', e => {
    mouse.x =  (e.clientX/innerWidth)*2  - 1;
    mouse.y = -(e.clientY/innerHeight)*2 + 1;
    raycaster.setFromCamera(mouse, camera);

    const wHits = raycaster.intersectObject(wikiCloud);
    const rHits = raycaster.intersectObject(rawCloud);
    let found = null, tc = null;
    if (wHits.length)      { found = wikiPts[wHits[0].index]; tc = TYPE_COLORS[found.type] || DEFAULT_COLOR; }
    else if (rHits.length) { found = rawPts[rHits[0].index];  tc = '#1565c0'; }

    if (found) {
        tooltip.style.display = 'block';
        const tx = e.clientX + 20, ty = e.clientY + 20;
        tooltip.style.left = (tx + 300 > innerWidth  ? e.clientX - 310 : tx) + 'px';
        tooltip.style.top  = (ty + 150 > innerHeight ? e.clientY - 160 : ty) + 'px';
        tooltip.innerHTML =
            '<div class="tip-title">' + found.title + '</div>' +
            '<span class="tip-badge" style="background:' + tc + '1a;color:' + tc + ';border:1px solid ' + tc + '55">' +
                (found.source === 'wiki' ? (found.type || 'concept') : 'raw') +
            '</span>' +
            (found.domain ? '<div class="tip-domain">' + found.domain + '</div>' : '') +
            (found.thesis ? '<div class="tip-thesis">' + found.thesis + '</div>' : '');
    } else {
        tooltip.style.display = 'none';
    }
});

window.addEventListener('resize', () => {
    camera.aspect = innerWidth/innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
});

(function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
})();
</script>
</body>
</html>"""

    html = (TMPL
        .replace("__POINTS__",      points_json)
        .replace("__EDGES__",       edges_json)
        .replace("__TYPE_COLORS__", type_colors_json)
        .replace("__TOTAL__",       f"{total:,}")
        .replace("__NEDGES__",      str(n_edges))
        .replace("__NWIKI__",       f"{n_wiki:,}")
        .replace("__NRAW__",        f"{n_raw:,}")
        .replace("__LEGEND__",      legend_items)
    )
    OUTPUT_PATH.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
