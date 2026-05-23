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
**Purpose:** A causal process, transmission channel, or operational procedure.
**Subdirectory:** `03_wiki/mechanisms/`
**Required fields:** all concept fields + `steps[]`
**Extra fields:**
```yaml
steps:
  - "Step 1: ..."
  - "Step 2: ..."
transmission_lags: immediate | short | medium | long
empirical_evidence: strong | mixed | weak | contested
```
**Example:** Interest Rate Transmission Channel, QE Portfolio Balance Effect, Repo Settlement Flow

### `entity`
**Purpose:** Institution, central bank, person, regulatory body, market instrument.
**Subdirectory:** `03_wiki/entities/`
**Required fields:** all concept fields + `entity_type`, `jurisdiction`
**Extra fields:**
```yaml
entity_type: institution | central_bank | person | instrument | market
jurisdiction: US | EU | JP | VN | global | ...
established: YYYY
mandate: "..."
```
**Example:** Federal Reserve, BOJ, BIS, JGB (instrument), SOFR (rate)

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
**Purpose:** A specific policy action, regime, or institutional decision with a defined period.
**Subdirectory:** `03_wiki/policies/`
**Required fields:** all concept fields + `jurisdiction`, `period`, `policy_type`
**Extra fields:**
```yaml
jurisdiction: US | EU | JP | VN | global
period: "2008-2014"
policy_type: conventional_monetary | unconventional_monetary | fiscal | regulatory | macroprudential
instruments: [list]
outcome: "..."
```
**Example:** Fed QE1-QE3, BOJ YCC Policy 2016-2024, Basel III Implementation

### `framework`
**Purpose:** Analytical framework, model, or conceptual structure used for analysis.
**Subdirectory:** `03_wiki/frameworks/`
**Required fields:** all concept fields + `components[]`, `application_domain`
**Extra fields:**
```yaml
components:
  - "Component 1"
  - "Component 2"
application_domain: monetary_policy | fiscal_policy | financial_stability | ...
key_equations: []        # Optional: LaTeX or plain text formulas
```
**Example:** IS-LM Model, Flow of Funds Framework, Basel Capital Framework, T-Account Analysis

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
