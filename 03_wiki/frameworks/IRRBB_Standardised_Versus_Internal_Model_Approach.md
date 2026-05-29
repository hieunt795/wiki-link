---
node_id: irrbb_standardised_versus_internal_model_approach_001
type: framework
title: IRRBB Standardised vs Internal Model Approach — Practitioner Perspective
aliases:
- IRRBB SA vs IMA
- IRRBB Pillar 2 principles
- BCBS 12 principles IRRBB
- supervisory outlier test SOT
- tiêu chuẩn IRRBB Basel Pillar 2
- phương pháp nội bộ rủi ro lãi suất sổ ngân hàng
- kiểm tra ngoại lệ giám sát SOT
domain:
  primary: alm
  secondary: []
tags:
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[BCBS]]'
  relation: related_to
- node: '[[Pillar2]]'
  relation: related_to
- node: '[[EVE]]'
  relation: related_to
- node: '[[NII]]'
  relation: related_to
- node: '[[SOT]]'
  relation: related_to
- supervisory-outlier-test
- standardised-approach
- internal-model
- regulatory-shocks
confidence: 1
stability: stable
thesis: 'BCBS 2016 (d368) adopted a principles-based Pillar 2 framework rather than
  a mandatory Pillar 1 standardised capital charge for IRRBB, structuring 12 principles
  that require banks to measure both EVE and NII under six regulatory rate shocks
  and apply a supervisory outlier test (SOT) that triggers enhanced scrutiny when
  the worst-case ΔEVe exceeds 15% of Tier 1 capital. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 3: Interest Rate Risk Management — The Practitioner''s Perspective'
parent_node: null
related:
- node: '[[Bcbs_Irrbb_Standards_2016]]'
  relation: related_to
- node: '[[ALM_Enterprise_Risk_Management_Framework]]'
  relation: related_to
- node: '[[ILAAP_Supervisory_Liquidity_Framework]]'
  relation: related_to
- node: '[[Interest_Rate_Basis_Risk_Measurement_ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

BCBS 2016 (d368) adopted a principles-based Pillar 2 framework rather than a mandatory Pillar 1 standardised capital charge for IRRBB, structuring 12 principles that require banks to measure both EVE and NII under six regulatory rate shocks and apply a supervisory outlier test (SOT) that triggers enhanced scrutiny when the worst-case ΔEVe exceeds 15% of Tier 1 capital. [LLM]

## Why Pillar 2 Rather Than Pillar 1

The BCBS considered but rejected a mandatory standardised Pillar 1 capital charge for IRRBB for several reasons: [LLM]

- Banking book risk profiles are highly heterogeneous across jurisdictions and business models, making a single standardised formula prone to both over- and under-capitalization. [LLM]
- The dual nature of IRRBB (EVE = economic value impact; NII = short-run earnings impact) does not reduce to a single capital number without losing critical information. [LLM]
- Supervisors already had Pillar 2 tools to address residual risk; a new Pillar 1 charge would double-count risk already captured under credit RWA for some instruments. [LLM]

The chosen Pillar 2 principles-based approach preserves supervisory judgment while establishing minimum standards for internal measurement. [LLM]

## The 12 BCBS Principles — Structural Grouping

### Risk Identification (Principles 1–3)

- **P1** — Identify all material IRRBB sub-types: repricing/gap risk, yield curve risk, basis risk, option risk. [LLM]
- **P2** — Monitor CSRBB (credit spread risk in the banking book) separately; it must not be conflated with IRRBB in the measurement framework. [LLM]
- **P3** — Capture automatic and behavioural optionality (prepayment, NMD decay, rate floors). [LLM]

### Measurement (Principles 4–6)

- **P4** — Measure both EVE and NII; neither metric alone is sufficient. [LLM]
- **P5** — Apply all six regulatory shock scenarios: parallel up, parallel down, steepener, flattener, short-rate up, short-rate down. [LLM]
- **P6** — Use conservative behavioural assumptions for NMDs and options; document assumptions; validate regularly. [LLM]

### Reporting and Governance (Principles 7–8)

- **P7** — ALCO receives structural hedging reports; the board approves risk appetite for IRRBB. [LLM]
- **P8** — Pillar 3 public disclosures of EVE and NII sensitivities under the six shocks, enabling market discipline. [LLM]

### Capital (Principle 9)

- **P9** — EVE sensitivity feeds into ICAAP capital allocation; NII sensitivity feeds into earnings buffers and business planning stress tests. [LLM]

### Supervisory Review (Principles 10–12)

- **P10** — Supervisors assess IRRBB risk profile and management quality as part of SREP. [LLM]
- **P11** — Supervisors may apply additional Pillar 2 capital add-ons for residual IRRBB after internal hedging. [LLM]
- **P12** — SOT (Supervisory Outlier Test): if the worst-case ΔEVe across all six shocks exceeds 15% of Tier 1 capital, the bank is classified as an "outlier" and must engage with supervisors on remediation. [LLM]

## Supervisory Outlier Test (SOT) Mechanics

The SOT threshold is: [LLM]

> **ΔEVe_worst / Tier_1_capital > 15%** → triggers supervisory escalation [LLM]

Key points on SOT application: [LLM]

- "Worst case" is defined as the maximum EVE decline across all six prescribed shock scenarios, floored at zero (gains do not offset losses from other scenarios). [LLM]
- The SOT is a trigger for enhanced dialogue, not an automatic capital charge; supervisors may still impose add-ons under Pillar 2 after review. [LLM]
- Banks must disclose whether they pass or fail the SOT in Pillar 3 disclosures. [LLM]

## Structural vs Transferable Risk — Governance Split

From a practitioner perspective, the 12 principles operationally divide IRRBB risk management into two governance domains: [LLM]

| Domain | Owner | Instruments |
|--------|-------|-------------|
| **Structural risk** | ALCO | NMD modeling, fixed-rate asset hedging, basis risk management, capital allocation for residual EVE |
| **Transferable risk** | Treasury (via FTP) | Customer derivative execution, short-term rate hedging, interbank funding |

[LLM]

This split ensures that ALCO retains accountability for hard-to-model behavioral risks while treasury manages measurable market risks within approved limits. [LLM]

---
*Source: Chapter 3 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). Distinct from the existing regulation node on BCBS d368, which covers the document content; this node covers the practitioner governance framework. All body sentences tagged [LLM] are synthesized. Confidence: 1.*
