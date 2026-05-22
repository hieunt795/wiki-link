# Wiki-Agentic  -  Gemini Agent Instructions
# Read this file completely before any operation.

---

## System Architecture  -  What Runs Where

This system has two separate compute layers. You must understand the split before doing anything.

```
YOUR JOB (Gemini  -  cloud LLM):
  - Read source files, extract knowledge, write wiki nodes        [INGEST]
  - Run coverage probes, read search results, write findings      [RESEARCH]
  - Synthesize drafts, run audit checklist, present to user       [ANALYSIS]
  - Write final report after user approval                        [REPORT]

OPERATOR'S JOB (runs locally, NOT you):
  - py -3.12 librarian.py sync       <- encodes docs into FAISS index (BGE-M3, 4GB model)
  - py -3.12 librarian.py daemon     <- starts/stops the embedding server
  - py -3.12 librarian.py sweep      <- batch ingest from Inbox
```

**BGE-M3** is an embedding model only (text -> 1024-dim vector). It is NOT a language model.
It runs as a background daemon on port 7432. You call it indirectly via `librarian.py` bash commands.
If the daemon is not running, search commands return empty results  -  they do not crash.

---

## Directory Map

```
01_schema/        <- READ ONLY: schema definitions, confidence scale, VI/EN dictionary
02_sources/       <- IMMUTABLE: never modify source files. Only _source_registry.yaml is writable.
03_wiki/          <- YOUR WRITE ZONE: wiki nodes you create and maintain
04_research/      <- YOUR WORKSPACE: one folder per research topic
05_reports/       <- WRITE-ONCE: final reports after audit approval only
06_templates/     <- READ ONLY: analysis frameworks and style templates
07_scripts/       <- READ ONLY: do not modify scripts
.cache/           <- AUTO-GENERATED: indexes rebuilt by sync; never commit
```

---

## Trigger Formats  -  How to Start Each Stage

When called by the user or by GitHub Actions, you receive one of these triggers:

```
INGEST: 02_sources/{path/to/file.md}
  -> Stage 1: read source, extract nodes, write wiki

RESEARCH: {topic_slug} | {Primary research question}
  -> Stage 2: run full research session for this topic

DRAFT: {topic_slug}
  -> Stage 3: write draft from existing findings, run audit

REPORT: {topic_slug}
  -> Stage 4: write final report (only after user says "approve")

AUDIT: {topic_slug}
  -> Stage 3 audit only: check existing draft, report results

MAINTENANCE
  -> Run lint + link + thin-node audit, report issues
```

---

## Pre-Flight Check  -  Run Before Any Search Operation

Before running any `search`, `synth`, `agentic`, or `deep` command, verify the daemon:

```bash
py -3.12 07_scripts/librarian.py daemon status
```

**If output is `[daemon] Running (PID XXXX)`:** proceed normally.

**If output is `[daemon] Not running`:**
- You CANNOT start the daemon (requires BGE-M3 4GB model, local only)
- Inform the user: "BGE-M3 daemon is not running. Please start it with: `Start-Job { py -3.12 07_scripts/bge_m3_daemon.py start }`"
- You can still do INGEST (writing wiki nodes) without the daemon
- You CANNOT do RESEARCH, ANALYSIS search, or DEEP queries

---

## Stage 1  -  INGEST: Source -> Wiki

**Trigger:** `INGEST: 02_sources/{path}` or any file dropped in `02_sources/Inbox/`

### Step 1: Read the source

Read the full file at the given path. For files > 500 lines, read in sections until you can identify all key concepts. Focus on:
- Mechanisms: how financial systems, policy transmission, and markets operate
- Frameworks: multi-component models, regulatory structures, analytical models
- Concepts: theoretical constructs with durable explanatory value

**Do NOT extract:**
- Current interest rates, current CB decisions, current market prices
- Events tied to specific recent dates (< 2 years)
- Superficial mentions (< 1 paragraph of real content)
- Concepts already in `03_wiki/index.md` (check it first)

### Step 2: Plan your nodes (1-5 per source)

Before writing, decide for each node:
- `type`: concept | mechanism | framework | entity | policy | indicator | relationship | contradiction
- Core thesis (1-3 sentences: what does this node assert?)
- Confidence score (be honest  -  see scale below)

**Most common types:** `mechanism` and `framework`

### Step 3: Write each wiki node

**File path:** `03_wiki/{type}/{Title_CamelCase_All_Significant_Words}.md`

```yaml
---
node_id: {lowercase_underscore_slug}_{type_abbrev}_001
type: {type}
title: {Full Title With Capital Words}
aliases:
  - {abbreviation or common name}
  - {Vietnamese translation}              # required  -  at least one VI alias

domain:
  primary: {domain}
  secondary: [{domain}]
tags: [{tag1}, {tag2}, {tag3}]

confidence: {1|2|3|4|5}                  # see scale below  -  when in doubt, go lower
stability: {stable|evolving|contested|stale}

thesis: >
  {The core claim in 1-3 sentences. This is what appears in search results.
   Be precise and mechanistic, not vague.}

source_refs:
  - path: {02_sources/relative/path/to/file.md}
    pages: "{chapter, section, or page range  -  write 'full document' if unknown}"
    weight: {primary|supporting|contradicting}

related:
  - node: "[[{LinkedNode_CamelCase}]]"
    relation: {relation_label}

date_created: {YYYY-MM-DD}
date_updated: {YYYY-MM-DD}
---
```

**Body content rules:**
- Use `##` section headers
- Include formulas, tables, and A -> B -> C causal chains where useful
- Cite every specific number inline: `[RAW-BOOK SX]`, `[RAW-BOOK p.X]`, `[RAW-CLIP]`, or `[LLM-E]`
- Mark EVERY sentence you synthesize (not directly from source): add `[LLM]`
- Target length: 300-900 words

**Type abbreviations for node_id:**
```
concept -> con    mechanism -> mec    framework -> frm
entity  -> ent    policy    -> pol    indicator -> ind
```

### Step 4: Update `03_wiki/index.md`

- Increment `Total nodes: N` at the top
- Increment the section count (e.g., `## Mechanisms (15)` -> `(16)`)
- Add bullet entry in correct section:
  ```
  - **[[Node Title As Written]]**  [N stars matching confidence]
    Thesis compressed to <= 20 words.
  ```
  Stars: confidence 1 = one star shown as (*oooo), 3 = (***oo), etc.

### Step 5: Append to `03_wiki/log.md`

Find the last INGEST entry, add after it:
```
- **{YYYY-MM-DD}**: INGEST: Created {type} node `{Title}` from {source_filename_only}
```

### Step 6: Update `02_sources/_source_registry.yaml`

Find the entry for the ingested file, update:
```yaml
{source_path}:
  status: partial       # pending -> partial (or full if exhaustively extracted)
  ingest_date: '{YYYY-MM-DD}'
  wiki_nodes:
    - 03_wiki/{type}/{Filename.md}
```
Also increment `meta.total_ingested` and recalculate `coverage_pct`.

### Step 7: Confirm output

After completing ingest, print:
```
Created:
  - 03_wiki/{type}/{Node1.md}
  - 03_wiki/{type}/{Node2.md}
Updated: index.md, log.md, _source_registry.yaml
Sync required: YES  -  run locally: py -3.12 07_scripts/librarian.py sync
```

---

## Stage 2  -  RESEARCH: Topic Investigation

**Trigger:** `RESEARCH: {topic_slug} | {Primary research question}`

### Step 1: Pre-flight check

```bash
py -3.12 07_scripts/librarian.py daemon status
py -3.12 07_scripts/librarian.py status
```

If daemon not running -> inform user, stop here.

### Step 2: Create workspace

Copy the template scaffold and fill in RESEARCH.yaml:

```
04_research/{topic_slug}/
  RESEARCH.yaml        <- fill in all fields
  findings/            <- one .md file per finding
  data/                <- fresh web-fetched data
  drafts/              <- draft versions
  audit_log.json       <- created in Stage 3
```

Fill RESEARCH.yaml:
```yaml
topic_slug: {slug}
title: "{Full Topic Title}"
created: {YYYY-MM-DD}
status: active
domain_template: 06_templates/domains/{domain}/{template}.yaml
style_template: 06_templates/styles/{research_memo|policy_note|scenario_analysis|executive_brief}.yaml
analysis_mode: standard    # or T_MODE_DEEP  -  see mode selection rules below
primary_question: >
  {The central question this research answers}
sub_questions:
  - "{Sub-question 1}"
  - "{Sub-question 2}"
  - "{Sub-question 3}"
```

### Step 3: Coverage probe  -  classify each sub-question

For each sub-question, run:
```bash
py -3.12 07_scripts/librarian.py synth "{sub_question}"
```

Read the output. The first line shows the probe result:
```
[probe] state=INGESTED  wiki_sem=0.71  raw_sem=0.40  label_hits=2  (120ms)
```

**Three states and what to do:**

| State | Meaning | Action |
|-------|---------|--------|
| `INGESTED` | Wiki has relevant nodes | Run `search`, use wiki nodes as primary source |
| `PENDING` | Raw sources have it, wiki doesn't | Run `synth` to get raw chunks; ingest after research |
| `TRUE_GAP` | Not in corpus at all | STOP  -  log to gaps[], suggest sources, flag in limitations |

Record probe results in RESEARCH.yaml `coverage_probe` section.

### Step 4: Search and collect evidence

**For INGESTED sub-questions:**
```bash
py -3.12 07_scripts/librarian.py search "{sub_question}" --top 10
```
Read the returned wiki node files. They are in `03_wiki/{type}/{Node.md}`.

**For PENDING sub-questions:**
```bash
py -3.12 07_scripts/librarian.py synth "{sub_question}"
```
The results include raw source chunks. Note which source files they come from.

**For complex topics with >= 3 sub-questions involving mechanism/plumbing/market:**
```bash
py -3.12 07_scripts/librarian.py agentic "{primary_question}"
```
This runs 5 parallel lenses: policy / macro / plumbing / treasury / timing.
Merge the results  -  nodes appearing in multiple lenses are highest priority.

**For TRUE_GAP sub-questions  -  DO NOT search further:**
```yaml
# Add to RESEARCH.yaml gaps[]:
- query: "{the sub_question}"
  type: TRUE_GAP
  logged: {YYYY-MM-DD}
  source_candidates:
    - "{Suggested source 1}"
    - "{Suggested source 2}"
  status: open
```
Suggested sources by domain:
- Monetary policy: BIS Working Papers, Fed FEDS Notes, ECB Working Papers, NBER WP
- Basel/capital: BCBS consultative papers, BIS Quarterly Review, FSB reports
- Markets: ISDA reports, SIFMA data, NY Fed Staff Reports

### Step 5: Write findings

Write one `.md` file per distinct finding in `04_research/{topic_slug}/findings/{concept_slug}.md`.

```yaml
---
finding_id: {topic}_{concept}_001
topic: {topic_slug}
sub_question: "{which sub_question this answers}"
confidence: {1-5}
status: draft                        # draft | stable
promote_to_wiki: false               # true only if passes promotion gate
source_nodes:
  - "[[Wiki_Node_Name]]"
source_raw:
  - "02_sources/{path}"
date: {YYYY-MM-DD}
---

## Finding

{Claim stated precisely. What is true, under what conditions, with what magnitude.}

## Evidence Chain

{A -> B -> C. Explicit mechanism, not "generally..."}

## Source Labels

{[RAW-BOOK SX] or [RAW-CLIP] for every specific number or quote.
 [LLM] for any synthesis you add beyond the source.}

## Limitations / Caveats

{What this finding does NOT establish. What conditions would invalidate it.}
```

**Promotion gate  -  only promote to wiki if ALL 5 conditions met:**
1. `confidence >= 3`
2. `status: stable` (you have reviewed the source passage directly)
3. No open contradiction blocking this claim
4. Reusable across multiple topics (not single-topic)
5. Not time-sensitive (structural/mechanistic, not current rates or recent events)

### Step 6: Update RESEARCH.yaml state

After collecting all evidence:
```yaml
sources_used:
  wiki:
    - "[[Node_Name_1]]"
    - "[[Node_Name_2]]"
  raw:
    - "02_sources/{file}"
findings:
  - file: "findings/{concept}.md"
    status: stable
    confidence: 3
```

---

## Stage 3  -  ANALYSIS: Draft + Audit

**Trigger:** `DRAFT: {topic_slug}` or naturally after Stage 2 completion

### Step 1: Load context

Read in this order:
1. `04_research/{topic_slug}/RESEARCH.yaml`  -  topic state, all sub-questions, gaps, findings
2. All files in `04_research/{topic_slug}/findings/`
3. `06_templates/domains/{domain}/{template}.yaml`  -  domain-specific analysis framework
4. `06_templates/styles/{style}.yaml`  -  output structure and tone rules

### Step 2: Run comprehensive agentic search

```bash
py -3.12 07_scripts/librarian.py agentic "{primary_question}" --deep
```

Read the merged results. For each returned wiki node, read its full content from `03_wiki/`.
This is the final retrieval pass before writing.

### Step 3: Fetch fresh data (if topic is time-sensitive)

For topics requiring current data (rates, CB decisions, market levels):
- Use WebFetch or WebSearch to get current data
- Save to `04_research/{topic_slug}/data/{YYYY-MM-DD}_{source}.md`
- Label all fetched numbers as `[WEB-{YYYY-MM-DD}]` in the draft
- Record in RESEARCH.yaml `sources_used.fresh_data[]`

If you cannot fetch fresh data: flag as limitation, do not fabricate numbers.

### Step 4: Select analysis mode

```
Standard (research_memo, policy_note, executive_brief):
  Use when: overview, policy assessment, literature synthesis
  Template: 06_templates/styles/{style}.yaml

T_MODE_DEEP:
  Use when:
    - User says "phan tich sau" / "deep analysis" / "co che" / "Treasury desk"
    - Topic involves T-account tracing across multiple entities
    - Topic involves repo mechanics, FX intervention, or CB operational plumbing
    - >= 3 sub-questions touch Plumbing or Treasury layer
  Template: 06_templates/domains/T_MODE_DEEP.md
  Rules: P1 temporal tags / P2 source labels on all numbers / P3 A->B->C chains / P4 one diagram only
```

### Step 5: Write draft

**File path:** `04_research/{topic_slug}/drafts/{YYYY-MM-DD}_draft_v{N}.md`

Draft frontmatter:
```yaml
---
draft_version: {N}
topic: {topic_slug}
date: {YYYY-MM-DD}
style: {style_template_id}
analysis_mode: {standard|T_MODE_DEEP}
audit_status: pending
---
```

Required sections (research_memo style):
```
TO / FROM / DATE / RE header
## Executive Summary      (max 200 words, lead with the conclusion)
## 1. {First finding section}
## 2. {Second finding section}
...
## Conclusions
## Limitations             (ALL TRUE_GAPs must appear here)
## Sources                 (table: Node | Type | Confidence | Primary Source)
```

Source labeling in body  -  use these exactly:
```
[RAW-BOOK SX]    directly from a book, section X
[RAW-BOOK p.X]   directly from a book, page X
[RAW-CLIP]       from a clipping or article in 02_sources/
[WEB-YYYY-MM-DD] web-fetched data with date
[LLM]            you synthesized this  -  not directly from source
[LLM-E]          your estimate or approximate range
```

### Step 6: Self-audit (run before showing draft to user)

Check all 10 items. Mark each PASS / FAIL / PARTIAL / N/A.

**Category A  -  Source Integrity:**
- A1: Every factual claim has [RAW-*], [WEB-*], or [LLM] marker  -  no bare assertions
- A2: No claim contradicts a confidence >= 4 wiki node without explanation
- A3: All web-fetched data has visible timestamp

**Category B  -  Logic Integrity:**
- B1: Causal chains are directionally consistent  -  no circular reasoning
- B2: Conclusions follow from evidence  -  no unsupported leaps
- B3: Counter-arguments or alternative interpretations acknowledged (warning only)

**Category C  -  Coverage Integrity:**
- C1: All sub_questions addressed OR explicitly noted as out-of-scope
- C2: All TRUE_GAP items appear in the Limitations section

**Category D  -  Contradiction Integrity:**
- D1: Open contradictions in RESEARCH.yaml acknowledged in draft (warning only)
- D2: Contradiction nodes created in 03_wiki/contradictions/ for conflicts found (warning only)

**Category E  -  Style:**
- E1: Required sections present per style template (warning only)

**T_MODE_DEEP additional checks (when analysis_mode == T_MODE_DEEP):**
- T1: All specific numbers have [WEB-*], [RAW-*], or [LLM-E]  -  BLOCKING
- T2: No gaming/combat metaphors  -  describe mechanisms, not label them (warning)
- T3: All causal claims follow A->B->C with explicit conditions  -  BLOCKING

### Step 7: Write audit_log.json

```json
{
  "topic": "{topic_slug}",
  "draft_version": 1,
  "audit_date": "{YYYY-MM-DD}",
  "checks": {
    "A1": {"status": "PASS|FAIL|PARTIAL", "note": ""},
    "A2": {"status": "PASS|FAIL|PARTIAL", "note": ""},
    "A3": {"status": "N/A|PASS|FAIL",     "note": ""},
    "B1": {"status": "PASS|FAIL",         "note": ""},
    "B2": {"status": "PASS|FAIL",         "note": ""},
    "B3": {"status": "PASS|FAIL",         "note": ""},
    "C1": {"status": "PASS|PARTIAL",      "note": ""},
    "C2": {"status": "PASS|FAIL",         "note": ""},
    "D1": {"status": "PASS|FAIL",         "note": ""},
    "D2": {"status": "PASS|FAIL",         "note": ""},
    "E1": {"status": "PASS|FAIL",         "note": ""}
  },
  "checks_passed": 0,
  "checks_failed": 0,
  "checks_partial": 0,
  "reviewer": "agent_self_audit",
  "final_approved": false
}
```

### Step 8: Present to user

Show only FAIL and PARTIAL items. Do NOT enumerate all 10 checks.

Format:
```
Audit complete: {N}/10 PASS, {M} FAIL, {K} PARTIAL

FAIL items requiring your decision:
  [A1] {specific claim without source label  -  line X of draft}
  [C2] TRUE_GAP "{query}" not in Limitations section

Draft saved: 04_research/{topic_slug}/drafts/{date}_draft_v1.md

To approve: reply "approve"
To revise: reply with corrections
```

---

## Stage 4  -  REPORT: Publish After Approval

**Trigger:** User replies "approve" / "oke approve" / "duyet" / "confirmed"

Only execute Stage 4 if `audit_log.json` exists AND all BLOCKING checks passed.
If any blocking check is FAIL, do NOT write the report  -  ask user to resolve first.

### Step 1: Set audit approval

Update `audit_log.json`:
```json
"reviewer": "user_approved",
"final_approved": true
```

### Step 2: Write final report

Apply style template -> write to:
```
05_reports/{YYYY-MM}/{descriptive_slug}.md
```

Report frontmatter:
```yaml
---
report_id: rpt_{topic}_{counter}
topic_slug: {topic_slug}
title: "{Full Report Title}"
style: {style}
date: {YYYY-MM-DD}
audit_approved: true
audit_log: 04_research/{topic_slug}/audit_log.json
confidence_floor: {lowest confidence of any wiki node cited}
---
```

### Step 3: Update report registry

Append to `05_reports/_index.yaml`:
```yaml
- slug: {descriptive_slug}
  title: "{Full Report Title}"
  date: {YYYY-MM-DD}
  file: "05_reports/{YYYY-MM}/{slug}.md"
  topic_slug: {topic_slug}
  style: {style}
  domain: {domain}
  audit_approved: true
  confidence_floor: {N}
  wiki_nodes_used:
    - "[[Node_Name_1]]"
    - "[[Node_Name_2]]"
```
Increment `meta.total_reports`.

### Step 4: Update wiki log

Append to `03_wiki/log.md`:
```
- **{YYYY-MM-DD}**: REPORT: Published {style} `{slug}`  -  {short description} (audit approved, confidence floor {N}, {M} wiki nodes used)
```

### Step 5: Check promotion gate for all findings

For each finding in RESEARCH.yaml with `promote_to_wiki: true`:
- Verify all 5 promotion conditions are met (confidence >= 3, stable, no open contradictions, reusable, not time-sensitive)
- If yes: create or update the wiki node, update index.md and log.md
- If no: leave as finding, note the blocking issue

### Step 6: Confirm output

```
Report published: 05_reports/{YYYY-MM}/{slug}.md
Registry updated: 05_reports/_index.yaml
Log updated: 03_wiki/log.md

Promotions: {N nodes promoted | 0 nodes promoted  -  see RESEARCH.yaml promotion_candidates}

Sync required: YES  -  run locally: py -3.12 07_scripts/librarian.py sync
```

---

## Decision Logic

### Wiki node vs research finding?

```
Create a wiki node IF the claim is:
  - Structural / mechanistic (how a system works  -  true regardless of date)
  - Supported by confidence >= 3 source
  - Reusable across multiple research topics
  Example: "Repo market haircut mechanics" -> wiki node

Keep as research finding ONLY if:
  - Current events, specific dates/rates/prices
  - Confidence < 3
  - Only relevant to this one topic
  Example: "SOFR was 5.31% on 2026-05-15" -> finding only, never wiki
```

### How to set confidence?

```
5  Multiple authoritative textbooks explicitly agree  -  core established theory
4  Single primary textbook OR multiple IMF/BIS/Fed working papers
3  Credible secondary source (quality article + institutional citations)
2  LLM deep-research document citing institutional sources
1  Pure LLM synthesis, no source verification  -  mark EVERYTHING [LLM]

Default by source type:
  Academic textbook (Bindseil, Tuckman, Singh): start at 3-4
  BIS/Fed/IMF working paper: 3
  AI deep-research citing institutions: 2
  Blog with strong citations: 2-3
  Blog without citations: 1
```

### What to do with TRUE_GAP?

```
1. Add to RESEARCH.yaml gaps[] with type: TRUE_GAP
2. Add to draft Limitations section  -  never fabricate content for gaps
3. Suggest 2-3 sources the user can acquire:
   Monetary:  BIS WP, Fed FEDS Notes, ECB WP, NBER working papers
   Basel:     BCBS consultative papers, BIS Quarterly Review, FSB reports
   Markets:   ISDA, SIFMA, NY Fed Staff Reports
4. DO NOT continue searching  -  gap is logged, move on to next sub-question
```

### Contradiction handling?

```
When two sources make incompatible factual claims:
1. Do NOT silently pick one side
2. Create 03_wiki/contradictions/Contra_{Topic}_{Counter}.md
3. Add to RESEARCH.yaml contradictions[]
4. In draft: present both claims, explain the conflict, note resolution status

Contradiction node template:
  node_id: contra_{topic}_{counter}
  type: contradiction
  claim_a: {statement + source}
  claim_b: {statement + source}
  resolution_status: open | context_dependent | resolved
  resolution_note: ""
  affects_nodes: ["[[NodeA]]", "[[NodeB]]"]
```

---

## Hard Rules  -  Never Break

1. **NEVER modify any file in `02_sources/`**  -  they are immutable. Only `_source_registry.yaml` is writable.
2. **Every wiki node must have at least one `source_ref`** pointing to a real file in `02_sources/`. No source = no node.
3. **Set `confidence: 1` on any node created without reading the source.** Raise only after reading a specific passage.
4. **Mark every synthesized sentence with `[LLM]`**  -  do not hide synthetic content.
5. **Do not run `librarian.py sync`**  -  BGE-M3 requires the 4GB local model; sync is the operator's job.
6. **Do not run `librarian.py daemon start/stop`**  -  daemon management is local-only.
7. **Do not write a final report without `"final_approved": true` in audit_log.json.**
8. **Do not promote time-sensitive facts to wiki**  -  current rates, prices, recent decisions stay in findings only.
9. **When sources disagree, create a contradiction node**  -  never pick a side silently.
10. **Vietnamese queries work natively**  -  pass them to librarian.py as-is; no translation needed.

---

## Commands Reference (all require daemon running)

```bash
# Check system state
py -3.12 07_scripts/librarian.py daemon status
py -3.12 07_scripts/librarian.py status

# Coverage probe + search (Stage 2)
py -3.12 07_scripts/librarian.py synth "{query}"               # probe + route to right layer
py -3.12 07_scripts/librarian.py probe "{query}"               # probe only (no search)
py -3.12 07_scripts/librarian.py search "{query}" --top 10     # full 4-phase KG2RAG
py -3.12 07_scripts/librarian.py agentic "{query}"             # 5-lens parallel search
py -3.12 07_scripts/librarian.py agentic "{query}" --deep      # T_MODE_DEEP (2 variants/lens)

# Thin-node audit (no daemon needed)
py -3.12 07_scripts/librarian.py deep monetary_policy --audit  # list nodes needing expansion

# Wiki health
py -3.12 07_scripts/librarian.py lint                          # orphans, broken links, stubs
py -3.12 07_scripts/librarian.py link                          # cross-reference audit
py -3.12 07_scripts/librarian.py gaps list                     # show open TRUE_GAPs

# Session management
py -3.12 07_scripts/librarian.py session-close {topic_slug}
py -3.12 07_scripts/librarian.py template-show {insight_id}
py -3.12 07_scripts/librarian.py template-apply {insight_id}
py -3.12 07_scripts/librarian.py template-reject {insight_id} --reason "..."
```

**Commands you must NOT run:**
```bash
# These require BGE-M3 (4GB local model)  -  operator runs these, not you
py -3.12 07_scripts/librarian.py sync
py -3.12 07_scripts/librarian.py embed
py -3.12 07_scripts/librarian.py daemon start
py -3.12 07_scripts/librarian.py daemon stop
py -3.12 07_scripts/librarian.py ingest   # use manual node writing instead
py -3.12 07_scripts/librarian.py sweep
```

---

## Naming Conventions

```
Wiki nodes:
  03_wiki/{type}/{Title_CamelCase_All_Significant_Words}.md
  node_id: {lowercase_underscore}_{type_abbrev}_001

Research files:
  04_research/{topic_slug}/findings/{concept_slug}.md   <- lowercase, underscores
  04_research/{topic_slug}/data/{YYYY-MM-DD}_{source}.md
  04_research/{topic_slug}/drafts/{YYYY-MM-DD}_draft_v{N}.md

Reports:
  05_reports/{YYYY-MM}/{descriptive_slug}.md

Domain values:
  monetary_policy    financial_markets    fiscal_policy
  macro_outlook      basel_risk           shadow_banking
```

---

## Maintenance Mode

**Trigger:** `MAINTENANCE`

Run in order, report any issues found:
```bash
py -3.12 07_scripts/librarian.py lint
py -3.12 07_scripts/librarian.py link
py -3.12 07_scripts/librarian.py deep monetary_policy --audit
py -3.12 07_scripts/librarian.py deep financial_markets --audit
py -3.12 07_scripts/librarian.py gaps list
py -3.12 07_scripts/librarian.py status
```

Report format:
```
Maintenance Report  -  {YYYY-MM-DD}
Lint: {N} issues ({M} blocking, {K} warnings)
Link: {N} broken links, {M} orphan nodes
Thin nodes: {N} nodes below confidence 3 or marked [LLM]
Open gaps: {N} TRUE_GAP entries pending
System: Daemon {Running|Stopped} | Dense index {Built|Not built} | {N} wiki nodes
```
