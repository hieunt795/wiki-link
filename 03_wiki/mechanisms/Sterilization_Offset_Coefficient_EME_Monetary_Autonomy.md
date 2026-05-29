---
node_id: sterilization_offset_coefficient_eme_001
type: mechanism
title: Sterilization Effectiveness — Offset and Sterilization Coefficients in EMEs
aliases:
- offset coefficient
- sterilization coefficient
- Kouri-Porter framework
- monetary policy autonomy EME
- hệ số offset
- hệ số sterilization
- tính hiệu quả vô hiệu hóa ngoại tệ
- tự chủ chính sách tiền tệ EM
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- sterilization
- fx_intervention
- capital_flows
- monetary_autonomy
- em_policy
- kouri_porter
- indonesia
- offset_coefficient
confidence: 3
stability: stable
thesis: 'Under open capital accounts with an FX target, the effectiveness of CB sterilization
  is constrained by two competing forces measured as coefficients: the offset coefficient
  (how much of CB tightening is neutralized by induced capital inflows) and the sterilization
  coefficient (how much of FX intervention liquidity is reabsorbed). When the offset
  coefficient exceeds the sterilization coefficient, the CB''s net control over money
  supply is negative — tightening attracts more inflows than can be sterilized, undermining
  monetary autonomy. [LLM]

  '
source_refs:
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: lines 265–273 (offset/sterilization coefficients, Indonesia case); lines
    289–293 (sterilization cost of reserve accumulation)
  weight: primary
parent_node: null
related:
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: quantitative_extension
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: cost_mechanism
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: policy_context
- node: '[[Policy_Trilemma_Efficiency_Frontier_Equivalence]]'
  relation: theoretical_root
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Two Coefficients That Define CB Effectiveness

Under open capital accounts with an active FX target, every CB sterilization operation triggers
a feedback loop through the capital account. Two coefficients capture this dynamic:

### Offset Coefficient (α)
Measures the fraction of CB domestic money contraction that is offset by induced capital inflows.

```
CB absorbs liquidity (tightening) → r_domestic rises
→ Interest rate differential widens → capital inflows increase
→ NFA rises → RM expands back

Offset = ΔCapital_inflows / ΔDomestic_credit_contraction
```

- **α = 0**: Full monetary autonomy — no capital flow offset
- **α = 1**: Zero autonomy — every tightening is fully offset by inflows
- **α = 0.7 (Indonesia 2000–2010)**: 70% of BI's liquidity absorption was offset by additional capital inflows [RAW-BOOK Perry p.269]

### Sterilization Coefficient (β)
Measures the fraction of FX-intervention-induced RM expansion that is reabsorbed by domestic OMO.

```
CB buys FX → NFA↑ → RM expands
→ CB sells T-bills / absorbs liquidity (sterilization)

Sterilization = ΔDomestic_credit_contraction / ΔNFA_expansion
```

- **β = 0**: Full pass-through — no sterilization, FX intervention is fully monetized
- **β = 1**: Full sterilization — all FX-induced RM expansion is reabsorbed
- **β = 0.5 (Indonesia 2000–2010)**: 50% of rupiah liquidity from FX intervention was reabsorbed [RAW-BOOK Perry p.269]

---

## The Autonomy Gap: When α > β

The critical condition:

```
Net monetary autonomy = β - α

If β > α → CB retains net control (sterilizes more than is offset)
If β < α → CB loses net control (offset exceeds sterilization capacity)
If β = 0.5 and α = 0.7 → autonomy gap = -0.2 → net capital-induced RM expansion
```

For Indonesia (2000–2010): α (0.7) > β (0.5) → net loss of monetary autonomy. "The relatively high offset coefficient compared to the sterilization coefficient was symptomatic of a low degree of monetary policy autonomy in Indonesia in terms of controlling foreign capital flow dynamics." [RAW-BOOK Perry p.269]

This autonomy gap explains why interest rate policy alone is insufficient for EMEs with large capital inflows — each rate hike partially funds itself with new inflows, reducing the effective tightening delivered to the domestic economy.

---

## Kouri-Porter (1974) Framework

The original econometric specification (Kouri and Porter 1974; extended by Cumby and Obstfeld 1982) estimates both coefficients from CB balance sheet data:

```
ΔNFA_t = α × ΔNDA_t + X_t + ε_t        [Capital flow equation: offset]
ΔNDA_t = β × ΔNFA_t + Z_t + μ_t        [CB reaction function: sterilization]
```

Where NDA = net domestic assets, NFA = net foreign assets (via BOP capital account). The system is estimated simultaneously because both ΔNDA and ΔNFA are endogenous to each other under a managed exchange rate. [LLM — methodology from Perry p.269, Kouri-Porter 1974 citation]

---

## Policy Implications: Three Responses to Low Autonomy

When α > β, the CB faces three non-exclusive responses [RAW-BOOK Perry p.270–272]:

**Response 1 — Non-interest rate instruments**: Reserve requirements, macroprudential tools as primary/supporting liquidity controls when interest rate effectiveness is limited by offset.

**Response 2 — Capital Flow Management (CFM)**: Directly reduces the volume of capital inflows that trigger the offset feedback. If inflows are restricted, α falls — each tightening induces smaller offsetting inflows. CFM converts the trilemma into a workable dilemma.

**Response 3 — Coordinated domestic/international liquidity management**: Simultaneous management of domestic OMO and FX intervention timing to minimize the offset window. Coordination is critical to avoid inadvertent monetary loosening from asynchronous operations.

---

## Sterilization Cost Link

Every unit of FX intervention that IS successfully sterilized (β) carries a quasi-fiscal cost:

```
Cost per sterilized unit = r_domestic − r_foreign
                        = EM policy rate − USD T-bill yield

For typical EME: r_domestic (6-10%) > r_foreign (4-5%)
→ Sterilization of each $1 of FX inflow costs ~1-5bps per year in carry
```

"The cost of accumulating FX reserves is large because the central bank is, therefore, required to sterilize the resultant liquidity." [RAW-BOOK Perry p.293]

Higher β (more successful sterilization) = higher quasi-fiscal cost. This creates a perverse incentive: CBs that are most effective at sterilizing inflows accumulate the largest quasi-fiscal losses. [LLM]

---

## Diagnostic: Monitoring Coefficients in Practice

The coefficients are not directly observable; they must be estimated from balance sheet data. Proxies:

| Indicator | What it tracks |
|-----------|---------------|
| NFA/NDA rolling correlation | High positive correlation → high offset environment |
| CB profit transfer trend | Declining → sterilization costs rising |
| Interest rate differential vs capital inflow volume | Large diff + large inflows → high α environment |
| Share of domestic M2 covered by NFA | Rising → NFA endogeneity increasing under FX target |
