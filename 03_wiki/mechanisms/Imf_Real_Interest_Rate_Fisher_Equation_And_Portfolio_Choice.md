---
node_id: imf_real_interest_rate_fisher_equation_portfolio_choice_001
type: mechanism
title: IMF Real Interest Rate — Fisher Equation And Portfolio Choice
aliases:
  - Fisher equation
  - real interest rate
  - nominal vs real interest rate
  - portfolio choice theory
  - financial asset returns
  - rate of return decomposition
  - phương trình Fisher
  - lãi suất thực và danh nghĩa
  - lý thuyết lựa chọn danh mục tài sản
  - chi phí cơ hội nắm giữ tiền
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
  - fisher_equation
  - real_interest_rate
  - nominal_interest_rate
  - inflation_expectation
  - portfolio_choice
  - opportunity_cost_of_money
  - asset_substitution
  - financial_repression
  - imf_macro_accounting
  - monetary_analysis
confidence: 4
stability: stable
thesis: >
  The Fisher equation decomposes the nominal interest rate into a real rate plus
  expected inflation: Rr ≈ Rn − Pᵉ (approximate) or Rr = (Rn − Pᵉ)/(1 + Pᵉ)
  (exact). Portfolio choice theory classifies assets into four types (money,
  bonds/credit instruments, equities, real assets), with demand driven by expected
  return, riskiness, and liquidity. In high-inflation environments where real returns
  on financial assets are negative, rational agents substitute away from money and
  domestic bonds toward real assets or foreign currency — the mechanism behind
  dollarization and financial repression.
source_refs:
  - path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md
    pages: "lines 4798–4827 (Box 5.9: Interest Rates and Rates of Return — 4 asset types, rate of return decomposition, Fisher equation approximation and discrete form, negative real rates in transition, portfolio substitution to real assets)"
    weight: primary
related:
  - node: "[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]"
    relation: opportunity_cost_drives_money_demand
  - node: "[[Currency_Substitution_Dollarization_Monetary_Control]]"
    relation: negative_real_rates_trigger_dollarization
  - node: "[[Financial_Repression_Via_Reserve_Creation]]"
    relation: financial_repression_mechanism
  - node: "[[Transition_Economy_Monetary_Special_Issues]]"
    relation: negative_real_rates_common_in_transition
  - node: "[[Monetary_Policy_Transmission_Mechanisms_Framework]]"
    relation: rate_channel_foundation
date_created: "2026-05-25"
date_updated: "2026-05-25"
---

## Four Asset Types: The Portfolio Choice Framework

Portfolio (asset demand) theory identifies four types of assets people can hold, ranked by liquidity and rate of return [RAW-BOOK IMF Macro Box 5.9 p.4804]:

```
1. Money (currency + demand deposits)
   Liquidity: Highest (perfect liquidity — the medium of exchange)
   Return: Zero (currency) or very low (demand deposits)
   Risk: Zero nominal risk; full inflation risk in real terms

2. Bonds / Credit Market Instruments
   Liquidity: High (marketable securities)
   Return: Interest payments + capital gain/loss
   Risk: Moderate; interest rate risk (bond price falls when rates rise)

3. Equities / Stocks
   Liquidity: Moderate (exchange-traded) to low (private equity)
   Return: Dividends + capital gain/loss
   Risk: High (residual claim; volatile earnings)

4. Real (Tangible) Assets — property, gold, commodities, foreign currency
   Liquidity: Low (illiquid; transaction costs high)
   Return: Capital gain/loss + imputed rental/service flows
   Risk: High nominal uncertainty; often low real-term risk
```

**Demand for any asset is governed by three characteristics** [RAW-BOOK IMF Macro Box 5.9 p.4804]:
1. **Expected rate of return / yield** — relative to other assets
2. **Riskiness of the expected return** — variance of returns
3. **Liquidity** — ease of converting to means of payment

## Rate of Return Decomposition

The total rate of return on a financial asset has two components [RAW-BOOK IMF Macro Box 5.9 p.4804]:

```
Total Return = Periodic income component + Capital gain/loss component
             = (Interest or dividend received per period)
             + (Change in market price of asset per period)
```

**Key implication — currency has zero return:**
"As a holding, currency pays no interest. Demand or checking deposits usually pay zero or low rate of interest compared with less liquid forms of wealth. By holding money, people sacrifice the higher rate of return they could earn from more illiquid assets such as bonds or time deposits." [RAW-BOOK IMF Macro Box 5.9 p.4804]

This sacrifice is the **opportunity cost of holding money** — measured by the nominal interest rate on alternative assets. The higher the nominal rate, the greater the cost of holding money → the lower the money demand.

## Fisher Equation: Decomposing Nominal Into Real

In the presence of inflation, the nominal interest rate is not a reliable guide to the real cost of borrowing or the real return on saving. The Fisher equation separates the two [RAW-BOOK IMF Macro Box 5.9 p.4808]:

### Approximate Form (low inflation)
```
Rr ≈ Rn − Pᵉ

Where:
  Rn = nominal interest rate (%)
  Pᵉ = expected inflation rate (%)
  Rr = real interest rate (%)

Example: Rn = 10%, Pᵉ = 8% → Rr ≈ 2%
```

### Exact Form (high inflation — discrete compounding)
```
(1 + Rr) = (1 + Rn) / (1 + Pᵉ)

Or equivalently:
Rr = (Rn − Pᵉ) / (1 + Pᵉ)

Example: Rn = 10%, Pᵉ = 50% → Rr = (10 − 50) / (1 + 0.50) = −26.7%
         (vs. approximate: −40%)
```

"When the inflation rate is low, (Rn − Pᵉ) gives a good approximation of the actual real interest rate. For high inflation, the discrete form should be used." [RAW-BOOK IMF Macro Box 5.9 p.4822]

## Negative Real Rates: Distortions and Asset Substitution

In many transition economies, nominal rates appeared high but real rates were often negative because inflation exceeded nominal returns [RAW-BOOK IMF Macro Box 5.9 p.4826]:

```
Nominal rate appears high: Rn = 30%
Inflation rate:           Pᵉ = 50%
Real rate:                Rr ≈ −20%

Result: Lenders lose real purchasing power; borrowers gain in real terms.
        Savers are penalized for holding domestic financial assets.
```

**Why negative real rates are macroeconomically distortionary:**
"Since saving and investment respond to movements in the real rates of return, a negative real return on financial assets suggests a disincentive to save and an incentive to spend, aggravating inflationary pressures and hurting long-term prospects for economic growth." [RAW-BOOK IMF Macro Box 5.9 p.4826]

### Portfolio Substitution Response to Negative Real Rates

When domestic financial assets offer negative real returns:
```
Agents substitute toward:
  → Real assets: property, gold, commodities (preserve real value)
  → Foreign currency: hard currency with positive real return
  → Durable consumer goods (brought forward purchases)

Result:
  → Domestic money demand collapses (↑velocity)
  → Domestic savings system loses intermediation function
  → Dollarization accelerates
  → Investment in productive capital falls
  → Inflation pressure intensifies (↑velocity, ↑demand)
```

This substitution pattern is the micro-foundation for both **dollarization** (shift to foreign currency) and **financial repression** (forced holding of domestic assets at artificially low rates).

## Connection to Monetary Policy Analysis

The Fisher equation links to the IMF monetary framework in two ways:

### 1. Demand for Money (Opportunity Cost)
```
M^d / P = L(Y, i)
where i = nominal interest rate = Rn = Rr + Pᵉ

Higher i → lower money demand → higher velocity V
High inflation → rising i → rising V → quantity theory: same M generates more inflation
```

This is why velocity rises during high inflation episodes — the opportunity cost of holding money rises with inflation, driving down money demand relative to income [RAW-BOOK IMF Macro Ch.5].

### 2. Financial Programming: Real vs. Nominal Anchors
```
IMF programs often target:
  - Nominal targets: M2 growth ceiling, NDA ceiling
  - Real objective: stable real interest rates above zero

Negative real rates signal:
  → Monetary accommodation too loose relative to inflation
  → Asset substitution will undermine money demand projections
  → NDA target will be breached as velocity rises
```

## Diagnostic

```
Observed: High nominal interest rates + high inflation
→ Calculate real rate using discrete Fisher formula: Rr = (Rn − Pᵉ)/(1+Pᵉ)
→ If Rr < 0: financial repression; expect asset flight to real assets/FX

Observed: Rising velocity + falling domestic savings rate
→ Check real deposit rates: likely negative
→ Negative real rates → portfolio substitution → velocity jump

Observed: Dollarization ratio rising
→ Consistent with: nominal rates not compensating for inflation
→ Policy response: either raise nominal rates (restore real positive return)
   or reduce inflation (preserve real value without extreme nominal rates)

Policy rule for stabilization:
  Target Rr > 0 on domestic deposits
  → Restores incentive to hold domestic currency
  → Reverses dollarization over time
  → Reinforces domestic savings mobilization
```
