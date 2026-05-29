---
node_id: debt_ceiling_extraordinary_measures_treasury_001
type: mechanism
title: Debt Ceiling Extraordinary Measures Treasury
aliases:
- extraordinary measures
- debt ceiling bypass
- TGA drawdown
- debt limit
- tran no cong
domain:
  primary: monetary_policy
tags:
- debt-ceiling
- tga
- treasury
- fiscal-monetary-interaction
- money-market
confidence: 3
stability: evolving
thesis: When the US debt ceiling binds, the Treasury deploys extraordinary measures
  to delay default while drawing down the TGA. The resulting TGA drawdown floods banking
  system reserves, creating a temporary liquidity surge that overstates system health
  before reversing sharply when the ceiling is lifted and Treasury refills the TGA.
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: Money Market Blindspot I and II
  weight: primary
parent_node: null
related:
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:tga
- node: '[[Ample Reserves Buffer Sizing TGA Volatility]]'
  relation: shared_tag:tga
- node: '[[Treasury General Account TGA Reserve Swap]]'
  relation: shared_tag:tga
- node: '[[Fed Fiscal Agent Treasury Relationship]]'
  relation: shared_tag:treasury
- node: '[[New Fed-Treasury Accord (2026 Proposal)]]'
  relation: shared_tag:treasury
date_created: '2026-05-20'
date_updated: '2026-05-20'
---


The debt ceiling forces a predictable two-phase liquidity cycle:

**Phase 1 - TGA Drawdown (ceiling binds):**
- Treasury suspends non-marketable security issuance (G Fund: ~250B; ESF; CSRD Fund)
- Government pays bills by spending TGA down toward zero
- Each dollar spent: TGA down, bank reserves up (Fed liability swap)
- Reserve flood -> deposits pushed into MMFs -> MMFs park in Fed RRP -> RRP surges

**Phase 2 - TGA Refill (ceiling lifted):**
- Treasury issues 500B-1T in T-bills to refill TGA
- T-bill issuance: private sector buys bills with bank deposits -> reserves fall
- MMFs shift from RRP into higher-yielding bills -> RRP collapses
- Net result: reserves drain, funding stress resurfaces (SOFR-FF basis tightens)

**Interaction with QT:**
During TGA drawdown, reserves released by TGA offset reserves destroyed by QT, creating the illusion of QT having minimal impact. The liquidity blindspot materializes when the Fed cannot distinguish TGA-driven liquidity from structural reserve scarcity.

**Key instruments:**
- G Fund (TSP): largest source, ~200B+ headroom
- ESF (Exchange Stabilization Fund)
- CSRD (Civil Service Retirement): deferrable non-marketable issuance


