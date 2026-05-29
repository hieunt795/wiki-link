---
node_id: ubr_hedge_fund_leverage_systemic_001
type: mechanism
title: Uncleared Bilateral Repo UBR Hedge Fund Leverage Systemic Risk
aliases:
- uncleared bilateral repo
- UBR repo
- shadow repo market
- hedge fund repo leverage
- repo thị trường bóng tối
domain:
  primary: financial_markets
tags:
- ubr
- repo
- hedge_fund
- leverage
- bilateral
- systemic_risk
- basis_trade
- nccbr
confidence: 1
stability: stable
thesis: Uncleared bilateral repo (UBR) is the most opaque segment of the U.S. repo
  market — where hedge funds borrow at 50:1+ leverage from dealer counterparties without
  central clearing or custody — executing basis trades and relative-value strategies;
  its $2T+ in outstanding transactions remained invisible to regulators until 2023,
  echoing the LTCM precedent (1998) where uncleared repo counterparty exposures nearly
  triggered a systemic meltdown.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batches 13-14 (chars ~100000-118000)
  weight: primary
parent_node: null
related:
- node: '[[Repo Market Clearing Segments FICC Triparty GCF DVP NCCBR]]'
  relation: extends
- node: '[[Sovereign Basis Trade Repo Leverage]]'
  relation: related_mechanism
- node: '[[NBFI Sovereign Market Supervisory Gap]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## What Is Uncleared Bilateral Repo (UBR)

UBR (also called NCCBR — Non-Centrally Cleared Bilateral Repo) is the bilateral segment of repo where:
- Two parties trade directly, without a central counterparty (CCP) like FICC
- No custodian (like BNY Mellon in triparty)
- Trades are anonymous — no central reporting; counterparties have no visibility into each other's full book [RAW-CLIP]

**Users**: Primarily hedge funds borrowing from primary dealers to fund leveraged strategies (50:1 or higher leverage ratios).

**Strategies funded**: 
1. On-the-run vs off-the-run Treasury relative value
2. Treasury cash-futures basis trade (long UST cash, short futures, funded via repo)
3. Other fixed income relative value arbitrage [RAW-CLIP]

## The LTCM Precedent (1998)

Long-Term Capital Management (LTCM) built massive counterparty exposures in uncleared bilateral repo with ~75 different counterparties:
- Each counterparty saw only its own exposure to LTCM, not the aggregate
- Total leverage and risk was invisible to regulators and market participants
- When LTCM's trades went wrong, Fed-orchestrated bailout was needed to prevent daisy-chain collapse [RAW-CLIP]

## 2023 Data Pilot: OFR Reveals the Scale

U.S. Treasury's Office of Financial Research (OFR) released the first data pilot on UBR in 2023:
- Revealed $2T+ in outstanding UBR transactions in the shadows
- Highlighted the leverage community (hedge funds) operating in regulatory darkness [RAW-CLIP]

## Why This Is Structurally Dangerous

When UBR leverage unwinds (as in March 2020 Treasury market dysfunction):
1. Hedge funds forced to sell USTs rapidly to meet margin calls
2. Dealers cannot absorb the selling pressure (balance sheet constraints)
3. UST market liquidity collapses → price discovery breaks
4. Fed must intervene with emergency QE or repo operations [RAW-CLIP]

## Reform Path: Mandatory Central Clearing

Post-2023, SEC proposed mandatory clearing for Treasury repos — pushing UBR into FICC-cleared structures to eliminate the opacity and allow bilateral exposure netting. Implementation timeline extends to 2025-2026. [LLM]
