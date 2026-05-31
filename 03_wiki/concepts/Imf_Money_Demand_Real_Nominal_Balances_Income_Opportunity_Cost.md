---
node_id: imf_money_demand_real_nominal_balances_income_opportunity_cost_001
type: concept
title: IMF Money Demand — Real vs Nominal Balances, Income Elasticity, and Opportunity Cost
aliases:
- money demand function
- real money balances
- nominal money demand
- income elasticity of money demand
- opportunity cost of holding money
- functions of money
- medium of exchange store of value unit of account
- cầu tiền tệ
- số dư tiền thực
- chi phí cơ hội nắm giữ tiền
- co giãn thu nhập cầu tiền
domain:
  primary: monetary_policy
  secondary: []
tags:
- money_demand
- real_money_balances
- nominal_money
- income_elasticity
- opportunity_cost
- velocity
- inflation
- portfolio_choice
- quantity_theory
- imf_macro_accounting
confidence: 3
stability: stable
thesis: 'Money demand is fundamentally a demand for real money balances (M/P) — what
  money can buy — not for a given number of currency units. In simplified form, real
  cash balance demand is positively related to real income and negatively related to
  the opportunity cost of holding money (nominal interest rate or expected inflation).
  If income elasticity equals 1, velocity is constant and the quantity theory holds
  cleanly; if elasticity < 1, velocity rises with income (more efficient payment technology);
  if elasticity > 1, velocity falls (luxury good interpretation of money). In hyperinflation,
  expected inflation supplants the nominal interest rate as the dominant opportunity
  cost, collapsing real money demand to a transaction minimum.'
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 4625–4700 (functions of money, real vs nominal balances, demand for
    money positively related to income and negatively to opportunity cost, income elasticity
    and velocity, Box 5.9 interest rates and portfolio choice, Box 5.10 hyperinflation
    and real money collapse)
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]'
  relation: money_demand_is_inverse_of_velocity_same_phenomenon
- node: '[[Imf_Real_Interest_Rate_Fisher_Equation_And_Portfolio_Choice]]'
  relation: opportunity_cost_measure_is_real_interest_rate
- node: '[[Transition_Economy_Monetary_Special_Issues]]'
  relation: velocity_jumps_in_transition_reflect_unstable_money_demand
- node: '[[Currency_Substitution_Dollarization_Monetary_Control]]'
  relation: dollarization_shifts_money_demand_to_FX_assets
- node: '[[Imf_Five_Monetary_Policy_Instruments_Reserve_Money_Control]]'
  relation: money_demand_determines_how_much_RM_translates_to_inflation
date_created: '2026-05-31'
date_updated: '2026-05-31'
---

## The Three Functions of Money

Money serves three functions in a market economy [RAW-BOOK IMF-macro p.4629-4633]:

| Function | Motive | Relationship to demand |
|----------|--------|----------------------|
| Medium of exchange | Transactions motive | Proportional to volume of transactions / income |
| Store of value | Portfolio/speculative motive | Sensitive to rate of return relative to other assets |
| Unit of account | Denominates prices, contracts | Not a liquidity function — institutional role |

The transactions motive (medium of exchange) drives the core money demand function. The store-of-value motive drives the **opportunity cost sensitivity** — when alternative assets offer higher returns, money becomes a costly store of value and demand falls.

"Money is defined here as a widely accepted means of payment or a medium of exchange." [RAW-BOOK IMF-macro p.4417 fn10]

---

## Real vs. Nominal Money Balances — A Critical Distinction

**Nominal money demand**: demand for a given number of currency units (e.g., rubles, zlotys).

**Real money demand**: demand for M/P — money expressed in terms of what it can purchase.

"The demand for money is fundamentally a demand for real money balances, because people hold money for what it can buy." [RAW-BOOK IMF-macro p.4685]

**Why the distinction matters for policy:**

```
If the CB doubles the money supply (M) and prices double (P):
  Real balances M/P are unchanged
  → No new purchasing power in the hands of the public
  → No real effect (at least in the long run)

If the CB doubles M but prices are sticky (P unchanged):
  Real balances M/P double temporarily
  → Excess real balances → spending rises → prices eventually catch up
  → Inflation is the mechanism that restores real balance equilibrium
```

This is why the quantity theory works as an inflation predictor: sustained excess money growth above real income growth → inflation (not permanent real wealth increase).

---

## The Money Demand Function

The simplified IMF money demand function [RAW-BOOK IMF-macro p.4687-4700]:

```
L(Y, i) = f(real income, opportunity cost)

Where:
  L = real money balances demanded (M/P)
  Y = real income (GDP proxy for transaction volume)
  i = opportunity cost of holding money (nominal interest rate OR expected inflation)

Partial derivatives:
  ∂L/∂Y > 0   (income effect — positive)
  ∂L/∂i < 0   (opportunity cost effect — negative)
```

In the quantity theory framework, this is connected to velocity:

```
M × V = P × Y   →   M/P = (1/V) × Y

(1/V) is the Cambridge k — the fraction of nominal income held as money balances

Velocity V = 1/k = PY/M
```

"Velocity and money demand are inversely related. They are essentially equivalent ways of describing the same phenomenon." [RAW-BOOK IMF-macro p.4669]

---

## Income Effect: Real Income and Transactions Demand

As real income grows, agents need more money to conduct a larger volume of transactions. The strength of this relationship is captured by the **income elasticity of money demand** (η):

```
η = % change in real money demand / % change in real income
```

Three cases and their velocity implications [RAW-BOOK IMF-macro p.4694 fn21]:

| Income Elasticity η | Interpretation | Velocity behavior with income ↑ |
|--------------------|-----------------|---------------------------------|
| η = 1 | Money demand grows proportionally with income | V is constant (classic QTM) |
| η < 1 | Less than proportional — payment technology improves as economies grow | V rises with income |
| η > 1 | More than proportional — money is a "luxury" good | V falls with income |

**Empirical pattern for developing/transition economies:** As the banking system deepens and access to banking expands, money demand tends to outpace income growth (η > 1 initially) → velocity falls during financial deepening. This is a key source of velocity instability in transition economies where structural change is rapid. [RAW-BOOK IMF-macro p.4874]

---

## Opportunity Cost Effect: Interest Rates and Inflation

**In financially developed economies:** The opportunity cost of holding money is the nominal interest rate — the return forgone by not holding interest-bearing bonds.

```
Opportunity cost = i (nominal interest rate)
Money demand: L falls as i rises
Mechanism: Higher rates → bonds, time deposits more attractive → shift from M1 to quasi-money
```

**In high-inflation economies:** The nominal interest rate may be administratively controlled (financial repression) or may cease to function. Expected inflation (πᵉ) becomes the dominant opportunity cost:

```
Expected inflation πᵉ → real value of money holdings erodes at rate πᵉ per period
Cost of holding money per period = πᵉ × (real money holdings)
```

"In cases of hyperinflation, the opportunity cost of holding money becomes too high and the demand for money is drastically reduced." [RAW-BOOK IMF-macro p.4700]

**Portfolio choice framework (Box 5.9):** Agents hold four asset types [RAW-BOOK IMF-macro p.4804]:

```
1. Money (currency, demand deposits) — near-zero return, maximum liquidity
2. Interest-bearing financial assets (bonds, credit instruments) — interest + capital gain/loss
3. Equities/stocks — dividends + capital appreciation, highest risk
4. Real assets (property, gold, commodities) — inflation hedge, illiquid

Decision rule for each asset: Expected return, riskiness, liquidity

When real return on financial assets → negative (high inflation):
  Agents shift from (1) and (2) → (4) [real assets] or (1_FX) [foreign currency]
  → Dollarization and de-monetization
```

---

## Hyperinflation: Collapse of Real Money Demand

Box 5.10 of the IMF text documents the extreme case [RAW-BOOK IMF-macro p.4892-4894]:

**Cagan definition:** Hyperinflation = monthly price increase ≥ 50%, sustained for several months.

**Key empirical findings across historical hyperinflations:**

```
Finding 1 — Real money demand collapses:
  Germany 1920s: Real money demand at end = 1/30th of level two years prior
  Mechanism: πᵉ dominates all other considerations → minimize money holdings

Finding 2 — Nominal interest rates become useless:
  At high inflation, lending at prescribed nominal rates virtually disappears
  → Best indicator of cost of holding money = expected inflation (not market rate)

Finding 3 — Highly variable inflation:
  Germany 1921-1923: Monthly inflation ranged from 0% to 500%
  → Large uncertainty → impossible to plan → massive social disruption from
     arbitrary wealth redistribution (debtors gain, creditors lose in real terms)
```

**Post-stabilization persistence:** "Even with actual sharp reductions in inflation, the demand for real balances remains subdued. Countries that have maintained an aggressive interest rate policy to ensure a positive real rate of return on domestic monetary assets have succeeded in restoring confidence in the domestic currency relatively quickly." [RAW-BOOK IMF-macro p.4874]

---

## Implications for Monetary Policy Design

**1. Quantity theory usability condition:**

```
M growth → inflation IF AND ONLY IF:
  (a) Velocity is stable or predictably changing
  (b) Y growth is known (potential output)

If velocity is unstable → M target may miss inflation target completely
```

**2. Calibrating reserve money targets:**

When setting an RM target in a financial program:

```
Step 1: Set inflation target (π*)
Step 2: Estimate real output growth (ẏ)
Step 3: Forecast velocity change (v̇)
Step 4: M2 growth = π* + ẏ + v̇ (from quantity equation in growth form)
Step 5: RM growth = M2 growth − multiplier growth
```

If v̇ is positive (velocity rising — typical in high-inflation environments with shrinking real balances), M2 target can be lower than output growth + inflation. If v̇ is negative (financial deepening — typical in stabilizing transition economies), M2 target must be higher than output + inflation to accommodate rising money demand.

**3. Indicator of monetary tightness:**

Real interest rate = nominal rate − expected inflation. When this is negative in a country, the CB is imposing a tax on savers (financial repression), suppressing money demand artificially. Restoration of positive real rates is a prerequisite for rebuilding money demand and stabilizing velocity. [RAW-BOOK IMF-macro p.4826 Box 5.9]
