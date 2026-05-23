---
node_id: imf_flow_of_funds_4_sector_consistency_framework_001
type: framework
title: IMF Flow Of Funds 4-Sector Consistency Framework
aliases:
- Flow of Funds Framework
- 4-Sector Macro Accounting
- Sectoral Balance Framework
- IMF Financial Programming
- Twin Deficits Identity
- Khung kế toán vĩ mô 4 khu vực
- Cân bằng tiết kiệm đầu tư IMF
domain:
  primary: monetary_policy
tags:
- imf
- flow_of_funds
- sectoral_balance
- financial_programming
- sna
- gfs
- bop
- monetary_survey
- twin_deficits
confidence: 4
stability: evolving
thesis: The IMF Flow of Funds framework integrates SNA, GFS, BoPM, and monetary survey
  into a quadruple-entry matrix where sectoral saving-investment gaps (Sp-Ip) + (Sg-Ig)
  = CAB, and every sector's real deficit is fully financed by financial transactions
  — forming the accounting backbone of IMF financial programming.
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'Chapter 6: The Flow of Funds: Macroeconomic Interrelations'
  weight: primary
related:
- node: '[[IMF Balance of Payments Framework and External Account Analysis]]'
  relation: shared_tag:imf
- node: '[[IMF GFS Fiscal Accounting Framework Deficit Measurement And Sustainability]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Analysis Quantity Theory Velocity And Exchange Rate Regimes]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Survey And Reserve Money Identity Framework]]'
  relation: shared_tag:imf
- node: '[[IMF SNA Real Sector Accounting GDP Identities And Sectoral Accounts]]'
  relation: shared_tag:imf
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The **Flow of Funds (FoF) Framework** integrates all four macroeconomic sectors — private, government, banking, and foreign — into a single consistent matrix where every surplus in one sector must be financed by deficits in others. It is the unifying accounting architecture underlying IMF financial programs [RAW-CLIP].

## The Four Primary Macroeconomic Accounts
| Account | Standard | Tracks |
|---------|----------|--------|
| National Income & Product (SNA) | 1993 SNA | GDP, absorption, saving, investment |
| Government Finance Statistics (GFS) | IMF GFS | Revenue, expenditure, deficit, financing |
| Balance of Payments (BoP) | BPM5/BPM6 | Current account, capital/financial account, reserves |
| Monetary Accounts (MBS) | IMF IFS | Reserve money, M2, NDA, NFA |

These four systems are mutually consistent: transactions in one appear as counterpart entries in others [RAW-CLIP].

## The Core Sectoral Balance Identity
For any open economy:

```
(Sp - Ip) + (Sg - Ig) = CAB

Where:
  Sp - Ip = Private sector saving-investment gap
  Sg - Ig = Government fiscal balance (surplus positive)
  CAB    = Current account balance
```

This identity shows: **fiscal deficit + private sector saving shortfall = current account deficit** [RAW-CLIP].

The three canonical situations:
1. **Twin Deficits (Situation 1):** Fiscal deficit is the primary source; reducing CAD requires fiscal adjustment
2. **Double Domestic Shortfall (Situation 2):** Both government deficit AND private saving shortfall; financing squeeze
3. **Fiscal Surplus with Private Boom (Situation 3):** CAD exists despite fiscal surplus → private consumption or investment boom; policy implications differ [RAW-CLIP]

## Flow of Funds Matrix Structure
The FoF matrix has sectors as columns, transactions as rows. Three blocks:

```
BLOCK 1: Nonfinancial Transactions (real sector)
  - Exports, imports, consumption, investment, government expenditure, taxes

BLOCK 2: Saving-Investment Balances (resource gaps)
  - Each sector's surplus or deficit

BLOCK 3: Financial Transactions (how gaps are financed)
  - Borrowing from banks, foreign borrowing, reserve changes, etc.
```

**Key property:** Each row sums to zero (closed system). Each column sums to zero (every sector finances its gap). This makes the system a **quadruple-entry accounting system** — each real transaction has: (1) real entry in sector A, (2) financial counterpart in sector A, (3) real entry in sector B, (4) financial counterpart in sector B [RAW-CLIP].

## Sign Conventions
- Transaction that **increases assets** or **decreases liabilities** → negative sign
- Transaction that **decreases assets** or **increases liabilities** → positive sign
- The "rest of the world" sector is recorded from the ROW's perspective (not the country's)

Example: Country's foreign borrowing (increase in foreign liabilities) = +200; ROW's net lending (increase in ROW assets) = -200. Both row and column still sum to zero [RAW-CLIP].

## Linking the Four Macroeconomic Accounts
The FoF framework is populated by data from the four macroeconomic accounts:

```
Private sector:  National income accounts (S, I) + monetary survey (credit)
Government:      GFS (revenue, expenditure, deficit, financing)
Banking:         Monetary survey (NFA, NCG, CPS, M2)
External:        Balance of payments (CAB, capital account, ΔReserves)
```

The banking sector is assumed to have **zero real transactions** (saving = investment = 0) — its only role is financial intermediation between sectors [RAW-CLIP].

## Financial Programming Application
A financial program sets quantitative targets for each sector's balance:
1. Select a target for CAB (external sustainability)
2. Determine required fiscal adjustment (Sg - Ig)
3. Residual private sector balance (Sp - Ip) must be consistent
4. Monetary targets: consistent with the NFA + NDA = M2 identity
5. Iterate until all four accounts are internally consistent [RAW-CLIP]

## Data Sources for FoF Construction
Primary sources (per IMF methodology):
- **GFS:** Government revenue, expenditure, deficit, financing breakdown
- **BOPS (Balance of Payments Statistics):** External current and capital accounts
- **MBS (Money and Banking Statistics):** NFA, NDA, M2, credit to government and private sector
- **National accounts:** GDP, saving, investment (from SNA)

When the same transaction appears in two data sources (e.g., NFA change in both BoP and monetary survey), a single primary source must be chosen to avoid double-counting [RAW-CLIP].


