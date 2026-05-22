---
node_id: basel_output_floor_specialized_lending_001
type: mechanism
title: Basel Output Floor Specialized Lending Impact
aliases:
  - output floor
  - sàn đầu ra Basel
  - 72.5% floor
  - IRB optimization constraint
  - output floor 72.5%
domain:
  primary: basel_risk
  secondary:
    - financial_markets
tags:
  - basel-iii
  - output-floor
  - RWA
  - IRB
  - specialized-lending
  - capital-charge
  - private-credit-driver
confidence: 1
stability: evolving
thesis: >
  The Output Floor (72.5% of SA-RWA, fully phased-in Jan 2027) prevents banks from using
  internal IRB models to reduce RWA below 72.5% of the Standardised Approach calculation,
  eliminating the capital optimization advantage that made specialized lending (project
  finance, CRE, unrated mid-market loans) viable on bank balance sheets — regardless of
  actual historical default rates. [LLM] This is the single largest driver of bank retreat
  from specialized corporate credit, creating the structural gap that private credit fills.
steps:
  - "Step 1: Bank calculates RWA using internal IRB model (historically 30-50% lower than SA for specialized assets)"
  - "Step 2: Output Floor applies: RWA_used = max(IRB_RWA, 72.5% × SA_RWA)"
  - "Step 3: Specialized lending assets — unrated, no external rating — default to high SA risk weights (100-150%)"
  - "Step 4: Capital charge spikes: holding specialized loan requires CET1 × 12.5 × high SA_RWA"
  - "Step 5: ROE of specialized lending collapses below hurdle rate → bank refuses to originate or hold"
  - "Step 6: Credit gap opens → private credit funds (not Basel-regulated) fill at higher spread"
transmission_lags: medium
empirical_evidence: strong
source_refs:
  - path: 02_sources/deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
    pages: "Section II.2 — Sàn Đầu Ra"
    weight: primary
  - path: 02_sources/deep-research/Private Credit, Basel, and Regional Dynamics.md
    pages: "Section 4 — Key Metrics"
    weight: supporting
related:
  - node: "[[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]]"
    relation: component_mechanism_of
  - node: "[[Private_Credit_SRT_NAV_Loans_Bank_Partnerships]]"
    relation: structural_driver_of
  - node: "[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
    relation: interacts_with
date_created: "2026-05-21"
date_updated: "2026-05-21"
---

## Overview

The Output Floor is the most structurally disruptive element of Basel III Endgame for specialized lenders. Prior to its introduction, large banks using advanced IRB models could produce RWA calculations 30–50% below the Standardised Approach for specialized, relationship-based loans. The Floor eliminates this advantage by enforcing a hard minimum: no matter what the internal model says, RWA cannot fall below 72.5% of what the SA would calculate. [LLM]

Phase-in schedule (per BIS d424):
| Date | Floor Level |
|------|-------------|
| Jan 2022 | 50% |
| Jan 2023 | 55% |
| Jan 2024 | 60% |
| Jan 2025 | 65% |
| Jan 2026 | 70% |
| Jan 2027 | 72.5% (final) |

## Mechanism / How It Works

A → B because [reason]:

- **Unrated specialized loans → high SA risk weights** because SA has no category for unrated middle-market borrowers with good track records; they default to 100–150% risk weight.
- **High SA RWA × 72.5% floor → large capital charge** because the floor prevents IRB from recognizing the bank's superior credit assessment of its relationship borrowers.
- **Large capital charge → ROE below hurdle** because the cost of regulatory capital (~10–13% CET1 × risk weight) exceeds the spread earned on the loan.
- **ROE below hurdle → bank exits segment** when condition: the bank can redeploy capital into fee income or lower-RWA assets at comparable or better returns.

EU banks face the largest impact: near 80% of Group 1 banks will be constrained by Output Floor, with total MRC rising ~21.3%, of which Output Floor accounts for 41.4% of total Basel III impact on Group 1 banks (ECB/EBA data). [LLM]

## Evidence and Sources

[RAW-Gemini Deep Research, Basel, Ngân hàng, Tín dụng Tư nhân — Section II.2]
[RAW-Private Credit Basel Regional Dynamics — Section 4]

## Related Concepts

The Output Floor works in combination with the [[LCR_NSFR_Long_Term_Lending_Penalty]] to make long-duration, specialized corporate lending structurally uneconomical. Together these two mechanisms are the primary structural drivers behind the shift from originate-to-hold to originate-to-distribute, and behind the rise of the [[Private_Credit_SRT_NAV_Loans_Bank_Partnerships]] model. See also [[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]] for the complete framework.
