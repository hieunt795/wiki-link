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
date_updated: '2026-05-25'
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

---

## Analytical Uses: External and Fiscal Imbalance Tracing

The FoF framework's interlocking structure allows analysts to trace the origins of imbalance in one sector and its repercussions across others [RAW-BOOK IMF Macro Ch.6 p.5518].

### External Imbalance (CAD Origin Analysis)
An increase in the current account deficit can be traced to either sector's saving-investment deterioration [RAW-BOOK IMF Macro Ch.6 p.5522]:
```
CAD increase → must come from:
  (a) Private sector: fall in Sp, or rise in Ip, or both
  (b) Government sector: rise in deficit (Ig - Sg increases)
  
Policy prescriptions differ:
  → Private consumption boom → demand management, possibly exchange rate
  → Private investment boom (Lawson doctrine): may be self-financing; 
    less urgent if inflows are FDI-quality
  → Government deficit → fiscal consolidation is the priority instrument

Financing analysis (from FoF table):
  → Rise in net foreign borrowing (NFB) by government or private sector
  → Increase in FDI
  → Drawdown of official reserves (reduction in NFA)
```

### Fiscal Imbalance (Transmission Analysis)
When government expenditure rises without offsetting revenue [RAW-BOOK IMF Macro Ch.6 p.5526]:

```
Case A: Financed by tax increase
  → Private disposable income falls
  → IF private sector cuts spending: private nonfinancial balance unchanged
    → No deterioration in CAB from private side
  → IF private sector maintains spending (reduces saving):
    → Private nonfinancial balance worsens
    → Private sector borrows from banking system OR runs down cash balances
      OR borrows abroad
    → CAB deteriorates regardless of which financing route

Case B: Financed by CB credit (monetization)
  → NCG rises → RM rises → M2 expands
  → Nominal GDP rises: (i) higher tax revenues partly offset initial deficit;
    (ii) private sector's nominal income rises → private balance improves
  → Private sector holds incremental savings as money balances (M2 demand)
  → If extra income induces both domestic AND import spending:
    → CAB deteriorates, affecting the external sector column

Key insight: The FoF matrix makes these transmission channels explicit and
  measurable — every financing route for the fiscal deficit shows up as a
  counterpart entry in another sector's financial transactions column.
```

### Flow of Funds Table: Column and Row Structure (Table 6.1)

The schematic FoF table has 6 sector columns + horizontal check column [RAW-BOOK IMF Macro Table 6.1 p.5535]:

```
Column 1: Overall Economy — GDP-level aggregates (X, M, Yt, TRt)
Column 2: Domestic Economy — consolidated domestic (= sum of cols 3+4+5)
Column 3: General Government — GFS data
Column 4: Private Sector — residual; national accounts minus government
Column 5: Banking System — monetary survey data; real balance = 0 by convention
Column 6: Rest of the World — from BOP, recorded from ROW perspective
Column 7: Horizontal Check — each row must sum to 0

Row blocks:
  Block 1 (nonfinancial): GNDI, consumption, investment, X, M, Yt, TRt
  Block 2 (gap row):       Nonfinancial balance (S - I) per sector
  Block 3 (financing):     FDI, NFB, ΔNFA, ΔM2, ΔNDC (by sector), nonbank
  Block 4 (residual):      Net errors and omissions (ΔOINd — balancing item)
  Block 5 (vertical check): Each column must sum to 0
```

The banking sector column shows: zero nonfinancial balance (convention) + ΔNFA (monetary) + ΔNDC (banking system's lending to govt + private) − ΔM2 = 0. This restates the monetary survey identity: ΔM2 = ΔNFA + ΔNDC + ΔOINb. [RAW-BOOK IMF Macro Table 6.1 p.5503–5504]

---

## Box 6.4 — Complete Sector Accounting Identities (All 8 Equations)

Full formal system from IMF Macro Accounting Box 6.4 [RAW-BOOK IMF Macro p.5489–5509]. Every row and column of the FoF matrix sums to zero — these equations make that constraint explicit for each sector.

```
─────────────────────────────────────────────────────────────────────
SECTOR 1: OVERALL ECONOMY
─────────────────────────────────────────────────────────────────────
Saving-investment gap:
  S − I = CAB                                      (economy-wide)
  −S + I + CAB = 0

GNDI definition (Eq. 1):
  −GNDI + C + I + X − M + Yt + TRt = 0            ... (1)
  ↔ GNDI = C + I + X − M + Yt + TRt
  ↔ CAB = GNDI − C − I = X − M + Yt + TRt

─────────────────────────────────────────────────────────────────────
SECTOR 2: GENERAL GOVERNMENT
─────────────────────────────────────────────────────────────────────
Saving-investment gap (Eq. 2):
  Sg − Ig = GNDIg − Cg − Ig                       ... (2)

Financing identity (Eq. 3):
  (Sg − Ig) + NFBg + ΔNDCg + NB = 0               ... (3)

  Variables:
    Sg − Ig  = fiscal surplus (+) or deficit (−)
    NFBg     = net foreign borrowing by government
    ΔNDCg    = net domestic bank credit to government (monetization)
    NB       = nonbank domestic borrowing (bond issuance to public)

─────────────────────────────────────────────────────────────────────
SECTOR 3: PRIVATE SECTOR (NONGOVERNMENT)
─────────────────────────────────────────────────────────────────────
Saving-investment gap (Eq. 4):
  Sp − Ip = GNDIp − Cp − Ip                       ... (4)

Financing identity (Eq. 5):
  FDIp + NFBp + ΔNDCp − ΔM2 − NB = 0             ... (5)

  Variables:
    FDIp   = FDI inflows to private sector
    NFBp   = net foreign borrowing by private sector
    ΔNDCp  = change in bank credit to private sector
    −ΔM2   = change in money holdings (accumulation = use of funds, sign −)
    −NB    = private sector's nonbank lending to government (sign −)

─────────────────────────────────────────────────────────────────────
SECTOR 4: BANKING SYSTEM
─────────────────────────────────────────────────────────────────────
Saving-investment gap (by convention):
  Sb − Ib = 0     (banking sector has zero real S-I balance)

Monetary survey identity (Eq. 6):
  ΔM2 − ΔNFA − ΔNDC − ΔOINb = 0                  ... (6)
  ↔ ΔM2 = ΔNFA + ΔNDC + ΔOINb

  Variables:
    ΔM2   = change in broad money (M2) — liabilities of banking system
    ΔNFA  = change in net foreign assets of banking system
    ΔNDC  = change in net domestic credit = ΔNDCg + ΔNDCp
    ΔOINb = change in other items net (residual; absorbs valuation effects)

─────────────────────────────────────────────────────────────────────
SECTOR 5: FOREIGN SECTOR (viewed from rest-of-world perspective)
─────────────────────────────────────────────────────────────────────
Saving-investment gap (Eq. 7):
  −CAB = −X + M − Yt − TRt                        ... (7)
  (ROW's surplus = country's current account deficit)

BOP financing identity (Eq. 8):
  CAB + Fr = 0
  −CAB − FDI − NFB + ΔNFA + ΔOINt = 0            ... (8)

  Variables:
    Fr    = total financing flow = FDI + NFB − ΔNFA − ΔOINt
    FDI   = total foreign direct investment inflows
    NFB   = total net foreign borrowing (= NFBg + NFBp)
    ΔNFA  = change in banking system net foreign assets (+ = reserve accumulation)
    ΔOINt = foreign sector other items net / errors and omissions

─────────────────────────────────────────────────────────────────────
CROSS-SECTOR CONSISTENCY CHECK
─────────────────────────────────────────────────────────────────────
Horizontal: each row sums to 0 (closed system)
Vertical:   each column sums to 0 (each sector's gap = financing)

Key cross-sector links:
  NDC = NDCg + NDCp  (banking credit split between govt and private)
  NFB = NFBg + NFBp  (foreign borrowing split between govt and private)
  NB appears as +NB in Eq. 3 (govt receives nonbank financing)
     and as −NB in Eq. 5 (private sector provides nonbank financing)
  → NB cancels in horizontal sum ✓

  ΔM2 in Eq. 5 (private accumulation) = ΔM2 in Eq. 6 (banking liability)
  → same variable, both sides of the intermediation relationship ✓
```

**Accounting limitation:** These 8 equations are accounting identities, not behavioral models. They hold ex post by construction. To derive policy implications, behavioral equations for consumption, investment, money demand, and capital flows must supplement the accounting constraints. [RAW-BOOK IMF Macro Ch.6 p.5455]


