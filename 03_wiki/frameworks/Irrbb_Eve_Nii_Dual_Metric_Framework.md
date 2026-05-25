---
node_id: irrbb_eve_nii_dual_metric_framework_001
type: framework
title: IRRBB EVE NII Dual Metric Framework
aliases:
- IRRBB Framework
- EVE NII Framework
- Interest Rate Risk Banking Book
- Khung đo lường IRRBB
domain:
  primary: monetary_policy
tags:
- basel
- irrbb
- eve
- nii
- banking_regulation
- alm
- interest_rate_risk
confidence: 4
stability: evolving
thesis: Basel IRRBB regulation (BCBS 368, 2016) mandates two complementary metrics
  — Economic Value of Equity (EVE) and Net Interest Income (NII) sensitivity — to
  measure structural interest rate risk in the banking book, capturing both long-run
  economic impact and short-run earnings impact from rate shocks.
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Chapter 3-4
  weight: primary
- path: 02_sources/regulator/bcbs/d368.md
  pages: "para 8–11 (IRRBB definition + EVE/NII intro), para 33–34 (EVE vs NII complementarity), para 69–70 (P8 disclosure: ΔEVE and ΔNII under 6 scenarios), para 88–89 (P12 outlier test: 15% Tier 1), Table B (six prescribed scenarios: parallel up/down, steepener, flattener, short rate up/down)"
  weight: supporting
related:
- node: '[[Basel Driven Credit Migration To Private Markets]]'
  relation: shared_tag:basel
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:basel
- node: '[[US Shadow Banking Post-GFC Market Based Finance Structure]]'
  relation: shared_tag:basel
- node: '[[Basel III Endgame — Capital, Liquidity, and Credit Migration]]'
  relation: shared_tag:basel
- node: '[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]'
  relation: shared_tag:alm
- node: '[[Bcbs_Irrbb_Standards_D368_2016]]'
  relation: regulatory_source
- node: '[[Bcbs_Irrbb_Nmd_Standardised_Framework]]'
  relation: nmd_detail
date_created: '2026-05-22'
date_updated: '2026-05-25'
---


## Overview
IRRBB (Interest Rate Risk in the Banking Book) is structural risk from maturity mismatches in a bank's non-trading positions. BCBS 368 (April 2016) established the current framework via 12 principles, adopting a **Pillar 2** approach over the originally proposed Pillar 1 standardized methodology. The Pillar 1 approach was rejected because heterogeneous banking business models made any standardized method either punitive or incomplete [RAW-CLIP].

## Three Sources of IRRBB
1. **Gap Risk:** Mismatches in repricing dates between assets, liabilities and off-balance-sheet positions (parallel and non-parallel yield curve shifts) [RAW-CLIP].
2. **Basis Risk:** Imperfect correlation between indices used for different instruments with similar tenors — e.g., a loan priced at prime rate funded by a LIBOR-indexed liability [RAW-CLIP].
3. **Option Risk:** Embedded optionality in banking products — prepayment options in mortgages, non-maturing deposit withdrawal rights, credit card drawdowns, fixed-rate loan commitments [RAW-CLIP].

## The Two-Metric Approach
**EVE (Economic Value of Equity):**
- Present value of all assets minus present value of all liabilities.
- A "gone concern" simplified equity valuation — no new business assumed.
- EVE sensitivity = change in EVE from a rate shock.
- Captures full balance sheet mismatches including long-tail optionality.
- Used for capital adequacy assessment [RAW-CLIP].

**NII (Net Interest Income):**
- Projected revenue from interest rate margin over a 1-2 year horizon.
- Incorporates new business origination.
- NII sensitivity = change in NII projection from a rate shock.
- Captures short-term earnings risk and capital origination capacity [RAW-CLIP].

Neither metric alone is sufficient:
- EVE misses time distribution of cashflows and earnings capacity.
- NII misses exposures beyond the 1-2 year horizon (mismatch concentration in medium-to-long term is invisible) [RAW-CLIP].

## Outlier Test (SOT)
A bank is considered an IRRBB outlier (requiring supervisory attention) if its EVE declines by more than **15% of Tier 1 capital** under any of the six prescribed rate scenarios (Basel parallel/non-parallel shocks) [RAW-CLIP].

## Role of Behavioral Assumptions
IRRBB measurement is fundamentally dependent on behavioral assumptions for:
- Non-maturity deposits (NMDs): rate elasticity, volume stickiness.
- Mortgage prepayment: client option exercise.
- Credit card/overdraft repricing limits.
- Capital maturity conventions.

Principle 5 of BCBS 368 mandates governance of these modeling assumptions as a core component — moving the focus from exposure control to structural risk management under model uncertainty [RAW-CLIP].


