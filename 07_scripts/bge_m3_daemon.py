"""Persistent BGE-M3 embedding server — TCP socket on 127.0.0.1:7432.

Lifecycle:
- Started by librarian.py (auto-start on first query via _start_lock)
- Monitors parent process via DAEMON_ANCHOR_PID env var
- Shuts down automatically when parent shell exits
- PID stored in .cache/daemon.pid

Protocol: JSONL over TCP (newline-delimited JSON requests/responses).

Request:
    {"query": "...", "mode": "dense|sparse|colbert|all",
     "top_k": 10, "threshold": 0.30,
     "wiki_only": false, "raw_only": false,
     "centroid_expand": false, "centroid_k": 3}

Response:
    {"dense_results": [...], "sparse_results": [...], "colbert_score": null,
     "elapsed_ms": 42}
"""

from __future__ import annotations

import json
import os
import socket
import sys
import threading
import time
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────
HOST = "127.0.0.1"
PORT = 7432
PID_FILE = Path(__file__).parent.parent / ".cache" / "daemon.pid"
IDLE_UNLOAD_SECONDS = 300   # 5 minutes idle → unload reranker from VRAM

_model = None
_model_lock = threading.Lock()
_last_query_time = time.time()


# ── Model loading ─────────────────────────────────────────────────────────────

def _load_model():
    global _model
    with _model_lock:
        if _model is not None:
            return _model
        print("[daemon] Loading BAAI/bge-m3 ...", flush=True)
        try:
            from FlagEmbedding import BGEM3FlagModel
            _model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
            print("[daemon] BGE-M3 loaded.", flush=True)
        except ImportError:
            print("[daemon] FlagEmbedding not installed. Run: pip install FlagEmbedding", flush=True)
            sys.exit(1)
        return _model


def _encode(texts: list[str], return_dense: bool, return_sparse: bool, return_colbert: bool) -> dict:
    model = _load_model()
    return model.encode(
        texts,
        return_dense=return_dense,
        return_sparse=return_sparse,
        return_colbert_vecs=return_colbert,
        batch_size=16,   # low peak memory — BGE-M3 fp16 ≈ 800MB/batch on CPU
    )


# ── Index references (set by librarian.py after build) ───────────────────────
_dense_index = None
_sparse_index = None
_fts_index = None


def set_indexes(dense, sparse, fts):
    global _dense_index, _sparse_index, _fts_index
    _dense_index = dense
    _sparse_index = sparse
    _fts_index = fts


# ── Request handling ──────────────────────────────────────────────────────────

def _handle_request(req: dict) -> dict:
    global _last_query_time
    _last_query_time = time.time()

    t0 = time.time()
    mode = req.get("mode", "dense")

    # Batch encode — returns raw vectors, no search
    if mode == "encode_batch":
        texts = req.get("texts", [])
        if not texts:
            return {"dense_vecs": [], "sparse_weights": [], "elapsed_ms": 0}
        enc = _encode(texts, return_dense=True, return_sparse=True, return_colbert=False)
        # Convert numpy arrays to native Python for JSON serialization
        dense_vecs_np = enc.get("dense_vecs")
        dense_vecs = dense_vecs_np.tolist() if hasattr(dense_vecs_np, "tolist") else []
        raw_weights = enc.get("lexical_weights", [{} for _ in texts])
        # lexical_weights: list of {token_id: np.float32} → convert to {str: float}
        sparse_weights = [
            {str(k): float(v) for k, v in w.items()} for w in raw_weights
        ]
        result = {
            "dense_vecs":     dense_vecs,
            "sparse_weights": sparse_weights,
            "elapsed_ms":     int((time.time() - t0) * 1000),
        }
        # Explicit cleanup — prevent tensor accumulation across batches (OOM on Windows)
        del enc, dense_vecs_np, raw_weights
        import gc
        gc.collect()
        return result

    query = req.get("query", "")
    top_k = req.get("top_k", 10)
    threshold = req.get("threshold", 0.30)
    wiki_only = req.get("wiki_only", False)
    raw_only = req.get("raw_only", False)
    centroid_expand = req.get("centroid_expand", False)
    centroid_k = req.get("centroid_k", 3)

    result: dict = {"dense_results": [], "sparse_results": [], "colbert_score": None}

    want_dense = mode in ("dense", "all")
    want_sparse = mode in ("sparse", "all")
    want_colbert = mode == "colbert"

    # Encode query
    enc = _encode([query], return_dense=want_dense, return_sparse=want_sparse, return_colbert=want_colbert)

    # Dense search
    if want_dense and _dense_index is not None:
        q_vec = enc["dense_vecs"][0]
        result["dense_results"] = _dense_index.search(
            q_vec, top_k=top_k, threshold=threshold,
            wiki_only=wiki_only, raw_only=raw_only,
        )

        # Centroid PRF expansion
        if centroid_expand and result["dense_results"]:
            seed_vecs = [_dense_index.reconstruct(r["faiss_idx"]) for r in result["dense_results"][:centroid_k]]
            import numpy as np
            centroid = np.mean(seed_vecs, axis=0)
            centroid = centroid / (np.linalg.norm(centroid) + 1e-9)
            extra = _dense_index.search(centroid, top_k=top_k, threshold=threshold,
                                        wiki_only=wiki_only, raw_only=raw_only)
            # Merge: deduplicate by node_id, keep best score
            seen = {r["node_id"] for r in result["dense_results"]}
            for r in extra:
                if r["node_id"] not in seen:
                    result["dense_results"].append(r)
                    seen.add(r["node_id"])

    # Sparse search
    if want_sparse and _sparse_index is not None:
        q_weights = enc.get("lexical_weights", [{}])[0]
        result["sparse_results"] = _sparse_index.query_sparse(
            q_weights, top_k=top_k, wiki_only=wiki_only, raw_only=raw_only,
        )

    result["elapsed_ms"] = int((time.time() - t0) * 1000)
    return result


def _handle_client(conn: socket.socket):
    try:
        buf = b""
        while True:
            data = conn.recv(4096)
            if not data:
                break
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                try:
                    req = json.loads(line.decode("utf-8"))
                    resp = _handle_request(req)
                    conn.sendall((json.dumps(resp) + "\n").encode("utf-8"))
                except Exception as e:
                    err = json.dumps({"error": str(e)}) + "\n"
                    conn.sendall(err.encode("utf-8"))
    finally:
        conn.close()


# ── Anchor monitoring (auto-shutdown when parent exits) ───────────────────────

def _monitor_anchor():
    anchor_pid = os.environ.get("DAEMON_ANCHOR_PID")
    if not anchor_pid:
        return
    anchor_pid = int(anchor_pid)
    while True:
        time.sleep(5)
        if not _is_pid_alive(anchor_pid):
            print("[daemon] Anchor process gone. Shutting down.", flush=True)
            PID_FILE.unlink(missing_ok=True)
            os._exit(0)


# ── Server entry point ────────────────────────────────────────────────────────

def cmd_start():
    """Start the daemon server. Called as subprocess by librarian.py."""
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()))

    # Pre-load model immediately at startup
    _load_model()

    # Start anchor monitor thread
    t = threading.Thread(target=_monitor_anchor, daemon=True)
    t.start()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(8)
    print(f"[daemon] Listening on {HOST}:{PORT}", flush=True)

    while True:
        conn, _ = srv.accept()
        ct = threading.Thread(target=_handle_client, args=(conn,), daemon=True)
        ct.start()


# ── Client-side query (called from search modules) ────────────────────────────

_start_lock = threading.Lock()
_daemon_proc = None


def query_daemon(
    query: str,
    mode: str = "dense",
    top_k: int = 10,
    threshold: float = 0.30,
    wiki_only: bool = False,
    raw_only: bool = False,
    centroid_expand: bool = False,
    centroid_k: int = 3,
) -> dict:
    """Send a query to the daemon. Auto-starts if not running."""
    _ensure_running()
    req = {
        "query": query, "mode": mode, "top_k": top_k, "threshold": threshold,
        "wiki_only": wiki_only, "raw_only": raw_only,
        "centroid_expand": centroid_expand, "centroid_k": centroid_k,
    }
    return _send(req)


def _send(req: dict, timeout: float = 300) -> dict:
    """Send a request to the daemon and return the response dict.

    timeout: seconds to wait for response (default 300 — encode_batch can be slow on CPU).
    """
    try:
        with socket.create_connection((HOST, PORT), timeout=10) as s:
            s.settimeout(timeout)          # longer timeout for the actual response
            payload = (json.dumps(req) + "\n").encode("utf-8")
            s.sendall(payload)
            resp = b""
            while True:
                chunk = s.recv(65536)      # larger buffer for big encode responses
                if not chunk:
                    break
                resp += chunk
                if b"\n" in resp:
                    break
            return json.loads(resp.split(b"\n")[0])
    except ConnectionRefusedError:
        return {"dense_results": [], "sparse_results": [], "error": "daemon not running"}


def _is_pid_alive(pid: int) -> bool:
    """Cross-platform: check if a process is alive."""
    try:
        if sys.platform == "win32":
            import ctypes
            SYNCHRONIZE = 0x00100000
            handle = ctypes.windll.kernel32.OpenProcess(SYNCHRONIZE, False, pid)
            if handle == 0:
                return False
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        else:
            os.kill(pid, 0)
            return True
    except (ProcessLookupError, PermissionError, OSError):
        return False


def _ensure_running():
    global _daemon_proc
    with _start_lock:
        # Check if already running via PID file
        if PID_FILE.exists():
            pid = int(PID_FILE.read_text().strip())
            if _is_pid_alive(pid):
                return  # already running
            PID_FILE.unlink(missing_ok=True)

        # Start as subprocess — no DAEMON_ANCHOR_PID: daemon must outlive the
        # calling process (sync exits after encoding; daemon stays for searches)
        import subprocess
        env = os.environ.copy()
        env.pop("DAEMON_ANCHOR_PID", None)   # remove if inherited from parent shell
        _daemon_proc = subprocess.Popen(
            [sys.executable, __file__, "start"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # Wait for daemon to become available (up to 180s for model load)
        for _ in range(360):
            time.sleep(0.5)
            try:
                with socket.create_connection((HOST, PORT), timeout=1):
                    return
            except (ConnectionRefusedError, OSError):
                pass
        raise RuntimeError("BGE-M3 daemon failed to start within 180 seconds.")


def is_running() -> bool:
    if not PID_FILE.exists():
        return False
    try:
        pid = int(PID_FILE.read_text().strip())
        return _is_pid_alive(pid)
    except Exception:
        return False


def cmd_stop():
    if not PID_FILE.exists():
        print("Daemon not running.")
        return
    pid = int(PID_FILE.read_text().strip())
    try:
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.kernel32.TerminateProcess(
                ctypes.windll.kernel32.OpenProcess(1, False, pid), 0
            )
        else:
            os.kill(pid, 15)  # SIGTERM
        PID_FILE.unlink(missing_ok=True)
        print(f"Daemon (pid {pid}) stopped.")
    except Exception as e:
        print(f"Could not stop daemon: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        cmd_start()
    elif len(sys.argv) > 1 and sys.argv[1] == "stop":
        cmd_stop()
    else:
        print("Usage: bge_m3_daemon.py start|stop")
