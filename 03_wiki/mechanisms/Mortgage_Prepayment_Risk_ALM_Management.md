---
node_id: mortgage_prepayment_risk_alm_management_001
type: mechanism
title: Mortgage Prepayment Risk and ALM Management
aliases:
- mortgage prepayment ALM
- MBS negative convexity
- OAS mortgage pricing
- CPR prepayment model
- MSR duration
- rủi ro trả nợ sớm thế chấp ALM
- mô hình CPR thế chấp
- độ lồi âm MBS
- lãi suất điều chỉnh OAS
domain:
  primary: alm
  secondary: []
tags:
- mortgage
- prepayment
- node: '[[MBS]]'
  relation: related_to
- node: '[[CPR]]'
  relation: related_to
- node: '[[OAS]]'
  relation: related_to
- negative-convexity
- node: '[[MSR]]'
  relation: related_to
- S-curve
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- stochastic-EaR
confidence: 1
stability: stable
thesis: 'Mortgage prepayment risk arises from four distinct borrower behaviors (turnover,
  rate-driven refinancing, cash-out refinancing, and default) that produce negative
  convexity in mortgage cash flows; the aggregate prepayment speed (CPR) drives MBS
  valuation via OAS pricing, and ALM must use stochastic earnings-at-risk rather than
  static gap analysis because hedge rebalancing costs materialize as rate volatility
  increases. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 9: Mortgage Prepayment Risk and ALM Management'
parent_node: null
related:
- node: '[[NMD_Stochastic_Three_Factor_Model]]'
  relation: related_to
- node: '[[Interest_Rate_Basis_Risk_Measurement_ALM]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

Mortgage prepayment risk arises from four distinct borrower behaviors that produce negative convexity in mortgage cash flows. [LLM] The aggregate prepayment speed (CPR) drives MBS valuation via OAS pricing, and ALM must use stochastic earnings-at-risk to capture hedge rebalancing costs under rate volatility. [LLM]

## Four Types of Prepayment

### 1. Turnover Prepayment

- Occurs when borrowers sell their home (job change, family change, relocation). [LLM]
- Baseline rate: approximately **0.7% CPR per month** (Conditional Prepayment Rate). [LLM]
- **Ageing ramp:** newly originated loans prepay slowly; turnover prepayments ramp up over an **18–24 month seasoning period** before reaching the steady-state CPR. [LLM]
- Not driven by interest rates; provides a floor level of prepayment regardless of rate environment. [LLM]

### 2. Rate-Driven Refinancing

- Occurs when market rates fall below the borrower's current coupon by a sufficient margin. [LLM]
- Follows an **S-curve** shape as a function of the refinancing incentive (current_coupon − market_rate): [LLM]
  - Below 0bp incentive: minimal refi activity (close to turnover CPR). [LLM]
  - At ~50bp incentive: refi speed accelerates sharply; S-curve is steepest. [LLM]
  - At ~150bp incentive: refi speed levels off (burnout: borrowers who remain have structural barriers to refinancing). [LLM]
- **Burnout effect:** as incentive increases, the pool of refinanceable loans shrinks because motivated borrowers have already refinanced; remaining borrowers have high prepayment barriers. [LLM]

### 3. Cash-Out Refinancing

- Borrowers refinance to extract home equity (house price appreciation). [LLM]
- Driven by LTV (loan-to-value) ratio and house price levels, not purely by rate incentive. [LLM]
- Can occur even when interest rates are flat or rising if home prices have appreciated significantly. [LLM]

### 4. Default-Related Prepayment

- Loan terminates early due to borrower default (followed by servicer liquidation of collateral). [LLM]
- Modeled separately via a default intensity/hazard rate process. [LLM]
- High-LTV, low-FICO loans have materially higher default-driven prepayment in stress scenarios. [LLM]

## Key Loan-Level Drivers

The prepayment model incorporates the following loan-level and macro variables: [LLM]

| Driver | Effect |
|--------|--------|
| **FICO score** | Higher FICO → easier refinancing → higher rate-driven CPR |
| **LTV ratio** | High LTV → constrained refi access (lender won't refinance underwater loan) |
| **Loan size** | Larger loans: higher dollar benefit from rate refi → faster CPR |
| **Burnout** | History of missed refi opportunities reduces current sensitivity |
| **Seasonality** | Spring/summer home-buying season → higher turnover prepayments |
| **Lock-in effect** | Borrowers with below-market rates resist selling homes (negative incentive to move) |

[LLM]

## MBS Cash Flow Formula with Survival Factor

The scheduled monthly cash flow for an MBS pool in period k is adjusted by a survival factor Fk: [LLM]

> **CF_k = (Interest_k + Scheduled_Principal_k + Prepayment_k) × F_k** [LLM]

Where: [LLM]
- F_k = Π(1 − CPR_m/12) for m = 1 to k (fraction of original pool remaining) [LLM]
- Prepayment_k = Outstanding_balance_{k−1} × SMM_k (Single Monthly Mortality = 1 − (1 − CPR_k)^{1/12}) [LLM]

As CPR increases, the survival factor declines faster, shortening the expected life of the cash flow stream. [LLM]

## Negative Convexity and MSR Duration

**Negative convexity** is the defining feature of mortgage instruments from an ALM perspective: [LLM]

- When rates fall: prepayments accelerate → MBS duration shortens → the asset declines in value relative to a non-callable bond. [LLM]
- When rates rise: prepayments slow → MBS duration extends → losses are larger than a straight bond's. [LLM]
- This asymmetric duration response creates a **negative convexity** profile (price-yield curve is concave rather than convex). [LLM]

**Mortgage Servicing Rights (MSRs):** [LLM]
- MSRs have **leveraged negative duration**: the MSR value rises as rates rise (slower prepayment → more future servicing income) and falls sharply as rates decline. [LLM]
- MSRs are often used as a natural hedge for the origination pipeline's interest rate risk but introduce concentrated convexity exposure. [LLM]

## OAS Pricing — Linking Prepayment Model to Valuation

Option-Adjusted Spread (OAS) prices the mortgage instrument net of its embedded prepayment option: [LLM]

> **MBS_price = E[Σ CF_k(r, prepayment_model) / (1 + r_k + OAS)^k ]** [LLM]

The OAS is derived from the LIBOR Market Model (LMM) or similar stochastic rate model to generate interest-rate paths; for each path, the prepayment model produces CPR; cash flows are discounted at the risk-free path rate plus OAS. [LLM] The OAS that equates the model price to the observed market price measures the credit/liquidity spread net of the option cost. [LLM]

## ALM Balance Sheet Integration

For gap-report and capital management purposes, the mortgage portfolio is represented as a **key-rate duration profile** rather than a single duration number: [LLM]

1. Convert the stochastic distribution of prepayment speeds into an expected cash flow profile across maturity buckets. [LLM]
2. Compute partial PV01 (key-rate duration) at each bucket. [LLM]
3. Construct a **replicating hedge portfolio** (receiver swaps or bonds) that matches the KRD profile. [LLM]
4. Report net position (mortgage KRD − hedge KRD) in the ALCO gap report. [LLM]

## Stochastic EaR Requirement

Static gap analysis (ΔNII = GAPᵢ × T × Δr) is insufficient for mortgages because: [LLM]

- Rate volatility causes hedge rebalancing: as rates move and prepayment speeds shift, the hedge portfolio must be adjusted, incurring transaction costs. [LLM]
- These rebalancing costs are proportional to volatility squared (gamma/convexity cost) and are invisible in a static shock scenario. [LLM]
- **Stochastic EaR** (earnings-at-risk using Monte Carlo rate paths) captures the distribution of NII outcomes including rebalancing costs, providing a more realistic risk measure for mortgage portfolios. [LLM]

---
*Source: Chapter 9 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
