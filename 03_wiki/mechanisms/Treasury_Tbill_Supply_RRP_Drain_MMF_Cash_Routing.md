---
node_id: treasury_tbill_supply_rrp_drain_mmf_routing_001
type: mechanism
title: Treasury T-bill Supply RRP Drain And MMF Cash Routing
aliases:
- T-bill RRP Substitution
- MMF Cash Routing Bills vs RRP
- Bill Supply Reserve Drain Mechanism
- Cung T-bill và tiêu hao RRP
- Điều hướng tiền mặt MMF
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- tbills
- rrp
- mmf
- tga
- treasury_issuance
- money_market
- reserves
- debt_limit
confidence: 1
stability: evolving
thesis: 'T-bill supply and Fed ON RRP balances are substitutes for MMF cash: high
  T-bill issuance routes MMF funds out of the RRP into bills (draining RRP, boosting
  reserves), while T-bill supply contractions — particularly during debt ceiling episodes
  — drive MMF cash back into the RRP, inflating it and preventing reserve growth even
  as the TGA is drawn down.'
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: batch 4 (chars ~25041-34659)
  weight: primary
parent_node: null
related:
- node: '[[Fed Overnight Reverse Repo ON RRP]]'
  relation: interacts_with
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: related_mechanism
- node: '[[Debt Ceiling Extraordinary Measures Treasury]]'
  relation: context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Core Substitution Mechanism

MMFs hold two primary overnight instruments:
1. **Fed ON RRP** — risk-free, Fed counterparty, IOER-adjacent rate
2. **T-bills** — risk-free, Treasury collateral, market rate

When T-bill supply is high, market rates on bills are competitive → MMFs prefer bills over RRP → **RRP drains, bank reserves increase** (as money flows from MMF parking at Fed to real-economy Treasury spending).

When T-bill supply falls, T-bill yields decline below RRP rate → MMFs revert to RRP → **RRP inflates, reserve growth stalls**. [RAW-CLIP]

## Treasury Bills as "Shock Absorber"

Treasury's self-proclaimed debt management objective: issue at lowest cost to taxpayer. Internal models favor higher bill share to reduce long-term interest expense.

**Operational design:**
- Coupon auctions run on fixed, predictable schedules
- T-bills (overnight to weeks maturity) absorb TGA volatility — used to fund unexpected spending or smooth debt limit disruptions
- T-bill issuance also "shock absorbs" sudden surges in duration supply that could spook markets [RAW-CLIP]

## Debt Limit Disruption

When debt ceiling binds:
1. Treasury cannot issue new bills → bill supply contracts
2. T-bill yields fall → MMFs park surplus in Fed RRP
3. TGA drawdown releases reserves into banking system, but these quickly re-park in RRP rather than staying as bank reserves
4. Net effect: **RRP inflates, interbank reserves do not build**

This creates a monetary plumbing "wedge" where TGA spending fails to deliver reserve growth to banks — exactly opposite to what QT unwinding or fiscal stimulus would normally achieve. [RAW-CLIP]

## Implications for Fed Rate Control

Fed's goal of an "empty RRP" (to ensure reserves are plentiful and IORB/EFFR spread is tight) is structurally dependent on Treasury maintaining high T-bill supply. Both Fed and Treasury share aligned incentives around keeping the T-bill printer active. [RAW-CLIP]

This alignment makes RRP management a joint fiscal-monetary coordination problem, not a purely Fed balance sheet issue. [LLM]
