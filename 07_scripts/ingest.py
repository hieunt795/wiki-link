"""Source → wiki node ingest pipeline.

Steps:
  1. Normalize markdown source
  2. Chunk with smart break points
  3. (Encoding done by librarian.py sync after node creation)
  4. LLM extraction → draft wiki nodes
  5. Write nodes to 03_wiki/{type}/
  6. Update index.md, log.md, _source_registry.yaml
"""

from __future__ import annotations

import re
import yaml
from datetime import date
from pathlib import Path

from chunker import chunk_markdown, _split_frontmatter

ROOT          = Path(__file__).parent.parent
WIKI_ROOT     = ROOT / "03_wiki"
SCHEMA_ROOT   = ROOT / "01_schema"
REGISTRY_PATH = ROOT / "02_sources" / "_source_registry.yaml"
LOG_PATH      = WIKI_ROOT / "log.md"
INDEX_PATH    = WIKI_ROOT / "index.md"

NODE_DIRS = {
    "concept":      WIKI_ROOT / "concepts",
    "mechanism":    WIKI_ROOT / "mechanisms",
    "entity":       WIKI_ROOT / "entities",
    "relationship": WIKI_ROOT / "relationships",
    "contradiction":WIKI_ROOT / "contradictions",
    "synthesis":    WIKI_ROOT / "synthesis",
    "policy":       WIKI_ROOT / "policies",
    "framework":    WIKI_ROOT / "frameworks",
    "indicator":    WIKI_ROOT / "indicators",
}

TODAY = date.today().isoformat()


def ingest_source(source_path: str | Path, dry_run: bool = False) -> list[Path]:
    """Ingest a single source file into wiki nodes.

    In dry_run mode, prints what would be created without writing files.
    Returns list of created wiki node paths.
    """
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"Source not found: {path}")

    print(f"[ingest] Processing: {path}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm, body = _split_frontmatter(text)

    # Determine domain from registry if available
    domain = _guess_domain(path, fm)
    print(f"[ingest] Domain: {domain}")

    # Chunk
    chunks = chunk_markdown(text, target_tokens=900, source_file=str(path))
    print(f"[ingest] {len(chunks)} chunks")

    # LLM extraction (requires Claude to be running as agent)
    # This function returns a prompt — the agent runs it and creates nodes
    extraction_prompt = _build_extraction_prompt(path, body, fm, domain, chunks)

    if dry_run:
        print("[ingest] DRY RUN — extraction prompt:")
        print(extraction_prompt[:2000])
        print("... (truncated)")
        return []

    # In agent-driven mode, print the extraction prompt for Claude to act on
    print("\n" + "="*60)
    print("INGEST EXTRACTION PROMPT")
    print("="*60)
    print(extraction_prompt)
    print("="*60 + "\n")
    print("[ingest] Review the prompt above and create wiki nodes accordingly.")
    print(f"[ingest] After creating nodes, run: python librarian.py sync")
    return []


def create_wiki_node(
    node_type: str,
    title: str,
    thesis: str,
    source_path: str,
    domain: str = "monetary_policy",
    aliases: list[str] | None = None,
    tags: list[str] | None = None,
    body: str = "",
    confidence: int = 1,
    pages: str = "",
) -> Path:
    """Write a single wiki node file with proper frontmatter.

    Called by the agent after LLM extraction.
    confidence starts at 1 (stub) — agent raises after verification.
    """
    node_dir = NODE_DIRS.get(node_type, WIKI_ROOT / "concepts")
    node_dir.mkdir(parents=True, exist_ok=True)

    slug = _slugify(title)
    node_id = f"{slug}_001"
    filename = _camel_case(title) + ".md"
    out_path = node_dir / filename

    # Avoid overwrite — bump counter if exists
    counter = 1
    while out_path.exists():
        counter += 1
        node_id = f"{slug}_{counter:03d}"
        out_path = node_dir / _camel_case(title) + f"_{counter:03d}.md"

    fm = {
        "node_id":    node_id,
        "type":       node_type,
        "title":      title,
        "aliases":    aliases or [],
        "domain":     {"primary": domain},
        "tags":       tags or [],
        "confidence": confidence,
        "stability":  "evolving",
        "thesis":     thesis,
        "source_refs": [
            {"path": _repo_relative_path(source_path), "pages": pages or "", "weight": "primary"}
        ],
        "related":    [],
        "date_created": TODAY,
        "date_updated": TODAY,
    }

    fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    body_text = body if body else f"[LLM] Auto-generated stub from {Path(source_path).name}. Review and expand.\n"

    content = f"---\n{fm_str}---\n\n{body_text}\n"

    if not out_path.exists():
        out_path.write_text(content, encoding="utf-8")
        print(f"[ingest] Created: {out_path.relative_to(WIKI_ROOT.parent)}")
        _append_log(f"INGEST: Created {node_type} node `{title}` from {Path(source_path).name}")
        _update_source_registry(str(source_path), str(out_path))

    return out_path


def _build_extraction_prompt(path: Path, body: str, fm: dict, domain: str, chunks) -> str:
    # Load node types schema for prompt context
    node_types_text = ""
    schema_file = SCHEMA_ROOT / "node_types.md"
    if schema_file.exists():
        node_types_text = schema_file.read_text(encoding="utf-8")[:3000]

    domain_vocab = _get_domain_vocab(domain)

    prompt = f"""You are ingesting a source document into the Wiki-Agentic knowledge base.

SOURCE FILE: {path}
DOMAIN: {domain}
TITLE FROM FRONTMATTER: {fm.get('title', path.stem)}

NODE TYPES AVAILABLE:
{node_types_text[:1000]}

DOMAIN VOCABULARY TO SEED EXTRACTION:
{domain_vocab}

SOURCE CONTENT (first 3000 chars):
{body[:3000]}

TASK:
Extract 3-8 distinct wiki nodes from this source. For each node:
1. Determine the type: concept | mechanism | entity | relationship | policy | framework | indicator
2. Write a 1-3 sentence thesis (the core claim, not a description of the document)
3. List aliases including Vietnamese equivalents where relevant
4. Set confidence: 1 (you are generating this, source not fully verified)
5. Tag with domain-relevant tags

For each node, call: create_wiki_node(node_type, title, thesis, source_path, domain, aliases, tags)

RULES:
- Do NOT set confidence > 1 on auto-generated nodes
- Mark any synthesized sentence with [LLM]
- thesis must be a claim, not "this document discusses..."
- Every node must have at least one alias
- Focus on structural/mechanistic knowledge, not time-sensitive facts
"""
    return prompt


def _get_domain_vocab(domain: str) -> str:
    vocab = {
        "monetary_policy": "interest rate, QE, QT, corridor, floor system, reserve requirements, forward guidance, inflation targeting, transmission mechanism, policy rate",
        "fiscal_policy": "primary deficit, debt sustainability, crowding out, fiscal multiplier, automatic stabilizers, TGA, government bond issuance",
        "basel_risk": "CET1, Tier 1, RWA, LCR, NSFR, G-SIB, TLAC, bail-in, countercyclical buffer, IRB, SA approach",
        "financial_markets": "yield curve, duration, DV01, swap spread, repo, SOFR, FX basis, collateral, haircut, term premium",
        "macro_outlook": "GDP, CPI, output gap, current account, capital flows, FX reserves, business cycle, fiscal stance",
    }
    return vocab.get(domain, "")


def _guess_domain(path: Path, fm: dict) -> str:
    """Guess domain from file path and frontmatter tags."""
    tags = " ".join(fm.get("tags", [])).lower()
    path_str = str(path).lower()

    if any(k in path_str for k in ["bindseil", "central_bank", "monetary", "fed", "ecb", "boj", "conks"]):
        return "monetary_policy"
    if any(k in path_str for k in ["basel", "capital", "private_credit"]):
        return "basel_risk"
    if any(k in path_str for k in ["tuckman", "homer", "yield", "fixed_income", "swap", "repo", "choudhry"]):
        return "financial_markets"
    if any(k in path_str for k in ["imf_macro", "lipschitz", "fiscal", "watts_wray"]):
        return "macro_outlook"
    if "alm" in path_str or "elkenbracht" in path_str or "tata" in path_str:
        return "financial_markets"

    return "monetary_policy"  # default


def _slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")


def _camel_case(title: str) -> str:
    words = re.sub(r"[^a-zA-Z0-9 ]", " ", title).split()
    return "_".join(w.capitalize() for w in words if w)


def _append_log(entry: str):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        LOG_PATH.write_text("# Wiki Operation Log\n\n", encoding="utf-8")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n- **{TODAY}**: {entry}")


def _repo_relative_path(path: str | Path) -> str:
    """Return a repo-relative path using forward slashes when possible."""
    p = Path(path)
    root = ROOT.resolve()
    try:
        return p.resolve(strict=False).relative_to(root).as_posix()
    except Exception:
        return p.as_posix()


def _update_source_registry(source_path: str, wiki_node_path: str):
    if not REGISTRY_PATH.exists():
        return
    try:
        data = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or {}
        sources = data.get("sources", {})
        rel = _repo_relative_path(source_path)
        if rel in sources:
            sources[rel]["wiki_nodes"] = sources[rel].get("wiki_nodes", [])
            wiki_rel = _repo_relative_path(wiki_node_path)
            if wiki_rel not in sources[rel]["wiki_nodes"]:
                sources[rel]["wiki_nodes"].append(wiki_rel)
            sources[rel]["status"] = "partial"
            sources[rel]["ingest_date"] = TODAY
            data["meta"]["total_ingested"] = sum(
                1 for s in sources.values() if s.get("status") in ("ingested", "partial")
            )
            total = data["meta"].get("total_sources", 1)
            data["meta"]["coverage_pct"] = round(
                data["meta"]["total_ingested"] / total * 100, 1
            )
            data["meta"]["last_updated"] = TODAY
            REGISTRY_PATH.write_text(
                yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
                encoding="utf-8"
            )
    except Exception as e:
        print(f"[ingest] Warning: could not update source registry: {e}")
