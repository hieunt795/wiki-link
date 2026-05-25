---
node_id: imf_monetary_analysis_quantity_theory_velocity_and_exchange_rate_regimes_001
type: framework
title: IMF Monetary Analysis Quantity Theory Velocity And Exchange Rate Regimes
aliases:
- IMF Quantity Theory Framework
- Monetary Analysis IMF Chapter 5
- Money Multiplier Framework
- Exchange Rate Regime Monetary Autonomy
- Phân tích tiền tệ IMF - thuyết số lượng tiền tệ
- Bộ số nhân tiền tệ và chế độ tỷ giá
domain:
  primary: monetary_policy
tags:
- imf
- quantity_theory
- velocity
- demand_for_money
- money_multiplier
- dollarization
- currency_substitution
- exchange_rate_regime
- sterilization
- fixed_rate
- floating_rate
- monetary_autonomy
- financial_programming
confidence: 4
stability: evolving
thesis: IMF monetary analysis builds from the quantity equation (MV=PY) through demand
  for money (income elastic, opportunity-cost elastic) to the money multiplier mm=(c+1)/(c+r),
  showing that under fixed exchange rates money supply is endogenous and monetary
  autonomy requires a floating regime, with sterilization as a costly short-term offset.
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'Chapter 5: Monetary Accounts and Analysis — sections on Monetary Analysis,
    Money Market Equilibrium, Special Issues'
  weight: primary
related:
- node: '[[IMF Balance of Payments Framework and External Account Analysis]]'
  relation: shared_tag:imf
- node: '[[IMF Flow Of Funds 4-Sector Consistency Framework]]'
  relation: shared_tag:imf
- node: '[[IMF GFS Fiscal Accounting Framework Deficit Measurement And Sustainability]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Survey And Reserve Money Identity Framework]]'
  relation: shared_tag:imf
- node: '[[IMF SNA Real Sector Accounting GDP Identities And Sectoral Accounts]]'
  relation: shared_tag:imf
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
Chapter 5 of the IMF macro accounting textbook provides the theoretical foundations linking the monetary survey to macro outcomes: quantity theory, demand for money, the money multiplier, currency substitution, and how the exchange rate regime determines the scope for monetary autonomy [RAW-CLIP].

## Quantity Theory of Money
The quantity equation: **M × V = P × Y** where M = money stock, V = income velocity, P = price level, Y = real output [RAW-CLIP].

**Velocity (V = 1/k):** The number of times the money stock turns over per period in financing nominal income. Velocity is the inverse of the Cambridge k (money demand as a share of income). In growth form:
`Ṁ/M = Ṗ/P + Ẏ/Y + V̇/V`

Under constant velocity (V̇/V = 0): money growth = inflation + real GDP growth. Excess money growth beyond real output growth generates inflation [RAW-CLIP].

**Empirical behavior of velocity:** Velocity is not constant — it rises with higher inflation and interest rates (higher opportunity cost of holding money reduces money demand, raising V), and is less sensitive to income changes [RAW-CLIP].

## Demand for Money
Real money demand (M/P) is [RAW-CLIP]:
- **Positively related to real income:** More transactions require more transaction balances; income elasticity determines velocity behavior (elasticity = 1 → constant V; elasticity < 1 → rising V with income growth)
- **Negatively related to opportunity cost:** Nominal interest rate (financially developed countries) or expected inflation rate (transition/high-inflation countries) as proxies for the cost of holding liquid balances vs. alternative assets

**Hyperinflation implication:** When opportunity cost becomes extreme, money demand collapses, requiring accelerating money creation to finance even constant real spending (Olivera-Tanzi effect) [LLM].

## Money Multiplier
**Simple multiplier:** Starting from RM = CY + R (reserve money = currency + bank reserves) and M = CY + DD (money = currency + demand deposits):

`mm = M/RM = (c + 1)/(c + r)`

where c = currency-to-deposit ratio (public behavior), r = reserve-to-deposit ratio (bank behavior + reserve requirements) [RAW-CLIP].

**General multiplier (M2):**
`mm = (c + b + 1) / (c + rd + rt×b + re)`
where rd = required reserve on demand deposits, rt = required reserve on time/savings deposits, b = time deposits/demand deposits ratio, re = excess reserve ratio [RAW-CLIP].

**Monetary authorities do not fully control M:** The multiplier depends on three agents:
1. Monetary authorities (set reserve requirements rd, rt)
2. Commercial banks (choose excess reserves re based on opportunity cost and liquidity preferences)
3. Non-bank public (choose c and b based on interest rates and inflation) [RAW-CLIP]

## Currency Substitution and Dollarization
When domestic inflation is high and variable, residents substitute foreign currency for domestic currency as a store of value, unit of account, and means of exchange — "dollarization" [RAW-CLIP].

**Dollarization ratio** (foreign currency deposits / broad money): rises from near-zero at reform start to 30-60% peak in high-inflation transition economies [RAW-CLIP].

**Policy implications** [RAW-CLIP]:
- Undermines monetary authorities' control over money supply (foreign currency component cannot be directly controlled)
- Exacerbates fiscal deficit inflation: reduced money demand shrinks seigniorage base
- Artificial reversal (forced conversion, indexed instruments) → "inflation explosion" when suppressed pressures release
- Solution: sound fiscal and financial policies → credibility → voluntary return to domestic currency

## Exchange Rate Regimes and Monetary Policy Autonomy

### Fixed Exchange Rate Regime
- Monetary authorities commit to buy/sell domestic currency at fixed price → NFA adjusts with interventions → reserve money (and money supply) adjusts endogenously [RAW-CLIP]
- **Money supply is rendered endogenous** — authorities cannot independently set it
- Domestic credit expansion → current account deficit → downward pressure on exchange rate → FX sale → ΔNFAm ↓ → money supply expansion is frustrated [RAW-CLIP]
- Benefit: imported monetary credibility from the anchor country's central bank; automatic discipline

### Sterilization (Offset Operations)
FX sale (↓NFA) offset by OMO purchase of securities (↑NDA) → reserve money unchanged → money supply unchanged [RAW-CLIP].

**Limits of sterilization** [RAW-CLIP]:
1. Requires broad, well-functioning securities market (absent in many transition economies)
2. Cost of interest payments on securities issued escalates with scale of intervention
3. Only effective for short periods; sustained sterilization is fiscally costly

### Floating Exchange Rate Regime
- Monetary authorities do not intervene → exchange rate clears FX market → money supply is under full domestic control [RAW-CLIP]
- **Monetary autonomy restored:** central bank can target domestic inflation or output
- Excessive credit creation → exchange rate depreciation (additional inflation channel in open economies)
- In practice: "pure float" is hypothetical — most countries run "dirty floats" with intervention when rate moves far from equilibrium [RAW-CLIP]

### Currency Board
Fixed exchange rate with no sterilization option — reserve money can only be created if fully backed by foreign exchange holdings [RAW-CLIP]. Adjustment is automatic (rising interest rates, falling prices/wages) but potentially painful for output if wages/prices are rigid.

## Capital Inflows Under Alternative Regimes
**Fixed rate + capital inflows:** FX intervention → RM ↑ → M ↑ → inflationary unless sterilized [RAW-CLIP]
**Floating rate + capital inflows:** Appreciation of domestic currency; competitiveness erosion [RAW-CLIP]
**Both regimes:** Risk of temporary consumption boom financed by capital inflows → debt accumulation → eventual absorption cut [RAW-CLIP]

## Private Sector Financing Identity (Box 6.4, Equations 4–5)

The private sector's saving-investment gap and its financing [RAW-BOOK IMF Macro Box 6.4 p.5499–5500]:

```
Private sector saving-investment gap (Eq. 4):
  Sp − Ip = GNDIp − Cp − Ip                       ... (4)

Private sector financing identity (Eq. 5):
  FDIp + NFBp + ΔNDCp − ΔM2 − NB = 0             ... (5)

Where:
  Sp − Ip  = Private saving-investment surplus (+) or deficit (−)
  FDIp     = FDI inflows to private sector (+ = increase in liabilities)
  NFBp     = Net foreign borrowing by private sector (+ = new borrowing)
  ΔNDCp    = Change in banking credit to private sector (+ = more credit)
  ΔM2      = Change in private sector's money holdings (+ = accumulation)
             → negative sign: accumulating money is a USE of financing, not a source
  NB       = Private sector's nonbank lending to government (+ = private buys govt bonds)
             → negative sign: buying govt bonds is a USE of savings, not a financing source

Sign convention (FoF framework):
  + = decrease in assets or increase in liabilities (SOURCES of financing)
  − = increase in assets or decrease in liabilities (USES of financing)
```

**Interpretation:**
```
When private sector is in DEFICIT (Sp − Ip < 0):
  → Financed by: FDI inflows (+FDIp), foreign borrowing (+NFBp),
    bank credit (+ΔNDCp), running down money balances (−ΔM2 < 0)
  → Reduced by: lending to government (+NB = buying bonds)

When private sector is in SURPLUS (Sp − Ip > 0):
  → Surplus deployed as: money accumulation (+ΔM2 > 0),
    lending to government (+NB > 0), repaying foreign loans (−NFBp < 0)
```

**Link to monetary survey (Eq. 6):**
ΔNDCp (private credit, part of ΔNDC in banking identity) + ΔM2 (private money demand)
together connect the private sector financing position to the banking sector balance sheet.
When private sector accumulates money (ΔM2 ↑), the banking sector's M2 liabilities grow —
the counterpart is credit creation (ΔNDCp ↑) or reserve accumulation (ΔNFA ↑).

