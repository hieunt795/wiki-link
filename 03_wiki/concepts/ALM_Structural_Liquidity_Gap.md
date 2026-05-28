---
node_id: alm_structural_liquidity_gap_001
type: concept
title: "ALM Structural Liquidity Gap — Medium-Long Term Liquidity Management"
aliases:
  - Structural liquidity
  - Medium-long term liquidity gap
  - Structural liquidity risk
  - Beyond-LCR liquidity management
  - NSFR structural liquidity
  - khe hở thanh khoản cơ cấu
  - quản lý thanh khoản trung dài hạn

domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - liquidity
  - nsfr
  - structural_liquidity
  - maturity_ladder
  - funding
  - behavioural_models

confidence: 1
stability: stable

thesis: >
  [LLM] Structural liquidity management governs the medium-to-long term balance between assets
  and liabilities beyond the 1-year short-term horizon (the LCR window), using gap ratios at
  1Y, 3Y, and 5Y horizons to limit excessive maturity transformation; the NSFR operationalizes
  the regulatory dimension of this management by requiring that available stable funding (ASF)
  exceeds required stable funding (RSF) on a one-year horizon, while internal structural limits
  add further buffers and behavioral modeling assumptions determine the effective funding profile
  of behavioural items.

source_refs:
  - path: 02_sources/books/alm/A - Asset liability optimization.md
    pages: "Ch 1 (Basel III LCR/NSFR overview), Ch 2 (Medium Long-Term Liquidity, Structural Liquidity Management)"
    weight: primary

related:
  - node: "[[ALM_Balance_Sheet_Optimization_Framework]]"
    relation: component_of
  - node: "[[ALM_Hedging_Strategy_Design]]"
    relation: related_to
  - node: "[[FTP_Methodology]]"
    relation: related_to

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Short-Term vs. Structural Liquidity

[LLM] ALM separates liquidity management into two distinct horizons:

**Short-term liquidity (≤ 1 year):**
- Governed by the Liquidity Coverage Ratio (LCR ≥ 100%)
- Focus: can the bank survive a 30-day stress scenario with HQLA?
- Operational gap ratios by time bucket: 45 days (≥110%), 3 months (≥80%), 6 months (≥60%)
- Managed through daily operational liquidity, repo operations, counterbalancing capacity (CBC)

**Structural liquidity (> 1 year):**
- Governed by the Net Stable Funding Ratio (NSFR ≥ 100%) as the regulatory floor
- Focus: is the bank's medium-long-term funding structure sustainable relative to asset maturities?
- Internal structural gap limits set at 1Y, 3Y, and 5Y horizons
- Managed through the funding plan, debt issuance strategy, and FTP curve incentives

[LLM] The crucial distinction: **short-term liquidity is about surviving a stress event**; structural liquidity is about **avoiding the conditions that create stress in the first place** (excessive maturity transformation, over-reliance on short-term wholesale funding).

## Structural Liquidity Measurement Framework

[LLM] The maturity ladder for structural liquidity positions all balance sheet items (and off-balance items) in their respective time buckets based on residual contractual maturity, with behavioral adjustments for non-maturing items:

**Asset side:**
- Cash and eligible bonds: included in counterbalancing capacity (liquid)
- Fixed-rate loans: mapped to contractual maturity
- Non-performing loans (NPLs): mapped to expected repayment schedule, or "irredeemable" if unknown
- Equity investments and intangibles: mapped as irredeemable
- Off-balance sheet (undrawn commitments): NSFR run-off factors applied

**Liability side:**
- Time deposits: contractual maturity
- CASA and behavioural deposits: modeled via behavioural assumptions (core/non-core split)
- Wholesale funding / issued bonds: contractual maturity
- Equity: irredeemable (never matures)

## Internal Structural Limits (Lubinska Framework)

[LLM] Three internal monitoring thresholds are established for structural liquidity:

**Structural Limit (> 1 year):**
Gap ratio (Cash inflows + CBC beyond 12M) / (Cash outflows beyond 12M) ≥ b%
[LLM] Typically b = 100%. Below this threshold, more medium-long assets are being funded by short-term liabilities than the policy allows. A breach requires lengthening funding maturity or reducing long-duration assets.

**Structural Warning 1 (> 3 years):**
Gap ratio (inflows > 3Y) / (outflows > 3Y) ≥ c%
[LLM] Typically c ≈ 70%. Provides early warning of deteriorating structural position in the medium term.

**Structural Warning 2 (> 5 years):**
Gap ratio (inflows > 5Y) / (outflows > 5Y) ≥ d%
[LLM] Typically d ≈ 60%. Focuses on the longest-duration segment, relevant for banks with significant mortgage portfolios.

## The NSFR as Regulatory Structural Liquidity Metric

[LLM] The NSFR (Net Stable Funding Ratio) translates structural liquidity principles into a mandatory ratio:

NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF) ≥ 100%

**ASF factors** (stability of funding sources):
- Capital and perpetual instruments: 100%
- Retail and SME deposits (>1Y or stable behavioral): 90–95%
- Stable short-term wholesale (< 6M): 0–50% depending on counterparty and maturity
- Long-term wholesale (> 1Y): 100%

**RSF factors** (liquidity needs of assets):
- Cash and central bank placements: 0%
- HQLA Level 1: 5–10%
- Interbank loans < 6M: 10–15%
- Unencumbered loans > 1Y (retail, corporate): 65–85%
- Encumbered assets > 1Y: 100%

[LLM] The NSFR calibration is based on two dimensions: **funding tenor** (longer-term funding more stable) and **funding type** (retail more stable than wholesale for same tenor). Assets require stable funding proportional to how illiquid and long-dated they are.

## Behavioral Assumptions for Structural Limits

[LLM] The structural liquidity profile is heavily dependent on behavioral assumptions for:
- **CASA deposits:** Core/non-core split determines effective maturity. Core balances (stable under all conditions) are assigned medium-term behavioral maturity (e.g., 3–5 years); volatile portion assigned overnight. The behavioral maturity directly drives the NSFR ASF factor.
- **Prepayment of mortgages:** Actual repayments (prepayments + scheduled amortization) shorten the effective asset maturity below the contractual term. Higher prepayment → shorter effective RSF tenor → less stable funding required → easier NSFR compliance, but also reduces NIM.
- **Rollover assumptions for wholesale funding:** What proportion of maturing wholesale funding can be rolled over? The rollover assumption determines the effective short-term funding profile.

[LLM] These assumptions must be validated by independent risk model validation and approved by ALCO and the Risk Committee before use in regulatory or internal reporting.

## Funding Plan Integration

[LLM] Structural liquidity management is inherently forward-looking and requires a medium-term funding plan (2–3 year horizon) that:
- Forecasts asset growth by product type and maturity
- Projects maturing liabilities by instrument and counterparty
- Plans new issuance (bonds, covered bonds, MREL-eligible instruments) to fill funding gaps
- Stress-tests the plan under scenarios of market-wide illiquidity and name-specific stress
- Incorporates a contingency funding plan (CFP) defining early warning indicators and action steps

[LLM] The structural liquidity framework therefore directly informs ALCO strategy, the annual funding plan, and the ILAAP submission to supervisors — making it one of the most consequential dimensions of ALM governance.
