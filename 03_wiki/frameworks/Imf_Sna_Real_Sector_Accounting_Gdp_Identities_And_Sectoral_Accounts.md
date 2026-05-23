---
node_id: imf_sna_real_sector_accounting_gdp_identities_and_sectoral_accounts_001
type: framework
title: IMF SNA Real Sector Accounting GDP Identities And Sectoral Accounts
aliases:
- System of National Accounts
- SNA 1993
- GDP Identity
- Expenditure Approach GDP
- Saving Investment Identity
- Hệ thống tài khoản quốc gia SNA
- Đồng nhất thức GDP
domain:
  primary: monetary_policy
tags:
- imf
- sna
- gdp
- national_accounts
- circular_flow
- saving_investment
- fiscal_external_identity
- real_sector
confidence: 4
stability: evolving
thesis: The 1993 SNA framework measures GDP via three equivalent approaches (production/income/expenditure),
  organizes each sector's transactions through a sequence of accounts from production
  to capital formation, and generates the fundamental identity that the current account
  equals the private saving-investment gap plus the fiscal balance — the backbone
  of IMF Article IV analysis.
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'Chapter 2: Analysis of the Real Sector'
  weight: primary
related:
- node: '[[IMF Balance of Payments Framework and External Account Analysis]]'
  relation: shared_tag:imf
- node: '[[IMF Flow Of Funds 4-Sector Consistency Framework]]'
  relation: shared_tag:imf
- node: '[[IMF GFS Fiscal Accounting Framework Deficit Measurement And Sustainability]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Analysis Quantity Theory Velocity And Exchange Rate Regimes]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Survey And Reserve Money Identity Framework]]'
  relation: shared_tag:imf
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The **1993 System of National Accounts (SNA)** provides the accounting framework underlying all IMF macroeconomic analysis. It defines how GDP is measured, how sectors interact, and how income flows through the economy via a sequence of interconnected accounts [RAW-CLIP].

## The Five Economic Sectors
1. **Households** — supply labor/capital, demand goods; save by not consuming income
2. **Enterprises** — employ factors of production, produce output, invest
3. **Financial Sector** — provide intermediation; transform maturity of assets
4. **Government** — provide public goods, collect taxes, regulate
5. **Rest of World (ROW)** — all nonresident transactions; external current account [RAW-CLIP]

## Three Approaches to GDP (All Equivalent)
```
PRODUCTION APPROACH:  GDP = Σ Gross Value Added (output - intermediate consumption)
INCOME APPROACH:      GDP = Wages + Profits + Taxes on production - Subsidies
EXPENDITURE APPROACH: GDP = C + I + G + (X - M)
```

Where:
- C = Private consumption
- I = Gross capital formation (investment)
- G = Government consumption
- X - M = Net exports (trade balance for goods and services)
[RAW-CLIP]

## Key Macroeconomic Aggregates and Identities
```
GDP = Value of final goods and services produced domestically
GNP = GDP + Net factor income from abroad

Absorption (A) = C + I + G   (domestic demand)
Resource Balance = GDP - A = X - M

National Saving (S) = GNP - C - G
National Investment (I) = Gross capital formation

Saving-Investment Gap: S - I = X - M + Net factor income ≈ Current Account Balance
```
[RAW-CLIP]

## The Circular Flow of Income
Income flows:
- Enterprises → Households (wages, dividends, rent)
- Households → Enterprises (spending on goods/services)

**Leakages** from the spending stream: taxes, imports, private saving
**Injections** into the spending stream: government spending, exports, investment

Sum of all leakages ≡ Sum of all injections (national accounts identity) [RAW-CLIP]

## The SNA Sequence of Accounts
The 1993 SNA is organized as a sequence of accounts for each sector:

| Account | Records |
|---------|---------|
| Production Account | Output minus intermediate consumption = Value added |
| Generation of Income | Value added → Primary income distribution (wages, profits, taxes) |
| Allocation of Income | Primary income + transfers received → Gross National Income |
| Secondary Distribution | GNI + current transfers → Gross Disposable Income |
| Use of Disposable Income | GDI - final consumption = Saving |
| Capital Account | Saving + capital transfers - investment = Net lending/borrowing |

The **Capital Account balance** (net lending/borrowing) is the sector's S-I gap and directly maps to the flow of funds financing requirement [RAW-CLIP].

## GDP Measurement Issues
**Nominal vs Real GDP:**
- Nominal GDP: values output at current prices
- Real GDP: values output at base-year constant prices
- GDP deflator: Nominal GDP / Real GDP × 100

**Inflation Measurement:**
- **CPI (Consumer Price Index):** Fixed Laspeyres basket; tracks household cost of living; upward bias (substitution effect)
- **GDP Deflator:** Implicit price index covering all domestic output; broader than CPI
- **PPI (Producer Price Index):** Factory-gate prices; leads CPI in the chain [RAW-CLIP]

**Transition Economy Measurement Problems:**
- Material Product System (MPS) vs SNA: MPS excluded services; overstated industrial output relative to true value added
- Underground economy and barter not captured in official statistics
- Rapid quality changes make real GDP comparisons unreliable [RAW-CLIP]

## Income and Employment Concepts
- **Real wages:** Nominal wages deflated by CPI; proper living standard measure
- **Unit labor costs:** Wage costs per unit of output (wages / productivity); key competitiveness indicator
- **Unemployment rate:** ILO definition: seeking work + available for work; "hidden unemployment" in transition economies [RAW-CLIP]

## Fiscal-External Linkage (Box 2.2 Identity)
```
GDP = C + I + G + X - M                        ... (expenditure)
     = GNP - Net factor payments abroad

GNP = C + S + T                                 ... (income)
     (S = private saving; T = taxes)

Combining:
(X - M) + Net factor income = S - I + (T - G)
Current Account ≈ Private S-I gap + Fiscal balance
```

This is the fundamental link between external and domestic imbalances exploited in every IMF Article IV consultation [RAW-CLIP].


