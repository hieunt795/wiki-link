---
node_id: capital_flow_push_pull_determinants_eme_001
type: framework
title: Capital Flow Push-Pull Determinants in EMEs
aliases:
- push pull capital flows
- determinants of capital flows
- hot money drivers
- Lucas paradox capital flows
- push factors EME
- pull factors EME
- nhân tố đẩy kéo dòng vốn
- yếu tố quyết định dòng vốn nước ngoài vào EM
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- capital_flows
- em_policy
- push_pull
- hot_money
- fdi
- portfolio_flows
- impossible_trinity
- lucas_paradox
confidence: 3
stability: stable
thesis: 'Capital flows to EMEs are jointly determined by global push factors (advanced-economy
  interest rates, VIX, global growth) and domestic pull factors (EME growth, yields,
  exchange rate stability, institutional quality). FDI is driven primarily by domestic
  fundamentals and governance; portfolio and banking flows are dominated by global
  push factors and respond faster and more reversibly. The composition of inflows
  determines the FX target + sterilization burden: PI and short-term bank flows require
  the most sterilization and generate the largest quasi-fiscal costs. [LLM]

  '
source_refs:
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: lines 66–122 (push-pull taxonomy, empirical evidence), lines 126–172 (Lucas
    paradox, productivity-capital mismatch), lines 172–230 (monetary stability effects,
    impossible trinity empirics)
  weight: primary
parent_node: null
related:
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: context_framework
- node: '[[Capital_Flow_Management_CFM_Taxonomy_Triggers_Instruments]]'
  relation: policy_response
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: creates_sterilization_pressure
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: vulnerability_trigger
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: offset_driver
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## The Push-Pull Framework

Capital flows to EMEs are determined by two independent factor sets that interact multiplicatively [RAW-BOOK Perry p.87]:

```
F_t = f(X_t [push], Y_t [pull], Z_t [structural])

Push factors X_t: global/advanced economy conditions (exogenous to EME)
Pull factors Y_t: domestic EME fundamentals (partly policy-controlled)
Structural Z_t:  exchange rate regime, financial depth, institutions
```

---

## Push Factors (Global — Exogenous to EME)

| Factor | Effect on EME inflows | Dominant for |
|--------|----------------------|-------------|
| **Advanced-economy interest rates** (US Fed, ECB, BoJ policy rates) | Low global rates → capital seeks higher EM yields → inflows surge | PI bonds, banking flows |
| **VIX (global risk premium)** | High VIX → flight to safety → outflows from EMEs; Low VIX → risk-on → inflows | PI equities, PI bonds |
| **Global economic growth** | Strong global growth → trade expansion → FDI for vertical integration | FDI (vertical) |
| **Institutional investor behavior** | Rebalancing, return-chasing, herding amplify flow reversals | PI during stress |
| **Contagion** | Stress in one EME triggers reassessment of peers (contagion channel, Calvo-Reinhart 1996) | All flow types |

**Key post-GFC finding**: During GFC, push factors (VIX, US rates) dominated PI flows. Post-GFC recovery shifted to pull factors as the primary driver — suggesting macro fundamentals matter more in calmer periods. [RAW-BOOK Perry p.109]

---

## Pull Factors (Domestic EME — Policy-Influenced)

| Factor | Effect | Dominant for |
|--------|--------|-------------|
| **Domestic economic growth** | Higher growth → higher expected investment returns | FDI, PI equities |
| **Yield differentials** (policy rate, bond yields, dividend) | Interest rate differential attracts carry trades | PI bonds, banking flows |
| **Exchange rate stability** | Stable FX → lower hedging cost → more inflows; implicit guarantee → unhedged FX borrowing | All types, especially PI |
| **Institutional quality** | Rule of law, property rights, political stability | FDI (horizontal and vertical) |
| **Financial market depth** | More instruments, better price discovery → more foreign investor confidence | PI bonds, equities |
| **Default risk / sovereign rating** | Upgrade → all flow types increase; history of default reduces FDI and PI | All |

**Exchange rate stability as a pull factor** is directly linked to the FX target quasi-fiscal nexus: maintaining a stable/appreciated exchange rate attracts more inflows, which then require more sterilization. [LLM]

---

## Composition of Inflows: Stability Hierarchy

Not all capital is equal in terms of CB sterilization burden and vulnerability:

| Flow Type | Push/Pull dominance | Volatility | Sterilization burden | Reversal risk |
|-----------|---------------------|-----------|---------------------|--------------|
| **FDI** | Pull-dominated | Low | Minimal (direct investment, no RM impact) | Very low |
| **Portfolio Equity (PI stocks)** | Push-dominated | High | Moderate | High (herding) |
| **Portfolio Bonds (PI bonds)** | Push-dominated | Very high | High (bond purchase → RM) | Very high |
| **Short-term bank flows** | Push-dominated | Very high | Highest (banking system funding → RM) | Highest |

"Short-term foreign capital flows are typically determined by the return and risks of a particular investment" — dominated by push factors and institutional behavior. [RAW-BOOK Perry p.54]

For CB sterilization cost analysis: PI bonds + banking flows are the critical categories — they respond most to interest rate differentials (pull factor) and VIX (push factor), creating the largest sterilization/quasi-fiscal burden under FX targeting.

---

## The Lucas Paradox: Why Capital Flows "Upwards"

Neoclassical theory predicts capital flows from rich to poor (higher marginal product in developing countries). Empirically, the opposite is observed (Lucas 1990):

**The paradox**: Countries with higher productivity growth (e.g., Korea, China) received LESS foreign capital than low-growth countries; advanced countries ran current account deficits while EMEs ran surpluses. [RAW-BOOK Perry p.130]

Three explanations relevant for EME policy analysis [RAW-BOOK Perry p.150–170]:

**1. Investment wedge**: Tax, regulatory costs, bureaucracy, FX controls → actual returns are lower than theoretical marginal product. Countries with high investment wedge underperform in attracting productive capital flows.

**2. Financial sector underdevelopment**: Inefficient financial intermediation → savings not channeled to productive uses → less complementarity between foreign and domestic capital. "The ability to optimally and efficiently mobilize domestic savings was shown to be a leading determinant of cross-border foreign capital flow misallocation." [RAW-BOOK Perry p.160]

**3. Default risk**: Countries with history of sovereign default attract significantly less FDI and PI — risk premium is persistent and non-linear (Reinhart-Rogoff 2004). "Not much foreign capital flows to countries with high default risk." [RAW-BOOK Perry p.170]

**Policy implication**: Attracting FDI and productive PI requires addressing investment wedge + financial depth + sovereign credibility — not just interest rate differentials. A high yield maintained via FX target + sterilization primarily attracts hot money (PI bonds, banking flows), not the FDI that would improve productivity without generating sterilization burden.

---

## Monetary Stability Effects: The Flow-Rate-Exchange Rate Nexus

Capital flow volatility creates additional complexity for monetary policy through three channels [RAW-BOOK Perry p.172–230]:

**Channel 1 — Direct FX market pressure**
PI and short-term flows directly affect supply/demand on FX market → exchange rate volatility. Under FX target, CB must intervene → NFA changes → RM changes → sterilization required.

**Channel 2 — Asset price transmission**
PI equity and bond flows affect stock prices and domestic bond yields. Impact on bond yields is sensitive to domestic fundamentals (inflation, current account) and increases with bond tenor duration. [RAW-BOOK Perry p.186]

**Channel 3 — Liquidity spillover**
Large inflows → banking system liquidity surplus → CB absorbs → liquidity measures offset by next inflow wave (the offset coefficient mechanism).

**Empirical quantification (Indonesia)**: Comovement between exchange rate and capital flows was 86% of exchange rate dynamics; comovement between exchange rate and interest differential was only 14% — indicating capital flows were the dominant driver of FX volatility, not the interest rate tool. [RAW-BOOK Perry p.263]

---

## Structural Factors (Z_t)

The exchange rate regime and financial depth modify how push and pull factors translate into flows:

**Exchange rate regime effect**: Pegged regimes attract more PI and banking flows because implicit FX guarantee lowers hedging cost → pull factor strengthened artificially → but also creates fear-of-floating dynamic when shock arrives. [LLM, connects to Em_Balance_Sheet_Crisis_Anatomy]

**Financial depth effect**: Deeper financial markets (more instruments, better price discovery) attract more PI but also make flows more responsive to global push factors (VIX). Countries with very thin domestic bond markets are more vulnerable to sudden capital reversals. [RAW-BOOK Perry p.50]

**Policy trilemma interaction**: Pegged countries empirically show stronger domestic-foreign interest rate comovement (evidence of lost monetary autonomy); non-pegged countries maintain greater autonomy even under high capital mobility — consistent with Mundell-Fleming. [RAW-BOOK Perry p.204]
