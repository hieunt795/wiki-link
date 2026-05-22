"""Shared dataclasses for the Wiki-Agentic retrieval system."""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class SearchResult:
    node_id:     str
    stem:        str            # filename stem (slug)
    label:       str            # human-readable title
    source_file: str            # path in 02_sources/ or 03_wiki/
    source:      str            # "wiki" | "raw"
    confidence:  str            # "1"-"5" or "" for raw sources
    thesis:      str            # thesis field from frontmatter
    tags:        list           # tags list
    score:       float          # final ranked score
    found_by:    str            # "dense" | "sparse" | "fts" | "kg_expand:X" | "chain:A→B"
    body:        str = ""       # body text (loaded on demand)
    heatmap_ctx: str = ""       # context snippet for display
    domain:      str = ""       # primary domain
    stability:   str = ""       # stable | evolving | contested | stale
    node_type:   str = ""       # concept | mechanism | entity | ...


@dataclass
class Probe:
    state:        str           # INGESTED | PENDING | TRUE_GAP
    wiki_sem:     float         # BGE-M3 dense score against wiki
    wiki_fts:     float         # FTS5 score against wiki
    raw_sem:      float         # BGE-M3 dense score against raw sources
    raw_fts:      float         # FTS5 score against raw sources
    phrase_wiki:  int           # FTS5 phrase hit count in wiki
    phrase_raw:   int           # FTS5 phrase hit count in raw
    label_hits:   int           # exact label matches in wiki
    label_cov:    float         # fraction of query tokens found in wiki labels
    elapsed_ms:   int


@dataclass
class GapEntry:
    query:    str
    state:    str               # TRUE_GAP
    topic:    str               # research topic slug
    wiki_sem: float
    raw_sem:  float
    timestamp: str              # ISO 8601


@dataclass
class TemplateInsight:
    insight_id:        str
    target_template:   str      # path to template file
    observation:       str
    evidence:          str
    proposed_change:   str
    priority:          str      # low | medium | high
    status:            str      # pending | accepted | rejected
    session_source:    str      # topic_slug
    created:           str      # ISO 8601 date


@dataclass
class WikiNode:
    """Parsed wiki node from frontmatter + body."""
    node_id:     str
    node_type:   str
    title:       str
    aliases:     list[str]
    domain:      str
    tags:        list[str]
    confidence:  int
    stability:   str
    thesis:      str
    source_refs: list[dict]
    related:     list[dict]
    body:        str
    file_path:   str
    date_updated: str = ""
