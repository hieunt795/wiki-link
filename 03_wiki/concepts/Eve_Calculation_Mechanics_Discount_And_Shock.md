---
node_id: eve_calculation_mechanics_discount_and_shock_001
type: concept
title: 'EVE Calculation Mechanics: Discounting Cashflows and Rate Shock'
aliases:
- EVE calculation
- Economic Value of Equity mechanics
- Delta EVE
- tính toán EVE
- giá trị kinh tế của vốn chủ sở hữu
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- EVE
- economic_value
- discounted_cashflow
- interest_rate_shock
- IRRBB
confidence: 1
stability: stable
thesis: '[LLM] EVE is calculated as the present value of all asset cashflows minus
  the present value of all liability cashflows (plus off-balance-sheet items), discounted
  at the current risk-free yield curve; a rate shock scenario repeats the calculation
  with a shifted curve, and the change in EVE (ΔEVE) measures the bank''s economic
  capital sensitivity to that shock.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch 2, sections 2.1.1–2.1.2
  weight: primary
parent_node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
related:
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: component_of
- node: '[[Duration_Gap_Analysis_Banking_Book]]'
  relation: related_to
- node: '[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Definition

EVE = EV(Assets) − EV(Liabilities) + EV(OBS assets) − EV(OBS liabilities).

[LLM] The economic value (EV) of any position is the sum of the present values of its future cashflows, discounted at an appropriate risk-free rate. [LLM] Equity itself is excluded from the EVE calculation; including equity would cause it to influence its own economic value, creating circularity. Under EU regulation (Commission Delegated Regulation 2024/856), all CET1 instruments and other perpetual own funds without call dates are excluded.

## Step-by-Step Calculation

[LLM] The EVE calculation proceeds in four steps:

1. **Map cashflows**: For each balance-sheet and off-balance-sheet position, determine the timing and amount of all future cashflows. Fixed-rate instruments have deterministic cashflows; floating-rate instruments must be projected (cashflows reset at next repricing). Positions with embedded optionality (prepayment, early withdrawal) require behavioral assumptions about expected cashflow timing.

2. **Discount each cashflow**: Each cashflow CF_t is discounted using the spot risk-free rate for its maturity:  
   EV = Σ CF_t / (1 + r)^t  
   where r is the annual discount rate and T is the total horizon until the last cashflow runs off.

3. **Compute baseline EVE**: Sum present values of all asset cashflows minus all liability cashflows. This is the baseline EVE under current rates.

4. **Apply shock and recompute (ΔEVE)**: Shift the discount rate from r to (r + Δr) for every maturity. Recompute EV for all positions. ΔEVE = EVE(shocked) − EVE(baseline). [LLM] A rise in rates lowers the PV of fixed cashflows; assets with longer duration lose more value than liabilities with shorter duration, so a bank with a positive duration gap loses EVE when rates rise.

## Key Modeling Constraints

[LLM] When cashflows depend on rates (e.g., floating-rate instruments, prepayable mortgages, non-maturity deposits), the cashflow projections themselves must be adjusted under the shocked scenario — not just the discount rate. [LLM] EBA guidelines (EBA/GL/2022/14) require that behavioral repricing dates for non-maturity retail and wholesale deposits be capped at a maximum weighted average of 5 years. The EBA specifies six supervisory shock scenarios: parallel up, parallel down, steepener, flattener, short rates up, short rates down.

## Supervisory Outlier Test (SOT) on EVE

[LLM] A bank becomes an outlier if ΔEVE exceeds 15% of Tier 1 capital under any of the six shock scenarios (CRD V 2019, Article 98). [LLM] The earlier CRD IV threshold of 20% of own funds still exists as a separate trigger requiring immediate notification to the competent authority. The shocked rate curve is subject to a maturity-dependent floor (starting at −150 bps for short maturities, rising by 3 bps per year to 0% at 50-year maturity under RTS/2022/10) to prevent unrealistic negative rate scenarios.

## EVE vs Accounting Value

[LLM] The economic value of a balance-sheet position may differ significantly from its accounting (book) value. A loan recorded at par (100% of notional) may have a higher economic value if the contractual interest rate exceeds current market rates; conversely, a bond held at amortized cost in an HTM portfolio may have a substantially lower economic value if rates have risen since issuance. This divergence was central to the Silicon Valley Bank failure in 2023.
