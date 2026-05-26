---
node_id: non_maturity_deposit_fair_margin_and_replicating_portfolio_001
type: mechanism
title: Non Maturity Deposit Fair Margin And Replicating Portfolio
aliases:
- NMD Fair Margin
- NMD Replicating Portfolio
- Biên lãi ròng tiền gửi không kỳ hạn
- Non-Maturity Deposit Hedging
domain:
  primary: alm
tags:
- alm
- non_maturity_deposits
- fair_margin
- replicating_portfolio
- banking_book
- hedge
confidence: 3
stability: evolving
thesis: 'Non-maturing deposits (NMDs) — accounts where clients can withdraw or deposit
  at any time and the bank can change the rate — are modeled via a ''fair margin''
  concept: the margin is the NPV-zero increase in the client coupon, and a dynamic
  investment strategy hedges this margin against interest rate movements, replacing
  the static replicating portfolio approach.'
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Chapter 7
  weight: primary
related:
  - node: "[[Irrbb_Eve_Nii_Dual_Metric_Framework]]"
    relation: eve_measurement_context
  - node: "[[Bcbs_Irrbb_Nmd_Standardised_Framework]]"
    relation: regulatory_framework
  - node: "[[Behavioralization_Non_Maturity_Deposit_Alm_Prepayment_Early_Withdrawal_Modeling]]"
    relation: behavioral_input
  - node: "[[Non_Maturity_Deposit_And_Revolving_Facility_Behavioral_Assumptions_Alco_Governance]]"
    relation: governance_link
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## The NMD Problem
Non-maturing deposits (NMDs) are structurally difficult to model for ALM because:
- The **client** can adjust notional at any time (withdrawal option).
- The **bank** can adjust the interest rate at any time (pricing option).
- No defined maturity date, no defined notional, no defined fixed rate [RAW-CLIP].

Some banks model NMDs as overnight — too conservative for liquidity risk and distorted for interest rate risk (if the bank pays more or less than overnight, a gain/loss still occurs even with "no risk" indicated) [RAW-CLIP].

## The Replicating Portfolio Model (Standard Approach)
The classical approach: maintain a fixed monthly investment rule (e.g., invest 30% in 3M, 30% in 1Y, 40% in 5Y bonds). The business margin = investment coupon minus client coupon [RAW-CLIP].

**Limitations:**
- Investment rule is static — does not adapt to current yield curve shape.
- Past-dependent: portfolio at any given time reflects the last 5 years of rates and volumes.
- Cannot accommodate pricing strategy changes cleanly [RAW-CLIP].

## The Fair Margin Concept (Elkenbracht-Huizing & Nauta, 2006/2017)
**Fair Margin definition:**
> The increase in client coupon (above the contractual client rate) that sets the **Net Present Value of NMDs = 0**.

Formally:
```
value(c(t) + margin) = 0
```
where `value(c(t))` is the present value of all projected NMD cashflows discounted at OIS rates, with client rate `c(t)` = f(market rate), and volume `V(t)` = f(growth model) [RAW-CLIP].

This is analogous to the "fair value" concept in derivatives pricing — a margin at which neither party subsidizes the other.

## Dynamic Hedge Strategy
**Method I (hedge total projected volume):**
1. Compute value sensitivities of NMDs (including fair margin) to yield curve.
2. Build an investment portfolio that exactly offsets these sensitivities in each rate bucket.
3. Monthly: roll the hedge, recalculate margin from accumulated P&L.
→ Result: highly stable margin; requires borrowing in short-term bucket; duration can be very long (10-20 years) [RAW-CLIP].

**Method II (hedge current volume only):**
- New volume treated as a fresh product hedged from inception.
- Less stable total margin, but each vintage of volume has its own very stable margin.
- Duration shorter (4-7 years); does not require net borrowing.
- More operationally tractable [RAW-CLIP].

## Practical Implications
- Both methods **significantly outperform** the replicating portfolio in falling rate environments [RAW-CLIP].
- The fair margin level is locked in at inception — starting in a low-rate environment locks in a low (but stable) margin. Banks can phase adoption over a business cycle to average [RAW-CLIP].
- The framework transfers interest rate risk from the NMD business unit to the ALM department via the fair margin; business earns margin deterministically [LLM].
- OIS curve is the proper discount curve for NMDs (overnight liquidity tenor).


