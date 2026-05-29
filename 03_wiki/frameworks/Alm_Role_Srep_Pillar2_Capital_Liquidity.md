---
node_id: alm_role_srep_pillar2_capital_liquidity_001
type: framework
title: ALM Role in SREP and Pillar 2 Capital/Liquidity Requirements
aliases:
- ALM in SREP
- SREP Pillar 2 ALM
- P2R P2G determination
- TSCR total SREP capital requirement
- vai trò ALM trong SREP
- yêu cầu Trụ cột 2 vốn và thanh khoản
- P2R P2G xác định vốn SREP
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- SREP
- Pillar2
- P2R
- P2G
- TSCR
- ICAAP
- ILAAP
confidence: 1
stability: stable
thesis: 'The Supervisory Review and Evaluation Process (SREP) evaluates banks across
  four areas (business model, governance, capital risks, liquidity risks) and imposes
  a Pillar 2 Requirement (P2R) as an individual add-on above Pillar 1; together they
  form the TSCR = P1 + P2R, which must be met at all times including stress; Pillar
  2 Guidance (P2G) is then added based on stress test results as a soft buffer above
  OCR; ALM''s primary SREP exposure is IRRBB (capital), ILAAP (liquidity), and funding
  plan credibility. [LLM]

  '
source_refs:
- path: 02_sources/books/alm/A - Bank Asset Liability Management Best Practice_ Yesterday,
    Today and Tomorrow-De Gruyter (2021).md
  pages: 'Chapter 13: ALM Role in SREP; Box 12.1; Box 13.2'
parent_node: null
related:
- node: '[[ALM_Enterprise_Risk_Management_Framework]]'
  relation: related_to
- node: '[[Integrated_Stress_Testing_Capital_Liquidity_Link]]'
  relation: related_to
- node: '[[ILAAP_Supervisory_Liquidity_Framework]]'
  relation: related_to
- node: '[[Bcbs_Irrbb_Standards_2016]]'
  relation: related_to
- node: '[[Alm_Operating_Model_Front_Middle_Office]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[Basel_III]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

The Supervisory Review and Evaluation Process (SREP) evaluates banks across four areas — business model, governance, risks to capital, and risks to liquidity — and imposes a Pillar 2 Requirement (P2R) as an individual add-on above Pillar 1. [LLM] Together they form the **Total SREP Capital Requirement** (TSCR = Pillar 1 + P2R), which must be met at all times including stress. [LLM] Pillar 2 Guidance (P2G) is then added based on stress test results as a soft buffer above the Overall Capital Requirement (OCR); ALM's primary SREP exposure is IRRBB (capital), ILAAP (liquidity), and funding plan credibility. [LLM]

## Capital Requirements Stack

```
OCR = TSCR + Combined Buffer Requirements (CCB 2.5% + CCyB + SyRB/G-SII/O-SII)
TSCR = Pillar 1 (CET1 4.5%, T1 6%, Total Capital 8%) + P2R (individual add-on)
P2G = soft buffer above OCR, set from stress test results
```

[LLM]

- **P2R**: Individual quantitative requirement; must be held at all times. [LLM] Per CRD V, P2R must be covered at minimum 56.25% by CET1 and at minimum 75% by T1. [LLM]
- **P2G**: Not a hard requirement; breach triggers notification to regulator and submission of capital recovery plan, but does not trigger immediate resolution. [LLM]
- **OCR**: Minimum requirement under going-concern conditions; combined buffers (CCB, CCyB, SyRB) can be temporarily drawn upon in stress per supervisory relief. [LLM]

## Four SREP Assessment Areas and ALM's Role

### A. Business Model Analysis

ALM contributes to: [LLM]
- Capital and funding planning (defining amounts, tenors, and rates of raised funds). [LLM]
- Maturity transformation steering (hedging IRR or changing balance sheet structure). [LLM]
- Pricing models and CoC calculations (input to strategic RoE). [LLM]
- Recovery and resolution plan inputs (a prerequisite for credible forward-looking strategy). [LLM]

### B. Internal Governance and Controls

ALM contributes to: [LLM]
- Organizational independence from conflict of interest (see operating model framework). [LLM]
- Implementing regulatory requirements into the ICAAP/ILAAP/RAS framework through subsequent policies. [LLM]
- Management board awareness of liquidity, capital, and regulatory development. [LLM]

The SREP governance score is typically the weakest area for all banks — no bank achieves the top score of "1" in this category. [LLM]

### C. Risks to Capital

ALM's direct mandate: [LLM]
- **IRRBB** is exclusively in ALM responsibility — proper policies and models must prove sustainability. [LLM]
- Credit, market, and operational risks are outside ALM scope (dependent on overall strategy and risk model). [LLM]
- ICAAP calculations for IRRBB feed into the P2R determination process. [LLM]

### D. Risks to Liquidity and Funding

ALM's direct mandate: [LLM]
- Liquidity buffer management and counterbalancing capacity. [LLM]
- Structural maturity mismatch and funding plan stability. [LLM]
- Liquidity contingency plans and stress testing. [LLM]
- ILAAP documentation provided by Risk controlling function (ALM provides inputs). [LLM]

## P2R Determination Process (Box 13.2)

Three steps under the ECB Single Supervisory Mechanism (SSM): [LLM]

1. **Risk-by-risk quantification**: Start from bank's ICAAP calculations. For most banks, supervisors substitute their own benchmarks because ICAAP calculations are not found sufficiently reliable on criteria of granularity, credibility, understandability, and comparability. [LLM]

2. **Reconciliation with CRD buffers**: Ensure the same risk is not double-counted in P2R and in macro-prudential buffers. [LLM]

3. **TSCR ratio calculation**: [LLM]
   > TSCR ratio = 8% × (total SREP capital requirement × 12.5) / total risk exposure amount

## SREP Proportionality Categories

Institutions are categorized by systemic importance (size, structure, scope, complexity, systemic risk): [LLM]

| Category | Description | Supervisory intensity |
|----------|-------------|----------------------|
| 1 | G-SIIs and O-SIIs + other systemically important | Full SREP, high frequency |
| 2 | Non-systemically important specialized with significant market shares | Moderate-high |
| 3 | Specialized with less significant market shares | Moderate |
| 4 | Small non-complex domestic institutions | Standard; only Pillar 1 in practice |

[LLM]

## Implications for ALM Practice

- SREP results cannot be predicted in advance (benchmarks are not disclosed), so budget/forecast should include **conservative P2R assumptions**. [LLM]
- IRRBB models must be documented, auditable, and defensible to regulators — SREP inspectors will challenge both the methodology and the inputs. [LLM]
- ILAAP stress testing must demonstrate stable and sustainable funding sources over the planning horizon. [LLM]
- ALM must maintain management awareness: the board must demonstrate understanding of IRRBB and ILAAP topics to receive favorable governance scores. [LLM]

---
*Source: Chapter 13 of Bardaeva (ed.), "Bank Asset Liability Management Best Practice" (De Gruyter, 2021). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
