---
node_id: slr_relief_valve_limited_efficacy_001
type: mechanism
title: SLR Relief Valve Limited Efficacy For UST Demand
aliases:
- SLR relief valve
- SLR UST demand constraint
- eSLR reform
- Fed leverage ratio reform
- Van xả SLR hạn chế tác dụng
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- slr
- leverage_ratio
- ust
- dealer_balance_sheet
- basel
- risk_based_capital
- swap_spreads
confidence: 1
stability: evolving
thesis: A partial SLR (Supplementary Leverage Ratio) reduction is a "faulty relief
  valve" for UST market liquidity because most large banks are bound by risk-based
  capital requirements, not SLR — so freeing SLR headroom does not incentivize additional
  UST purchases when banks fund those purchases with reserves (also 0% RWA), and only
  the most leverage-constrained banks see any benefit.
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: batch 15-16 (chars ~121242-138915)
  weight: primary
parent_node: null
related:
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: extends
- node: '[[Swap Spreads Balance Sheet Plumbing Frictions]]'
  relation: context
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
steps:
- 'Step 1: A partial SLR (Supplementary Leverage Ratio) reduction is a "faulty relief valve" for UST market liquidity because most large banks are bound by risk-based capital requirements, not SLR'
- 'Step 2: so freeing SLR headroom does not incentivize additional UST purchases when banks fund those purchases with reserves (also 0% RWA), and only the most leverage-constrained banks see any benefit'

---

## Why SLR Reduction ≠ UST Demand Boost

**Setup:** Banks must hold capital against both leverage exposure (SLR) and risk-weighted assets (RWA). The binding constraint is whichever is LARGER.

**Scenario A — Bank bound by risk-based capital (common case):**
- SLR reduction frees some leverage capital, but risk-based capital is still the binding constraint
- Bank won't buy USTs (0% RWA) just because it has more SLR headroom; risk-based constraint unchanged
- Result: SLR cut provides no meaningful relief [RAW-CLIP]

**Scenario B — Bank bound by SLR:**
- Bank buys USTs (0% RWA) funded by reserves (also 0% RWA)
- This doesn't change the risk-based capital requirement at all
- Duration risk, internal limits, and other factors may still prevent buying
- A bank choosing NOT to use $40B of seemingly "excess" SLR capacity may have legitimate reasons [RAW-CLIP]

**True Relief Would Require:** Excluding USTs from risk-based capital ratios entirely (not just reducing SLR) — this would make USTs the preferred instrument for both leverage AND risk-based optimization.

## Swap Spread Signal

Conks uses the **swap spread curve** as the primary plumbing health gauge:
- **Widening (less negative) spread** = plumbing frictions decreasing = bullish UST demand signal
- **Narrowing (more negative) spread** = plumbing stress increasing

Post-QT end (December 2025): Swap spreads widened significantly on a combination of SLR reform expectations + non-SLR catalysts (Treasury buybacks, paused coupon issuance increases, QT end). Further widening will slow until regulators implement stronger deregulation. [RAW-CLIP]

## Policy Implication

A partial SLR change may satisfy some regulatory officials but won't deliver the "juice" needed for deep, structural UST market liquidity. The strongest intervention — UST exclusion from risk-based ratios — remains politically contentious. [LLM]
