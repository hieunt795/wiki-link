---
node_id: svb_2023_failure_alm_lessons_001
type: concept
title: SVB 2023 Failure — ALM Lessons
aliases:
  - SVB failure
  - Silicon Valley Bank 2023
  - SVB duration mismatch
  - SVB HTM portfolio failure
  - sự sụp đổ SVB 2023
  - bài học quản lý ALM từ SVB
  - rủi ro thời hạn danh mục HTM
domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - SVB
  - duration-mismatch
  - HTM-portfolio
  - concentration-risk
  - governance-failure
  - node: "[[IRRBB]]"
    relation: related_to
  - node: "[[ALM]]"
    relation: related_to
  - node: "[[NMD]]"
    relation: related_to
confidence: 1
stability: stable
thesis: >
  The SVB failure in March 2023 exemplifies how unhedged duration mismatch in a
  held-to-maturity bond portfolio, combined with a concentrated correlated depositor
  base and governance failures (vacant CRO, model manipulation), can convert a
  mark-to-model paper loss into a catastrophic liquidity run: a $15.2bn realized
  loss triggered a 60% deposit outflow in 48 hours, rendering the bank insolvent. [LLM]
source_refs:
  - path: "02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md"
    pages: "Ch4, SVB Case Study (lines 2557–2675)"
related:
  - node: "[[Eve_Calculation_Mechanics_Discount_And_Shock]]"
    relation: related_to
  - node: "[[NMD_Stochastic_Three_Factor_Model]]"
    relation: related_to
  - node: "[[Integrated_Stress_Testing_Capital_Liquidity_Link]]"
    relation: related_to
  - node: "[[ALM_Enterprise_Risk_Management_Framework]]"
    relation: related_to
date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Thesis

The SVB failure in March 2023 exemplifies how unhedged duration mismatch in a held-to-maturity bond portfolio, combined with a concentrated correlated depositor base and governance failures, can convert a mark-to-model paper loss into a catastrophic liquidity run. [LLM]

## Portfolio Composition and Duration Mismatch

By end-2022, SVB held a $95 billion bond portfolio in its AFS and HTM books with an average duration of approximately 6.25 years. [LLM] Key structural features: [LLM]

- **HTM classification**: Most bonds were reclassified to HTM to avoid marking unrealized losses through OCI, hiding the economic deterioration from regulatory capital ratios. [LLM]
- **Unrealized loss**: The hidden mark-to-market loss on the HTM portfolio reached $15.2 billion by end-2022 — larger than SVB's entire equity base. [LLM]
- **Duration gap**: With a 6.25-year asset duration against much shorter liability duration (NMDs with behavioral maturity < 1 year for concentrated tech deposits), the duration gap was approximately 3 years. [LLM]
- **Rate sensitivity**: A 200bp rate shock implied roughly a $12.5 billion EVE loss — consistent with the realized loss when bonds were sold to fund outflows. [LLM]

## Hedging Failure

SVB's hedging program was systematically dismantled: [LLM]

- By end-2022, only approximately **0.4% of the bond portfolio was hedged** with interest rate swaps. [LLM]
- During 2022, SVB unwound approximately **$11 billion in interest rate swaps** — a decision motivated by the desire to "juice P&L" by avoiding the negative carry of the hedge at prevailing rate levels. [LLM]
- The unwinding was approved despite the rising-rate environment and the growing duration mismatch. [LLM]

This represents a textbook violation of the principle that hedging programs should be maintained through rate cycles, not dismantled when hedges become costly. [LLM]

## Depositor Base — Concentrated and Correlated

SVB's liability structure was uniquely fragile: [LLM]

- **>88% of deposits were uninsured** (above FDIC $250k limit), primarily from venture capital firms and technology startups. [LLM]
- **Depositor correlation**: The VC/tech sector is informationally dense and interconnected; news of stress propagated instantly via Twitter and group chats, enabling a simultaneous coordinated run. [LLM]
- **Standard NMD modeling failure**: Conventional NMD behavioral models assume depositor behavior is driven by rate differentials and individual economics. SVB's depositor base violated this: outflows were driven by institutional fear and herding, not rate sensitivity. [LLM]
- The bank modeled deposits as having a longer behavioral maturity than was warranted for a concentrated, informationally connected institutional depositor base. [LLM]

## Governance Failures

Three compounding governance failures enabled the crisis: [LLM]

1. **Vacant CRO**: The Chief Risk Officer position was vacant for approximately 8 months during the critical 2022 period when the rate shock was materializing and hedges were being unwound. [LLM]
2. **Model manipulation**: SVB extended the modeled duration of its deposit base without adequate empirical support, reducing the apparent interest rate risk in internal models and EVE reporting. [LLM]
3. **Lack of board challenge**: The risk committee failed to escalate the growing duration mismatch or question the hedge unwind decisions. [LLM]

## ALM Lessons

Five structural lessons for bank ALM practice: [LLM]

| Lesson | Implication |
|--------|-------------|
| **HTM does not eliminate risk** | Reclassification to HTM hides OCI losses but cannot prevent cash losses when bonds must be sold to fund outflows |
| **Hedging must be maintained through rate cycles** | Unwinding hedges to improve short-term P&L transfers risk to future periods |
| **NMD modeling must reflect depositor composition** | Concentrated institutional depositors require shorter behavioral maturity assumptions than retail base |
| **Depositor correlation is catastrophic** | An informationally connected depositor base can organize a run in hours — standard LCR models assume uncorrelated outflows |
| **Governance failures amplify technical failures** | Vacant CRO and model manipulation removed the final defense layers that might have caught the duration mismatch |

[LLM]

## Regulatory Response

The SVB failure prompted supervisory attention to: [LLM]
- Mandatory EVE SOT reporting for mid-sized banks (previously exempt in the US). [LLM]
- Scrutiny of HTM portfolio size relative to capital. [LLM]
- Enhanced NMD behavioral modeling requirements for concentrated depositor bases. [LLM]

---
*Source: Chapter 4, SVB Case Study, Tata (ed.), "Bank ALM" (2025). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
