---
node_id: imf_inflation_analysis_cpi_gdp_deflator_four_types_core_001
type: framework
title: IMF Inflation Analysis — CPI vs GDP Deflator, Four Inflation Types, Core vs Underlying
aliases:
  - inflation taxonomy IMF
  - CPI versus GDP deflator
  - four types of inflation
  - core inflation underlying inflation
  - policy-induced inflation
  - inertial inflation NAIRU
  - phân tích lạm phát IMF
  - lạm phát cơ bản vs lạm phát đo lường
  - bốn loại lạm phát
  - chỉ số CPI vs deflator GDP
  - lạm phát quán tính NAIRU
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
  - inflation
  - cpi
  - gdp_deflator
  - core_inflation
  - nairu
  - cost_push
  - demand_pull
  - inertial_inflation
  - price_measurement
  - monetary_policy_framework
  - em_policy
confidence: 4
stability: stable
thesis: >
  The IMF inflation analysis framework distinguishes four causal types (policy-induced,
  cost-push, demand-pull, inertial) and two measurement dimensions (one-time price-level
  shift vs. sustained inflation rate; measured vs. core/underlying inflation). The CPI
  and GDP deflator measure different things: coverage (consumer vs. all production),
  treatment of imports (included in CPI, excluded from deflator), and aggregation method
  (Laspeyres fixed-basket vs. Paasche current-basket). Core/underlying inflation —
  abstracting from discrete one-off shocks — is the policy-relevant variable, especially
  in transition and EM economies with frequent administered-price adjustments.
source_refs:
  - path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md
    pages: "lines 878–927 (inflation measurement and types: CPI vs GDP deflator, 4 inflation categories, core/underlying, Japan non-accommodation, NAIRU)"
    weight: primary
related:
  - node: "[[Imf_Gfs_Fiscal_Accounting_Framework_Deficit_Measurement_And_Sustainability]]"
    relation: fiscal_inflation_nexus
  - node: "[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]"
    relation: monetary_program_context
  - node: "[[Central_Bank_Credibility_Supply_Shock_Policy_Space]]"
    relation: policy_response_framework
  - node: "[[EM_Central_Bank_Policy_Mix_FIT_Framework]]"
    relation: modern_equivalent
date_created: "2026-05-24"
date_updated: "2026-05-24"
---

## Core Distinction: One-Time Price Level vs. Sustained Inflation

The most important analytical distinction in inflation analysis is between a **one-time increase in the price level** and **persistent, sustained inflation**:

```
One-time price shock:
  Event → Price level jumps → Stabilizes at new level
  Examples: administered price hike, excise tax increase, discrete devaluation
  → Does NOT add to underlying/core inflation IF monetary policy holds firm

Sustained inflation:
  ΔP/P > 0 every period, persistent increase in the overall price level
  → Requires continuous money supply expansion (monetary accommodation)
```

"A rise in administered prices will raise the overall level of prices in the first instance. However, this increase will in turn bring about the needed relative price changes without necessarily adding to underlying, or core inflation, which reflects the basic changes in the overall price level, abstracting from unusual, one-time increases caused by events such as increases in administered prices and excise taxes or discrete devaluations of the exchange rate." [RAW-BOOK IMF Macro p.888]

**Policy implication:** A central bank facing a one-time cost shock (oil, energy, food) does not need to tighten if the shock does not trigger second-round wage/price effects. Japan's response to the 1970s oil shock is the canonical example: "Japan...managed to keep inflation under control because the authorities followed non-accommodating financial policies and the population accepted a temporary reduction in real incomes." [RAW-BOOK IMF Macro p.890]

The moment monetary policy **accommodates** a cost shock (expands money supply to prevent real income decline), the one-time price level shift becomes sustained inflation. This is the cost-push phenomenon — triggered by supply, amplified by monetary policy.

---

## CPI vs. GDP Deflator — Three Key Differences

Both indices measure "inflation" but measure different things. The divergence matters significantly when:
- Import prices change sharply (energy shocks, currency depreciation)
- Relative prices shift between consumer and producer goods
- Productivity growth differs between sectors

### Difference 1 — Coverage: Consumer vs. All Production

```
CPI: Measures only goods and services bought by the average consumer
     → Excludes: machinery, equipment, intermediate goods bought by firms
     → Excludes: government procurement (defense, public investment)

GDP Deflator: Measures ALL goods and services produced in the economy
     → Includes: capital goods, government output, business services
     → Includes: changes in producer prices throughout the production chain
```

An increase in machinery prices → visible in GDP deflator, invisible in CPI. [RAW-BOOK IMF Macro p.905]

### Difference 2 — Import Coverage: Domestic Production Only vs. Consumer Basket

```
GDP Deflator: Covers only domestically produced goods
              → A change in import prices has NO direct impact on the GDP deflator
              (imports are netted out in GDP = C + I + G + X − M)

CPI: Includes imported goods in the consumer basket
     → A currency depreciation immediately raises CPI through import prices
     → In open EMs with high import dependence: FX depreciation → CPI spike
```

This divergence is most significant for EM economies with high import shares (Vietnam: fuel, raw materials ~30% of imports). A currency depreciation appears in CPI but not in the GDP deflator. [RAW-BOOK IMF Macro p.907]

### Difference 3 — Index Type: Laspeyres vs. Paasche

```
CPI (Laspeyres — fixed-weight index):
  Uses base-year quantities as weights — the basket is fixed
  Advantage: Comparable over time (consistent basket)
  Bias: OVERSTATES inflation by ignoring substitution effects
        (consumers switch away from expensive goods, but the index
         keeps weighting the now-expensive goods at their old share)

GDP Deflator (Paasche — current-weight index):
  Uses current-year quantities as weights — the basket shifts with production
  Advantage: Reflects actual current composition of output
  Bias: UNDERSTATES inflation (upweights goods whose relative price fell
        because output shifted toward cheaper goods)
```

"The fixed weight index (Laspeyres index) ignores the so-called substitution effects among products...It therefore tends to **overstate inflation**. The flexible weight index (Paasche index), on the other hand, tends to **understate the extent of inflation**." [RAW-BOOK IMF Macro p.911]

**Practical implication for analyst:** When CPI inflation > GDP deflator, typically reflects either import price pass-through OR consumer substitution ignored by the fixed basket. Large CPI–deflator divergence signals composition-of-demand shift that the CPI misses.

---

## The Four Inflation Types

The IMF framework identifies four causal categories of inflation. They differ in their preconditions, persistence, and correct policy response.

### Type 1 — Policy-Induced Inflation

```
Cause:     Excessive fiscal deficit → monetary financing → M expansion
Condition: Government cannot or will not close deficit through taxes/spending cuts
Persistence: High — self-perpetuating through expectations and fiscal pressure
Examples:  Germany/Austria hyperinflations 1920s; many EM high-inflation episodes

Policy fix: Fiscal consolidation is prerequisite; monetary tightening alone is temporary
```

"Policy-induced inflation, which is often caused by expansionary monetary measures that reflect excessive fiscal deficits and their monetary financing, is often at the root of high inflations." [RAW-BOOK IMF Macro p.919]

Non-policy-induced inflation: caused by exogenous factors (drought, external shock). Does not require monetary accommodation but CAN become policy-induced if accommodated.

### Type 2 — Cost-Push Inflation

```
Cause:     Rising production costs (wages outpacing productivity; energy prices)
Condition: Labor market structure allows wage-price spiral; monetary policy accommodates
           OR: can develop even at high unemployment if sector-specific
Persistence: Medium — depends on accommodation and second-round wage effects

Key mechanism: Wages are the dominant production cost; wage > productivity growth
               → unit labor cost rises → firms raise prices → workers demand higher wages
               → spiral continues if monetary policy validates
```

"Cost-push inflation is caused by rising costs and may develop even when unemployment is high and resource utilization low...cost-push inflation cannot persist if monetary policy refuses to accommodate it, in which case the wage increases lead to higher unemployment rather than higher inflation." [RAW-BOOK IMF Macro p.920–921]

The accommodation decision is the critical policy variable: non-accommodation converts cost-push from an inflation problem into an unemployment problem.

### Type 3 — Demand-Pull Inflation

```
Cause:     Excess aggregate demand pushing up prices
Source:    Internal (overly expansionary fiscal/monetary policy)
           OR External shock (commodity export boom, terms of trade improvement)
Condition: Actual output > potential output (positive output gap)
Persistence: Depends on whether demand expansion persists and expectations adjust
```

"Demand-pull inflation is caused by excess aggregate demand pushing up the overall price level. The boost to demand can come from internal or external shocks but frequently results from overly expansionary monetary and fiscal policies." [RAW-BOOK IMF Macro p.922]

### Type 4 — Inertial Inflation

```
Cause:     Embedded in wage and financial contracts (indexation)
Condition: Prevailing rate anticipated → written into all contracts → self-perpetuating
Persistence: Highest — the defining characteristic; changes only through policy shock
             or credible disinflation anchoring expectations

This is the core/underlying rate referenced in policy analysis
```

"Inertial inflation tends to persist at the same rate until economic events cause it to change...Most modern inflation is classified as inertial. The inertial inflation rate is sometimes referred to as the core or underlying inflation rate." [RAW-BOOK IMF Macro p.923]

**Key insight:** Shocks (supply or demand side) cause actual inflation to move above or below the inertial rate temporarily. The policy challenge is preventing temporary deviations from ratcheting the inertial rate upward through expectations adjustment.

---

## Core vs. Measured Inflation: The Policy-Relevant Variable

For policymakers — especially in EM and transition economies — the critical variable is **underlying (core) inflation**, not the measured CPI rate:

```
Measured CPI inflation = Core/underlying inflation
                       + One-time price level components
                       + Import price pass-through (exchange rate effects)
                       + Seasonal food/energy components
```

"While the underlying rate of inflation is not always easy to measure precisely, it can be estimated and may provide a **better guide to policy** than the measured rate of price inflation. Especially in the transition economies, analysts should focus on the underlying rate of inflation rather than on the measured rate of inflation because of the structural changes and reforms taking place, which inevitably result in a number of discrete adjustments in the prices of many goods and services." [RAW-BOOK IMF Macro p.888]

**Practical consequence:** In Vietnam, CPI spikes driven by energy price adjustments or FX pass-through are not by themselves evidence of monetary excess. The relevant diagnostic is whether core inflation (ex-energy, ex-food, or ex-administered prices) is rising — that signals demand pressure or embedded inertia. [LLM — applied to Vietnam context]

---

## NAIRU: The Employment-Inflation Link

The **Non-Accelerating Inflation Rate of Unemployment (NAIRU)** defines the level of unemployment consistent with stable inflation:

```
Actual unemployment > NAIRU  → Deflationary pressure (output gap negative)
Actual unemployment < NAIRU  → Inflationary pressure (output gap positive)
Actual unemployment = NAIRU  → Stable inflation (neutral stance)
```

"The Non-Accelerating Inflation Rate of Unemployment, or NAIRU, is an equilibrium rate of unemployment. The NAIRU is defined as the rate of joblessness that is compatible with a stable rate of inflation." [RAW-BOOK IMF Macro p.952]

Five types of unemployment are distinguished by the IMF framework:
1. **Seasonal** — calendar-driven shifts in supply/demand (agriculture, tourism)
2. **Frictional** — job-matching lag; not long-lasting; contributes to better job matches
3. **Cyclical** — recession-driven; most responsive to demand stimulus
4. **Structural** — skill/geographic mismatch; hard to cure without retraining
5. **Disguised** — marginal product of worker ≈ 0; economy benefits from reallocation

**NAIRU analytical implication:** In inflation targeting frameworks, the output gap (actual vs. potential GDP) and unemployment gap (actual vs. NAIRU) are the key leading indicators of inflationary pressure — ahead of actual CPI movement, which reflects past conditions.

---

## Diagnostic

```
SIGNAL: CPI >> GDP deflator in same period
→ Import price pass-through dominant (FX depreciation; oil shock)
→ Policy-relevant question: Is core inflation rising too?
→ If core stable: one-time level shift; no accommodation needed

SIGNAL: Core inflation rising despite stable CPI (e.g., food/energy falling)
→ Domestic demand pressure; inertial expectations building
→ Requires tightening to prevent inertia from embedding

SIGNAL: Wage growth persistently > productivity growth
→ Cost-push channel active
→ Policy choice: tighten (higher unemployment) or accommodate (higher inflation)
→ Non-accommodation is correct if inflation expectations still anchored

SIGNAL: Inflation persistent despite fiscal consolidation
→ Inertial component dominant
→ Requires credible disinflation program (heterodox stabilization or IT framework)
→ Wage/price controls as temporary complement to monetary anchor

SIGNAL: Measured inflation spike with administered price adjustments
→ One-time level shift; NOT sustained inflation
→ Focus on second-round effects: do wages respond?
→ If wages stable: monetary policy can hold; one-off shock absorbed
```
