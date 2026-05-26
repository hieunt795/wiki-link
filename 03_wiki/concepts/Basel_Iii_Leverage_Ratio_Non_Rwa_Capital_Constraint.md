---
node_id: basel_iii_leverage_ratio_non_rwa_capital_constraint_001
type: concept
title: "Basel III Leverage Ratio: Non-RWA Capital Backstop"
aliases:
  - leverage ratio Basel III
  - LEV Basel
  - supplementary leverage ratio
  - SLR
  - tỷ lệ đòn bẩy Basel III
  - đòn bẩy phi rủi ro
domain:
  primary: basel_risk
  secondary:
    - financial_markets
tags:
  - leverage_ratio
  - slr
  - tier1_capital
  - exposure_measure
  - off_balance_sheet
  - non_rwa
  - dealer_constraints
  - basel3
confidence: 3
stability: stable
thesis: >
  The Basel III leverage ratio (Tier 1 capital / total exposure measure ≥ 3%)
  is a non-risk-based backstop to the RWA capital framework — it constrains
  balance sheet expansion regardless of risk weight, capturing both on-balance
  sheet assets and off-balance sheet items (derivatives at 1.4× (RC+PFE),
  SFT exposures, and undrawn commitments) under a single gross exposure measure
  that cannot be reduced by collateral netting or credit risk mitigation.
source_refs:
  - path: 02_sources/regulator/bcbs/BaselFramework.md
    pages: "LEV10 (scope), LEV20 (calculation, 3% minimum), LEV30 (exposure measurement: on-BS, derivatives, SFTs, off-BS), LEV40 (G-SIB requirement)"
    weight: primary
related:
  - node: "[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]"
    relation: complementary_constraint
  - node: "[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
    relation: us_implementation_context
  - node: "[[Basel_Gsib_Surcharge_Bucket_Methodology_Capital_Add_On]]"
    relation: g_sib_additional_requirement
  - node: "[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]"
    relation: part_of_four_constraints
date_created: "2026-05-26"
date_updated: "2026-05-26"
---

## Overview

The leverage ratio is designed as a **non-risk-sensitive backstop**: it prevents the risk-based capital framework from being gamed through very low risk weights applied to large balance sheets. A bank can have excellent RWA-based capital ratios while being excessively leveraged — the leverage ratio catches this case.

**Formula:** `Leverage Ratio = Tier 1 Capital / Total Exposure Measure ≥ 3%`

Unlike the risk-based framework, **no collateral netting, no credit risk mitigation, no risk weights** are applied. The exposure measure is predominantly gross.

## Exposure Measure Components (LEV30)

**1. On-balance sheet exposures**
- All assets at accounting values, less specific provisions
- Central bank reserves may be excluded at national discretion (with offsetting increase in calibration)
- No netting of assets and liabilities

**2. Derivative exposures**
- Measured as: `1.4 × (Replacement Cost + Potential Future Exposure)`
- The 1.4 scalar alpha captures systemic risk in derivatives portfolios
- Eligible bilateral netting contracts reduce RC but not the alpha multiplier entirely

**3. Securities financing transactions (SFTs)**
- Repo, reverse repo, securities lending
- Gross treatment with limited netting for cash legs of same-counterparty SFTs
- Captures the prime brokerage and dealer balance sheet expansion that RWA misses

**4. Off-balance sheet items**
- Undrawn credit commitments, guarantees, trade finance
- Apply Credit Conversion Factor (CCF) — typically 10%–100% depending on commitment type
- Unconditionally cancellable commitments may use 10% CCF

## Why Non-Additive with RWA Constraint

The leverage ratio and RWA-based capital constraints are **not simply additive** — they bind alternately:
- For high-risk-weight assets (corporate loans, EM exposure): RWA constraint typically binds
- For low-risk-weight but large-volume assets (sovereign bonds, derivatives, repo): **leverage ratio binds**

This is why repo market intermediation and Treasury dealer activity are disproportionately constrained by the leverage ratio: government bonds carry 0% risk weight (RWA irrelevant) but full notional counts in the exposure measure.

## G-SIB Add-On (LEV40)

G-SIBs face a leverage ratio buffer of **50% of their G-SIB risk-based buffer** in CET1:
- Bucket 1 G-SIB (1.0% RWA buffer) → 0.5% leverage ratio buffer
- Bucket 3 G-SIB (2.0% RWA buffer) → 1.0% leverage ratio buffer

This creates an additional binding constraint for G-SIBs engaged in low-risk-weight activities.

## US-Specific Implementation (SLR)

The US **Supplementary Leverage Ratio** applies 3% minimum to all covered BHCs and 5% to G-SIBs. During COVID-19, the Fed temporarily excluded reserves and Treasuries from the SLR denominator (2020-2021); reversion to full treatment contributed to dealer capacity constraints in Treasury markets. See `[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]` for the treasury market transmission.

## Related Concepts

The leverage ratio is the third leg (after RWA capital ratios and LCR/NSFR) of the Basel III constraint system documented in `[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]`. Its interaction with US dealer capacity is the core mechanism in `[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]`.
