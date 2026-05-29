---
node_id: imf_monetary_aggregate_targeting_innovation_controllability_001
type: framework
title: IMF Monetary Aggregate Targeting — Financial Innovation, Broader Aggregates,
  and the Controllability-Relevance Dilemma
aliases:
- monetary aggregate targeting
- M3 M4 L aggregates
- financial innovation velocity
- controllability vs relevance
- eclectic monetary indicators
- near-money assets
- mục tiêu tổng tiền tệ
- đổi mới tài chính và tốc độ lưu thông tiền tệ
- tính kiểm soát so với tính liên quan
domain:
  primary: monetary_policy
tags:
- monetary_aggregate
- financial_innovation
- velocity
- m3_m4
- controllability
- relevance
- near_money
- intermediate_target
- monetary_policy_indicators
- imf_macro_accounting
- money_demand
confidence: 4
stability: stable
thesis: 'Financial innovation blurs the boundary between money and near-money assets
  (demand deposits earning interest, liquid mutual funds), making M1 and M2 velocity
  unstable and potentially unreliable as intermediate monetary policy targets. Broader
  aggregates M3/M4/L are more "relevant" (better linked to aggregate demand) but less
  "controllable" (no reserve requirements, issued by non-bank institutions). This
  creates a fundamental dilemma: the aggregate most relevant to aggregate demand is
  the least controllable. The IMF solution is an eclectic multi-indicator approach
  — use monetary aggregates alongside interest rates, the yield curve, and the exchange
  rate.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 4764–4776 (financial innovation, velocity instability, controllability-relevance
    dilemma, eclectic approach), lines 4570–4579 (M3/M4/L aggregate definitions, broader
    money spectrum)
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]'
  relation: velocity_instability_from_innovation_modifies_quantity_theory
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: M2_is_core_of_monetary_survey_but_innovation_pushes_toward_M3_M4
- node: '[[Imf_Money_Multiplier_Ratio_Decomposition_Three_Agent]]'
  relation: near_money_outside_banking_system_breaks_multiplier_relationship
- node: '[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]'
  relation: NDA_ceiling_targets_M2_but_innovation_complicates_targeting
- node: '[[Imf_Real_Interest_Rate_Fisher_Equation_And_Portfolio_Choice]]'
  relation: portfolio_shifts_driven_by_near_money_returns_explain_velocity_instability
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## The Problem: Financial Innovation Blurs the Money Boundary

Standard monetary analysis relies on a stable money demand function. Financial innovation disrupts this in two ways:

**1. Near-money assets become more liquid:**
- Demand deposits now earn interest comparable to bonds → people hold deposits for return, not just transactions
- Mutual funds investing in stocks/bonds become easily withdrawable → bonds and stocks approach money-like liquidity
- Result: the line between "money" and "near-money" shifts continuously [RAW-BOOK IMF-macro p.4764]

**2. Velocity of M1/M2 becomes unstable:**
- When households shift between M2 and near-money assets, M2 velocity fluctuates without proportional changes in aggregate demand
- "Rapid changes in households' holdings of money and near-money assets can make the velocity of money (either M1 or M2) unstable. Thus, the quantity of money can be an unreliable guide to changes in aggregate demand." [RAW-BOOK IMF-macro p.4774]

---

## The Monetary Aggregate Spectrum

From narrow to broad [RAW-BOOK IMF-macro p.4570]:

```
M1 (Narrow Money)
  Currency outside banks
  + Demand deposits
  ─────────────────────────────────────────────
M2 (Broad Money)
  = M1
  + Quasi-money: time deposits, savings deposits
  + Foreign currency deposits of residents
  + Certificates of deposit
  + Security repurchase agreements
  ─────────────────────────────────────────────
M3
  = M2
  + Travelers checks
  + Commercial papers (money market mutual funds,
    cash vouchers)
  + Wider range of instruments and institutions
  ─────────────────────────────────────────────
M4
  = M3
  + Liquid government securities
  + Negotiable bonds
  + Liabilities of other financial intermediaries
  ─────────────────────────────────────────────
L (Liquidity)
  = M4
  + Less liquid financial assets: T-bills, govt bonds,
    mortgage bonds, some corporate bonds
```

**Direction of change:**
- Broader → more "relevant" (closer to total liquidity influencing demand)
- Broader → less "controllable" (no reserve requirements, issued outside banking system)

---

## The Controllability–Relevance Dilemma

| Aggregate | Relevance to AD | Controllability | Reserve Requirements |
|-----------|----------------|-----------------|----------------------|
| M1 | Transactions-driven | High | Direct (on demand deposits) |
| M2 | Good for most economies | High-Medium | Direct (time/savings deposits) |
| M3 | Better in financially developed economies | Medium | Partial (money market instruments) |
| M4 | Broader liquidity | Low | Minimal |
| L | Full liquidity | Very Low | None |

**Core tension:** [RAW-BOOK IMF-macro p.4774-4775]
> "The broader the monetary aggregate, the less ability the monetary authorities have to control it, since many forms of near money have no reserve requirement and are issued by institutions outside the banking system. The authorities therefore face a dilemma: they may adopt a broader, 'more relevant' monetary aggregate for targeting but will have less control over it."

**Pitfall of cherry-picking:**
Policymakers tempted to use "the aggregate that gives the most favorable data" at a particular time — but this misleads both policymakers and the public. [RAW-BOOK IMF-macro p.4776]

---

## The IMF Solution: Eclectic Multi-Indicator Approach

When monetary aggregates become unstable guides, the IMF recommends a broader set of indicators [RAW-BOOK IMF-macro p.4776]:

```
Monetary indicators toolkit:
  1. Monetary aggregates (M1, M2, or M3 where appropriate)
  2. Nominal and real interest rates
  3. Yield curve (structure of interest rates by maturity)
  4. Exchange rate behavior
  5. Credit growth (CPS as real sector proxy)
```

**For transition economies specifically:** Given rapid structural and behavioral changes, adopt an eclectic approach toward the choice of intermediate monetary targets and monetary indicators — no single aggregate reliably captures conditions. [RAW-BOOK IMF-macro p.4776]

---

## Implications for IMF Financial Programming

The NDA ceiling in IMF programs typically targets M2 (as defined in the monetary survey) rather than M3/M4:
- M2 is directly observable and controlled via the banking survey
- M3/M4 require data on other financial institutions (OFIs) — less timely
- But in financially developed economies, if M2 velocity is unstable, the M2-based NDA ceiling may miss aggregate demand developments

**Transition economy calibration challenge:** In early transition, as velocity falls sharply (financial deepening begins, money demand rises), the NDA ceiling must be recalibrated — a given M2 target may correspond to very different aggregate demand outcomes depending on velocity. This is precisely why the IMF uses the quantity equation in growth form (`ṁ = ṗ + ẏ + v̇`) and explicitly models velocity change when setting M2 targets. [RAW-BOOK IMF-macro p.4672-4673]

---

## Worked Example: Financial Deepening and M2 Targeting

```
Assumption: CB targets M2 growth = 12%

Case A — Constant velocity (V):
  ṁ = ṗ + ẏ + v̇ → 12% = π + 5% + 0%
  → π = 7% (inflation)

Case B — Financial deepening (V falling 5%/year):
  12% = π + 5% + (−5%)
  → π = 12% → problem solved? NO:
  → The M2 growth of 12% is consistent with ONLY 2% inflation
  → If CB targets 12% M2 mechanically, actual inflation = 2%, not 7%
  → The CB would UNDERESTIMATE money demand and create INSUFFICIENT money supply
  [LLM-E: illustrative example]

Conclusion: When V changes, fixed M2 target requires V forecast to avoid errors.
```

---

## Policy Takeaway

The fundamental insight: "present definitions of money are likely to change in the future." [RAW-BOOK IMF-macro p.4579] Monetary policy must adapt its choice of intermediate target as the financial system evolves. The hierarchy is:

```
Primary target: Price stability (ultimate goal)
           ↑
Intermediate: M2 (if velocity is stable), M3 (if M2 velocity unstable)
           ↑
Operating: Reserve money (RM) / short-term interest rate
           ↑
Instrument: OMO / discount window / reserve requirements
```

When financial innovation destabilizes the intermediate-to-ultimate link, the CB may need to skip directly to targeting the operating instrument (interest rate) and rely on the transmission mechanism to reach price stability — the logic behind inflation targeting replacing monetary targeting in many countries.
