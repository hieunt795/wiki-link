"""Source → wiki node ingest pipeline.

Steps:
  1. Normalize markdown source
  2. Chunk with smart break points
  3. (Encoding done by librarian.py sync after node creation)
  4. LLM extraction → draft wiki nodes
  5. Write nodes to 03_wiki/{type}/
  6. Update index.md, log.md, _source_registry.yaml

Deep mode (--deep):
  Processes ALL chunks in batches of BATCH_SIZE, with progress tracking
  and deduplication. Resumes from last completed batch on rerun.
"""

from __future__ import annotations

import json
import re
import sys
import yaml
from datetime import date
from pathlib import Path

# Force UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from chunker import chunk_markdown, _split_frontmatter

ROOT              = Path(__file__).parent.parent
WIKI_ROOT         = ROOT / "03_wiki"
SCHEMA_ROOT       = ROOT / "01_schema"
NODE_TEMPLATE_DIR = ROOT / "06_templates" / "core" / "node_creation"
REGISTRY_PATH     = ROOT / "02_sources" / "_source_registry.yaml"
LOG_PATH          = WIKI_ROOT / "log.md"
INDEX_PATH        = WIKI_ROOT / "index.md"
PROGRESS_PATH     = ROOT / ".cache" / "ingest_progress.json"

# Chunks per extraction batch in deep mode
BATCH_SIZE = 3
# Skip batch if useful content (non-heading lines) is below this char count
MIN_CONTENT_CHARS = 150

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
    "regulation":   WIKI_ROOT / "regulations",
}

TODAY = date.today().isoformat()


# ── Progress tracking ─────────────────────────────────────────────────────────

def _load_progress() -> dict:
    if PROGRESS_PATH.exists():
        try:
            return json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_progress(progress: dict):
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_PATH.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")


def _mark_batch_done(source_key: str, batch_idx: int):
    progress = _load_progress()
    done = progress.get(source_key, [])
    if batch_idx not in done:
        done.append(batch_idx)
    progress[source_key] = done
    _save_progress(progress)


def _completed_batches(source_key: str) -> set[int]:
    return set(_load_progress().get(source_key, []))


# ── Existing wiki node index (for deduplication) ─────────────────────────────

def _existing_node_titles() -> list[str]:
    titles = []
    for node_dir in NODE_DIRS.values():
        if not node_dir.exists():
            continue
        for f in node_dir.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                fm, _ = _split_frontmatter(text)
                if fm.get("title"):
                    titles.append(fm["title"])
            except Exception:
                pass
    return titles


# ── Main ingest entry point ───────────────────────────────────────────────────

def ingest_source(
    source_path: str | Path,
    dry_run: bool = False,
    deep: bool = False,
    start_batch: int = 0,
    max_batches: int = 0,
) -> list[Path]:
    """Ingest a single source file into wiki nodes.

    deep=True: process all chunks in batches (resumes from progress).
    start_batch: skip to this batch index (0-based).
    max_batches: stop after this many batches (0 = no limit).
    """
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"Source not found: {path}")

    print(f"[ingest] Processing: {path.name}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm, body = _split_frontmatter(text)
    domain = _guess_domain(path, fm)
    print(f"[ingest] Domain: {domain}")

    chunks = chunk_markdown(text, target_tokens=900, source_file=str(path))
    print(f"[ingest] {len(chunks)} chunks")

    if not deep:
        # ── Original single-pass mode ────────────────────────────────────────
        extraction_prompt = _build_extraction_prompt(path, body, fm, domain, chunks)
        if dry_run:
            print("[ingest] DRY RUN — extraction prompt:")
            print(extraction_prompt[:2000])
            print("... (truncated)")
            return []
        print("\n" + "=" * 60)
        print("INGEST EXTRACTION PROMPT")
        print("=" * 60)
        print(extraction_prompt)
        print("=" * 60 + "\n")
        print("[ingest] Review the prompt above and create wiki nodes accordingly.")
        print(f"[ingest] After creating nodes, run: python librarian.py sync")
        return []

    # ── Deep mode: all chunks, batch by batch ────────────────────────────────
    source_key = _repo_relative_path(path)
    batches = [chunks[i:i + BATCH_SIZE] for i in range(0, len(chunks), BATCH_SIZE)]
    completed = _completed_batches(source_key)

    print(f"[ingest][deep] {len(batches)} batches total, {len(completed)} already done.")
    print(f"[ingest][deep] Source: {source_key}\n")

    # Full type-selection cheatsheet (replaces old truncated node_types.md slice)
    node_types_text = _node_type_cheatsheet()

    domain_vocab = _get_domain_vocab(domain)

    # Ensure atomic root-term nodes exist for terms present in this source (real source_ref)
    if not dry_run:
        seed_atomic_nodes(domain, path)

    batches_run = 0

    for batch_idx, batch in enumerate(batches):
        if batch_idx < start_batch:
            continue
        if batch_idx in completed:
            print(f"[ingest][deep] Batch {batch_idx + 1}/{len(batches)} — already done, skipping.")
            continue

        # Skip near-empty batches (mostly headings/whitespace)
        combined_text = "\n\n".join(c.text for c in batch)
        content_chars = len(re.sub(r"^#+\s.*$", "", combined_text, flags=re.MULTILINE).strip())
        if content_chars < MIN_CONTENT_CHARS:
            print(f"[ingest][deep] Batch {batch_idx + 1}/{len(batches)} — thin content ({content_chars} chars), skipping.")
            _mark_batch_done(source_key, batch_idx)
            continue

        existing_titles = _existing_node_titles()
        prompt = _build_extraction_prompt_batch(
            path=path,
            fm=fm,
            domain=domain,
            batch=batch,
            batch_num=batch_idx + 1,
            total_batches=len(batches),
            node_types_text=node_types_text,
            domain_vocab=domain_vocab,
            existing_titles=existing_titles,
        )

        if dry_run:
            print(f"\n[ingest][deep] DRY RUN — Batch {batch_idx + 1}/{len(batches)}")
            print(prompt[:800])
            print("... (truncated)")
            if batch_idx == 0:
                break
            continue

        print(f"\n{'=' * 60}")
        print(f"BATCH {batch_idx + 1}/{len(batches)}  |  {path.name}  |  domain={domain}")
        print(f"{'=' * 60}")
        print(prompt)
        print(f"{'=' * 60}")
        print(f"[ingest][deep] After creating nodes for this batch, call:")
        print(f"  _mark_batch_done('{source_key}', {batch_idx})")
        print(f"{'=' * 60}\n")

        batches_run += 1
        if max_batches and batches_run >= max_batches:
            print(f"[ingest][deep] Reached max_batches={max_batches}. Run again to continue.")
            break

    remaining = len(batches) - len(completed) - batches_run
    print(f"\n[ingest][deep] Session done. Batches processed this run: {batches_run}. Still remaining: {remaining}.")
    if remaining > 0:
        next_batch = max((b for b in range(len(batches)) if b not in completed and b >= start_batch + batches_run), default=None)
        if next_batch is not None:
            print(f"[ingest][deep] Resume with: python librarian.py ingest {source_key} --deep --start-batch {next_batch}")

    return []


# ── Prompt builders ───────────────────────────────────────────────────────────

# Compact decision cheatsheet for all 10 node types. Replaces the old truncated
# node_types.md slices ([:800]/[:1000]/[:3000]) that only exposed concept+mechanism
# to the extractor — the root cause of the mechanism/concept type skew.
_TYPE_CHEATSHEET = """Choose the SINGLE best type for each node. Decision rules (check in order):

1. entity      → a NAMED actor or thing: central bank, institution, regulatory body,
                committee, person, market, or financial instrument.
                Includes: Fed, ECB, BOJ, SBV, PBoC, BIS, IMF, FSB, BCBS, MAS, BOE,
                ALCO, ISDA, SIFMA, JGB, SOFR, T-bill.
                Ask: "Is this a specific named WHO or WHAT-thing?"

2. indicator   → a MEASURABLE quantity with units + frequency + data source.
                Must answer: what is the unit? how often is it measured? where does data come from?
                Examples: NII ($), EVE ($), LCR (%), SOFR (bps/daily/NY Fed), CPI (%/monthly).
                A named metric without a clear unit/frequency stays as `concept`.

3. regulation  → a BINDING rule issued by an official regulatory/supervisory body.
                Signs: document number (Circular 22, BCBS d424), effective_date, binding_on field.
                Source usually under 02_sources/regulator/. NOT for CB operational decisions.

4. policy      → a SPECIFIC DATED decision or regime by an authority, with a defined period.
                Must have: named authority + start year (and often end year).
                Examples: Fed QE1-QE3 (2008-2014), BOJ YCC (2016-2024), Volcker shock (1979-1982),
                ECB PEPP (2020-2022), US_1970s_Stagflation_Policy_Regime, ECB_2024_Operational_Framework.
                If the node title contains a year or decade → ask yourself "is this a policy?" first.

5. framework   → a REUSABLE ANALYTICAL MODEL or tool with ENUMERABLE NAMED COMPONENTS.
                Must have: (a) named components that can be listed as a YAML array, AND
                (b) an application_domain (what analysis task does it enable?).
                Examples: IS-LM (components: IS curve, LM curve), IRRBB EVE/NII dual-metric
                (components: EVE metric, NII metric, shock scenarios), Flow of Funds (4-sector).
                NOT a framework: a description of how something works (→ concept or mechanism),
                a policy regime with a year, or a taxonomy without analytical components.

6. mechanism   → a CAUSAL PROCESS that unfolds in SEQUENTIAL STEPS (A→B→C).
                Must have real steps that could be listed as step 1, step 2, step 3.
                The word "mechanics" or "transmission" in a title does NOT make it a mechanism
                — only pick this if there is a genuine causal chain with conditions.

7. synthesis   → integrates ≥2 existing wiki nodes into a claim larger than their sum.
8. contradiction → documents two conflicting sourced claims on one topic.
9. relationship  → a single named directional edge between two nodes (rare as a standalone file).

10. concept    → DEFAULT. Any atomic idea/term that is none of the above.
                Use when: a topic is important but doesn't have enumerable components (→ not framework),
                no causal steps (→ not mechanism), no measurement unit (→ not indicator),
                no specific date/period (→ not policy), not a named actor (→ not entity).
                Examples: ALM, IRRBB (risk type), NMD, OAS, duration, collateral velocity,
                reserve requirements, corridor system, financial repression.

CLASSIFICATION GUARDS — check these before writing the type:
- "framework" without listing actual components → demote to `concept`
- "mechanism" without being able to write step 1 / step 2 → demote to `concept`
- Node title contains a year or decade + named authority → consider `policy` before `framework`
- Named body (BCBS, SBV, IMF, ALCO, ISDA…) → `entity`, not concept
- Measurable ratio/metric → `indicator`, not concept
- Create an ATOMIC node for any core domain term that deserves its own definition, even if
  the chunk only mentions it in passing (so other nodes can link to it)."""


def _load_node_template(type_name: str) -> str:
    """Load the node creation template for a given type from 06_templates/core/node_creation/."""
    path = NODE_TEMPLATE_DIR / f"{type_name}.yaml"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def _load_classify_template() -> str:
    """Load the classification decision tree from 06_templates/core/node_creation/classify.yaml."""
    path = NODE_TEMPLATE_DIR / "classify.yaml"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return _TYPE_CHEATSHEET  # fallback to inline if file missing


def _node_type_cheatsheet() -> str:
    """Return classification guidance — prefers classify.yaml template, falls back to inline."""
    return _load_classify_template()


def _build_extraction_prompt_batch(
    path: Path,
    fm: dict,
    domain: str,
    batch: list,
    batch_num: int,
    total_batches: int,
    node_types_text: str,
    domain_vocab: str,
    existing_titles: list[str],
) -> str:
    # Summarise headings in this batch for context
    headings = list(dict.fromkeys(c.heading for c in batch if c.heading))
    heading_ctx = " > ".join(headings) if headings else "(no section heading)"

    # Combine chunk texts
    combined = "\n\n---\n\n".join(c.text for c in batch)
    # Trim to ~5000 chars to stay within comfortable prompt length
    if len(combined) > 5000:
        combined = combined[:5000] + "\n... [truncated]"

    # Dedup hint: first 10 existing titles
    dedup_sample = existing_titles[:15]
    dedup_hint = "\n".join(f"  - {t}" for t in dedup_sample) if dedup_sample else "  (none yet)"

    return f"""You are ingesting batch {batch_num}/{total_batches} of source: {path.name}
Domain: {domain} | Section: {heading_ctx}
Source path: {_repo_relative_path(path)}

NODE TYPE SELECTION:
{node_types_text}

DOMAIN VOCABULARY (each core term below deserves its own atomic node — create it if missing):
{domain_vocab}

CONTENT (batch {batch_num}/{total_batches}):
{combined}

ALREADY IN WIKI (do NOT duplicate these):
{dedup_hint}

TASK — extract 1-4 NEW distinct wiki nodes from this batch content.

FRONTMATTER rules:
- Pick the right type per the cheatsheet above
- thesis: 1-3 sentence core CLAIM (not "this document discusses...")
- aliases: both acronym AND full name, plus Vietnamese equivalents
- confidence: 1 (auto-generated stub)
- Source ref pages: batch {batch_num} (chars ~{batch[0].position}-{batch[-1].position + len(batch[-1].text)})
- Skip introductory, bibliographic, or already-covered content

BODY — write a FULL structured body for each node (not a stub):

Use this format, selecting sections appropriate to the node type:

  ## Overview
  [2-4 paragraphs expanding the thesis. Use **bold** for key terms on first use.
   Mark every synthesised sentence [LLM]. Write in present tense.]

  ## [Type-specific section — choose ONE that fits:]
  - concept/framework → ## How It Works
    [Explain the structure, components, or causal logic. For frameworks: describe
     each component in 1-2 sentences. Use "A → B because [reason]" for causal claims.]
  - mechanism         → ## Causal Chain
    [Narrate each step: "Step N: X happens → Y follows when [condition]."]
  - policy            → ## Context and Instruments
    [Historical background, named instruments used, key decisions/dates.]
  - entity            → ## Role and Mandate
    [What this entity does, its formal mandate, who it reports to.]
  - indicator         → ## Interpretation
    [What the number means, direction of reading, normal ranges if known.]
  - regulation        → ## Key Requirements
    [What is required, of whom, phase-in timeline if applicable.]

  ## Evidence and Sources
  [Cite specific passages. Format: [RAW-BOOK p.X], [RAW-CLIP Title], [LLM-E estimate].
   Distinguish primary from supporting sources.]

  ## Related Concepts
  [1-2 connecting sentences linking to related nodes with [[wikilink]] syntax.]

SOURCE LABELS for body text:
  [RAW-BOOK p.X]    direct page reference in the raw source
  [RAW-CLIP Title]  from a Clipping in 02_sources/
  [LLM]             LLM-synthesised sentence — mark ALL synthesis
  [LLM-E ~range]    LLM-estimated range, not verified

For each node call:
  create_wiki_node(node_type, title, thesis,
                   source_path="{_repo_relative_path(path)}", domain="{domain}",
                   aliases=[...], tags=[...],
                   body="## Overview\\n\\n[full body here]\\n\\n## ...")

After creating nodes for this batch, mark it complete:
  _mark_batch_done("{_repo_relative_path(path)}", {batch_num - 1})
"""


def _build_extraction_prompt(path: Path, body: str, fm: dict, domain: str, chunks) -> str:
    """Original single-pass prompt (non-deep mode)."""
    node_types_text = _node_type_cheatsheet()

    domain_vocab = _get_domain_vocab(domain)

    return f"""You are ingesting a source document into the Wiki-Agentic knowledge base.

SOURCE FILE: {path}
DOMAIN: {domain}
TITLE FROM FRONTMATTER: {fm.get('title', path.stem)}

NODE TYPE SELECTION:
{node_types_text}

DOMAIN VOCABULARY (each core term deserves its own atomic node — create it if missing):
{domain_vocab}

SOURCE CONTENT (first 3000 chars):
{body[:3000]}

TASK:
Extract 3-8 distinct wiki nodes from this source. For each node:

FRONTMATTER:
1. Type — use the cheatsheet (concept | mechanism | entity | policy | framework |
   indicator | regulation | synthesis | contradiction | relationship).
   Do NOT default to "mechanism" or "framework" — check the decision rules.
2. thesis — 1-3 sentence core CLAIM (not "this document discusses...")
3. aliases — BOTH acronym and full name, plus Vietnamese equivalents
4. confidence: 1 (auto-generated, source not fully verified)
5. tags — domain-relevant lowercase hyphenated tags

Also: create an ATOMIC node for any core domain term used in the source that lacks
its own node (ALM, IRRBB, NII, EVE, NMD, ALCO, OAS, FTP...).

BODY — write a FULL structured body for each node:

  ## Overview
  [2-4 paragraphs expanding the thesis. Bold key terms. Mark [LLM] on synthesis.]

  ## [Type-specific section:]
  - concept/framework → ## How It Works (structure, components, logic)
  - mechanism         → ## Causal Chain (step-by-step: "Step N: X → Y when [cond]")
  - policy            → ## Context and Instruments (background, instruments, key dates)
  - entity            → ## Role and Mandate (what it does, formal mandate)
  - indicator         → ## Interpretation (what the number means, direction, ranges)
  - regulation        → ## Key Requirements (what is required, of whom, phase-in)

  ## Evidence and Sources
  [[RAW-BOOK p.X] or [RAW-CLIP Title] — cite specific passages, not just the file name.]

  ## Related Concepts
  [1-2 sentences linking to related nodes with [[wikilink]] syntax.]

SOURCE LABELS: [RAW-BOOK p.X] | [RAW-CLIP Title] | [LLM] for all synthesis | [LLM-E ~range]

For each node, call:
  create_wiki_node(node_type, title, thesis, source_path, domain, aliases, tags,
                   body="## Overview\\n\\n[full body here]\\n\\n## ...")

RULES:
- Do NOT set confidence > 1 on auto-generated nodes
- Mark EVERY synthesised sentence with [LLM]
- Focus on durable structural knowledge, not time-sensitive facts
"""


# ── Wiki node writer ──────────────────────────────────────────────────────────

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
    parent_node: str | None = None,
    related: list | None = None,
    extra_fields: dict | None = None,
) -> Path:
    """Write a single wiki node file with proper frontmatter.

    Called by the agent after LLM extraction.
    confidence starts at 1 (stub) — agent raises after verification.

    extra_fields: type-specific frontmatter (e.g. entity_type/jurisdiction for entity,
    steps for mechanism, indicator_type/frequency for indicator). Merged into frontmatter.
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
        out_path = node_dir / (_camel_case(title) + f"_{counter:03d}.md")

    fm_data = {
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
        "parent_node": parent_node,
        "related":    related or [],
        "date_created": TODAY,
        "date_updated": TODAY,
    }
    if extra_fields:
        fm_data.update(extra_fields)

    fm_str = yaml.dump(fm_data, allow_unicode=True, default_flow_style=False, sort_keys=False)
    body_text = body if body else f"[LLM] Auto-generated stub from {Path(source_path).name}. Review and expand.\n"

    content = f"---\n{fm_str}---\n\n{body_text}\n"

    if not out_path.exists():
        out_path.write_text(content, encoding="utf-8")
        print(f"[ingest] Created: {out_path.relative_to(WIKI_ROOT.parent)}")
        _append_log(f"INGEST: Created {node_type} node `{title}` from {Path(source_path).name}")
        _update_source_registry(str(source_path), str(out_path))

    return out_path


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get_domain_vocab(domain: str) -> str:
    vocab = {
        "monetary_policy": "interest rate, QE, QT, corridor, floor system, reserve requirements, forward guidance, inflation targeting, transmission mechanism, policy rate",
        "fiscal_policy": "primary deficit, debt sustainability, crowding out, fiscal multiplier, automatic stabilizers, TGA, government bond issuance",
        "alm": "asset liability management, FTP, funds transfer pricing, IRRBB, ALM, NMD, behavioralization, gap analysis, LCR, NSFR, behavioral model, maturity gap, repricing, EVE, NII, core deposit, replicating portfolio, non-maturity deposit, term deposit, overdraft, liquidity management banking book",
        "basel_risk": "CET1, Tier 1, RWA, LCR, NSFR, G-SIB, TLAC, bail-in, countercyclical buffer, IRB, SA approach",
        "financial_markets": "yield curve, duration, DV01, swap spread, repo, SOFR, FX basis, collateral, haircut, term premium",
        "macro_outlook": "GDP, CPI, output gap, current account, capital flows, FX reserves, business cycle, fiscal stance",
    }
    return vocab.get(domain, "")


# ── Atomic root-term registry ─────────────────────────────────────────────────
# Core domain terms that MUST each have their own atomic node so other nodes can link
# to them (the missing-hub problem). Each spec: type + canonical title + aliases
# (acronym + full + Vietnamese) + tags + optional type-specific extra_fields.
# seed_atomic_nodes() creates one only if (a) no node already covers the term AND
# (b) the term actually appears in the source being ingested (so source_ref is real).

ATOMIC_TERMS: dict[str, dict[str, dict]] = {
    "alm": {
        "ALM": dict(type="concept", title="Asset-Liability Management (ALM)",
                    aliases=["ALM", "Asset Liability Management", "Asset-Liability Management",
                             "quản lý tài sản nợ", "quản lý tài sản - nợ"],
                    tags=["alm", "balance-sheet"]),
        "IRRBB": dict(type="concept", title="Interest Rate Risk in the Banking Book (IRRBB)",
                      aliases=["IRRBB", "Interest Rate Risk in the Banking Book",
                               "rủi ro lãi suất trên sổ ngân hàng"],
                      tags=["irrbb", "alm", "interest-rate-risk"]),
        "NII": dict(type="indicator", title="Net Interest Income (NII)",
                    aliases=["NII", "Net Interest Income", "thu nhập lãi thuần"],
                    tags=["nii", "alm", "earnings"],
                    extra_fields=dict(indicator_type="financial", frequency="quarterly",
                                      data_source="bank financial statements")),
        "EVE": dict(type="indicator", title="Economic Value of Equity (EVE)",
                    aliases=["EVE", "Economic Value of Equity", "giá trị kinh tế của vốn chủ sở hữu"],
                    tags=["eve", "alm", "irrbb"],
                    extra_fields=dict(indicator_type="financial", frequency="quarterly",
                                      data_source="ALM model output")),
        "NMD": dict(type="concept", title="Non-Maturity Deposit (NMD)",
                    aliases=["NMD", "Non-Maturity Deposit", "NMDs", "tiền gửi không kỳ hạn"],
                    tags=["nmd", "alm", "deposit", "behavioral-model"]),
        "ALCO": dict(type="entity", title="Asset-Liability Committee (ALCO)",
                     aliases=["ALCO", "Asset Liability Committee", "ủy ban quản lý tài sản nợ"],
                     tags=["alco", "governance", "alm"],
                     extra_fields=dict(entity_type="institution", jurisdiction="global")),
        "FTP": dict(type="concept", title="Funds Transfer Pricing (FTP)",
                    aliases=["FTP", "Funds Transfer Pricing", "định giá điều chuyển vốn nội bộ"],
                    tags=["ftp", "alm", "pricing"]),
        "OAS": dict(type="indicator", title="Option-Adjusted Spread (OAS)",
                    aliases=["OAS", "Option-Adjusted Spread", "chênh lệch điều chỉnh quyền chọn"],
                    tags=["oas", "fixed-income", "spread"],
                    extra_fields=dict(indicator_type="market", frequency="daily",
                                      data_source="market pricing")),
    },
    "basel_risk": {
        "LCR": dict(type="indicator", title="Liquidity Coverage Ratio (LCR)",
                    aliases=["LCR", "Liquidity Coverage Ratio", "tỷ lệ đảm bảo thanh khoản"],
                    tags=["lcr", "basel", "liquidity"],
                    extra_fields=dict(indicator_type="financial_stability", frequency="monthly",
                                      data_source="regulatory reporting")),
        "NSFR": dict(type="indicator", title="Net Stable Funding Ratio (NSFR)",
                     aliases=["NSFR", "Net Stable Funding Ratio", "tỷ lệ nguồn vốn ổn định ròng"],
                     tags=["nsfr", "basel", "liquidity"],
                     extra_fields=dict(indicator_type="financial_stability", frequency="quarterly",
                                       data_source="regulatory reporting")),
    },
}


def _existing_node_keys() -> set[str]:
    """Lowercased set of all titles, aliases and file stems currently in the wiki."""
    keys: set[str] = set()
    for node_dir in NODE_DIRS.values():
        if not node_dir.exists():
            continue
        for f in node_dir.glob("*.md"):
            keys.add(f.stem.lower())
            try:
                fm, _ = _split_frontmatter(f.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                continue
            if not fm:
                continue
            if fm.get("title"):
                keys.add(str(fm["title"]).lower())
            for a in (fm.get("aliases") or []):
                keys.add(str(a).lower())
    return keys


def seed_atomic_nodes(domain: str, source_path: str | Path, dry_run: bool = False) -> list[str]:
    """Ensure atomic root-term nodes exist for terms that appear in this source.

    Creates a node only when the term has no existing coverage (title/alias/stem) AND
    the term (acronym or full name) literally appears in the source text — guaranteeing
    a real source_ref. Returns list of created (or would-create, if dry_run) titles.
    """
    registry = ATOMIC_TERMS.get(domain, {})
    if not registry:
        return []
    path = Path(source_path)
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    text_low = text.lower()
    existing = _existing_node_keys()
    created: list[str] = []

    for term, spec in registry.items():
        spec_aliases = [str(a) for a in spec.get("aliases", [])]
        # already covered?
        if any(a.lower() in existing for a in spec_aliases) or spec["title"].lower() in existing:
            continue
        # does the term actually appear in this source? (acronym as word, or full name)
        acronym_hit = re.search(rf"\b{re.escape(term)}\b", text) is not None
        name_hit = any(a.lower() in text_low for a in spec_aliases if len(a) > 4)
        if not (acronym_hit or name_hit):
            continue
        created.append(spec["title"])
        if dry_run:
            continue
        create_wiki_node(
            node_type=spec["type"],
            title=spec["title"],
            thesis=f"[LLM] Atomic root node for {term} — auto-seeded so other nodes can link "
                   f"to it. Definition pending review/expansion from {path.name}.",
            source_path=str(path),
            domain=domain,
            aliases=spec_aliases,
            tags=spec.get("tags", []),
            confidence=1,
            extra_fields=spec.get("extra_fields"),
        )
    if created:
        verb = "Would seed" if dry_run else "Seeded"
        print(f"[ingest][atomic] {verb} {len(created)} root node(s): {', '.join(created)}")
    return created


def _guess_domain(path: Path, fm: dict) -> str:
    """Guess domain from file path and frontmatter tags."""
    path_str = str(path).lower()

    if any(k in path_str for k in ["bindseil", "central_bank", "monetary", "fed", "ecb", "boj", "conks"]):
        return "monetary_policy"
    if any(k in path_str for k in ["basel", "capital", "private_credit"]):
        return "basel_risk"
    if any(k in path_str for k in ["tuckman", "homer", "yield", "fixed_income", "swap", "repo", "choudhry"]):
        return "financial_markets"
    if any(k in path_str for k in ["imf_macro", "lipschitz", "fiscal", "watts_wray"]):
        return "macro_outlook"
    if any(k in path_str for k in ["alm", "elkenbracht", "tata", "ftp", "bc030304", "bc030306"]):
        return "alm"

    return "monetary_policy"


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
