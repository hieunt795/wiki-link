---
node_id: pboc_rmb_fix_counter_cyclical_factor_and_fx_management_001
type: concept
title: PBOC RMB Fix Counter Cyclical Factor And FX Management
aliases:
- CNY Daily Fix Mechanism
- CCF Counter-Cyclical Factor
- RMB Management Framework
- PBOC FX Intervention
- Cơ chế tỷ giá tham chiếu hàng ngày
- Hệ số chống chu kỳ CCF
domain:
  primary: monetary_policy
tags:
- pboc
- china
- rmb
- cny
- ccf
- daily_fix
- fx_intervention
- cfets
- bbop
- crawling_peg
confidence: 3
stability: evolving
thesis: The PBOC manages CNY via a daily central parity fix with ±2% band, augmented
  by a discretionary Counter-Cyclical Factor (CCF) embedded in the fix formula; since
  late 2023, conservative CCF settings have made the fix behave like a crawling peg,
  creating a positive CFETS-USDCNY correlation that signals PBOC is suppressing automatic
  stabilizer effects.
source_refs:
- path: 02_sources/Clipping/RMB (part 2)_ PBOC unlikely to allow RMB to appreciate
    sharply under continued conservative FX management approach.md
  pages: Full document
  weight: primary
- path: 02_sources/Clipping/RMB (part 1)_ Fundamentals point to appreciation in 2026
    but milder than last year.md
  pages: Full document
  weight: secondary
- path: 02_sources/Clipping/PBOC heavy dollar buying in April after significant dollar
    selling in March.md
  pages: Full document
  weight: contextual
parent_node: null
related:
- node: '[[PBOC Monetary Policy Framework And Interest Rate Transmission]]'
  relation: shared_tag:pboc
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The PBOC manages the CNY/USD exchange rate through a **daily central parity fixing** system with a ±2% intraday band, augmented by discretionary tools including the Counter-Cyclical Factor (CCF), FX reserve intervention, and SOE bank agents. Since late 2023 (Pan Gongsheng era), PBOC has adopted a more **conservative, symmetry-breaking** approach that deliberately weakens automatic stabilizer effects [RAW-CLIP].

## The Daily Fix Formula
The CNY daily fixing (central parity) is set each morning using three components:
```
Slope of USDCNY fixing = (spot deviation from previous fixing)
                        + (overnight USD move vs basket)
                        + CCF (Counter-Cyclical Factor, discretionary)
```
The CCF is the only discretionary component — it can amplify, dampen, or reverse the market-implied move [RAW-CLIP].

## Counter-Cyclical Factor (CCF) Mechanics
- **Purpose:** Offset herding/pro-cyclical market pressure. When the market pushes CNY too far in one direction, CCF adds a correction [RAW-CLIP].
- **Formula is unpublished** — only CFETS member banks know the CCF formula in full. PBOC announces only the coefficient weighting [RAW-CLIP].
- **Since late 2023 (Pan Gongsheng):** CCF has been set conservatively, meaning the daily fix acts more like a **crawling peg** than a flexible rate. PBOC deliberately keeps the fix close to the previous day's level regardless of market signals [RAW-CLIP].

## BBOP Model (Fundamental RMB Anchor)
The Balance of Payments Outlook (BBOP) model estimates CNY fair value from:
```
BBOP = Current Account (CA) + Foreign Direct Investment (FDI) + Portfolio Flows
```
**2025 example:** CA surplus ~$700bn; portfolio outflow ~$300bn → BBOP ≈ $104bn (net positive, supportive of CNY) [RAW-CLIP].

Key finding: **Valuation (REER) is a poor short-term predictor** of CNY moves. BBOP is a better structural anchor for medium-term direction [RAW-CLIP].

## CFETS Basket Correlation (Post-2023 Signal)
Since late 2023, the CFETS basket (CNY vs 24-currency basket) has shown a **positive correlation with USDCNY** — meaning:
- When CNY strengthens vs USD → CNY weakens vs basket
- When CNY weakens vs USD → CNY strengthens vs basket

This is the **opposite of pre-2023 behavior** and signals that PBOC is managing the dollar rate directly (via conservative CCF) rather than letting the basket serve as an automatic stabilizer [RAW-CLIP].

## FX Intervention Toolkit
| Tool | Mechanism | Visibility |
|------|-----------|------------|
| CCF adjustment | Daily fix formula component | Low (unpublished formula) |
| FX Reserve Buy/Sell | Direct USD purchase or sale from $3.2T reserves | Medium (reported monthly, lag) |
| SOE Bank Agents | State banks instructed to buy/sell FX on behalf of PBOC | Low (no direct attribution) |
| Window guidance | Informal instructions to banks on FX settlement behavior | Very low |
[RAW-CLIP]

## FX Reserve Dynamics (2026 Context)
- **March 2026:** PBOC sold ~$64bn in FX reserves (largest recent sell episode) — resisting CNY depreciation pressure [RAW-CLIP].
- **April 2026:** PBOC bought ~$51bn (largest recent buy episode) — absorbing USD inflows, preventing CNY appreciation [RAW-CLIP].
- CCF was heavily engaged in April 2026, keeping the fix below spot to slow appreciation [RAW-CLIP].
- Pattern confirms: **two-way conservative management** — PBOC resists both excessive depreciation AND excessive appreciation [LLM].

## Market FX Behavior Post-2018
- The CNY FX market has become counter-cyclical since the US-China trade war (2018): market participants anticipate PBOC resistance and trade against the trend [RAW-CLIP].
- This counter-cyclical market behavior **weakened in 2024** as uncertainty increased and participants reduced positioning [RAW-CLIP].
- PBOC is explicitly mindful of pro-cyclical herding risk and uses CCF to prevent self-reinforcing momentum [RAW-CLIP].


