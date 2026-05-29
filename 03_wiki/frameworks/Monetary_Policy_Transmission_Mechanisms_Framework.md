---
node_id: mptm_framework_001
type: framework
title: Monetary Policy Transmission Mechanism — All Channels
aliases:
- MPTM
- monetary policy transmission mechanism
- transmission channels
- interest rate channel
- credit channel
- balance sheet channel
- risk-taking channel
- cơ chế truyền dẫn chính sách tiền tệ
- kênh truyền dẫn lãi suất
- kênh tín dụng
domain:
  primary: monetary_policy
  secondary:
  - macro_outlook
  - financial_markets
tags:
- monetary-transmission
- MPTM
- interest-rate-channel
- credit-channel
- balance-sheet-channel
- financial-accelerator
- risk-taking-channel
confidence: 3
stability: stable
thesis: 'The monetary policy transmission mechanism (MPTM) maps the process by which
  central bank interest rate decisions propagate through 7 channels — interest rate,
  asset price, exchange rate, expectations, bank lending, bank capital, and balance
  sheet — to ultimately affect inflation and output. The "money view" channels (interest
  rate, asset price, exchange rate) assume efficient financial markets; the "credit
  view" channels (lending, capital, balance sheet) emphasize financial frictions,
  asymmetric information, and the financial accelerator. The risk-taking channel adds
  a post-GFC dimension: low rates reduce risk perception, inducing excessive risk-taking.
  Total lag from policy to full effect: typically 6-8 quarters.

  '
source_refs:
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-3.md
  pages: Ch.5 §5.1–5.4, pp.860-1109
  weight: primary
parent_node: null
related:
- node: '[[Monetary_Policy_Instruments_Operational_Framework]]'
  relation: starts_from
- node: '[[Inflation_Targeting_Framework_Central_Bank]]'
  relation: context_for
- node: '[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]'
  relation: initiates_via
- node: '[[Monetary_Policy_Transmission_Collateral_Channel]]'
  relation: specialized_channel_within
- node: '[[Collateral_Framework_Haircuts_Central_Bank_Credit]]'
  relation: affects_balance_sheet_channel
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:monetary-transmission
date_created: 2026-05-20
date_updated: 2026-05-20
---


## MPTM Overview Map

```
Central Bank Decision (Policy Rate + Monetary Operations)
          ↓
    [Financial Sector Stage]
    ├── Short-term rates (interbank → deposit → lending)
    ├── Exchange rates (via interest rate differential, UIP/CIP)
    ├── Asset prices (bonds, stocks, property)
    ├── Credit supply (volume + pricing)
    └── Expectations (inflation, growth, exchange rate)
          ↓
    [Real Economy Stage]
    ├── Aggregate demand (consumption + investment + net exports)
    └── Aggregate supply (cost of capital, wage contracts)
          ↓
    Final Targets: Inflation + Output
```

Lag profile: Financial sector responds in 1-6 months; real economy in 2-8 quarters. Exchange rate and asset prices react fastest (days-weeks); bank lending rates 3-6 months; output/inflation 6-8 quarters. [RAW-BOOK Perry §5.2.2]

**Complexity factors:**
1. Behavioral changes: bank behavior, risk appetite, expectation formation
2. Variable lags: longer in bank-dominated economies with underdeveloped capital markets
3. Channel dominance shifts: money supply channel dominant in less developed economies → interest rate/asset price channels dominant as markets develop
4. Asymmetry: rates rise faster than fall; tightening effect amplified vs. easing (financial accelerator)

---

## Money View Channels (Efficient Market Assumption)

### 1. Interest Rate Channel
**Core mechanism:**
```
Policy rate ↓ → Short-term interbank rate ↓ → Deposit/lending rates ↓
    ├→ User cost of capital ↓ → Business investment ↑ (neoclassical model)
    └→ Intertemporal substitution → Household consumption ↑
```

Transmission equation (reduced form):
```
Lending rate = f(policy rate, bank internal conditions: LDR, CAR, NPL, deposit mix)
```

Key caveat: Effectiveness depends on term structure — policy rate affects short-term rates; long-term investment decisions respond to long-term rates. Central bank must anchor long-term rate expectations through credibility. [RAW-BOOK Perry §5.3.1]

**Pass-through lag:** 3-6 months for deposit/lending rates to adjust (term deposits and loan agreements must mature first).

### 2. Asset Price Channel

**Sub-channel A: Tobin's q (Investment)**
```
Policy rate ↓ → Discount rate ↓ → Market value of firms ↑
→ Tobin's q = market value / replacement cost ↑
→ Investment ↑ (profitable to expand by issuing equity)
```

**Sub-channel B: Wealth Effect (Consumption)**
```
Policy rate ↓ → Bond yields ↓, stock prices ↑, property prices ↑
→ Household net worth ↑
→ Lifecycle/permanent income model: higher resources → consumption ↑
```

Portfolio formation follows Markowitz: households allocate across CB instruments (risk-free), deposits, bonds, stocks, physical assets. Policy rate change reallocates optimal portfolio → asset price adjustments. [RAW-BOOK Perry §5.3.2]

### 3. Exchange Rate Channel

**Trade mechanism:**
```
Policy rate ↓ → Domestic return ↓ vs. offshore → Capital outflow → Exchange rate depreciation
→ Exports ↑, Imports ↓ → Net exports ↑ → Output ↑
```

**Pass-through to inflation:**
- Direct: Imported goods prices rise immediately with depreciation
- Indirect: via net exports → output gap → inflation
- PPP benchmark: ∆p = α + β∆s + γ∆p* (pass-through coefficient β typically <1)

Pass-through lower in countries with: floating exchange rates, credible CB, low import dependence for consumer goods. [RAW-BOOK Perry §5.3.3]

### 4. Expectations Channel

```
CB signals future rate path (forward guidance, dot plot, communications)
→ Economic agents form expectations about inflation and growth
→ Inflation expectations affect real interest rates (Fisher effect: r_real = r_nominal - π_expected)
→ Real interest rates affect investment and consumption decisions
→ Supply side: corporate price setting responds to inflation expectations
```

Fisher equation applied: `i_e = r_f + π_e` → forward rates extract inflation expectations. [RAW-BOOK Perry §5.3.4]

**Credibility premium:** Higher CB credibility → smaller deviation of inflation expectations from target → smaller output/inflation distortions when policy adjusts.

---

## Credit View Channels (Financial Frictions)

The credit view builds on Bernanke-Gertler (1995): three empirical anomalies the money view cannot explain — (1) composition (durable goods respond more to short-term rates than the theory implies), (2) propagation (effects persist after rate reversal), (3) amplification (small rate changes trigger disproportionate output moves).

### 5. Bank Lending Channel (Stiglitz-Weiss, Bernanke-Blinder)

**Supply-side credit rationing:**
```
Asymmetric information → adverse selection → banks ration credit
Monetary tightening → bank funding constraints → lending supply ↓ (even without demand drop)
Effect concentrated on: bank-dependent borrowers (SMEs, households without capital market access)
```

Credit supply function:
```
Credit supply = f(lending rate r_k, economic outlook y, credit risk ρ_k, liquidity LDR, capital CAR)
```

Banks can price discriminate by borrower type: same funding rate → different lending rates based on monitoring cost + credit risk. Distributive effect of monetary policy on credit allocation. [RAW-BOOK Perry §5.4.1]

**Dominance conditions:** Bank lending channel strongest in bank-dominated economies with underdeveloped capital markets. In advanced economies with deep bond/equity markets, non-bank financing substitutes for bank credit → channel weaker.

### 6. Bank Capital Channel (Van den Heuvel)

```
Monetary tightening → higher NPLs, lower NIM, lower asset prices → bank capital ↓
→ CAR constraint binds → credit supply further constrained
→ Bank cannot issue equity (equity issuance costly in downturns)
→ Amplification of credit contraction beyond interest rate effect
```

Procyclicality dynamic:
- **Upswing:** Easing → NIM ↑ → profits ↑ → capital ↑ → credit expands more than rate effect
- **Downswing:** Tightening → NPL ↑ → capital ↓ → credit contracts more than rate effect (financial deleveraging cycle) [RAW-BOOK Perry §5.4.1]

### 7. Balance Sheet Channel — Financial Accelerator (Bernanke-Gertler-Gilchrist, Kiyotaki-Moore)

**External Finance Premium (EFP):**
```
Borrower private information → moral hazard risk → lender imposes EFP
EFP = premium over risk-free rate to cover cost of verification
EFP rises as borrower balance sheet weakens
```

**Financial Accelerator:**
```
Policy rate ↓ → Asset prices ↑ → Collateral value ↑ → EFP ↓ → Credit access ↑ → Investment ↑
    → Output ↑ → Asset prices ↑ further → [self-reinforcing upswing]

Policy rate ↑ → Asset prices ↓ → Collateral value ↓ → EFP ↑ → Credit constraint tightens
    → Investment ↓ → Output ↓ → Asset prices ↓ further → [self-reinforcing downswing]
```

Amplification: small shock to policy rate → amplified through balance sheet dynamics → disproportionate output response. Explains boom-bust cycles. [RAW-BOOK Perry §5.4.2]

**Collateral Constraints (Kiyotaki-Moore):**
Loan ceiling = f(collateral market value). When rates rise → asset prices fall → collateral value falls → credit ceiling falls → investment falls → feeds back to further asset price decline. Limited liability creates moral hazard that makes this channel operative.

### 8. Risk-Taking Channel (Borio-Zhu, Allen-Carletti — post-GFC addition)

```
Low rates for extended period →
    ├→ Banks reach for yield (risk tolerance ↑)
    ├→ Compression of risk premiums (VaR models show low volatility → reduced capital requirements)
    ├→ Asset price inflation → net worth ↑ → default probability ↓ (model-based)
    └→ Financial product innovation (derivatives proliferation, structured products)
             → Systemic risk accumulates outside traditional MPTM framework
```

Policy implication: Low rates not only stimulate real economy — they also reduce risk perception and encourage excessive leverage. Monetary policy easing through this channel can contribute to financial instability even while achieving short-term inflation/output targets. Foundation for post-GFC macroprudential policy mandate. [RAW-BOOK Perry §5.2.1 — Ch.15 reference]

---

## Channel Comparison Summary

| Channel | View | Key Mechanism | Lag | Dominant Where |
|---------|------|--------------|-----|----------------|
| Interest rate | Money | Cost of capital, intertemporal substitution | 3-6m financial; 6-8q real | All economies |
| Asset price (Tobin's q) | Money | Investment via market value of firm | 1-4q | Deep capital markets |
| Asset price (wealth) | Money | Consumption via household net worth | 2-6q | High household financial asset ownership |
| Exchange rate | Money | Net exports, import prices | Fast (1-3m) for prices; 2-4q for trade | Open economies, EMEs |
| Expectations | Money | Inflation expectations anchor real rates | Depends on credibility | ITF economies |
| Bank lending | Credit | Credit rationing via bank funding | 3-12m | Bank-dominated economies, SMEs |
| Bank capital | Credit | CAR-constrained lending | 1-4q | Post-crisis deleveraging |
| Balance sheet (EFP) | Credit | Financial accelerator via collateral | 2-8q | All — amplifies other channels |
| Risk-taking | Credit (post-GFC) | Risk perception compression → excessive leverage | 2-5yr | Low-rate environments |

---

## Implications for Monetary Policy Strategy

1. **Channel mapping before strategy**: Dominant channel in the economy determines the operational target and intermediate variables (money supply target if money channel dominant; interest rate target if interest rate channel dominant)

2. **Leading indicators** selection: Variables in dominant channel transmission path → inflation forecasting variables for forward-looking policy

3. **Lag management**: Policy must be pre-emptive and forward-looking given 6-8 quarter horizon. "Lean against the wind" requires acting before full transmission is visible

4. **Asymmetric effects**: Tightening may be more powerful than easing in downturns (financial accelerator dominant in downswings; credit rationing adds to interest rate effect)

5. **EME considerations**: Exchange rate channel important; capital flow volatility adds external transmission; macroprudential tools supplement interest rate when financial cycle diverges from business cycle

[See [[Inflation_Targeting_Framework_Central_Bank]] for post-GFC policy mix addressing the risk-taking channel via macroprudential policy]

