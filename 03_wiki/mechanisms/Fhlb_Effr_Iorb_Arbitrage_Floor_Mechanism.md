---
node_id: fhlb_effr_iorb_arbitrage_floor_mechanism_001
type: mechanism
title: FHLB EFFR IORB Arbitrage Floor Mechanism
aliases:
- FHLB arbitrage
- EFFR floor mechanism
- co che san EFFR
- Fed Funds arbitrage IORB
domain:
  primary: monetary_policy
tags:
- fed
- effr
- iorb
- fhlb
- floor_system
- reserve_scarcity
- sofr
- money_market
confidence: 1
stability: evolving
thesis: 'The Federal Funds rate (EFFR) is maintained near the IORB floor primarily
  through FHLB arbitrage: FHLBs, ineligible for IORB, lend reserves to banks at EFFR
  (slightly below IORB), which deposit at the Fed for a spread; this creates a soft
  floor on EFFR and means SOFR rising above IORB is the key leading indicator that
  reserve scarcity is transitioning from ample to binding.'
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: ''
  weight: primary
related:
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## FHLB Arbitrage (Floor Maintenance Mechanism)
[LLM] Core mechanism keeping EFFR pinned at/near IORB floor:
- FHLBs (Federal Home Loan Banks) cannot earn IORB (not eligible as reserve-holders)
- FHLBs lend Fed Funds to banks at EFFR (slightly below IORB)
- Banks borrow at EFFR -> deposit at Fed at IORB -> earn the spread
- This arbitrage is the primary driver of Fed Funds volume; genuine interbank need is minimal
- When FHLBs pull back (e.g., to fund advances or chase repo yield), EFFR can drift up by 1-5bps

## Rate Hierarchy in Floor System (normal ample reserves)
[LLM] Expected order: ONRRP floor < EFFR < IORB (corridor top). When reserves are ample:
- SOFR (secured/repo) tends to trade below EFFR (unsecured) due to collateral support
- SOFR-EFFR spread (repo-interbank basis) is typically -5 to +5bps

## Reserve Scarcity Transition Signal
[LLM] When SOFR begins to rise above IORB:
- Signal: banks are deploying reserves into repo to capture spread -> reserve demand exceeding supply
- Arbitrage tug-of-war: SOFR > IORB -> banks sell reserves into repo -> IORB pulls SOFR back down
- Rates ascend together until 'breaking point' (equivalent of Sep 2019 repo spike)
- Conks uses SOFR-EFFR widening and ONRRP balance as leading scarcity indicators


