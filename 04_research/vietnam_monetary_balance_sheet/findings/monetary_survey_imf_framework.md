---
finding_id: vietnam_monetary_survey_001
topic: vietnam_monetary_balance_sheet
sub_question: SQ1, SQ2
title: "Vietnam Monetary Survey — IMF Chapter 5 Structure (2017–2022)"
confidence: 2
status: provisional
date: "2026-05-26"
sources_used:
  - World Bank API (FM.LBL.BMNY.CN, FM.AST.NFRG.CN, FS.AST.PRVT.GD.ZS)
  - data/2026-05-26_worldbank_monetary_data.md
framework_nodes:
  - "[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]"
  - "[[Imf_Monetary_Survey_Valuation_Adjustment_Transaction_Flow_Decomposition]]"
---

## Vietnam Monetary Survey — IMF Analytical Form

Cấu trúc theo IMF Box 5.7 (Chapter 5): M2 = NFA + NDA; NDA = NCG + CPS + OIN

```
MONETARY SURVEY — VIETNAM (VND TRILLIONS, END OF YEAR)
════════════════════════════════════════════════════════════════════════
                    2017    2018    2019    2020    2021    2022
────────────────────────────────────────────────────────────────────────
ASSETS SIDE
NFA (Net Foreign Assets)
  Banking system     1,262   1,538   2,128   2,638   2,688   2,314
  [NFA/M2 %]        16.2%   17.6%   21.4%   23.3%   21.7%   17.6%

NDA (Net Domestic Assets)
  = M2 − NFA        6,511   7,222   7,826   8,673   9,717  10,796

  CPS (Private credit, est.) 6,544  7,381   8,326   9,295  10,549  12,021
  NCG + OIN (residual)  -33   -159    -500    -622    -832  -1,225
  [NCG+OIN/M2 %]    -0.4%   -1.8%   -5.0%   -5.5%   -6.7%   -9.3%

LIABILITIES SIDE
M2 (Broad Money)    7,773   8,760   9,954  11,311  12,405  13,110
  [M2/GDP %]       123.5%  125.0%  129.2%  140.6%  146.2%  136.3%

NFA/M2 (%)          16.2%   17.6%   21.4%   23.3%   21.7%   17.6%
CPS/M2 (%)          84.2%   84.3%   83.7%   82.2%   85.0%   91.7%
NCG+OIN/M2 (%)      -0.4%  -1.8%   -5.0%   -5.5%   -6.7%   -9.3%
════════════════════════════════════════════════════════════════════════
```

**Confidence note [LLM]:** CPS in VND derived as CPS/GDP% × GDP_VND (World Bank). NCG + OIN is a residual (NDA - CPS). Actual breakdown between NCG and OIN requires SBV balance sheet data — not available in World Bank series. Treat NCG+OIN residual as combined item.

---

## M2 Growth Decomposition (IMF Framework)

Áp dụng identity: ΔM2 = ΔNFA + ΔCPS + Δ(NCG+OIN)

```
CONTRIBUTION TO M2 GROWTH (percentage points)
════════════════════════════════════════════════════════════════
Year    ΔM2%    ΔNFA pp   ΔCPS pp   Δ(NCG+OIN) pp   Check
────────────────────────────────────────────────────────────────
2018    +12.7   +3.5      +10.8     -1.7             ✓
2019    +13.6   +6.7      +10.8     -3.9             ✓
2020    +13.6   +5.3      +10.2     -2.0             ✓
2021    +9.7    +0.4      +11.1     -1.8             ✓
2022    +5.7    -3.0      +11.9     -3.2             ✓
════════════════════════════════════════════════════════════════
```

*Method: ΔNFA pp = ΔNFA / M2(t-1); ΔCPS pp = ΔCPS / M2(t-1); residual absorbs difference [LLM-E]*

**Key finding:** CPS contributes consistently ~10-12 pp to M2 growth every year. NFA was additive during 2018-2020 reserve accumulation, turned negative drag in 2022. NCG+OIN is a mild drag throughout — government is net depositor at banking system.

---

## Monetary Survey Balance Sheet — Qualitative (T-Account)

```
SBV BALANCE SHEET (Central Bank — IMF Box 5.2 structure)
┌─────────────────────────────┬────────────────────────────────┐
│ ASSETS                      │ LIABILITIES                    │
├─────────────────────────────┼────────────────────────────────┤
│ NFA_cb                      │ Reserve Money (M0)             │
│   FX reserves (peak $109 bn)│   Currency in circulation      │
│   Gold                      │   Commercial bank reserves at  │
│   SDR holdings              │   SBV (required + excess)      │
│   IMF reserve position      │                                │
│   − SBV FX liabilities      │ Government deposits            │
│                             │   (Kho bạc Nhà nước tại SBV)  │
├─────────────────────────────┼────────────────────────────────┤
│ NCG_cb                      │ SBV-issued bills (sterilization│
│   Government securities held│   OMO instruments, T-bills     │
│   Direct loans to Treasury  │   issued by SBV)               │
│   − Government deposits     │                                │
│     at SBV                  │ Foreign liabilities            │
├─────────────────────────────┼────────────────────────────────┤
│ Cb (claims on DMBs)         │ Capital + OIN_cb               │
│   OMO lending               │                                │
│   Refinancing credit        │                                │
└─────────────────────────────┴────────────────────────────────┘
Identity: NFA_cb + NCG_cb + Cb + OIN_cb = M0 + Govt deposits + Fgn liabilities
```

**DATA_CAVEAT [LLM]:** SBV does not publish analytical balance sheet in IMF format publicly. Above structure is inferred from IMF Box 5.2 applied to Vietnam context. For M0 and Cb figures, see SBV Annual Report.

---

## Structural Features of Vietnam's Monetary Accounts

### 1. Bank-Dominated Financial System
M2/GDP at 136-146% (2020-2022) reflects near-total dependence on banking for financial intermediation. Capital markets (bond, equity) shallow. Almost all savings intermediated through commercial banks → M2 tracks total financial depth.

### 2. Credit-Driven M2 Growth
CPS contributes ~10-12 pp to annual M2 growth regardless of external conditions. This is structural: government-directed credit growth targets (SBV sets annual credit growth quotas, "room tín dụng"). Vietnam operates a **credit quota system** — each bank receives annual credit growth allowance from SBV. This makes CPS expansion highly policy-determined, not purely market-driven. [LLM — inferred from structure; verify with SBV circular]

### 3. Government Net Depositor Position
The negative NCG+OIN residual (-1,225 tn VND in 2022 = -9.3% of M2) implies the government sector is a net depositor at the banking system — government deposits exceed government securities held by banks (or government borrows little from banking system). This is consistent with:
- Vietnam's relatively low public debt (37% of GDP)
- Government issuance of bonds primarily to institutional buyers (insurance, social security funds)
- Large State Treasury (KBNN) deposits at commercial banks used as fiscal buffer

### 4. NFA Dynamics — Reserve Accumulation Phase and Reversal

**Phase 1: Accumulation 2016-2021**
SBV accumulated FX reserves: $36.5 bn → $109.4 bn (+$73 bn). In VND terms, NFA rose 946 → 2,688 tn (+1,742 tn). This was a sustained BoP surplus driven by FDI inflows and export growth. SBV partially sterilized via OMO and T-bill issuance — but M2 still grew 14%/year, suggesting only partial sterilization.

**Phase 2: Defense 2022-2024**
Fed rate hikes triggered USD strengthening. SBV sold reserves: $109.4 bn → $83.1 bn (-$26.3 bn). VND depreciated from 23,160 to 25,138 VND/USD. Banking system NFA dropped from 2,688 → 2,314 tn (-374 tn). This dragged M2 growth from +9.7% (2021) to +5.7% (2022). CPS offset: banks continued credit expansion (+1,472 tn) to partially compensate.

**Valuation adjustment note** [per [[Imf_Monetary_Survey_Valuation_Adjustment_Transaction_Flow_Decomposition]]]:
VND depreciated 2022-2024 (23,160 → 25,138 VND/USD = +8.5% depreciation). This means:
- Positive valuation adjustment on USD-denominated NFA assets (same USD reserves worth more in VND)
- Partially offsetting the outright reserve sales
- True transaction-based ΔNFA (actual selling) is LARGER in magnitude than total ΔNFA stock change

### 5. Inflation Stability Despite High M2 Growth
Vietnam maintained CPI of 1.83-3.62% (2021-2024) despite M2/GDP of 136-146%. This is possible because:
- Velocity of money (V = nominal GDP / M2) declining as financial deepening increases M2 relative to spending
- Import-sensitive price level with VND mostly stable until 2022
- Price controls on fuel, electricity (government utilities) suppressing headline CPI
- Quantity theory (MV = PY) holds but V fell structurally, absorbing M2 growth

Velocity: V = GDP/M2
- 2017: 6,294/7,773 = 0.81
- 2019: 7,707/9,954 = 0.77
- 2021: 8,487/12,405 = 0.68
- 2022: 9,621/13,110 = 0.73
[LLM-E: computed from WB data]

---

## Data Gaps and Next Steps

**TRUE_GAP items remaining:**
1. SBV balance sheet breakdown: actual M0 (reserve money), Cb (claims on commercial banks), NCG separate from OIN
2. FX deposit share within M2 (dollarization proxy)
3. SBV sterilization instruments: volume of OMO bills outstanding, required vs. actual reserve ratio
4. Credit quota ("room tín dụng") by year and bank — key policy variable
5. SBV interest rate structure: refinancing rate, OMO rate, overnight interbank rate

**Recommended sources to acquire:**
- SBV Annual Report 2022, 2023, 2024 (PDF) → analytical balance sheet + M0 data
- IMF Vietnam Article IV 2024 Staff Report (Appendix tables) → full monetary survey in IMF format
- BIS Credit Statistics → Vietnam CPS/GDP long series (better than WB for bank-by-bank)
