---
node_id: enhanced_taylor_rule_eme_fx_augmented_001
type: mechanism
title: Enhanced Taylor Rule for EME — FX Deviation Augmentation
aliases:
- augmented Taylor rule EME
- FX-augmented Taylor rule
- exchange rate in monetary policy rule
- enhanced rule open economy
- Taylor rule exchange rate pass-through
- quy tắc Taylor mở rộng cho EM
- quy tắc lãi suất có tỷ giá
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- taylor_rule
- fx_intervention
- monetary_policy_rule
- open_economy
- exchange_rate_passthrough
- em_policy
- inflation_targeting
- interest_rate
confidence: 3
stability: stable
thesis: 'Standard Taylor rules (inflation deviation + output gap → interest rate)
  are incomplete for EMEs with significant exchange rate pass-through to inflation.
  An FX-augmented ("enhanced") Taylor rule adds real exchange rate deviation from
  equilibrium as a third driver of the policy rate. Empirical estimates show this
  coefficient ranges from 0 (pure IT countries like Chile) to 0.8 (Mexico) with Indonesia
  at 0.3, reflecting how directly the exchange rate feeds into the CB''s reaction
  function. The enhanced rule produces better R-squared fit and more optimal countercyclical
  response than the standard rule in high-pass-through EMEs. [LLM]

  '
source_refs:
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: lines 273–285 (Enhanced Taylor rule specification, Indonesia/Chile/Mexico
    coefficients)
  weight: primary
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-4.md
  pages: 'lines 516–524 (Taylor rule open economy extension, Ball 1997; Svensson 1997a);
    lines 574–575 (exchange rate as operational target: Singapore, Hong Kong)'
  weight: secondary
parent_node: null
related:
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: operational_implementation
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: monetizes_fx_target_into_rate_rule
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: interaction_through_capital_flows
- node: '[[Inflation_Targeting_Framework_Central_Bank]]'
  relation: open_economy_extension
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Standard vs Enhanced Taylor Rule

**Standard Taylor rule** (Taylor 1993, for closed economy or ignoring FX):
```
i_t = i* + α(π_t − π*) + β(y_t − y*)

Where:
  i_t   = nominal policy rate
  i*    = long-run equilibrium rate
  α     = inflation response coefficient (typically > 1 per Taylor principle)
  β     = output gap response coefficient
  π*    = inflation target
  y*    = potential output
```

**Enhanced (augmented) Taylor rule** for open EMEs [RAW-BOOK Perry p.279]:
```
i_t = i* + α(π_t − π*) + β(y_t − y*) + γ_e × e_t + δ × i_{t-1}

Where:
  e_t  = real exchange rate deviation from equilibrium value
  γ_e  = exchange rate response coefficient
  δ    = interest rate smoothing parameter (inertia / gradual adjustment)
```

The enhanced rule is an "interesting format because it takes into consideration the flexibility of the exchange rate's role" for small open economies. [RAW-BOOK Perry p.279]

---

## Theoretical Justification

Two channels justify including `e_t` in the monetary policy rule:

**Channel 1 — Direct pass-through to inflation**
In small open EMEs, imported goods make up a large share of the CPI basket. Exchange rate depreciation directly raises import prices → CPI → requires tighter policy to offset. A CB ignoring `e_t` will systematically underreact to depreciation-driven inflation. [RAW-BOOK Perry p.279 + Ball 1997]

**Channel 2 — Aggregate demand via competitiveness**
Real appreciation compresses net exports → contractionary demand effect → may warrant looser policy than the inflation/output gap alone suggest. Symmetrically, real depreciation stimulates demand → inflationary → tighter policy warranted. [LLM — Ball 1997 extension]

**Svensson (1997a)** and **Ball (1997)** provide the theoretical basis: in an open economy, exchange rate changes affect both the supply side (import costs) and demand side (net exports), making the FX term a legitimate addition to the loss-minimizing reaction function. [RAW-BOOK Perry p.522]

---

## Empirical Coefficient Estimates: γ_e

Cross-country variation in `γ_e` reflects the degree of exchange rate pass-through and the CB's revealed preference for FX stabilization:

| Country | γ_e estimate | Interpretation |
|---------|-------------|----------------|
| **Chile** | ≈ 0 | Pure IT: FX freely floats; CB does not respond to exchange rate deviations |
| **Indonesia (BI)** | ≈ 0.3 | Moderate FX response: CB adjusts rate for ~30% of exchange rate gap |
| **Mexico (Banxico)** | ≈ 0.8 | High FX response: exchange rate strongly integrated into rate decision |

Source: Juhro and Mochtar (2009) for Indonesia; Edwards (2006) cross-country comparison. [RAW-BOOK Perry p.284]

"In general, the results provided sufficient justification to include the behavior of exchange rates in the implementation of monetary policy based on the ITF, which was supported by the data." [RAW-BOOK Perry p.284]

---

## Interest Rate Smoothing Parameter (δ)

The parameter δ captures **gradualism** — CBs adjust rates slowly toward the target implied by the rule rather than jumping immediately. [RAW-BOOK Perry p.283]

For Indonesia: δ ≈ 0.7–0.8 — "large autoregressive interest rate parameter indicated a conservative monetary policy response through interest rate smoothing (gradualism)." [RAW-BOOK Perry p.283]

The high δ means the **effective** policy response to exchange rate deviations is:
```
Immediate rate change = (1 - δ) × γ_e × e_t = 0.2–0.3 × 0.3 × e_t
```
Only 6–9% of the exchange rate gap passes through to the rate in the first period, with the remainder spread over subsequent periods.

---

## Empirical Fit

For Indonesia (Juhro-Mochtar 2009 estimation):

| Rule | R-squared | Key finding |
|------|-----------|-------------|
| Standard Taylor rule | 90% | Captures basic inflation/output dynamics |
| Enhanced rule (+ e_t) | 98% | Better fit; FX deviation statistically significant at 5% |

Both rules: inflation deviation parameter was 2–3× larger than output gap parameter → **price stability is the dominant mandate** even in the enhanced specification. The FX term supplements but does not replace the inflation mandate. [RAW-BOOK Perry p.283]

---

## Policy Implications: When Does γ_e Matter?

**γ_e matters most when:**
1. Exchange rate pass-through is large (EME with high import share in CPI, commodity exporters)
2. Inflation expectations are not firmly anchored (FX movements trigger immediate price revision)
3. Capital flow volatility regularly generates large exchange rate gaps vs equilibrium
4. Financial dollarization creates balance sheet effects from FX movements

**γ_e should be near zero (Chile model) when:**
1. Inflation expectations are firmly anchored (FX doesn't move CPI expectations)
2. FX is primarily driven by terms-of-trade → better to adjust output gap and let FX be shock absorber
3. CB independence and credibility are high

---

## Connection to FX Target and Quasi-Fiscal Costs

The enhanced Taylor rule provides the **feedback mechanism** through which FX targeting generates quasi-fiscal costs:

```
Capital inflows (appreciation pressure)
→ Real FX appreciates above equilibrium → e_t < 0
→ Enhanced rule: policy rate ↓ (accommodative response to appreciation)
→ Rate cut reduces interest rate differential → inflows slow (reduces sterilization pressure)
→ BUT: if CB can't cut rates (inflation above target, α(π − π*) > 0):
  → CB must intervene in FX market instead → NFA↑ → sterilization needed → quasi-fiscal cost
```

This shows that the enhanced Taylor rule and FX intervention are **substitute instruments** — when the rate can respond to the exchange rate gap, less FX intervention is needed, and quasi-fiscal costs fall. When the rate is constrained (by inflation or political factors), FX intervention must compensate, generating sterilization costs. [LLM]

---

## Exchange Rate as Operational Target (Extreme Case)

For very open economies (Singapore, Hong Kong), the exchange rate IS the operational target rather than a supplementary variable [RAW-BOOK Perry trang-4 p.574]:
- Singapore MAS: manages SGD NEER against basket of currencies; interest rates are endogenous
- Hong Kong Currency Board: full NFA/RM backing; no monetary policy independence; γ_e → ∞ (rate fully determined by FX)

This is the extreme end of the enhanced Taylor rule where all policy weight shifts from `α + β` terms to `γ_e → ∞`, resulting in zero domestic monetary policy autonomy — the hard peg endpoint of the FX target constraint.
