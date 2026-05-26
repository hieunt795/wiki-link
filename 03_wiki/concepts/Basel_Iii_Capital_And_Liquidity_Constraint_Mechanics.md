---
node_id: basel_iii_capital_and_liquidity_constraint_mechanics_001
type: framework
title: Basel III Capital And Liquidity Constraint Mechanics
aliases:
- Basel III Mechanics
- RWA Capital Requirements
- Output Floor Basel Endgame
- LCR NSFR Liquidity Rules
- Cơ chế vốn Basel III
- Sàn đầu ra Basel
domain:
  primary: basel_risk
tags:
- basel
- rwa
- output_floor
- lcr
- nsfr
- capital_ratio
- slr
- private_credit
confidence: 3
stability: evolving
thesis: Basel III imposes four interlocking constraints on bank balance sheets — RWA-based
  capital ratio, Output Floor (72.5% of standardized RWA), Leverage Ratio (3-5% unweighted),
  LCR (30-day HQLA buffer), and NSFR (structural funding ratio) — that jointly make
  holding long-duration, unrated, or specialized corporate credit economically punitive,
  driving credit migration to private markets.
source_refs:
- path: 02_sources/deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
  pages: Full document
  weight: primary
related:
- node: '[[Basel Driven Credit Migration To Private Markets]]'
  relation: shared_tag:basel
- node: '[[US Shadow Banking Post-GFC Market Based Finance Structure]]'
  relation: shared_tag:basel
- node: '[[Basel III Endgame — Capital, Liquidity, and Credit Migration]]'
  relation: shared_tag:basel
- node: '[[IRRBB EVE NII Dual Metric Framework]]'
  relation: shared_tag:basel
- node: '[[Basel Output Floor Specialized Lending Impact]]'
  relation: shared_tag:rwa
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
Basel III creates four distinct constraint axes on bank balance sheets. Each constrains a different margin of bank activity; their interaction makes holding long-term, unrated credit structurally irrational [RAW-CLIP].

## 1. RWA-Based Capital Ratio
```
CET1 Capital / Total RWA ≥ 10-13% (depending on G-SIB buffer + conservation buffer)
```
- **Risk weights:** Unrated corporate loans (middle market) → 100% RW; investment-grade corporates (SA) → 75%
- Leveraged buyout / leveraged loans → >100% RW due to high PD
- Banks using IRB models can reduce RWA below standardized, but Output Floor caps this benefit [RAW-CLIP]

## 2. Output Floor (Basel III Endgame)
Banks using Internal Ratings-Based (IRB) models cannot compute RWA below **72.5% of standardized RWA**.

| Implementation Date | Floor |
|--------------------|-------|
| 2022-01-01 | 50.0% |
| 2023-01-01 | 55.0% |
| 2024-01-01 | 60.0% |
| 2025-01-01 | 65.0% |
| 2026-01-01 | 70.0% |
| 2027-01-01 | **72.5%** (final) |

Impact: Specialized lending (infrastructure, project finance, commercial real estate) with strong internal risk models but no public rating gets floor-constrained, making the credit unprofitable [RAW-CLIP].

## 3. Leverage Ratio (SLR Equivalent)
```
Tier 1 Capital / Total Exposure (on + off balance sheet) ≥ 3% (G-SIBs: 3% + buffer)
```
- **Risk-blind**: Counts Treasuries and HQLA the same as leveraged loans
- Creates an absolute cap on balance sheet expansion regardless of asset quality
- US SLR is identical in spirit; COVID SLR relief (March 2020 - March 2021) showed how powerful this constraint is [RAW-CLIP]

## 4. LCR (Liquidity Coverage Ratio)
```
HQLA Stock / Net Cash Outflows (next 30 days stress scenario) ≥ 100%
```
- Committed credit lines to corporate/private credit funds → assumed 10-30% drawdown in stress
- Banks must hold low-yielding HQLA (reserves, Treasuries) as buffer against these contingent outflows
- Creates an opportunity cost for granting revolving credit lines to leveraged entities [RAW-CLIP]

## 5. NSFR (Net Stable Funding Ratio)
```
Available Stable Funding / Required Stable Funding ≥ 100%
```
Key RSF factors:
- Loans >1yr to non-financial corporates: **85% RSF** → must fund with 85 cents of stable funding per dollar
- Loans <1yr: 50% RSF
- Result: Long-term corporate lending requires expensive long-term funding (retail deposits, long bonds) [RAW-CLIP]

## Combined Effect: ROE Collapse
For an unrated leveraged loan on a bank's balance sheet:
- High RWA → large capital charge (floor-constrained if using IRB)
- High leverage ratio consumption → crowded out by lower-risk, higher-revenue assets
- NSFR penalty (85% RSF if >1yr)
- LCR buffer needed for revolving lines

Each layer erodes ROE. The only rational responses: (1) exit the asset class, (2) distribute risk via SRT/CLOs, (3) partner with private credit funds who lack these constraints [RAW-CLIP].


