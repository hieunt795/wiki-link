---
node_id: indicator_iorb_001
type: indicator
title: IORB — Interest on Reserve Balances
aliases:
- IORB
- IOR
- IOER
- interest on excess reserves
- interest on reserves
- lãi suất dự trữ
domain:
  primary: monetary_policy
tags:
- interest-rate
- reserves
- fed-floor
- ample-reserves
- policy-rate
confidence: 3
stability: stable
indicator_type: monetary
frequency: daily (set by FOMC decision)
data_source: Federal Reserve Board — set at each FOMC meeting; effective next business
  day
interpretation: 'IORB is the floor for the federal funds rate in the ample reserves
  framework: no bank will lend reserves below the rate it earns by simply holding
  them at the Fed. When EFFR trades below IORB, it signals FHLB arbitrage (FHLBs can''t
  earn IORB but lend to banks above it). When market rates persistently approach or
  exceed IORB, reserve scarcity is emerging and the Fed should act.

  '
thesis: 'IORB is the interest rate the Federal Reserve pays on all reserve balances
  held by depository institutions, serving as the effective floor of the federal funds
  rate under the ample reserves operating framework. It replaced the distinction between
  required reserve interest (IOR) and excess reserve interest (IOER) in July 2021,
  when reserve requirements were set to zero. IORB is the primary lever the Fed uses
  to transmit the FOMC''s target range into overnight money markets.

  '
source_refs:
- path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
  weight: primary
- path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
  weight: supporting
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  weight: supporting
parent_node: null
related:
- node: '[[EFFR_Effective_Federal_Funds_Rate]]'
  relation: floors
- node: '[[Fed_Ample_Reserves_Range_Floor_Framework]]'
  relation: core_instrument_of
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: above
- node: '[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]'
  relation: defines_floor_of
- node: '[[Fhlb_Effr_Iorb_Arbitrage_Floor_Mechanism]]'
  relation: drives
- node: '[[Reserve_Floor_Payment_System_Demand]]'
  relation: related_to
- node: '[[Federal_Reserve]]'
  relation: set_by
date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

**Interest on Reserve Balances (IORB)** is the rate the Federal Reserve pays on overnight deposits held by depository institutions (banks, credit unions, thrifts). Set by the Board of Governors at each FOMC meeting, IORB is the primary floor mechanism of the ample reserves operating framework.

Prior to July 2021, the Fed paid different rates on required reserves (IOR) and excess reserves (IOER); since reserve requirements were zeroed in March 2020 and formally eliminated in July 2021, all reserve balances earn IORB.

## Floor Mechanism Logic

In the ample reserves framework, no bank should lend reserves in the fed funds market below IORB — lending at less than the risk-free deposit rate at the Fed is irrational. Therefore:

EFFR ≥ IORB in theory.

In practice, EFFR trades a few basis points **below** IORB due to FHLB arbitrage: Federal Home Loan Banks hold reserves at the Fed but do not earn IORB (they are non-depository institutions). FHLBs lend overnight to banks at IORB minus a spread. Banks accept because the transaction has zero balance-sheet cost (reserve-for-reserve swap). This FHLB–bank arbitrage is the mechanical reason EFFR reliably prints below IORB. See [[Fhlb_Effr_Iorb_Arbitrage_Floor_Mechanism]].

## IORB as Policy Transmission

The FOMC targets a 25bps range for EFFR. IORB is set at the **top of the target range** (or close to it). ON RRP is set 5–10bps below IORB, providing a sub-floor for money market funds. This creates:

```
ON RRP rate < SOFR ≈ EFFR < IORB ≈ top of target range < SRF rate
```

[RAW-CLIP ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER]

## Reserve Scarcity Signal

When the banking system transitions from ample to scarce reserves, EFFR begins drifting upward toward IORB — and eventually above IORB — because banks bid competitively for reserves they can no longer easily source. The Conks framework uses EFFR-IORB spread as a real-time scarcity monitor. [RAW-CLIP Conks Money Market Update]

## Current Level

As of April 2026, IORB stands at 3.75% (top of 3.50–3.75% target range). [RAW-CLIP CB Commentary April 2026]
