---
node_id: nii_sensitivity_forecast_static_dynamic_balance_sheet_001
type: mechanism
title: 'NII Sensitivity and Forecasting: Static vs Dynamic Balance Sheet Assumptions'
aliases:
- NII forecast
- NII sensitivity
- net interest income sensitivity
- earning gap analysis
- dự báo thu nhập lãi thuần
- độ nhạy cảm NII
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- NII
- interest_income
- balance_sheet_assumptions
- rate_shock
- IRRBB
- repricing
confidence: 1
stability: stable
thesis: '[LLM] NII sensitivity measures the change in a bank''s net interest income
  for a given interest rate shock relative to a baseline forecast; its magnitude depends
  critically on the balance sheet assumption chosen (run-off, static, or dynamic)
  and on the timing of repricing events across asset and liability products.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch 2, sections 2.2.1–2.2.5
  weight: primary
parent_node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
related:
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: component_of
- node: '[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## What NII Measures

NII = Interest Income (assets) − Interest Expense (liabilities) for a defined period.

[LLM] In ALM, the focus is not on the absolute level of NII but on how it changes when interest rates shift. NII sensitivity = NII(shocked scenario) − NII(baseline). [LLM] Positions that are not interest-rate-sensitive (real estate, equity investments, intangible assets, bank equity) are excluded from the NII sensitivity calculation.

## Balance Sheet Assumptions

Three standard assumptions govern how maturing positions are treated:

- **Run-off view**: Maturing positions are not replaced. The balance sheet shrinks over time as all transactions mature. [LLM] This is the most conceptually simple but least realistic view; it is used for EVE calculations (run-off balance sheet) under the EBA supervisory outlier test.

- **Static view**: Maturing positions are replaced by comparable positions with the same instrument type, volume, original maturity, and commercial margin — but repriced at prevailing market rates. [LLM] This is the regulatory requirement for NII reporting under EBA supervisory frameworks (Article 4(4), Delegated Regulation 2024/856) and represents a going-concern assumption.

- **Dynamic view**: The balance sheet evolves according to the bank's business plan, incorporating changes in customer volumes, new product origination, and management decisions. [LLM] This is the most complex assumption and is used in internal NII planning (Section 3.2), but not for the standardized supervisory outlier test.

## NII Forecast Process

[LLM] The NII forecast begins with the current balance sheet (all on- and off-balance-sheet positions at their existing coupons and maturities). Moving into the future, each position is tracked through its repricing events:

1. **Before repricing**: Use the position's current coupon rate.
2. **At repricing**: Replace the old coupon with the market rate for the product's reset tenor, plus the commercial margin.
3. **After repricing**: Apply the new coupon for the remainder of the period until the next reset.

[LLM] Two assumptions must be made about future rates: (a) forward rates (implied by today's yield curve, the "expectation theory" approach), or (b) unchanged rates (current spot rates, widely used by practitioners because forward rates embed a liquidity premium and have historically been poor predictors of actual future rates). [LLM] The choice of forward-rate vs unchanged-rate assumption materially affects the shape of the NII forecast, particularly for receiver swaps, which look deceptively attractive when short rates are assumed to remain low.

## NII Sensitivity Calculation

[LLM] Once a baseline NII is established, the same repricing calculation is run under a shocked rate scenario (e.g., instantaneous −100 bp parallel shift). The shocked yield curve replaces the baseline curve at each future repricing date. The NII sensitivity is the difference between the two 3-year totals. The book's illustrative model bank shows: baseline 3-year NII = 42.47; shock scenario NII = 42.08; sensitivity = −0.39 (for a −100 bp shock).

## Earning Gap as a Summary Metric

[LLM] The earning gap (income gap) is a simplified summary of NII sensitivity to a 1% parallel shock. It groups positions by their first repricing date within a one-year horizon. For each repricing bucket, the periodic earning gap = net repricing gap × 1% × (remaining months in year / 12). Summing across all buckets gives the total earning gap, which estimates the decline in first-year NII for a 1% rate increase. [LLM] In the illustrative model bank, the total earning gap is −0.25, implying a NII decline of −1.00 for a 400 bp parallel rate rise.

## Regulatory Limit (SOT on NII)

[LLM] Under EBA/RTS/2022/10, the supervisory outlier test on NII flags a bank as an outlier when ΔNII / Tier 1 capital exceeds 5% under a parallel shock up or parallel shock down scenario. [LLM] The NII SOT uses a static (constant) balance sheet assumption and a one-year calculation horizon; it also requires commercial margins to be included (unlike the EVE SOT where margins may be excluded).

## EVE vs NII Trade-off

[LLM] A key practical tension in IRRBB management is that actions that improve EVE sensitivity can worsen NII sensitivity, and vice versa. A bank that immunizes its EVE by matching asset and liability durations may introduce NII volatility if short-term funding reprices before long-term fixed assets. Adding a receiver swap helps NII in a declining-rate environment but increases EVE duration gap. EBA requires banks to manage both metrics simultaneously (the "simultaneous compliance problem", Section 5.4 of Tata 2025).
