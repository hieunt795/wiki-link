---
node_id: lcr_nsfr_long_term_lending_penalty_001
type: mechanism
title: LCR NSFR Long-Term Lending Penalty
aliases:
- LCR penalty
- NSFR structural cost
- liquidity rules long-term lending
- chi phí thanh khoản cho vay dài hạn
- Basel liquidity squeeze
domain:
  primary: basel_risk
  secondary:
  - monetary_policy
tags:
- LCR
- NSFR
- liquidity-regulation
- basel-iii
- long-term-lending
- HQLA
- funding-cost
- private-credit-driver
confidence: 3
stability: stable
thesis: 'LCR forces banks to hold HQLA ≥ 30-day stressed net cash outflows (including
  assumed draw-down of 10% on committed credit lines to non-financial corporates and
  30-40% on committed liquidity/credit lines to financial entities per LCR40), while
  NSFR requires stable funding covering 85% of notional for unrated performing loans
  ≥1yr (NSF30.31); together these rules create a structural funding cost penalty —
  HQLA opportunity cost on the LCR side, expensive long-term stable funding premium
  on the NSFR side — that makes long-duration corporate and specialized lending uneconomical
  relative to short-term or HQLA assets.

  '
steps:
- 'Step 1 (LCR): Bank extends €100M committed credit line to PE/corporate borrower'
- 'Step 2 (LCR): LCR40 applies 10% drawdown rate for committed credit lines to non-financial
  corporates → bank must hold €10M HQLA (govts, CB reserves) against contingent outflow'
- 'Step 3 (LCR): HQLA earns near-zero yield → opportunity cost = (lending spread −
  HQLA yield) × €10M for the undrawn portion'
- 'Step 4 (NSFR): Bank makes €100M unrated corporate loan, residual maturity >1yr
  → RSF factor = 85% per NSF30.31(2)'
- 'Step 5 (NSFR): Must fund €85M with ASF sources: stable retail deposits (95% ASF)
  or long-term wholesale bonds (100% ASF) — both carry tenor premium over short-term
  wholesale (0% ASF)'
- 'Step 6: Combined LCR opportunity cost + NSFR stable-funding premium eliminates
  spread advantage → bank exits long-term corporate lending'
transmission_lags: medium
empirical_evidence: strong
source_refs:
- path: 02_sources/regulator/bcbs/BaselFramework.md
  pages: LCR20 (30-day stress scenario), LCR30 (HQLA definition), LCR40.40-42 (wholesale
    run-off rates), NSF30.31 (85% RSF for unrated performing loans ≥1yr), NSF99 (ASF/RSF
    summary tables)
  weight: primary
- path: 02_sources/deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
  pages: Section II.4 — Quy Tắc Thanh Khoản
  weight: supporting
parent_node: null
related:
- node: '[[Basel_Output_Floor_Specialized_Lending_Impact]]'
  relation: works_in_conjunction_with
- node: '[[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]]'
  relation: component_mechanism_of
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: related_constraint
- node: '[[Private_Credit_SRT_NAV_Loans_Bank_Partnerships]]'
  relation: structural_driver_of
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:LCR
- node: '[[Basel III Endgame — Capital, Liquidity, and Credit Migration]]'
  relation: shared_tag:LCR
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: shared_tag:LCR
- node: '[[Swap Spreads — Drivers, Balance Sheet Frictions, and Plumbing Indicators]]'
  relation: shared_tag:LCR
- node: '[[Basel Regional Implementation Dynamics]]'
  relation: shared_tag:basel-iii
date_created: '2026-05-21'
date_updated: '2026-05-21'
---


## Overview

While RWA and the Output Floor attack the capital (equity) side of bank economics, LCR and NSFR attack the funding (liability) side. The combined effect is a double squeeze that makes holding long-duration, illiquid corporate loans structurally unprofitable for regulated banks. [LLM]

**LCR mechanics (LCR20/40):** Requires High Quality Liquid Assets (unencumbered govt bonds, CB reserves) ≥ net cash outflows over a 30-day stress scenario. LCR40 applies product-specific draw-down rates: committed credit lines to non-financial corporates → 10%; committed liquidity lines to non-financials → 30%; committed credit/liquidity lines to financial institutions → 40%. The HQLA opportunity cost (near-zero yield vs. lending spread) applies to the buffer required against contingent outflows.

**NSFR mechanics:** Available Stable Funding (ASF) ≥ Required Stable Funding (RSF). RSF factors:
- Loans >1yr to non-financial corporates: **85%**
- Loans <1yr to non-financial corporates: **50%**
- HQLA (govts, CB reserves): **0%**

This asymmetry structurally punishes maturity transformation — the core banking function — for corporate exposures.

## Mechanism / How It Works

Key condition: The penalty only dominates when [spreads on long-term corporate loans < funding cost premium imposed by NSFR + HQLA drag from LCR]. In a low-rate environment, this condition is almost always met because spreads compressed while HQLA drag (opportunity cost of holding near-zero-yield reserves) remained large. [LLM]

## Evidence and Sources

[RAW-Gemini Deep Research — Section II.4: LCR (BIS bcbs238), NSFR (BIS d295)]

## Related Concepts

The LCR/NSFR penalty compounds with [[Basel_Output_Floor_Specialized_Lending_Impact]] to produce a complete economic case for bank retreat from specialized lending. The resulting funding gap is the structural supply-side driver of private credit growth documented in [[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]].

