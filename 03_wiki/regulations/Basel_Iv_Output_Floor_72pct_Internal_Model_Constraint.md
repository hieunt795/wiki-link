---
node_id: basel_iv_output_floor_72pct_internal_model_constraint_001
type: regulation
title: 'Basel IV Output Floor: 72.5% SA-RWA Floor on Internal Models'
aliases:
- output floor Basel IV
- 72.5% floor
- RWA floor
- sàn đầu ra Basel IV
- model floor IRB
- output floor standardised approach
domain:
  primary: basel_risk
tags:
- output_floor
- rwa
- irb
- internal_models
- standardised_approach
- basel4
- capital_adequacy
- credit_risk
confidence: 3
stability: stable
thesis: 'The output floor requires that a bank''s total RWA (used for capital ratio
  calculation) must not fall below 72.5% of the RWA computed using only standardised
  approaches — constraining the capital reduction achievable through internal models
  (IRB for credit risk, IMA for market risk, IMM for counterparty credit risk) and
  eliminating incentives for excessive model optimisation, particularly in specialised
  lending and low-risk mortgage portfolios.

  '
source_refs:
- path: 02_sources/regulator/bcbs/BaselFramework.md
  pages: RBC20.4, RBC20.11-20.13 (output floor mechanics and calculation), RBC90 (phase-in
    2023-2028)
  weight: primary
parent_node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
related:
- node: '[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]'
  relation: rwa_denominator_constraint
- node: '[[Basel_Output_Floor_Specialized_Lending_Impact]]'
  relation: credit_impact_application
- node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
  relation: component_of
- node: '[[Basel_Driven_Credit_Migration_To_Private_Markets]]'
  relation: credit_migration_driver
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## Mechanism

The output floor creates a **binding floor on RWA** used for capital adequacy calculation:

```
Floored RWA = MAX(
  Model RWA  [using IRB, IMA, IMM nominated approaches],
  72.5% × SA-RWA  [using standardised approaches only]
)
```

Capital ratios (CET1, Tier 1, Total) are calculated using `Floored RWA` as the denominator. A bank running sophisticated internal models cannot let its reported capital ratios reflect model-optimised RWA lower than 72.5% of what standardised approaches would produce.

## Numerical Example (from RBC20.13)

| Risk category | Model RWA | SA-RWA |
|---|---|---|
| Credit risk | 62 | 124 |
| Market risk | 2 | 4 |
| Operational risk | 12 | 12 |
| **Total** | **76** | **140** |

72.5% × 140 = **101.5** (floor)

Since 101.5 > 76, the bank must use **101.5** as its RWA for capital ratio purposes — a 33.5% increase vs. unconstrained model RWA.

## Approaches Excluded from SA-RWA Calculation

The "base of the output floor" must use **only** standardised approaches (RBC20.11-12). Specifically excluded:
- IRB approach for credit risk
- SEC-IRBA (securitisation internal-ratings-based approach)
- IMA for market risk
- VaR models for counterparty credit risk
- IMM for counterparty credit risk

If a bank uses these for its nominated approaches, it must separately compute SA-RWA using the standardised alternatives for the floor calculation.

## Phase-In Schedule (RBC90, effective 1 January 2023)

| Year | Floor level |
|---|---|
| 2023 | 50% |
| 2024 | 55% |
| 2025 | 60% |
| 2026 | 65% |
| 2027 | 70% |
| 2028 onwards | **72.5%** (full) |

During phase-in: supervisors may cap the **incremental increase** in total RWA from the floor at 25% of pre-floor RWA in any single period.

## Why It Matters: Specialised Lending

IRB models for specialised lending (project finance, object finance, commodities finance, real estate) historically generated very low risk weights vs. standardised approach. The output floor effectively closes this gap — a bank using IRB for specialised lending still faces a capital floor equivalent to 72.5% of the SA risk weight (typically 100-150%). [LLM] This is the primary mechanism by which Basel IV increases capital costs for corporate lending held on bank balance sheets, driving credit migration to unregulated private credit markets.

## Related Concepts

`[[Basel_Output_Floor_Specialized_Lending_Impact]]` documents the empirical impact on specific lending categories. `[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]` explains the capital ratios that use floored RWA as the denominator. `[[Basel_Driven_Credit_Migration_To_Private_Markets]]` traces the market-structure consequence: capital cost increase → bank originate-to-distribute → private credit fills the gap.
