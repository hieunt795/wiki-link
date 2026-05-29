---
node_id: warsh_reserve_floor_and_structural_demand_constraint_mec_001
type: mechanism
title: Warsh Reserve Floor And Structural Demand Constraint
aliases:
- structural demand floor
- reserve floor constraint
- ranh buoc tang tru du
- tran cau cau truc cua du tru
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- warsh
- reserves
- floor
- structural_demand
- qt
- sofr
- liquidity
confidence: 3
stability: stable
thesis: 'Warsh''s balance-sheet shrinking program runs into a reserve-floor constraint:
  the Fed cannot reduce reserves below the system''s structural demand without causing
  money-market dislocations. This makes the question not whether the balance sheet
  can be smaller, but how far it can shrink before SOFR and related rates lose their
  stable floor.

  '
source_refs:
- path: 02_sources/Clipping/Warsh and the Fed's Balance Sheet.md
  pages: full document
  weight: primary
- path: 02_sources/Clipping/The Checking Account of the U.S. Federal Government....md
  pages: full document
  weight: supporting
parent_node: null
related:
- node: '[[Warsh Balance Sheet Stimulus Swap]]'
  relation: contested_by
- node: '[[Fed Balance Sheet Size and Policy Rate Independence]]'
  relation: operating_context
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: rate_control_context
- node: '[[TGA Volatility And Reserve Buffer Demand]]'
  relation: related_constraint
- node: '[[Warsh Fed Balance Sheet Operating Doctrine]]'
  relation: implementation_constraint
date_created: 2026-05-24
date_updated: 2026-05-24
---

## Core Mechanism
[RAW-CLIP] The source says that once reserve balances are reduced below roughly 9% of GDP, money-market rates like SOFR spike.

[RAW-CLIP] It also says that structural demand for Fed liabilities comes from regulation and from the banking system's liquidity dependence.

[LLM] This means a smaller Fed balance sheet is not a free good. There is a floor below which the system starts to price reserve scarcity rather than neutral liquidity.

## Why The Floor Exists
[LLM] Banks need reserves for payment execution, regulatory compliance, and balance-sheet management.

[LLM] Money-market participants also treat reserve supply as a stabilizing input, so the Fed's own balance-sheet size can shape demand for its liabilities.

[LLM] In that environment, QT is only safe if it respects the structural demand floor and does not rely on a one-for-one idea that every dollar of shrinkage creates room for a rate cut.

## Warsh Implication
[LLM] The Warsh critique tries to lower the floor by reducing regulation and reserve supply at the same time.

[LLM] The operational risk is that the floor may prove less flexible than the doctrine assumes, because payment-system mechanics and market habits do not disappear just because the Fed wants a smaller footprint.

[LLM] So this mechanism is the hard constraint on the broader Warsh doctrine: balance-sheet reduction is feasible only inside the reserve-demand envelope of the system.

