---
node_id: pboc_monetary_policy_framework_and_interest_rate_transmission_001
type: framework
title: PBOC Monetary Policy Framework And Interest Rate Transmission
aliases:
- PBOC Framework
- China MP Framework
- LPR Reform 2024
- Khung chính sách tiền tệ PBOC
- Tỷ lệ cơ sở cho vay Trung Quốc
domain:
  primary: monetary_policy
tags:
- pboc
- china
- monetary_policy_framework
- lpr
- mlf
- 7day_repo
- dr007
- slf
- rrr
- window_guidance
confidence: 3
stability: evolving
thesis: The PBOC operates a hybrid quantity-price framework where M2+TSF serve as
  intermediate targets, DR007 is the operational target, and the 7-day OMO reverse
  repo is the primary policy rate since July 2024 — supported by an asymmetric SLF/excess-reserve
  corridor, multiple structural facilities, and discretionary window guidance.
source_refs:
- path: 02_sources/academic/Guo_Chinas_Monetary_Policy_Framework_2025.md
  pages: Full document
  weight: primary
- path: 02_sources/Clipping/China's Monetary Policy Framework and Financial Market
    Transmission _ Bulletin.md
  pages: Full document
  weight: secondary
related:
- node: '[[PBOC RMB Fix Counter Cyclical Factor And FX Management]]'
  relation: shared_tag:pboc
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The People's Bank of China (PBOC) operates a **hybrid monetary policy framework** that combines quantity-based intermediate targets with price-based operational targets. Since 2024, China has accelerated the transition toward a price-based system, with the 7-day reverse repo (OMO) rate becoming the de-facto primary policy rate [RAW-CLIP].

## Intermediate Targets
- **M2 (broad money supply):** Traditional quantity anchor; still published but increasingly supplementary [RAW-CLIP].
- **Total Social Financing (TSF):** Broader credit aggregate capturing shadow banking flows; key indicator for overall credit conditions [RAW-CLIP].
- **DR007 (7-day interbank pledged repo rate):** The primary operational target — PBOC steers DR007 toward the OMO 7-day reverse repo rate [RAW-CLIP].

## Interest Rate Corridor
```
SLF Rate (Standing Lending Facility)     ← Ceiling (+100bps above 7-day repo)
          ↑
7-day OMO Reverse Repo Rate              ← Primary policy rate (main anchor)
          ↓
Excess Reserve Rate                      ← Floor (-145bps below 7-day repo)
```
The corridor width is asymmetric: ceiling is +100bps above, floor is approximately -145bps below the 7-day OMO rate [RAW-CLIP].

## Policy Rate Reform — July 2024
Prior to July 22, 2024, the Loan Prime Rate (LPR) was formally linked to the Medium-term Lending Facility (MLF) rate. The PBOC decoupled LPR from MLF and re-anchored it to the 7-day reverse repo rate [RAW-CLIP]. This change:
- Elevated the 7-day OMO rate as the single unambiguous primary policy rate
- Reduced MLF to a liquidity management tool rather than a rate signal
- Aligned China's framework more closely with international best practice [RAW-CLIP]

## Liquidity Facilities (Full Table)
| Facility | Tenor | Role |
|----------|-------|------|
| OMO (7-day reverse repo) | 7 days | Main operational tool; primary rate signal |
| SLF (Standing Lending Facility) | Overnight to 3M | Ceiling; emergency bilateral lending |
| MLF (Medium-term Lending Facility) | 1 year | Medium-term liquidity; no longer the LPR anchor |
| TMLF (Targeted MLF) | Up to 3 years | Structural support for SME/agricultural lending |
| PSL (Pledged Supplementary Lending) | 1-5 years | Infrastructure and policy bank support |
| TLF (Temporary Lending Facility) | Short-term | Crisis backstop |
| CRA (Cash Reserve Account) | Overnight | Daily liquidity management |
[RAW-CLIP]

## Reserve Requirement Ratio (RRR)
RRR peaked above 20% in 2011 and has been on a declining path since. PBOC uses RRR cuts as a structural liquidity injection tool, distinct from price-based rate signals [RAW-CLIP].

## Macroprudential Assessment (MPA) Framework
A quarterly scoring system for banks covering capital adequacy, leverage, liquidity, credit policy, and pricing behavior. MPA scores affect banks' access to PBOC facilities and can substitute for direct window guidance [RAW-CLIP].

## Window Guidance
PBOC routinely uses informal (non-binding but powerful) guidance to banks on credit targets, sector allocation, and FX positioning. Window guidance operates outside formal rate channels and is central to directed credit policy [RAW-CLIP].

## FX Management Tools
PBOC manages the CNY through:
1. **Daily Fixing:** CNY/USD central parity set each morning; spot rate may trade ±2% around fix [RAW-CLIP].
2. **Counter-Cyclical Factor (CCF):** Discretionary adjustment embedded in the daily fix formula to offset pro-cyclical market pressure [RAW-CLIP].
3. **FX Reserve Intervention:** Direct buying/selling of USD via reserves ($3.2T as of 2026) [RAW-CLIP].
4. **SOE Bank Agents:** State-owned banks act as FX settlement agents to manage flow without visible PBOC footprint [RAW-CLIP].

## Transmission Mechanism Constraints
Interest rate transmission from PBOC policy rate to bank lending rates is weak compared to advanced economies due to:
- Administered deposit rate floors limiting bank liability repricing
- Large share of fixed-rate lending contracts
- Dominance of state-owned banks reducing competitive pricing pressure
- Credit quota guidance overriding rate signals [RAW-CLIP]


