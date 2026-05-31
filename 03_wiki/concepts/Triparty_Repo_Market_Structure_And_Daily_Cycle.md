---
node_id: triparty_repo_market_structure_and_daily_cycle_001
type: concept
title: Triparty Repo Market Structure And Daily Cycle
aliases:
- Triparty Repo
- BNYM Custodian Repo
- NCCBR
- Non-Centrally Cleared Bilateral Repo
- Thị trường repo ba bên
domain:
  primary: monetary_policy
tags:
- repo
- triparty
- bnym
- nccbr
- on_rrp
- srf
- mmf
- plumbing
confidence: 3
stability: evolving
thesis: The US triparty repo market is a $4-5 trillion overnight funding market where
  BNYM acts as sole custodian/settlement agent; its daily operational cycle creates
  structural rate floors (ON RRP at 1pm) and ceilings (SRF at 1:30-1:45pm), while
  the opaque non-centrally-cleared bilateral repo (NCCBR) segment provides ~$2 trillion
  in hedge fund leverage outside regulatory visibility.
source_refs:
- path: 02_sources/books/conks/Conk - Repo.md
  pages: Full document
  weight: primary
parent_node: null
related:
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:repo
- node: '[[Collateral Velocity and Rehypothecation]]'
  relation: shared_tag:repo
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:repo
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:repo
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: shared_tag:repo
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
US repo markets split into three segments: (1) **triparty** (BNYM custodian, MMFs as cash providers, ~$4-5T); (2) **GCF (General Collateral Finance)** — cleared inter-dealer triparty; (3) **NCCBR** — bilateral, non-cleared, ~$2T, primarily hedge fund leverage [RAW-CLIP].

## Daily Operational Cycle (Triparty)
| Time | Event |
|------|-------|
| 7:00am | BNYM opens; collateral allocations begin |
| 8:00-9:00am | Peak settlement activity; rates discovered |
| 1:00pm | **ON RRP opens** — MMFs can park at Fed floor rate; sets floor for triparty GC rates |
| 1:30-1:45pm | **SRF window** — banks/dealers can borrow from Fed at ceiling rate |
| 3:30pm | BNYM net settlement; collateral returned to dealers |

This daily cycle means repo rates are effectively bounded: ON RRP sets the floor by providing an alternative to cash lenders; SRF sets the ceiling by providing an alternative to repo borrowers [RAW-CLIP].

## Key Participants
- **Cash Lenders:** Money Market Funds (primary), corporate treasuries, municipalities
- **Collateral Providers (Borrowers):** Primary dealers, banks, GSEs
- **Custodian/Settlement:** BNYM (sole provider — single point of failure risk)
- **NCCBR Borrowers:** Hedge funds (levering Treasury positions, basis trades)

## NCCBR — The Opaque Segment
NCCBR (~$2T) operates bilaterally between prime brokers and hedge funds. Key features:
- Not centrally cleared → no CCP netting, full bilateral exposure
- Not reported in real-time to DTCC → regulatory blind spot
- Primary vehicle for **Treasury basis trade leverage** (buy cash bond, short futures)
- When basis trade unwinds (as in March 2020 and April 2025), repo demand spikes, potentially stressing BNYM settlement [LLM]

## Interconnection With ON RRP and SRF
The Fed's ON RRP and SRF instruments work *through* the triparty infrastructure: ON RRP drains excess cash from MMFs into Fed liabilities (reducing triparty repo supply); SRF injects liquidity to dealers when triparty rates spike above SRF rate [RAW-CLIP].


