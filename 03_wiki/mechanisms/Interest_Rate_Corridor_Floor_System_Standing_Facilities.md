---
node_id: interest_rate_corridor_floor_system_standing_facilities_001
type: mechanism
title: Interest Rate Corridor Floor System Standing Facilities
aliases:
- interest rate corridor
- floor system
- corridor approach
- standing facilities
- he thong hanh lang lai suat
- he thong san lai suat
- IORB
- deposit facility
domain:
  primary: monetary_policy
tags:
- corridor
- floor-system
- standing-facilities
- omo
- overnight-rate
- iorb
- dfr
confidence: 4
stability: evolving
thesis: The interest rate corridor brackets overnight interbank rates between a CB
  lending facility (ceiling) and deposit facility (floor). In normal times, OMOs keep
  rates near the midpoint; in excess-reserve environments (post-QE), the system degenerates
  into a floor system where the overnight rate equals the deposit facility rate and
  is controlled via that rate, not reserve quantity.
source_refs:
- path: 02_sources/books/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md
  pages: Ch4-6, Bindseil 2014
  weight: primary
related: []
date_created: '2026-05-20'
date_updated: '2026-05-20'
---

The interest rate corridor is defined by two standing facilities that bracket overnight interbank rates.

**Corridor structure:**
- Upper bound: Marginal Lending Facility rate (penalty for overnight borrowing from CB)
- Lower bound: Deposit Facility rate (remuneration for excess reserves parked at CB)
- Overnight rate oscillates within this corridor; OMOs target the midpoint or a specific level

**Three implementation approaches (Bindseil Ch4):**

1. **One-directional standing facility:** Only a borrowing facility, no deposit facility. CB provides liquidity via OMOs; overnight rate forms between zero and the lending rate. Pre-crisis ECB/Fed approach before deposit facilities were fully utilized.

2. **Symmetric corridor (classic):** OMOs calibrated so banking sector neither borrows from lending facility nor deposits at deposit facility on average. Rate targets midpoint. Requires accurate forecasting of autonomous factors (banknotes, TGA equivalent). Used by ECB pre-2008.

3. **Full allotment within corridor:** CB provides all demanded liquidity at fixed rate; excess goes to deposit facility. System becomes a floor system when deposit rate = target rate. Post-2008 reality for most major CBs.

**Corridor width optimization:**
Wider corridor -> more rate volatility within period -> greater penalty for forecast errors
Narrower corridor -> less incentive for interbank trading (banks bypass each other, go straight to CB)
Optimal width balances volatility absorption vs. interbank market function (typically 25-100bps historically)

**Martingale property:** In a reserve-averaging system, overnight rates follow a martingale within the maintenance period. Banks have incentive to front-load if they expect rate rises, creating end-of-period spikes unless the CB intervenes.

**Floor system evolution:** When reserves are ample (post-QE), the overnight rate gravitates to the deposit facility rate. The corridor becomes a floor. CB controls rate via deposit rate, not OMO quantity. This is the dominant implementation framework post-2008 for Fed (IORB), ECB (DFR), BOE (Bank Rate on reserves).

