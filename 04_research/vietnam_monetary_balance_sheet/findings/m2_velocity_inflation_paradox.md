---
finding_id: vietnam_m2_velocity_001
topic: vietnam_monetary_balance_sheet
sub_question: SQ2, SQ4
title: "Vietnam M2/GDP High but Inflation Low — Velocity Decline and Structural Explanation"
confidence: 3
status: provisional
date: "2026-05-26"
sources_used:
  - World Bank API (FM.LBL.BMNY.GD.ZS, FP.CPI.TOTL.ZG, FR.INR.RINR)
  - data/2026-05-26_worldbank_monetary_data.md
framework_nodes:
  - "[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]"
  - "[[Imf_Inflation_Analysis_Cpi_Gdp_Deflator_Four_Types_Core]]"
---

## The Puzzle

Vietnam's M2/GDP ratio reached 146% in 2021 — among highest globally, comparable to China (220%), Japan (190%), and far above the ASEAN average (~80-100%). Yet CPI inflation stayed at 1.83-3.62% throughout 2020-2024. Why?

## Quantity Theory Framework

```
Quantity equation: M × V = P × Y
→ V = P×Y / M = nominal GDP / M2

VIETNAM VELOCITY OF MONEY (M2):
Year    GDP (VND tn)    M2 (VND tn)    V = GDP/M2
────────────────────────────────────────────────────
2017    6,294           7,773          0.810
2018    7,009           8,760          0.800
2019    7,707           9,954          0.775
2020    8,044           11,311         0.711
2021    8,487           12,405         0.684 ← trough
2022    9,621           13,110         0.734
────────────────────────────────────────────────────
[LLM-E: computed from WB data]
```

Velocity fell from 0.81 (2017) to 0.68 (2021) — a 16% decline in 5 years. This means each unit of M2 was "turning over" less frequently to finance GDP spending. Fast M2 growth + declining V = M2 growth absorbed into financial deepening, not price increases.

## Why Velocity Declined: Three Structural Drivers

**1. Financial Deepening (Dominant)**
As Vietnam's economy financializes (more bank accounts, more deposits, longer holding periods), M2 grows faster than nominal spending. Newly banked population stores wealth in deposits → M2 rises without proportional velocity. Vietnam's financial inclusion rate rose significantly in 2015-2021.

**2. Time Deposit Preference**
Vietnamese households park savings in time deposits (quasi-money) rather than transactional accounts. High CPS/M2 (84-92%) and positive real rates (2.6-8.9%) incentivize holding bank deposits. These deposits are in M2 but do not circulate for daily transactions → V falls.

**3. COVID Liquidity Hoarding (2020-2021)**
M2/GDP spike to 146% in 2021 driven by: (1) SBV rate cuts (refinancing rate cut from 6% to 4%), (2) COVID liquidity facilities, (3) precautionary savings surge during lockdowns. Nominal GDP growth slowed while M2 expanded → V fell sharply.

## Credit Quota System and Inflation Control

Vietnam runs a **credit quota ("room tín dụng") system**: SBV allocates annual credit growth limits to each commercial bank (typically 12-15% system-wide). This means:
- CPS growth is administratively capped → M2 growth capped at 12-15%/year
- Even if banks have excess liquidity (from NFA inflows), they cannot lend beyond quota
- This prevents credit-driven inflation even with high M2/GDP

**IMF framework implication:** Vietnam's NCG + OIN residual stays negative (government is net depositor) partly because SBV uses government bond issuance as sterilization — commercial banks are required to hold government securities (quasi-sterilization via regulatory requirements).

## Real Interest Rate Signal

Real interest rate (lending rate minus CPI) stayed positive at 2.59-8.99% throughout 2015-2023. High real rates:
1. Incentivize savings over spending → V falls
2. Reduce credit demand at the margin → CPS growth below credit quota in some years
3. Attract deposit inflows → M2 grows from liability side even without credit expansion

2023 real rate = 7.08% (highest since 2015) — after SBV raised rates in late 2022 response to Fed tightening. This further suppressed velocity and supported VND.

## Summary T-Account: What Drives Vietnam's High M2/GDP?

```
STRUCTURAL FACTOR               EFFECT ON M2/GDP
──────────────────────────────────────────────────
Bank-dominated intermediation   ↑ M2/GDP (no capital market alternative)
Credit quota system             Controls growth rate but not level
FDI-driven BoP surplus          NFA ↑ → M2 ↑ (partial sterilization)
Time deposit culture            Quasi-money ↑ relative to nominal GDP
Financial inclusion growth      New deposits → M2 ↑ structurally
Administrative price controls   CPI suppressed → V appears to fall
──────────────────────────────────────────────────
RESULT: M2/GDP = 136-146%, CPI = 2-4%
  → Not a contradiction; reflects financial depth, not monetary instability
```

## Policy Implication for IMF NDA Analysis

If Vietnam were under an IMF financial program:
- **NDA ceiling** would be calibrated to allow M2 to grow ~12-15% (consistent with nominal GDP growth + financial deepening)
- **ΔNDA = ΔM2(target) − ΔNFA(program)** → with NFA declining (2022-2024), NDA ceiling would need to expand to maintain M2 growth
- Vietnam's CPS quota system effectively functions as an informal NDA ceiling — an institutional analog to IMF financial programming constraints

**Comparison to IMF Monetary Analysis framework** [[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]:
Vietnam fits the "financially deepening economy" case where quantity theory holds but V is declining trend, requiring upward adjustment to money demand to maintain inflation target consistency.
