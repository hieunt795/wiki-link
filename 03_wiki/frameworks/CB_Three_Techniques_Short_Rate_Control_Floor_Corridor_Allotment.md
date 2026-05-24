---
node_id: cb_three_techniques_rate_control_001
type: framework
title: CB Three Techniques Short Rate Control Floor Corridor Full Allotment
aliases:
- floor system monetary policy
- corridor system monetary policy
- full allotment system
- rate control techniques central bank
- separation principle monetary policy
- standing facility corridor
- ba kỹ thuật điều tiết lãi suất ngắn hạn
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- central_bank
- monetary_policy_implementation
- standing_facilities
- corridor_system
- floor_system
- omo
- reserves
- interbank_market
confidence: 4
stability: stable
thesis: "Bindseil (2014) identifies three fundamental techniques for a central bank to control the short-term interbank overnight rate: (1) one-directional standing facility (floor or ceiling system — banks systematically use one facility, which anchors market rates); (2) symmetric corridor with OMO volume set by CB (two-sided standing facilities equidistant from target, with market rate floating to target if net reserves balanced); (3) full allotment OMO within corridor (banks choose quantity demanded at a fixed rate, which anchors the market rate). These are the only three logically distinct approaches; all real-world implementations are combinations or variants. The 'separation principle' — that macroeconomic rate-setting and day-to-day implementation are fully separable — breaks down in crisis."
source_refs:
- path: 02_sources/books/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md
  pages: "lines 922-1270 (Chapters 4 and 6: Three Techniques + Corridor Width)"
  weight: primary
related:
- node: '[[Fed Balance Sheet Floor Payment System Reserve Demand]]'
  relation: applies_framework
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: related_mechanism
- node: '[[CB Reserve Requirements Taxonomy Surplus Shortage Liquidity Framework]]'
  relation: companion
- node: '[[Fed Reserve Demand Reduction Four Policy Tools]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## The Separation Principle (Normal Times)

In normal times, monetary policy has a "separation principle" (Sollbruchstelle — predetermined breaking point):
- **Economics department**: Determines optimal short-term rate target from macroeconomic model (transmission mechanism → ultimate objectives)
- **Markets department**: Implements the rate target through market operations daily

This dichotomy means implementation experts don't need to understand macro strategy and vice versa. The transmission mechanism is assumed to work reliably through interest rates; as long as the short-term rate is controlled, the exact mechanism doesn't matter. [RAW-CLIP]

**Breakdown in crisis**: When arbitrage relationships between financial instruments break down and funding constraints become pervasive, the short-term rate alone is insufficient as an operational target → CB must give guidance on multiple target variables; implementation directly affects monetary stance. [RAW-CLIP]

## The Three Instruments

Central banks use three main monetary policy instruments:
1. **Open market operations (OMO)**: CB-initiated transactions — outright purchases/sales, or collateralized credit operations (repos/reverse repos). [RAW-CLIP]
2. **Standing facilities**: Bank-initiated operations, with CB commitment to transact under specified conditions. Three types: (i) discount facility (outright sale of bills at discount rate — now obsolete), (ii) borrowing/Lombard facility (overnight/short-term collateralized borrowing from CB at penalty rate), (iii) deposit facility (overnight deposit with CB at below-market rate). [RAW-CLIP]
3. **Reserve requirements**: Minimum sight deposits banks must hold at CB (measured end-of-day; may be averaged over maintenance period). [RAW-CLIP]

## Technique 1 — One-Directional Standing Facility (Floor or Ceiling System)

**Mechanism**: Banking system is kept systematically in structural surplus (floor system) or deficit (ceiling system) of reserves relative to requirements, so banks systematically use one standing facility. That facility's rate = market rate by arbitrage.

**Ceiling variant (19th-century discount window era, ECB pre-2008)**: CB keeps banking system in structural deficit → banks always borrow at borrowing facility rate → overnight rate ≤ borrowing facility rate (can't be higher — cheaper to use facility) and ≥ facility rate (lenders won't accept less than the facility rate available to all). [RAW-CLIP]

**Floor variant (Fed/BoE post-QE with IORB)**: CB keeps banking system in structural surplus of reserves (via QE outright purchases) → banks always deposit at deposit facility → overnight rate ≥ deposit facility rate (no one lends below the available deposit return) and ≤ facility rate (borrowers prefer facility to higher interbank rates). [RAW-CLIP]

Examples:
- German Reichsbank 1900: Discount facility dominant; discount rate = market rate; Lombard at +100bps
- Fed January 2013: Outright holdings $2,670B; excess reserves $1,509B; IOER = effective floor at 25bps [RAW-CLIP]

**Key property**: Rate changes require changing only the standing facility rate — no recalibration of OMO volumes needed.

## Technique 2 — Symmetric Corridor with CB-Determined OMO Volume

**Mechanism**: CB offers both borrowing facility (rate iB) and deposit facility (rate iD), set symmetrically around target: i* = (iB + iD) / 2. CB sets OMO volume such that expected end-of-day reserves = required reserves → equal probability of system being short or long. [RAW-CLIP]

**Rate determination**: Market rate = weighted average of two facility rates, weights = P(system short) and P(system long). If CB perfectly calibrates liquidity (equal probability), market rate = middle of corridor = i*. [RAW-CLIP]

**Rate changes**: Implemented by shifting the entire corridor [iD, iB] up or down (keeping width fixed) without changing OMO volume. [RAW-CLIP]

Examples:
- BoE pre-2008: Bank Rate ± 25bps corridor; current accounts of banks ≈ required reserves; near-zero standing facility use
- Eurosystem pre-2008: Main refi rate ± 100bps corridor; structural reliance on weekly MROs; near-zero standing facility use [RAW-CLIP]

**Interbank market**: Arbitrage ensures interbank is active — banks prefer to trade with each other at a rate better than the standing facility rates. Corridor width determines intensity of interbank activity: wider = more interbank trading, more price discovery; narrower = CB takes over intermediation.

## Technique 3 — Full Allotment OMO within Corridor

**Mechanism**: CB offers credit OMO at fixed rate iOMO within the corridor, with full allotment — banks receive whatever they bid. Banks bid to ensure post-allotment expected overnight rate = iOMO. [RAW-CLIP]

**Result**: Equivalent to technique 2 mathematically (expected rate = iOMO), but quantity is bank-chosen rather than CB-chosen. Key difference: information asymmetries (banks forecast own liquidity needs better; CB forecasts aggregate autonomous factors better) and bid aggregation noise create additional randomness in aggregate volume. [RAW-CLIP]

**Crisis application**: ECB moved to full allotment in October 2008. During crisis, banks bid in excess of the neutral equilibrium quantity → excess reserves accumulated → post-allotment market rates fell well below iOMO (floor regime emerges within a corridor framework). [RAW-CLIP]

Examples: Danmarks Nationalbank, Suomen Pankki (pre-2008); ECB (post-Oct 2008).

## Corridor Width — Trade-offs

| Corridor Width | Rate Volatility | Interbank Market | CB Risk-Taking |
|---------------|-----------------|------------------|----------------|
| Narrow (< 25bps) | Very low | Thin (little incentive) | High (CB absorbs idiosyncratic bank shocks) |
| Moderate (25-50bps) | Low | Active (margin to trade) | Moderate |
| Wide (100-150bps) | Higher | Very active | Low |

Key trade-off (Bank of Canada 1995): Wide enough to incentivize interbank trading (banks should always find better rates in market than standing facilities), but narrow enough to contain rate volatility. [RAW-CLIP]

Additional consideration (Hoerova-Monnet 2010): Interbank market provides ex ante incentives for sound bank management — bilateral interaction requires each borrower to signal creditworthiness. Setting corridor too narrow → CB replaces market discipline. [RAW-CLIP]

## Martingale Property of Overnight Rates

Within a reserve maintenance period, overnight rates must satisfy a martingale property: E(i_t+1 | I_t) = i_t — the expected future overnight rate equals the current overnight rate, given current information. [RAW-CLIP]

**Logic**: If i_t > E(i_t+1), all banks would borrow now and lend later → current rate falls → martingale restored. Averaging over maintenance period is the precondition for this property (allows inter-temporal arbitrage of reserve fulfilment across days). [RAW-CLIP]

**Practical deviations**: End-of-maintenance-period volatility spike; no-overdraft constraint creates asymmetric backloading pressure; transaction costs limit intra-day interbank arbitrage. [RAW-CLIP]
