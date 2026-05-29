---
node_id: qt_reserve_drain_effectiveness_and_deposit_funding_condition_001
type: mechanism
title: QT Reserve Drain Effectiveness And Deposit Funding Condition
aliases:
- QT Transmission Conditions
- QT Deposit vs MMF Funding
- Reserve Drain Mechanics
- Cơ chế truyền dẫn QT
domain:
  primary: monetary_policy
tags:
- qt
- quantitative_tightening
- reserves
- mmf
- on_rrp
- deposits
- fed
confidence: 3
stability: evolving
thesis: Quantitative Tightening (QT) only reduces bank reserves and tightens credit
  conditions when it is funded by bank deposit outflows; when funded by MMF withdrawals
  from ON RRP, only the Fed's ON RRP liability shrinks while reserves are unchanged
  — making that QT phase financially neutral for banks.
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: Full document
  weight: primary
parent_node: null
related:
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:qt
- node: '[[Warsh Balance Sheet Stimulus Swap]]'
  relation: shared_tag:qt
- node: '[[Quantitative Tightening QT Balance Sheet Runoff]]'
  relation: shared_tag:qt
- node: '[[Reserve Floor — Payment System Demand and the Minimum Ample Level]]'
  relation: shared_tag:qt
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:reserves
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## The Core Asymmetry
QT (Fed lets maturing securities roll off without reinvestment) causes the Fed's balance sheet to shrink, but the transmission to bank credit depends entirely on *who* was holding the cash that funded the maturing Treasury:

### Case 1: Bank-Deposit Funded QT (Effective Tightening)
```
Treasury matures → Fed receives $ from bank → Bank reserve at Fed ↓
Bank must shrink assets or seek wholesale funding → Credit conditions tighten
```
Reserves shrink → banks feel balance sheet pressure → effective monetary tightening [RAW-CLIP].

### Case 2: MMF-Funded QT (Neutral for Banks)
```
Treasury matures → Fed receives $ from MMF via ON RRP withdrawal → ON RRP balance ↓
Bank reserves UNCHANGED → no credit tightening
```
Only the Fed's ON RRP liability shrinks, not reserves. Banks are unaffected [RAW-CLIP].

## Historical Pattern (2022-2024 QT)
The 2022-2024 QT episode proceeded in two phases:
1. **Phase 1 (2022-early 2023):** ON RRP balances high (~$2.5T). QT funded primarily by MMF ON RRP withdrawals. Banks barely affected — this was a "stealth QT" that drained Fed liabilities without touching bank reserves.
2. **Phase 2 (2023-2024):** ON RRP balances fell toward zero. QT began hitting bank reserves. Stress signals appeared (SOFR spikes, repo volatility). Fed slowed QT pace [LLM].

## Policy Implication
The Fed cannot distinguish ex ante how much of each $B in QT flows from deposits vs MMF. It must observe:
- ON RRP balance level (proxy for "buffer before reserves get hit")
- Repo market rates vs IORB spread (stress signal)
- Bank reserve level vs estimated LCLoR [RAW-CLIP]

This makes QT inherently uncertain in its transmission timing — a key argument for maintaining ample reserves framework rather than returning to pre-GFC scarcity.


