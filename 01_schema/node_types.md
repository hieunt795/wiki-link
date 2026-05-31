# Node Types — Wiki Taxonomy

Wiki nodes in `03_wiki/` are organized by type. Each type has a distinct purpose,
required fields, and promotion criteria. The type is declared in frontmatter: `type: concept`.

---

## Type Registry

### `concept`
**Purpose:** Atomic theoretical concept — the building block of the knowledge graph.
**Subdirectory:** `03_wiki/concepts/`
**Required fields:** `type`, `node_id`, `title`, `aliases`, `domain`, `tags`, `confidence`, `thesis`, `source_refs`
**Optional fields:** `related`, `contradicts`, `stability`
**Example:** Quantitative Easing, Yield Curve Control, Reserve Requirements

### `mechanism`
**Purpose:** A causal process, transmission channel, or operational procedure that unfolds in sequential steps.
**Subdirectory:** `03_wiki/mechanisms/`
**Required fields:** all concept fields + `steps[]`

`steps[]` is **mandatory** — it must list the causal chain. If you cannot write at least two concrete steps (A happens → B follows because of condition C), use `concept` instead.

**Extra fields:**
```yaml
steps:
  - "Step 1: [what happens and why]"
  - "Step 2: [what follows and under what condition]"
transmission_lags: immediate | short | medium | long
empirical_evidence: strong | mixed | weak | contested
```
**Example:** Interest Rate Transmission Channel, QE Portfolio Balance Effect, Repo Settlement Flow, Bank-NBFI Leverage Loop

**Anti-pattern:** Using "mechanism" for anything with "mechanics" or "transmission" in the title. The word is not a signal — the existence of a real causal chain is. A description of how repo works without a step-by-step operational chain → `concept`.

### `entity`
**Purpose:** Any named actor or thing: central bank, institution, regulatory body, committee, person, market, or financial instrument.
**Subdirectory:** `03_wiki/entities/`
**Required fields:** all concept fields + `entity_type`, `jurisdiction`
**Extra fields:**
```yaml
entity_type: institution | central_bank | regulatory_body | committee | person | instrument | market
jurisdiction: US | EU | JP | VN | SG | UK | global | ...
established: YYYY
mandate: "..."
```
**Example:** Federal Reserve, ECB, BOJ, SBV, PBoC, BIS, IMF, FSB, BCBS, MAS, BOE, ISDA, ALCO, JGB (instrument), SOFR (rate)

**Anti-pattern:** A named regulatory body (BCBS, FSB, IMF, SBV) described as a concept because it "sounds like a concept". Any named organisation → `entity`.

### `relationship`
**Purpose:** Named, directional relationship between two wiki nodes.
**Subdirectory:** `03_wiki/relationships/`
**Required fields:** all concept fields + `from_node`, `to_node`, `relation_type`
**Relation types:** `mechanism_of`, `produces`, `constrains`, `depends_on`, `interacts_with`,
`often_combined_with`, `substitutes_for`, `amplifies`, `attenuates`
**Example:** QE → produces → Portfolio Balance Effect

### `contradiction`
**Purpose:** Documents conflicting claims from different sources on the same topic.
**Subdirectory:** `03_wiki/contradictions/`
**Naming convention:** `Contra_{Topic}_{Counter}.md`
**Required fields:**
```yaml
claim_a:
  statement: "..."
  sources: [path]
  confidence: N
  stance: "..."
claim_b:
  statement: "..."
  sources: [path]
  confidence: N
  stance: "..."
resolution_status: open | resolved | context_dependent
resolution_note: "..."
affects_nodes: ["[[NodeA]]", "[[NodeB]]"]
```
**Lifecycle:** OPEN → CONTEXT_DEPENDENT → RESOLVED

### `synthesis`
**Purpose:** Cross-domain or cross-source integration that is more than the sum of its parts.
**Subdirectory:** `03_wiki/synthesis/`
**Required fields:** all concept fields + `synthesizes[]`, `synthesis_method`
**Extra fields:**
```yaml
synthesizes:
  - "[[NodeA]]"
  - "[[NodeB]]"
synthesis_method: comparative | integrative | reconciliation | extension
```
**Example:** Fiscal-Monetary Interaction under QE, Basel + Shadow Banking Interaction

### `policy`
**Purpose:** A specific dated policy action, regime, or institutional decision tied to a named authority and a defined period. Covers both CB operational frameworks anchored to a year and historical policy regime shifts.
**Subdirectory:** `03_wiki/policies/`
**Required fields:** all concept fields + `jurisdiction`, `period`, `policy_type`
**Extra fields:**
```yaml
jurisdiction: US | EU | JP | VN | global
period: "2008-2014"          # Required — even "2024-present" or "1970s" counts
policy_type: conventional_monetary | unconventional_monetary | fiscal | regulatory | macroprudential
instruments: [list]
outcome: "..."
```
**Example:** Fed QE1-QE3 (2008-2014), BOJ YCC 2016-2024, Volcker Shock 1979-1982, ECB New Operational Framework 2024, US 1970s Stagflation Policy Regime, ECB PEPP 2020-2022

**Signal:** If the node title contains a year, decade, or reform label tied to a named authority → use `policy` before considering `framework`.

**Anti-pattern:** Calling a dated CB operational framework a `framework` because it sounds structural. ECB's 2024 range-floor decision is a `policy` (it has a year, a named authority, and an effective date). A `framework` has no specific date — it's a timeless analytical tool.

### `framework`
**Purpose:** A reusable analytical model or tool with enumerable named components and a defined application domain. Timeless — not tied to a specific year or authority decision.
**Subdirectory:** `03_wiki/frameworks/`
**Required fields:** all concept fields + `components[]`, `application_domain`

`components[]` is **mandatory** — it must list the actual named parts of the framework. A node without enumerable components is a `concept`, not a framework.

**Extra fields:**
```yaml
components:
  - "Component name 1"     # Named sub-parts, dimensions, or metrics the framework uses
  - "Component name 2"
application_domain: monetary_policy | fiscal_policy | alm | financial_stability | ...
key_equations: []        # Optional: LaTeX or plain text formulas
```
**Example:** IS-LM Model (components: IS curve, LM curve), IRRBB EVE/NII Dual-Metric (components: EVE metric, NII metric, shock scenarios), IMF Flow of Funds 4-Sector (components: households, firms, government, rest-of-world), Basel Capital Stack (components: CET1, Tier 1, Total Capital, buffers)

**Anti-patterns — these are NOT frameworks:**
- A description of how something works without enumerable components → `concept` or `mechanism`
- A dated CB operational decision with a year (ECB 2024 framework, Volcker 1979) → `policy`
- A taxonomy or classification scheme without analytical application → `concept`
- A historical regime or event tied to a decade → `policy`

### `indicator`
**Purpose:** Economic or financial indicator used in analysis and monitoring.
**Subdirectory:** `03_wiki/indicators/`
**Required fields:** all concept fields + `indicator_type`, `frequency`, `data_source`
**Extra fields:**
```yaml
indicator_type: monetary | fiscal | market | survey | real | financial_stability
frequency: daily | weekly | monthly | quarterly | annual
data_source: "Fed H.4.1"
interpretation: "..."
data_range: "YYYY-present"
```
**Example:** SOFR, CPI, Reserve Bank Credit, JGB 10Y Yield, LCR Ratio

### `regulation`
**Purpose:** A binding regulatory requirement, standard, or rule issued by an official regulatory or supervisory body. Distinct from `policy` (which covers CB decisions and regimes) and `framework` (analytical models) — regulations are legally or institutionally binding on specific entities.
**Subdirectory:** `03_wiki/regulations/`
**Source directory:** `02_sources/regulator/{issuing_body}/`
**Required fields:** all concept fields + `issuing_body`, `jurisdiction`, `regulation_type`, `current_status`
**Extra fields:**
```yaml
issuing_body: BCBS | SBV | Fed | ECB | FSB | IOSCO | MAS | BOJ | BIS | other
jurisdiction: global | US | EU | VN | JP | SG | UK | ...
regulation_type: capital | liquidity | leverage | conduct | reporting | macroprudential | fx_policy | payment_system | resolution | other
document_id: "Official document name or number (e.g. BCBS d424, Circular 22/2023/TT-NHNN)"
effective_date: YYYY-MM-DD        # Date rule takes effect (or first phase)
current_status: proposed | consultative | final | phased_in | superseded
binding_on: banks | g-sibs | broker_dealers | all_financial_entities | central_banks | ...
key_requirements:
  - "Requirement 1: ..."
  - "Requirement 2: ..."
phase_in_schedule: "Optional: describe phase-in timeline if applicable"
```
**Example:** Basel III Capital Requirements, SBV Circular 22 on Credit Limits, Fed Regulation W (affiliate transactions), BCBS IRRBB Standards, Basel IV Output Floor

---

## Decision Tree — Borderline Cases

```
Is it a NAMED actor / organisation / instrument?
  YES → entity  (Fed, ECB, BCBS, SBV, ALCO, JGB, SOFR, IMF, FSB, MAS, ISDA...)
  NO  ↓

Does it have a MEASUREMENT UNIT + FREQUENCY + DATA SOURCE?
  YES → indicator  (NII in $, LCR in %, EVE in $, SOFR in bps/daily)
  NO  ↓

Is it a BINDING RULE from an official regulatory body with a document ID?
  YES → regulation  (BCBS d424, SBV Circular 22, ECB SREP P2R...)
  NO  ↓

Is it tied to a NAMED AUTHORITY + SPECIFIC YEAR/PERIOD (even "2024-present")?
  YES → policy  (Fed QE1-3, BOJ YCC 2016-2024, ECB New Framework 2024,
                 Volcker Shock 1979-1982, US 1970s Stagflation Regime...)
  NO  ↓

Can you LIST NAMED COMPONENTS in a YAML array AND name an application domain?
  YES → framework  (IS-LM: [IS curve, LM curve], IRRBB: [EVE, NII, scenarios]...)
  NO  ↓

Can you write STEP 1 / STEP 2 / STEP 3 as a real causal chain?
  YES → mechanism  (rate cut → bank cost down → loan spread down → credit up...)
  NO  ↓

→ concept  (default for everything else)
```

**Common misclassifications to avoid:**

| What you see | Wrong type | Correct type |
|---|---|---|
| "ECB New Operational Framework 2024" | framework | policy — has year + named CB |
| "Volcker Fed Reaction Function Break" | framework | policy — 1979 regime shift |
| "US 1970s Stagflation Policy Regime" | framework | policy — decade + regime |
| "BCBS, FSB, IMF" described as concept | concept | entity — named regulatory body |
| "NII sensitivity" with no unit/frequency | concept | indicator — if units given |
| "LCR cashflow mechanics" | mechanism | concept — no step-chain, just description |
| "CB reserve taxonomy" | framework | concept — taxonomy ≠ analytical framework |

---

## Promotion Rules

A finding in `04_research/` becomes a stable wiki node when ALL are true:

1. `confidence >= 3` — at least one reliable secondary source
2. `status: stable` — agent has reviewed, not just auto-generated draft
3. No open contradictions blocking the claim
4. Reusable beyond the current research topic
5. Not time-sensitive (structural/mechanistic knowledge, not current data)

**What stays in `04_research/` and NEVER gets promoted:**
- Current policy rates and market levels (stale within weeks)
- Event-specific findings ("BOJ held rates at 0.5% on May 20, 2026")
- Unverified synthesis with confidence < 3
- Findings relevant only to one specific research question

---

## File Naming Conventions

```
03_wiki/{type}/{Title_In_CamelCase}.md

Examples:
  03_wiki/concepts/Quantitative_Easing.md
  03_wiki/mechanisms/Interest_Rate_Transmission_Channel.md
  03_wiki/entities/Federal_Reserve.md
  03_wiki/contradictions/Contra_QE_Money_Multiplier_001.md
  03_wiki/policies/Fed_QE_Programs_2008_2014.md
  03_wiki/frameworks/Flow_Of_Funds_Framework.md
  03_wiki/indicators/SOFR_Rate.md
  03_wiki/synthesis/Fiscal_Monetary_Interaction_QE.md
  03_wiki/regulations/Basel_III_Capital_Requirements.md
  03_wiki/regulations/SBV_Circular_22_Credit_Limits.md
```

Node IDs (the `node_id` field) use lowercase with underscores:
```
node_id: quantitative_easing_001
node_id: interest_rate_transmission_channel_001
node_id: contra_qe_money_multiplier_001
node_id: basel_iii_capital_requirements_001
node_id: sbv_circular_22_credit_limits_001
```
