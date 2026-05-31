# Frontmatter Convention — Wiki Node Specification

Every file in `03_wiki/` MUST have valid YAML frontmatter. This is the contract
that governs retrieval, reranking, linting, and cross-linking behavior.

---

## Full Frontmatter Template

```yaml
---
# ── IDENTITY ──────────────────────────────────────────────────────────────────
node_id: concept_title_001                 # Lowercase + underscores. Stable forever — never rename.
type: concept                              # See 01_schema/node_types.md for full taxonomy
title: "Full Human-Readable Title"
aliases:
  - Short Name
  - Acronym
  - tên tiếng Việt                         # Include Vietnamese aliases for bilingual search

# ── CLASSIFICATION ─────────────────────────────────────────────────────────────
domain:
  primary: monetary_policy                 # One of: monetary_policy | fiscal_policy |
                                           #   alm | basel_risk | financial_markets | macro_outlook
  secondary:                               # Optional additional domains
    - financial_markets
tags:                                      # Lowercase, hyphenated. Max 10.
  - central-bank
  - balance-sheet
  - unconventional-policy

# ── KNOWLEDGE QUALITY ──────────────────────────────────────────────────────────
confidence: 1                              # 1–5. Always start at 1. See 01_schema/confidence_scale.md.
stability: evolving                        # stable | evolving | contested | stale

# ── CORE CONTENT ───────────────────────────────────────────────────────────────
thesis: >                                  # 1–3 sentences. The essential claim of this node.
  [The central, durable claim this node makes. Written in present tense.
   This is what the retrieval system indexes most heavily.]

# ── PROVENANCE ────────────────────────────────────────────────────────────────
source_refs:                               # At least one required for confidence >= 2.
  - path: 02_sources/books/author_title/filename.md
    pages: "ch4, pp.112-135"               # Section/page reference within the source
    weight: primary                        # primary | supporting | contradicting

# ── HIERARCHY ─────────────────────────────────────────────────────────────────
parent_node: null                          # Optional. Single primary parent. null if top-level.
                                           # Priority: parent_framework > parent_mechanism
                                           # > component_of > part_of
                                           # Excludes extends/implements (peer-level).

# ── RELATIONSHIP GRAPH ────────────────────────────────────────────────────────
related:                                   # Optional. Use [[wikilink]] syntax.
  - node: "[[Other_Node_Title]]"
    relation: mechanism_of                 # See relation types in node_types.md
contradicts:                               # Optional. Must create a contradiction node.
  - node: "[[Conflicting_Node]]"
    note: "Brief description of the conflict"
    contradiction_node: "[[Contra_Topic_001]]"

# ── LIFECYCLE ─────────────────────────────────────────────────────────────────
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
promoted_from: null                        # Path to research finding if promoted
---
```

---

## Type-Specific Extra Fields

### `mechanism` nodes add:
```yaml
steps:
  - "Step 1: [what happens]"
  - "Step 2: [what follows]"
transmission_lags: immediate | short | medium | long
empirical_evidence: strong | mixed | weak | contested
```

### `entity` nodes add:
```yaml
entity_type: institution | central_bank | person | instrument | market
jurisdiction: US | EU | JP | VN | global
established: YYYY
mandate: "..."
```

### `contradiction` nodes replace thesis with:
```yaml
claim_a:
  statement: "..."
  sources:
    - path: "02_sources/..."
      weight: primary
  confidence: N
  stance: "label for this position"
claim_b:
  statement: "..."
  sources:
    - path: "02_sources/..."
      weight: primary
  confidence: N
  stance: "label for this position"
resolution_status: open | resolved | context_dependent
resolution_note: "..."
analyst_note: "..."
affects_nodes:
  - "[[NodeA]]"
  - "[[NodeB]]"
```

### `policy` nodes add:
```yaml
jurisdiction: US | EU | JP | VN | global
period: "YYYY-YYYY"
policy_type: conventional_monetary | unconventional_monetary | fiscal | regulatory | macroprudential
instruments:
  - "Instrument 1"
  - "Instrument 2"
outcome: "..."
```

### `indicator` nodes add:
```yaml
indicator_type: monetary | fiscal | market | survey | real | financial_stability
frequency: daily | weekly | monthly | quarterly | annual
data_source: "..."
interpretation: "..."
```

### `regulation` nodes add:
```yaml
issuing_body: BCBS | SBV | Fed | ECB | FSB | IOSCO | MAS | BOJ | BIS | other
jurisdiction: global | US | EU | VN | JP | SG | UK | ...
regulation_type: capital | liquidity | leverage | conduct | reporting | macroprudential | fx_policy | payment_system | resolution | other
document_id: "Official document name/number"
effective_date: YYYY-MM-DD
current_status: proposed | consultative | final | phased_in | superseded
binding_on: banks | g-sibs | broker_dealers | all_financial_entities | central_banks | ...
key_requirements:
  - "..."
phase_in_schedule: "Optional"
```

---

## Validation Rules (enforced by linter.py)

**Hard failures (linter blocks sync):**
- Missing `node_id`, `type`, `title`, `confidence`, `thesis`
- `confidence >= 2` with empty `source_refs`
- `type: contradiction` without both `claim_a` and `claim_b`
- `contradicts:` entry without a matching `contradiction_node`

**Soft warnings (linter reports but does not block):**
- `confidence: 1` nodes older than 30 days (should be reviewed or deleted)
- No `related:` entries (isolated node — check for missing links)
- `stability: stale` without a `last_reviewed` update in the past 90 days
- Body contains `[LLM]` but `confidence > 2` (inconsistent trust signal)
- Missing Vietnamese alias when domain involves Vietnamese policy context

---

## Body Format (after frontmatter)

All nodes share the same opening and closing sections. The middle section varies by type.

### Shared sections (all types)

```markdown
## Overview

[2-4 paragraphs. Expand on the thesis. Use **bold** for key terms on first introduction.
 Write in present tense. Mark every synthesised sentence with [LLM].]
```

### Type-specific middle section

```markdown
## How It Works          ← concept, framework
[Explain the structure, components, or logic. For frameworks: describe each component
 in 1-2 sentences. Use "A → B because [reason]. B → C when [condition]" for causal claims.]

## Causal Chain          ← mechanism
[Narrate each step from the steps[] list:
 "Step 1: X happens because [reason]."
 "Step 2: Y follows when [condition]. If [exception], the chain breaks at this point."
 Every causal claim must state the condition under which it holds.]

## Context and Instruments   ← policy
[Historical background: what problem this policy addressed, what preceded it.
 Instruments used: bullet list of specific tools with dates if applicable.
 Key decisions or turning points with dates.]

## Role and Mandate      ← entity
[What this entity does and why it exists. Formal mandate if applicable.
 Who it reports to, who it regulates. Governance structure if relevant.]

## Interpretation        ← indicator
[What the number means: which direction is "good", what normal ranges look like.
 How to read movements: "a rise in X signals Y because [reason]."
 Common misreadings to avoid.]

## Key Requirements      ← regulation
[What exactly is required, expressed as clear rules.
 Who it is binding on. Phase-in schedule if applicable.
 Consequences of non-compliance if stated in source.]
```

### Shared closing sections (all types)

```markdown
## Evidence and Sources

[Cite specific passages. Format: [RAW-BOOK p.X] or [RAW-CLIP Title] or [WEB-YYYY-MM-DD].
 Distinguish primary from supporting: "The primary treatment is [RAW-...]. [RAW-...] provides
 additional context but treats X differently."]

## Contradictions and Debates

[Only if contradicts: field is populated. Explain the debate.
 Reference the contradiction node: see [[Contra_Topic_001]].]

## Related Concepts

[1-2 sentences per related node, written as prose, not bullet list. Explain HOW they relate:
 "[[QE]] produces the portfolio balance effect described in [[Portfolio_Balance_Effect]]
  — this node explains the mechanism; that node explains the magnitude and conditions."]
```

### Quality bar for body content

- **Minimum**: 3 substantive paragraphs in Overview + one type-specific section + Evidence
- **No stubs**: A body that says "Review and expand" or just echoes the thesis is not acceptable
- **Cite specifically**: "[RAW-BOOK Ch.4]" is weak; "[RAW-BOOK p.112, Table 4.3]" is correct
- **[LLM] scope**: Mark the entire sentence, not just a phrase — if you synthesised it, mark it
- **Causal conditions**: Never write "A causes B" — write "A causes B when [condition]"

---

## Source Label Format (used in body text)

| Label | Meaning | Example |
|-------|---------|---------|
| `[RAW-BOOK p.X]` | Direct page reference in raw source | `[RAW-Bindseil p.112]` |
| `[RAW-CLIP]` | From a Clipping in 02_sources/ | `[RAW-CLIP What about Japan Part I]` |
| `[WEB-YYYY-MM-DD]` | Web-fetched data with date | `[WEB-2026-05-20]` |
| `[LLM-E]` | LLM-estimated range, not verified | `[LLM-E ~50-70bps]` |
| `[LLM]` | LLM-synthesized sentence | marks entire sentence as unverified |

Use `[citation needed]` as a placeholder when a claim needs sourcing but source is not yet found.
