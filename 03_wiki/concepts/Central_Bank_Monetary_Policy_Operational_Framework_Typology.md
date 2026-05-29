---
node_id: central_bank_monetary_policy_operational_framework_typology_001
type: framework
title: Central Bank Monetary Policy Operational Framework Typology
aliases:
- CB Operational Framework Typology
- Corridor vs Floor System
- Standing Facility Framework
- Full Allotment System
- Phân loại khung vận hành NHTW
- Khung lãi suất hành lang
domain:
  primary: monetary_policy
tags:
- monetary_policy
- corridor
- floor_system
- standing_facility
- full_allotment
- fed
- ecb
- bindseil
confidence: 4
stability: evolving
thesis: 'Central bank monetary policy operations can be classified into three archetypes
  by how they control the short-term interest rate: (1) one-directional standing facility
  with daily OMOs, (2) symmetric corridor with CB-determined OMO volume, and (3) full-allotment
  lending within a standing-facility corridor; the choice determines whether reserves
  are scarce, ample, or excess, and how the interbank market functions.'
source_refs:
- path: 02_sources/books/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md
  pages: Ch. 1, 4, 6
  weight: primary
parent_node: null
related:
- node: '[[Monetary Policy Instruments Operational Framework]]'
  relation: shared_tag:corridor
- node: '[[Interest Rate Corridor Floor System Standing Facilities]]'
  relation: shared_tag:corridor
- node: '[[ECB New Operational Framework 2024]]'
  relation: shared_tag:floor_system
- node: '[[Fed Ample Reserves Range Floor Framework]]'
  relation: shared_tag:floor_system
- node: '[[Fed Policy Rate Shift EFFR to Secured Rate TGCR]]'
  relation: shared_tag:floor_system
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
Bindseil (2014) classifies central bank monetary policy implementation frameworks by their approach to interest rate control. The key variables are: (1) reserve scarcity/abundance; (2) whether banks use standing facilities; (3) the role of open market operations [RAW-CLIP].

## The Three Archetypes

### Type 1: One-Directional Standing Facility (Pre-20th Century)
- **Only a lending facility** (no deposit facility)
- Central bank provides credit at the Lombard/discount rate
- Banks borrow from CB to cover reserve shortfalls; no floor for excess reserves
- Overnight rate moves between 0 (floor = no deposit rate) and Lombard rate (ceiling)
- Examples: German Reichsbank pre-WWI; early US Fed discount window [RAW-CLIP]

### Type 2: Symmetric Corridor with OMO Volume Set by CB (Pre-GFC standard)
- **Two-sided corridor**: lending rate (ceiling) + deposit rate (floor)
- CB estimates reserve demand and sets OMO volume to keep system near zero excess
- Overnight rate trades near midpoint of corridor
- Interbank market (fed funds, EONIA) active and liquid — banks actively lend/borrow excess reserves
- Examples: ECB pre-2008, Bank of England pre-2008, pre-GFC Fed [RAW-CLIP]

### Type 3: Full Allotment / Floor System (Post-GFC)
- CB offers unlimited credit at fixed rate (full allotment tender) OR creates excess reserves via QE
- Excess reserves flood system → overnight rate falls to deposit facility rate (floor)
- Interbank market withers — no incentive to lend to peers when CB deposit available
- Two variants:
  - **Full allotment** (ECB 2008+): banks borrow as much as they want at policy rate
  - **Ample reserves** (Fed 2008+): excess reserves created by QE; floor = IORB [RAW-CLIP]

## The Separation Principle
In normal times, monetary policy has a **Sollbruchstelle** (predetermined breaking point):
1. **Economics dept:** Identifies optimal interest rate target via transmission mechanism analysis
2. **Markets dept:** Implements that rate through OMOs + standing facilities

This separation **breaks down in crises**: when transmission is impaired (e.g., interbank market seizes), controlling the short-term rate is insufficient — CB must directly intervene in credit markets, credit spreads, term rates [RAW-CLIP].

## Choosing the Framework
| Framework | Reserve Level | Interbank Activity | CB Footprint |
|-----------|-------------|------------------|-------------|
| Type 1 (one-directional) | Scarce | High (no floor) | Minimal |
| Type 2 (symmetric corridor) | Near-zero excess | High | Minimal |
| Type 3 (floor/full allotment) | Excess | Low | Large |

The choice of framework determines the CB balance sheet size — a Type 3 system structurally requires a large balance sheet. This is the core tension in the **CB Balance Sheet Trilemma** [LLM].

## Reserve Requirements in Framework Design
Reserve requirements (RR) serve multiple functions:
1. **Buffer**: average RR over maintenance period smooths overnight rate volatility
2. **Structural deficit**: if RR > autonomous factors creating liquidity, banks must borrow from CB (maintaining interbank market)
3. **Signal**: changes in RR signal policy stance (historical use)

ECB: 1% of non-bank liabilities <2yr maturity, averaged over ~1-month maintenance period [RAW-CLIP].


