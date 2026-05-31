---
node_id: fhlb_ibda_intraday_resolution_liquidity_001
type: concept
title: FHLB IBDA Intraday Resolution Liquidity and Fed Funds Market Survival
aliases:
- IBDA
- Interest-Bearing Deposit Account
- resolution liquidity
- intraday liquidity requirements
- G-SIB living wills
- FHLB as Fed Funds lender
- intraday HQLA buffer
- thanh khoản nội ngày
- tài khoản tiền gửi chịu lãi
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- FHLB
- IBDA
- fed-funds
- resolution-liquidity
- G-SIB
- living-wills
- intraday
- IORB
- money-market
- ample-reserves
confidence: 3
stability: evolving
thesis: 'Post-2017, the Fed''s G-SIB resolution liquidity requirements (from "living
  wills") created demand for around-the-clock HQLA buffers that overnight Fed Funds
  cannot satisfy. FHLBs — barred from earning IORB — filled this gap by supplying
  intraday reserves to G-SIBs via IBDAs (Interest-Bearing Deposit Accounts) at 5-10bps
  above the FOMC target range. This is why the Fed Funds market survived post-2008
  despite being nearly extinct — it evolved into an IBDA/intraday liquidity mechanism
  dominated by FHLB lending. FHLBs now constitute ~97% of all Fed Funds lending.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's Global Put Part I; The Fed's Global Put Part II
  weight: primary
parent_node: null
related:
- node: '[[EFFR_Effective_Federal_Funds_Rate]]'
  relation: rate_set_in_this_market
- node: '[[LCLoR_Lowest_Comfortable_Level_Of_Reserves_And_QT_Calibration]]'
  relation: IBDA_demand_grows_as_reserves_drain
- node: '[[Fed_Policy_Rate_Shift_EFFR_To_Secured_Rate_Tgcr]]'
  relation: why_EFFR_is_a_FHLB_artifact_not_genuine_interbank_market
- node: '[[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]]'
  relation: upstream_regulatory_driver_of_resolution_requirements
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## Why the Fed Funds Market Still Exists

Post-2008, unsecured interbank lending (Fed Funds) fell ~80%. With G-SIBs holding massive reserves from QE, there was no reason to borrow overnight in the traditional sense. Yet the Fed Funds market survived — just for a completely different reason.

By mid-2017, the Fed imposed **resolution liquidity requirements** on G-SIBs: not just end-of-day HQLA buffers (Basel III LCR) but **intraday and around-the-clock** HQLA coverage. This came from G-SIB "living wills" — mandatory resolution plans that G-SIBs must file with regulators, specifying how they could be wound down in failure. Every entity of a G-SIB had to maintain continuous HQLA buffer at all hours. [RAW-CLIP Conks Global Put II]

## The Problem with Overnight Fed Funds

Overnight (o/n) Fed Funds trades have a timing gap: the lender (FHLB) returns funds to the borrower (G-SIB) for a few hours in the early morning before renewing the trade. During that window, the G-SIB's intraday buffer drops. This **fails to satisfy round-the-clock resolution liquidity requirements**.

## IBDAs (Interest-Bearing Deposit Accounts) — The Solution

FHLBs, seeking to solve G-SIBs' intraday problem while earning yield on their reserves:

```
FHLB opens an IBDA at the G-SIB's commercial bank
  → IBDA functions as a deposit account (not a renewed overnight loan)
  → Funds stay in the G-SIB's books 24/7 — no morning gap
  → G-SIB's resolution liquidity requirement satisfied at all times
  → FHLB earns IBDA rate = 5-10bps ABOVE the Fed's FOMC target range
```

**Why FHLBs supply this:** FHLBs cannot earn IORB (only depository banks earn IORB; FHLBs are GSEs). They must deploy reserves via lending. IBDAs pay 5-10bps above target range — significantly better than alternative investments for FHLBs.

**Why G-SIBs pay the premium:** Non-compliance with resolution liquidity carries reputational damage, forced suspension of capital distributions (dividends, buybacks), and regulator scrutiny. Paying 5-10bps premium is far cheaper than non-compliance. [RAW-CLIP Conks Global Put II]

## FHLB Dominance of the Fed Funds Market

| Participant | Role |
|------------|------|
| FHLBs | ~97% of all Fed Funds lending (primarily via IBDAs) |
| Foreign bank branches (FBOs) | EFFR arbitrage: borrow FF → earn IORB (no FDIC fee) |
| Small domestic banks | Acquire interbank liquidity for periodic reserve needs |
| G-SIBs | Borrowers — rarely lend; enter only for sudden regulatory shortfalls |

**FHLB-FBO EFFR arbitrage:** Foreign bank branches (FBOs) pay no FDIC insurance → earn IORB on deposited reserves → borrow FF from FHLBs at below-IORB rate → pocket spread. This arbitrage keeps EFFR slightly below IORB. [RAW-CLIP Conks Global Put I]

## IBDA Market Evolution

| Period | IBDA Volume | Driver |
|--------|-------------|--------|
| Pre-2017 | ~$0 | Living will requirements not yet binding |
| Late 2018 | ~$15B | G-SIB demand grew as Fed's first QT drained reserves |
| Post-COVID (2020) | ~$5B | QE flooded reserves → G-SIBs self-sufficient |
| QT2 (2022-2025) | All-time highs | Reserve drain → G-SIBs need IBDAs for intraday coverage |

As QT drains reserves, G-SIBs can no longer self-fund intraday requirements → IBDA demand surges. This is a direct transmission mechanism: Fed QT → lower reserves → higher IBDA demand → upward pressure on EFFR. [RAW-CLIP Conks Global Put II]

## FHFA Proposed Restrictions (Post-SVB)

Following the 2023 SVB crisis, the FHFA (FHLB's regulator) proposed reducing FHLB access to banks with weaker credit ratings and imposing lending limits in the regular Fed Funds market (not IBDA).

**Implication:** Fewer FHLB loans via overnight FF → fewer private dollar lenders of last resort at the top of the dollar rates hierarchy → more reliance on Fed swap lines. This is why swap line volume was expected to rise even outside stress periods, and why QT was expected to pause earlier than models suggested. [RAW-CLIP Conks Global Put II]

## Why This Matters for EFFR Targeting

EFFR (the Fed's policy target) is set primarily by:
1. FHLB → FBO arbitrage trades (FF borrowing below IORB)
2. FHLB → G-SIB IBDA trades (above IORB)
3. Small banks' periodic reserve needs

This means EFFR is **not** a genuine interbank borrowing rate — it is an artifact of GSE regulatory constraints (FHLBs can't earn IORB) and bank resolution requirements (IBDAs). This is the core argument for the Fed to shift its target to TGCR (a genuine secured market rate). [LLM synthesis from RAW-CLIP Conks New Target I & II]
