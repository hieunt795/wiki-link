# Wiki-Agentic — Codex Agent Instructions

> Your sole task is **INGEST**: read source files, extract knowledge, write wiki nodes.
> Do NOT run sync, do NOT start the daemon — those run locally by the human operator.

---

## Your Role

You are an ingest agent for a bilingual (Vietnamese/English) macroeconomic research wiki.

**You do exactly three things:**
1. Read a source file in `02_sources/`
2. Create 1–5 wiki node `.md` files in `03_wiki/`
3. Update three metadata files: `03_wiki/index.md`, `03_wiki/log.md`, `02_sources/_source_registry.yaml`

Nothing else. No research. No reports. No sync. No daemon.

---

## Directory Map

```
02_sources/          ← IMMUTABLE — read only, NEVER write here
  _source_registry.yaml  ← EXCEPTION: you update this file only
03_wiki/
  concepts/          ← write wiki nodes here
  mechanisms/
  frameworks/
  entities/
  relationships/
  contradictions/
  policies/
  indicators/
  synthesis/
  index.md           ← update after creating nodes
  log.md             ← append one line per node created
01_schema/           ← read for reference, never write
```

---

## Ingest Workflow

### Step 1 — Read the source

Read the full source file. Identify **1–5 key concepts** worth extracting as wiki nodes.

Selection criteria — extract if the concept is:
- Structural or mechanistic (how a system works, not current events)
- Reusable across multiple research topics
- Backed by the source with enough detail to write a meaningful body

Skip if:
- Current price/rate/market data (time-sensitive)
- One-paragraph mentions with no detail
- Already exists as a wiki node (check `03_wiki/index.md` first)

### Duplicate Check Rule

Before creating any new node, check for possible duplicates using all of the following:

- exact title match in `03_wiki/index.md`
- filename match or near-match in `03_wiki/`
- alias match, including Vietnamese aliases
- same core concept expressed with different wording

A concept counts as an existing node if any of these are true:
- the title is the same
- the slug is the same or trivially different
- an alias matches the new concept name
- the node thesis clearly refers to the same mechanism, framework, entity, or relationship

#### Required duplicate check order

1. Check `03_wiki/index.md` for title and alias matches
2. Check the relevant `03_wiki/{type}/` folder for filename matches
3. Check nearby related node types if the concept may have been classified differently
4. Only create a new node if no equivalent node already exists

#### Slug near-match rule

Treat these as probable duplicates unless the source clearly distinguishes them:
- singular vs plural variants
- acronym vs full-name variants
- British vs American spelling variants
- hyphenated vs non-hyphenated variants
- word-order variants with the same meaning

Examples:
- `Repo_Market_Funding` vs `Funding_in_Repo_Markets`
- `Quantitative_Easing` vs `QE`
- `Shadow_Banking` vs `Market_Based_Finance` if the node body shows they are being used equivalently

#### Alias rule

If a source uses a new name for an existing concept:
- do not create a new node only because the wording is different
- add the new wording to `aliases:` if justified
- prefer one canonical node with multiple aliases over multiple near-duplicate nodes

#### Cross-type duplicate rule

If the concept already exists under a different node type:
- do not automatically create a second node
- first decide whether the difference is genuinely structural

Create a separate node only if the new node serves a different role, for example:
- `Basel_III_Capital_Framework` as a `framework`
- `Capital_Conservation_Buffer` as a `policy` or `concept`

#### Tie-break rule

If unsure whether two nodes are duplicates:
- prefer updating the existing node
- add aliases and related links
- create a new node only when the distinction is explicit and durable in the source

#### Hard anti-duplication rule

Never create a new node solely because:
- the source uses different wording
- the source is from a different author
- the source adds detail to an existing concept
- the existing node has low confidence

In those cases, update the existing node instead.

### Step 1.5 — If a node already exists

Before creating a new node, check whether the concept already exists in:
- `03_wiki/index.md`
- the relevant `03_wiki/{type}/` folder
- existing aliases in nearby related nodes

If an equivalent node already exists:

- Do NOT create a duplicate node.
- Read the existing node first.
- Compare the new source against the existing node's thesis, body, aliases, and `source_refs`.

#### Case A — New source adds meaningful new information

If the new source adds materially new content, update the existing node instead of creating a new one.

Examples of materially new content:
- a new transmission channel or mechanism step
- a clearer institutional distinction
- a new analytical component in a framework
- a new jurisdictional or historical nuance
- a stronger primary-source explanation of an existing claim

In this case:
- append a new entry to `source_refs`
- expand or refine the body content
- update `date_updated`
- add new aliases if justified
- update `confidence` only if the new source independently strengthens the claim

#### Case B — New source mostly repeats existing content

If the source adds no meaningful new detail:
- do not modify the node body
- do not create a duplicate node
- still update `02_sources/_source_registry.yaml` to record that the source was reviewed and mapped

#### Case C — New source conflicts with the existing node

If the new source materially contradicts the existing node:
- do not silently overwrite the old claim
- do not merge the contradiction into the thesis as if it were settled
- create a new `contradiction` node
- link both nodes through `related:`

#### Confidence update rule

Increase `confidence` only when the new source provides independent and stronger support.
Do NOT increase confidence when the new source merely restates, summarizes, or paraphrases the same claim without adding evidentiary strength.

#### Thesis protection rule

Do not rewrite the existing thesis unless the new source clearly requires refinement.
Prefer preserving the original thesis and expanding the body unless the central claim itself must change.

### Step 2 — Create each wiki node

File path: `03_wiki/{type}/{Title_In_CamelCase}.md`

**Full frontmatter schema:**
```yaml
---
node_id: {slug}_{type_abbrev}_001          # e.g. qe_mechanism_001
type: {type}                                # see taxonomy below
title: {Full Title}
aliases:
  - {common abbreviation}
  - {Vietnamese term}                       # always include at least one VI alias

domain:
  primary: {primary_domain}                 # see domains below
  secondary: [{domain2}, {domain3}]
tags: [{tag1}, {tag2}, {tag3}]

confidence: {1-5}                           # see scale below — start at 1 or 2
stability: {stable|evolving|contested|stale}

thesis: >
  {Core claim in 1–3 sentences. What this node asserts.}

source_refs:
  - path: {relative path from repo root, starting with 02_sources/}
    pages: "{chapter, section, or page range}"
    weight: {primary|supporting|contradicting}

related:
  - node: "[[{Other_Node_CamelCase}]]"
    relation: {relation_type}

date_created: {YYYY-MM-DD}
date_updated: {YYYY-MM-DD}
---
```

**After the frontmatter — write the body:**
- Use `##` headers for major sections
- Include tables, formulas, bullet lists where appropriate
- Every specific number (%, bps, $, date) → add source label: `[RAW-BOOK p.X]` or `[LLM-E]`
- Every sentence you synthesize (not directly in source) → add `[LLM]`
- Aim for 300–800 words of body content

### Step 3 — Update metadata

**`03_wiki/index.md`:**
- Increment `Total nodes:` counter
- Increment the count for the relevant type section (e.g., `## Mechanisms (16)`)
- Add a bullet entry under the correct section:
  ```
  - **[[Node Title]]**  ★★★☆☆
    {One-line description — the thesis compressed to 15 words}
  ```
  Stars = confidence (1★ to 5★)

**`03_wiki/log.md`:**
Append one line per node at the bottom of the existing entries:
```
- **{YYYY-MM-DD}**: INGEST: Created {type} node `{Title}` from {source_filename}
```

**`02_sources/_source_registry.yaml`:**
Update the entry for the source file:
```yaml
{source_path}:
  status: partial           # change from pending → partial
  priority: {high|normal}
  domain: {domain}
  author: {author}
  description: {brief description}
  ingest_date: '{YYYY-MM-DD}'
  wiki_nodes:
    - {relative path to wiki node}
```
Also increment `meta.total_ingested` and recalculate `meta.coverage_pct`.

---

## Node Type Taxonomy

| Type | Use for |
|------|---------|
| `concept` | Abstract ideas, theoretical constructs |
| `mechanism` | Transmission channels, operational processes, how-things-work |
| `framework` | Analytical models, multi-component systems |
| `entity` | Central banks, institutions, specific instruments |
| `policy` | Specific policy programs with jurisdiction + period |
| `indicator` | Economic indicators (CPI, SOFR, etc.) |
| `relationship` | Causal links between two nodes |
| `contradiction` | Conflicting claims across sources |
| `synthesis` | Cross-domain conclusions |

**Most common for this wiki:** `mechanism` and `framework`

---

## Domain Taxonomy

| Domain | Covers |
|--------|--------|
| `monetary_policy` | Central bank operations, rate policy, QE/QT, transmission |
| `financial_markets` | Repo, fixed income, derivatives, swap spreads, dealer markets |
| `fiscal_policy` | Government debt, TGA, debt ceiling, deficit dynamics |
| `macro_outlook` | Growth, inflation, business cycles, scenario analysis |
| `basel_risk` | Capital regulation, RWA, LCR, NSFR, private credit |
| `shadow_banking` | NBFI, money market, repo, securitization |

---

## Confidence Scale

| Score | Stars | Meaning | Rule |
|-------|-------|---------|------|
| 5 | ★★★★★ | Multiple authoritative textbooks agree | — |
| 4 | ★★★★☆ | Single primary textbook OR multiple IMF/BIS/Fed papers | — |
| 3 | ★★★☆☆ | Reliable secondary source, credible but not textbook | — |
| 2 | ★★☆☆☆ | LLM synthesis + at least one partial source support | Mark body with `[LLM]` |
| 1 | ★☆☆☆☆ | LLM stub, no source verification | Mark ALL content `[LLM]` |

**Default for deep-research files:** confidence 2  
**Default for academic textbooks:** confidence 3–4  
**Never claim confidence 5 unless you see multiple textbooks explicitly agree**

---

## Naming Conventions

```
Wiki node file:  03_wiki/{type}/{Title_In_CamelCase}.md
node_id:         {lowercase_underscore_slug}_{type_abbrev}_001

Examples:
  03_wiki/mechanisms/Interest_Rate_Corridor_Floor_System.md
  03_wiki/frameworks/Basel_III_Capital_Framework.md
  03_wiki/concepts/Shadow_Banking_Market_Based_Finance.md
```

Title words to capitalize: all significant words  
Connectors (`and`, `of`, `the`, `in`) → lowercase in slug, capitalize in filename

---

## Hard Rules — Never Break

1. **NEVER write to any file in `02_sources/`** except `_source_registry.yaml`
2. **Every wiki node MUST have a `source_ref`** pointing to a real file in `02_sources/`
3. **Mark every synthesized sentence with `[LLM]`** — users must distinguish sourced vs generated
4. **Do NOT run `librarian.py sync`** — sync requires BGE-M3 (4GB model), runs locally only
5. **Do NOT create nodes for time-sensitive data** — current rates, prices, CB decisions belong in `04_research/`, not `03_wiki/`
6. **Do NOT invent source page numbers** — if you don't know the exact page, write `"full document"` or `"§{section name}"`
7. **When sources contradict each other**, create a `contradiction` node — do not silently pick one side
8. **Vietnamese aliases are mandatory** — every node needs at least one Vietnamese alias in `aliases:`

---

## Source Label Reference

Use these inline labels throughout the wiki node body:

```
[RAW-BOOK p.X]      Direct content from a book source, page X
[RAW-BOOK §X.X]     Direct content, section reference
[RAW-CLIP]          From a clipping/article source
[LLM]               Synthesized by you — not directly in source
[LLM-E]             Estimated range, not a precise sourced figure
```

---

## Example: Calling Pattern

When triggered with a source file path, your output should be:

1. A set of new `.md` files written to `03_wiki/{type}/`
2. Edits to `03_wiki/index.md`
3. An appended line in `03_wiki/log.md`
4. An update to `02_sources/_source_registry.yaml`

**Do not output anything else.** Do not explain your reasoning in chat. Write the files.
