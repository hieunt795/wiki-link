---
node_id: fed_ample_reserves_rate_control_framework_001
type: mechanism
title: Fed Ample Reserves Rate Control Framework
aliases:
- Ample Reserves Framework
- Fed Rate Control Post-GFC
- IORB ON RRP SRF Corridor
- Khung kiểm soát lãi suất dự trữ dồi dào
domain:
  primary: monetary_policy
tags:
- fed
- iorb
- on_rrp
- srf
- ample_reserves
- rate_control
- qt
confidence: 3
stability: evolving
thesis: 'Post-GFC, the Fed shifted from scarce-reserve corridor to ample-reserve floor
  system: IORB sets the ceiling, ON RRP sets the floor, and SRF acts as a backstop
  ceiling, making fed funds rate control near-automatic without daily open market
  operations.'
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: Full document
  weight: primary
related:
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:fed
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The Federal Reserve operates two distinct reserve regimes: **pre-GFC scarce reserves** (Fed controlled FFR via daily OMOs) and **post-GFC ample reserves** (Fed uses administered rates to set a floor/ceiling corridor) [RAW-CLIP].

## The Three-Rate Corridor
- **IORB (Interest on Reserve Balances):** Paid to banks for every dollar of reserves; functions as the effective **ceiling** for secured overnight rates — no bank will lend below IORB when it earns that risk-free [RAW-CLIP].
- **ON RRP (Overnight Reverse Repo Facility):** Available to non-bank eligible counterparties (MMFs, GSEs, primary dealers); functions as the **floor** — cash can always earn ON RRP rate rather than lending below it [RAW-CLIP].
- **SRF (Standing Repo Facility):** Fed lends to banks and primary dealers at SRF rate against Treasury/agency collateral; functions as a **backstop ceiling** — no bank needs to borrow above SRF rate [RAW-CLIP].

## Pre-GFC vs Post-GFC Contrast
| Regime | Reserve Level | Rate Control Mechanism | Daily Ops |
|--------|--------------|----------------------|-----------|
| Pre-GFC | Scarce (~$10-15B) | Daily OMO to hit target | Required |
| Post-GFC | Ample ($3-6T peak) | Administered rates (IORB/ON RRP) | Not required |

The transition was forced by QE: excess reserves flooded the system, making the scarce-reserve corridor inoperable [RAW-CLIP].

## Quantitative Tightening (QT) Transmission
QT is only effective at tightening financial conditions when reserves drain from **bank deposits** (bank reserves shrink = credit capacity shrinks). When QT is funded by MMF withdrawals from ON RRP, only ON RRP balances shrink — reserves are unchanged and no tightening occurs [LLM].

## Key Calibration Issue
The Fed does not know the "lowest comfortable level of reserves" (LCLoR) ex ante. QT proceeds until repo/money market stress signals (e.g., Sept 2019 repo spike) indicate proximity to LCLoR. The SRF is designed to prevent a recurrence of that episode [RAW-CLIP].


