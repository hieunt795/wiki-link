---
node_id: fhlb_foreign_bank_iorb_arbitrage_001
type: mechanism
title: FHLB Foreign Bank EFFR IORB Arbitrage Fed Funds Market
aliases:
- FHLB IORB arbitrage
- foreign bank IORB-EFFR spread
- Fed Funds arbitrage trade
- giao dịch chênh lệch IORB-EFFR
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- fhlb
- iorb
- effr
- fed_funds
- foreign_banks
- arbitrage
- reserves
- interbank
confidence: 1
stability: stable
thesis: The U.S. Fed Funds market is now sustained almost entirely by a single arbitrage trade — Federal Home Loan Banks (FHLBs), which cannot earn IORB on reserves, lend reserves to foreign bank branches at EFFR; those foreign banks (exempt from U.S. regulatory costs) deposit the reserves at the Fed and earn the IORB-EFFR spread (~5-10bps), representing the last meaningful unsecured interbank lending activity in the post-Basel III system.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batches 36-38 (chars ~205000-225000)
  weight: primary
related:
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: context
- node: '[[Fed Policy Rate Shift EFFR To Secured Rate TGCR]]'
  relation: related_mechanism
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Mechanism

**Step 1 — FHLB issues agency discount notes:**
Federal Home Loan Banks (FHLBs) borrow from government MMFs by issuing short-term agency discount notes at a rate below EFFR.

**Step 2 — FHLB lends Fed Funds at EFFR:**
FHLBs use agency note proceeds to lend reserves (Fed Funds) to eligible borrowers — primarily foreign bank branches — at EFFR (e.g. 5.33%).

**Step 3 — Foreign banks earn IORB spread:**
Foreign bank NY branches borrow Fed Funds at EFFR and park them at the Fed, earning IORB (e.g. 5.40%).
Profit = IORB - EFFR ≈ 5-10bps. [RAW-CLIP]

## Why Only This Trade Survives

**FHLBs**: Government-sponsored enterprises with Fed master accounts, but not eligible to earn IORB on their reserve balances → must lend reserves to earn any return.

**Foreign banks**: Not subject to U.S. domestic bank regulations (e.g. FDIC insurance fees, GSIB surcharges) → can profit from the IORB-EFFR spread that U.S. domestic banks cannot efficiently arbitrage. [RAW-CLIP]

**U.S. domestic banks**: Subject to FDIC fees and GSIB surcharges that eliminate the economics of the arbitrage; have abundant reserves already → no incentive to participate in Fed Funds market.

## Structural Implication

The near-demise of the Fed Funds market means:
- EFFR is no longer a meaningful interbank lending rate — it primarily reflects this thin FHLB-foreign bank arbitrage
- Fed now sets policy via IORB (the risk-free rate for reserves), not by targeting EFFR through open market operations
- Volume: ~$100B/day Fed Funds vs. ~$1.1T/day SOFR — SOFR has become the operational monetary standard [RAW-CLIP]
