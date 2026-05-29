---
node_id: cb_fx_swap_intervention_mechanics_and_off_balance_sheet_exposure_001
type: mechanism
title: CB FX Swap Intervention Mechanics And Off Balance Sheet Exposure
aliases:
- CB FX swap
- buy-sell swap intervention
- sell-buy swap
- FX swap off-balance sheet
- hoán đổi ngoại tệ can thiệp NHTW
- công cụ swap tỷ giá NHTW
- near leg far leg FX swap
domain:
  primary: monetary_policy
tags:
- fx_intervention
- fx_swap
- off_balance_sheet
- nfa
- reserve_management
- sterilization
- dollar_liquidity
- hidden_reserves
- em_policy
confidence: 1
stability: evolving
thesis: '[LLM] A central bank FX swap (buy-sell or sell-buy) consists of two legs
  settled at different dates: the near leg changes NFA immediately, while the far
  leg creates an off-balance-sheet forward commitment that reverses the NFA position
  at maturity. CB use swaps rather than spot to (1) inject/drain FX liquidity temporarily
  without permanently depleting reserves, (2) obscure intervention scale from monthly
  reserve reports, and (3) provide short-term dollar funding to commercial banks without
  surrendering spot reserves. The outstanding far-leg book reduces net effective reserves
  below reported gross reserves.'
source_refs:
- path: 04_research/ma_fx_target_balance_sheet/findings/fx_swap_intervention_mechanics.md
  pages: TRUE_GAP — pending ingest of BIS WP 119 (Patel & Cavallino 2019), BIS QR
    Sep 2022
  weight: primary
parent_node: '[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]'
related:
- node: '[[CB Hidden FX Reserves Net Effective Intervention Capacity]]'
  relation: consequence — swap far-leg book reduces net effective reserves
- node: '[[CB FX Forward And NDF Intervention Delivery Versus Cash Settlement]]'
  relation: sibling_instrument — forward is single-leg; swap is two-leg with reversal
- node: '[[CB FX Options And Cancelable Forward Intervention Structures]]'
  relation: sibling_instrument — options add optionality vs swap commitment
- node: '[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]'
  relation: parent_mechanism — swap is one implementation of sterilized intervention
- node: '[[FX Swap Basis CIP Deviation Dollar Scarcity]]'
  relation: market_context — CIP deviation affects swap pricing for CB
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

[LLM] Auto-generated stub — TRUE_GAP, awaiting source ingest. See 04_research/ma_fx_target_balance_sheet/findings/fx_swap_intervention_mechanics.md for full analysis.

