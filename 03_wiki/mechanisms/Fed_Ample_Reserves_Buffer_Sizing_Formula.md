---
node_id: fed_ample_reserves_buffer_sizing_formula_001
type: mechanism
title: Fed Ample Reserves Buffer Sizing Formula
aliases:
- ample reserves buffer formula
- Fed reserve buffer sizing
- bộ đệm dự trữ dồi dào
- công thức tính dự trữ Fed
domain:
  primary: monetary_policy
tags:
- fed
- reserves
- ample_reserves
- tga
- desk_operations
- rate_control
- balance_sheet
confidence: 1
stability: evolving
thesis: The ample reserves buffer the Fed Desk maintains to avoid rate-control failures
  can be estimated as B = sqrt(Δ) × σ × z*(εΔ/2), where Δ is the interval between
  Desk operations, σ is the standard deviation of TGA changes over that period, and
  ε governs acceptable fault probability; for a 2-week interval with σ≈$100bn and
  1% annualized fault probability, the formula implies a buffer of ~$150-250bn — below
  which TGA volatility can trigger a September 2019-style reserve shortage. [LLM]
source_refs:
- path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
  pages: ''
  weight: primary
parent_node: null
related:
- node: '[[Ample_Reserves_Buffer_Sizing_Tga_Volatility]]'
  relation: canonical_formula_node
- node: '[[Tga_Volatility_And_Reserve_Buffer_Demand]]'
  relation: qualitative_channel
date_created: '2026-05-23'
date_updated: '2026-05-24'
---

## Scope Boundary

[LLM] This file is retained as a duplicate routing stub for the same buffer-sizing source.

[LLM] The canonical formula node is [[Ample_Reserves_Buffer_Sizing_Tga_Volatility]].

[LLM] The qualitative TGA-volatility transmission channel is [[Tga_Volatility_And_Reserve_Buffer_Demand]].

[LLM] Do not expand this file unless the canonical formula node is archived or this file receives a clearly distinct source scope.

