---
node_id: mortgage_prepayment_risk_alm_management_001
type: concept
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
- negative-convexity
- S-curve
- stochastic-EaR
confidence: 3
stability: stable
thesis: 'Mortgage prepayment risk arises from four distinct borrower behaviors (turnover,
  rate-driven refinancing, cash-out refinancing, and default) that produce negative
  convexity in mortgage cash flows; the aggregate prepayment speed (CPR) drives MBS
  valuation via OAS pricing, and ALM must use stochastic earnings-at-risk rather than
  static gap analysis because hedge rebalancing costs from dynamic delta hedging materialize
  as rate volatility increases.

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
- node: '[[MBS]]'
  relation: related_to
- node: '[[CPR]]'
  relation: related_to
- node: '[[OAS]]'
  relation: related_to
- node: '[[MSR]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

Mortgage loans form one of the largest asset classes on bank balance sheets. In most markets they bear not only interest rate risk, but also convexity and prepayment (model) risk. [RAW-Elkenbracht-Huizing ch.9 p.1] The prepayment rate is a function of loan characteristics and economic variables such as interest rates and home prices, and determines the survival factor F_k — the probability that the loan still exists at month k — which scales the cashflow in each period. [RAW-Elkenbracht-Huizing ch.9 p.1]

## Four Types of Prepayment

Prepayment models differentiate between four types: [RAW-Elkenbracht-Huizing ch.9 p.2]

### 1. Turnover Prepayment

Occurs when a borrower prepays a mortgage due to relinquishing the property. Key drivers: [RAW-Elkenbracht-Huizing ch.9 p.2]

- **Ageing ramp:** it takes about **18–24 months** for turnover speeds to reach their normal level — approximately **0.7% per month** for 30Y Freddie Mac loans over 2000–2016.
- **Seasonality:** more people relocate in summer than winter.
- **Lock-in effect:** if mortgage rates are high, relocating increases the homeowner's borrowing costs, making them less likely to relocate.
- **Loan size:** smaller loans typically turn over faster (first-time buyers upgrading to a larger home).
- **Home prices / LTV:** in a strong housing market, borrowers are more likely to turn over to realise appreciation; in a weak market, high LTV constrains the ability to buy a new home.

### 2. Rate-Driven Refinancing

Triggered by borrowers refinancing to benefit from a lower market rate. The incentive (note rate − market rate) produces a **typical S-curve**: [RAW-Elkenbracht-Huizing ch.9 p.2]

- Prepayments increase fastest at an incentive of approximately **50bp**.
- Speed levels off when the advantage reaches approximately **150bp**.

Additional drivers: FICO score (lower FICO → harder to refinance), LTV (high LTV → constrained access), loan size (larger loans recapture refinancing costs at smaller incentive), **burnout** (borrowers who have not exercised past refinancing opportunities are assumed less likely to do so going forward), media effect, and state-level cost differences. [RAW-Elkenbracht-Huizing ch.9 p.2]

### 3. Cash-Out Refinancing

Driven by borrowers monetising home price appreciation by refinancing into a higher-balance mortgage. During the housing bubble approximately 90% of refinancing prepayments took out cash; this fell to 15% post-GFC and recovered to over 40% by end-2016. Often modelled jointly with turnover and rate-driven prepayments. [RAW-Elkenbracht-Huizing ch.9 p.3]

### 4. Default Prepayment

Occurs when the borrower defaults; the lender or guarantor may incur a loss depending on LTV at default. Functions of loan age, FICO score and LTV. Not covered in detail by this source (book focuses on interest rate risk). [RAW-Elkenbracht-Huizing ch.9 p.3]

## Valuation: OAS and Prepayment Models

To value mortgage products, the prepayment model is linked to an interest rate model (e.g., the LIBOR Market Model). The prepayment model functions as the payoff function of the interest rate instrument. Because prepayment models are typically path-dependent, Monte Carlo simulation is required. An **option-adjusted spread (OAS)** is added to the discount rate so that the model price matches observed market prices. [RAW-Elkenbracht-Huizing ch.9 p.3]

The practical implication of negative convexity: [RAW-Elkenbracht-Huizing ch.9 p.3]

- When rates **drop** → expected prepayment rates increase → mortgage duration shortens → in a hedged long-mortgage position, the hedger must buy back part of the hedge at a higher price → loss.
- When rates **rise** → prepayments slow → duration extends.

**MSRs** have highly leveraged negative durations: convexity is negative when rates are near or above the coupon, and positive when rates are low. Origination income is highly correlated with prepayment activity and can serve as a natural hedge to the mortgage-servicing asset — offsetting duration, convexity, and prepayment model error. [RAW-Elkenbracht-Huizing ch.9 p.3]

## ALM Balance-Sheet Integration

One approach for representing a mortgage position in a gap report: convert the **key-rate duration profile** of the position into a replicating partial differential hedge portfolio of zero-coupon bonds with the same KRD profile. [RAW-Elkenbracht-Huizing ch.9 p.4]

For earnings-at-risk, the largest risk in portfolios with significant negative convexity is **hedge rebalancing costs** that occur over time. This requires modelling the dynamic adjustment of hedges as the scenario progresses — including rebalancing of options hedging convexity or simulation of dynamic delta hedging. P&L from delta hedging depends on the relation between realised and implied volatility. [RAW-Elkenbracht-Huizing ch.9 p.4]

## Stochastic EaR vs. Static Gap

Historical data (25 years to 2017) shows average realised swaption volatility (3M×10Y) of approximately 5.8bp/day vs. 6.45bp implied — suggesting a risk premium on implied volatility. However, in adverse markets dynamic delta hedging can trigger large losses. [RAW-Elkenbracht-Huizing ch.9 p.4]

Regulatory stress scenarios (e.g., 2017 CCAR severe adverse) often assume realised volatility no higher than 4.9bp/day — **understating** delta hedging costs. The recommended approach for instruments with embedded options is **stochastic earnings-at-risk**: simulate a large number of scenarios with realistic realised volatility levels, then examine the distribution of earnings rather than a difference between two low-volatility scenarios. [RAW-Elkenbracht-Huizing ch.9 p.4]
