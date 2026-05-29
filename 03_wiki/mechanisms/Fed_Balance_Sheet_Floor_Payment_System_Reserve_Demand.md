---
node_id: fed_bs_floor_payment_system_001
type: mechanism
title: Fed Balance Sheet Floor Payment System Reserve Demand
aliases:
- Fed balance sheet floor
- payment system reserve floor
- reserve demand payment system
- September 2019 repo crunch
- Fedwire reserve constraint
- sàn bảng cân đối kế toán Fed
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- fed_balance_sheet
- reserves
- payment_system
- fedwire
- sofr
- iorb
- qt
- ample_reserves
- repo
confidence: 1
stability: stable
thesis: 'The U.S. payment system (Fedwire ~$7.3T/day) creates a structural floor on
  the size of the Fed''s balance sheet: large banks (GSIBs) are unwilling to use Fed
  liquidity facilities (daylight overdrafts, Discount Window, Standing Repo) due to
  regulatory stigma and post-GFC liquidity regulation self-sufficiency requirements,
  so they pre-load opening reserve balances instead; when QT reduces reserves below
  this floor, banks throttle outgoing payments, creating a self-fulfilling liquidity
  crunch with repo rates spiking far above IORB — as on September 17, 2019, when SOFR
  spiked 315bps above IORB.'
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: lines 1-320 (Sections I, II, III — Abstract through Searching for Ampleness)
  weight: primary
parent_node: null
related:
- node: '[[Fed Policy Rate Shift EFFR To Secured Rate TGCR]]'
  relation: extends
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: related_mechanism
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: context
- node: '[[Fed Balance Sheet Size And Policy Rate Independence]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Why the Fed's Balance Sheet Cannot Shrink Freely

Total reserve balances have grown ~300× from ~$10B (early 2007) to ~$3T (2026). Three structural drivers:

1. **GSIB daylight overdraft stigma**: Pre-GFC, top-10 banks averaged ~$120B/day daylight overdrafts. Post-GFC peak system-wide daylight overdrafts < $5B/day. Under Regulation YY, GSIBs must demonstrate self-sufficient intraday liquidity — drawing on Fed facilities signals failure to do so. [RAW-CLIP]

2. **IORB removes incentive to lend excess reserves**: Pre-GFC, banks actively lent excess reserves to avoid receiving zero. Now IORB remunerates reserves at near-market rates → holding reserves is attractive investment, reducing interbank reallocation. JPMorgan withdrew $350B from the Fed (2023-2025) to buy Treasuries when the yield curve steepened, illustrating reserves-as-investment. [RAW-CLIP]

3. **Higher frictional borrowing costs post-GFC**: FDIC fees up to 42bps + special 13bps assessment; GSIB surcharges; leverage capital requirements → arbitrage between IORB and repo rates is uneconomic for most banks. [RAW-CLIP]

## Payment Throttling → Self-Fulfilling Crunch

When reserves are insufficient, banks delay outgoing Fedwire payments (throttle) waiting for incoming payments first:
- Large bank's outgoing payments react to recent incoming payments (receipt-reactive behavior)
- Each bank waiting for others → coordination failure → gridlock
- Shadow price of reserve balances becomes high and volatile
- Money market rates spike far above IORB [RAW-CLIP]

**Key empirical fact**: A one-standard-deviation increase in trailing-average payment delay to dealer banks predicts a 7bps increase in SOFR-IORB. When dealer-bank opening balances are low, repo rates are elevated and can spike to hundreds of bps above IORB. [RAW-CLIP]

## September 17, 2019 — The Inflection Point

- System-wide reserves fell to $1.4T → record low
- SOFR spiked to 315bps above IORB (interdealer repo: ~1000bps above)
- Payment delays peaked at record highs
- GSIBs declined to arbitrage the spike via SRF — despite $50B takeup, rates stayed elevated
- Fed added $75B in reserves by October 7, 2019

Expected "smooth Poole curve" kink at reserve ampleness boundary did not materialize — the transition was a jump discontinuity, not a gradual slope. [RAW-CLIP]

## The EFFR vs SOFR Problem

- EFFR volume: ~$100B/day (mostly FHLB-foreign bank IORB arbitrage, ≈$2-3B true interbank)
- SOFR: ~$8.8T outstanding, ~$6T overnight — the operationally relevant market
- EFFR demand elasticity to reserve supply has remained near zero even during rate spikes
- Proposal (Logan and Schulhofer-Wohl 2025): TGCR may be more appropriate than EFFR as the FOMC's actual target rate [RAW-CLIP]

## Liquidity Regulation as Amplifier

Under Reg YY (Enhanced Prudential Standards for GSIBs):
- Comprehensive Liquidity Analysis and Review (CLAR) requires intraday self-sufficiency
- Resolution Liquidity Adequacy and Positioning (RLAP) adds failure-resolution intraday liquidity requirement
- Supervisors prefer reserves over T-bills for meeting LCR HQLA, even though they are formally equivalent — reserves can't fail to convert to cash; T-bills require a sale that may signal stress
- Jamie Dimon (JPM earnings 2019): opening balance goes from $120B to $60B intraday — CLAR requires it must never hit zero under stress; this is the "red line" [RAW-CLIP]

The combination of GSIB self-sufficiency mandates and IORB remuneration has created a structurally higher minimum balance sheet size than the pre-GFC payment system required. [LLM]
