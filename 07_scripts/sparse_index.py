"""BGE-M3 sparse vector index — SQLite inverted index.

Stores neural-learned token weights (NOT traditional BM25). These are
BGE-M3 `lexical_weights` output: token_id → weight, capturing semantic
importance in addition to lexical frequency.

Also builds an FTS5 full-text search index for exact phrase matching and
label coverage probing (used by synthesis_search.probe()).
"""

from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path

SPARSE_DB = Path(__file__).parent.parent / ".cache" / "bge_m3_sparse.db"
FTS_DB    = Path(__file__).parent.parent / ".cache" / "wiki_fts.db"


# ── Sparse index (BGE-M3 lexical weights) ─────────────────────────────────────

class SparseIndex:
    def __init__(self, db_path: Path = SPARSE_DB):
        self.db_path = db_path
        self._conn: sqlite3.Connection | None = None

    def _connect(self) -> sqlite3.Connection:
        if self._conn is None:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self._conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute("PRAGMA synchronous=NORMAL")
        return self._conn

    def create_tables(self):
        conn = self._connect()
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS sparse_postings (
                token_id  INTEGER,
                doc_id    TEXT,
                weight    REAL,
                source    TEXT,
                PRIMARY KEY (token_id, doc_id)
            );
            CREATE INDEX IF NOT EXISTS idx_sparse_token ON sparse_postings(token_id);
            CREATE INDEX IF NOT EXISTS idx_sparse_doc   ON sparse_postings(doc_id);

            CREATE TABLE IF NOT EXISTS sparse_meta (
                doc_id      TEXT PRIMARY KEY,
                stem        TEXT,
                label       TEXT,
                source      TEXT,
                source_file TEXT,
                confidence  TEXT,
                tags        TEXT,
                thesis      TEXT,
                domain      TEXT
            );
        """)
        conn.commit()

    def insert_doc(self, doc_id: str, lexical_weights: dict[int, float], meta: dict):
        """Insert or replace a document's sparse weights."""
        conn = self._connect()
        source = meta.get("source", "")

        # Upsert metadata
        conn.execute("""
            INSERT OR REPLACE INTO sparse_meta
                (doc_id, stem, label, source, source_file, confidence, tags, thesis, domain)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (
            doc_id,
            meta.get("stem", ""),
            meta.get("label", ""),
            source,
            meta.get("source_file", ""),
            str(meta.get("confidence", "")),
            json.dumps(meta.get("tags", [])),
            meta.get("thesis", "")[:500],
            meta.get("domain", ""),
        ))

        # Delete old postings for this doc then re-insert
        conn.execute("DELETE FROM sparse_postings WHERE doc_id=?", (doc_id,))
        conn.executemany(
            "INSERT INTO sparse_postings(token_id,doc_id,weight,source) VALUES(?,?,?,?)",
            [(int(tid), doc_id, float(w), source) for tid, w in lexical_weights.items()]
        )
        conn.commit()

    def query_sparse(
        self,
        query_weights: dict[int | str, float],
        top_k: int = 10,
        wiki_only: bool = False,
        raw_only: bool = False,
    ) -> list[dict]:
        """Score documents by dot product of query × doc sparse vectors."""
        conn = self._connect()

        scores: dict[str, float] = {}
        for token_id, qw in query_weights.items():
            tid = int(token_id)
            source_filter = ""
            if wiki_only:
                source_filter = " AND source='wiki'"
            elif raw_only:
                source_filter = " AND source='raw'"

            rows = conn.execute(
                f"SELECT doc_id, weight FROM sparse_postings WHERE token_id=?{source_filter}",
                (tid,)
            ).fetchall()

            for doc_id, dw in rows:
                scores[doc_id] = scores.get(doc_id, 0.0) + float(qw) * float(dw)

        if not scores:
            return []

        top_docs = sorted(scores.items(), key=lambda x: -x[1])[:top_k]

        results = []
        for doc_id, score in top_docs:
            row = conn.execute(
                "SELECT stem,label,source,source_file,confidence,tags,thesis,domain FROM sparse_meta WHERE doc_id=?",
                (doc_id,)
            ).fetchone()
            if row:
                results.append({
                    "node_id":    doc_id,
                    "stem":       row[0],
                    "label":      row[1],
                    "source":     row[2],
                    "source_file": row[3],
                    "confidence": row[4],
                    "tags":       json.loads(row[5] or "[]"),
                    "thesis":     row[6],
                    "domain":     row[7],
                    "score":      score,
                })

        return results

    def clear(self):
        conn = self._connect()
        conn.executescript("""
            DELETE FROM sparse_postings;
            DELETE FROM sparse_meta;
        """)
        conn.commit()

    def status(self) -> dict:
        if not self.db_path.exists():
            return {"built": False}
        conn = self._connect()
        n_docs = conn.execute("SELECT COUNT(DISTINCT doc_id) FROM sparse_meta").fetchone()[0]
        n_postings = conn.execute("SELECT COUNT(*) FROM sparse_postings").fetchone()[0]
        return {"built": True, "docs": n_docs, "postings": n_postings}


# ── FTS5 index (exact phrase matching + coverage probe) ───────────────────────

class FTSIndex:
    """SQLite FTS5 index for exact phrase matching and label coverage probing.

    NOT used for primary ranking (BGE-M3 sparse handles that).
    Used for:
    - synthesis_search.probe(): label matching, phrase hit counting
    - Exact term lookups (acronyms: NSFR, YCC, CET1)
    - Vietnamese query augmentation via vi_en.py
    """

    def __init__(self, db_path: Path = FTS_DB):
        self.db_path = db_path
        self._conn: sqlite3.Connection | None = None

    def _connect(self) -> sqlite3.Connection:
        if self._conn is None:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self._conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
            self._conn.execute("PRAGMA journal_mode=WAL")
        return self._conn

    def create_tables(self):
        conn = self._connect()
        conn.executescript("""
            CREATE VIRTUAL TABLE IF NOT EXISTS fts_docs USING fts5(
                node_id,
                stem,
                label,
                thesis,
                body,
                tags,
                source,
                source_file,
                confidence,
                domain,
                content='',
                tokenize='unicode61 remove_diacritics 0'
            );

            CREATE TABLE IF NOT EXISTS fts_meta (
                node_id     TEXT PRIMARY KEY,
                stem        TEXT,
                label       TEXT,
                source      TEXT,
                source_file TEXT,
                confidence  TEXT,
                tags        TEXT,
                thesis      TEXT,
                domain      TEXT
            );
        """)
        conn.commit()

    def insert_doc(self, doc_id: str, label: str, thesis: str, body: str,
                   tags: list, source: str, source_file: str,
                   confidence: str, domain: str, stem: str = ""):
        conn = self._connect()
        conn.execute("DELETE FROM fts_docs WHERE node_id=?", (doc_id,))
        conn.execute("""
            INSERT INTO fts_docs(node_id, stem, label, thesis, body, tags, source, source_file, confidence, domain)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (doc_id, stem, label, thesis, body[:2000], " ".join(tags), source, source_file, confidence, domain))

        conn.execute("""
            INSERT OR REPLACE INTO fts_meta(node_id,stem,label,source,source_file,confidence,tags,thesis,domain)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, (doc_id, stem, label, source, source_file, confidence, json.dumps(tags), thesis[:500], domain))
        conn.commit()

    def query_fts(
        self,
        query: str,
        top_k: int = 10,
        wiki_only: bool = False,
        raw_only: bool = False,
    ) -> list[dict]:
        """FTS5 BM25 search. Used for phrase matching and fallback retrieval."""
        conn = self._connect()

        # Escape FTS5 special chars
        safe_query = _escape_fts(query)
        source_clause = ""
        if wiki_only:
            source_clause = " AND source='wiki'"
        elif raw_only:
            source_clause = " AND source='raw'"

        try:
            rows = conn.execute(f"""
                SELECT node_id, stem, label, source, source_file, confidence, tags, thesis, domain,
                       rank
                FROM fts_docs
                WHERE fts_docs MATCH ? {source_clause}
                ORDER BY rank
                LIMIT ?
            """, (safe_query, top_k)).fetchall()
        except sqlite3.OperationalError:
            return []

        results = []
        for row in rows:
            results.append({
                "node_id":    row[0],
                "stem":       row[1],
                "label":      row[2],
                "source":     row[3],
                "source_file": row[4],
                "confidence": row[5],
                "tags":       json.loads(row[6] or "[]"),
                "thesis":     row[7],
                "domain":     row[8],
                "score":      abs(float(row[9])),  # FTS5 rank is negative
            })

        return results

    def label_hits(self, query: str, source: str = "wiki") -> int:
        """Count documents whose label exactly matches any query token."""
        conn = self._connect()
        tokens = query.lower().split()
        count = 0
        for tok in tokens:
            if len(tok) < 2:
                continue
            n = conn.execute(
                "SELECT COUNT(*) FROM fts_meta WHERE LOWER(label) LIKE ? AND source=?",
                (f"%{tok}%", source)
            ).fetchone()[0]
            count += n
        return count

    def label_token_coverage(self, query: str, source: str = "wiki") -> float:
        """Fraction of query tokens found in any wiki label."""
        conn = self._connect()
        tokens = [t for t in query.lower().split() if len(t) > 2]
        if not tokens:
            return 0.0
        matched = 0
        for tok in tokens:
            n = conn.execute(
                "SELECT COUNT(*) FROM fts_meta WHERE LOWER(label) LIKE ? AND source=?",
                (f"%{tok}%", source)
            ).fetchone()[0]
            if n > 0:
                matched += 1
        return matched / len(tokens)

    def phrase_hit_count(self, query: str, source: str) -> int:
        """Count FTS5 hits for query against a specific source type."""
        results = self.query_fts(query, top_k=100, wiki_only=(source == "wiki"), raw_only=(source == "raw"))
        return len(results)

    def clear(self):
        conn = self._connect()
        conn.executescript("""
            DELETE FROM fts_docs;
            DELETE FROM fts_meta;
        """)
        conn.commit()

    def status(self) -> dict:
        if not self.db_path.exists():
            return {"built": False}
        conn = self._connect()
        n = conn.execute("SELECT COUNT(*) FROM fts_meta").fetchone()[0]
        return {"built": True, "docs": n}


def _escape_fts(query: str) -> str:
    """Escape FTS5 special characters in query string."""
    special = set('"*^()~')
    escaped = "".join(c if c not in special else " " for c in query)
    # Wrap in quotes if it looks like a phrase
    cleaned = escaped.strip()
    return cleaned if cleaned else '""'
