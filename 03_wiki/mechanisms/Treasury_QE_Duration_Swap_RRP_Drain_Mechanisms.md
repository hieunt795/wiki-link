---
node_id: treasury_qe_duration_rrp_drain_001
type: mechanism
title: Treasury QE Duration Swap And RRP Drain Mechanisms
aliases:
- Treasury QE
- Treasury buybacks duration swap
- RRP drain Treasury QE
- unintended Treasury QE
- mua lại kho bạc làm nới lỏng định lượng
domain:
  primary: fiscal_policy
  secondary: monetary_policy
tags:
- treasury
- buybacks
- rrp
- qe
- duration
- net_liquidity
- mmf
- reserves
confidence: 1
stability: stable
thesis: Treasury buybacks can function as "Treasury QE" via two distinct mechanisms — (1) duration-reducing swap (buy long-dated bonds, re-issue short-dated), which removes duration risk from private hands and stimulates risk assets if announced explicitly; and (2) RRP-drain QE (MMF withdraws from RRP to buy new Treasury bills which fund the buyback), which involuntarily boosts net liquidity without Fed balance sheet expansion.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batches 24-26 (chars ~136000-160000)
  weight: primary
related:
- node: '[[Treasury Buybacks Sovereign Debt Liquidity Intervention]]'
  relation: extends
- node: '[[Treasury Tbill Supply RRP Drain MMF Cash Routing]]'
  relation: related_mechanism
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Type 1 — Duration-Reducing Buyback (Deliberate Stimulus)

Treasury buys back long-dated bonds (e.g. 30-year) → re-issues shorter-dated (e.g. 2-year notes):
- Removes duration risk from private sector → investors no longer need to sell riskier assets to hedge duration
- Lower duration → lower bond volatility → more risk appetite
- To be stimulative like traditional QE, officials must announce this intention explicitly (psychological channel)
- Proposed 2024 buybacks are "duration neutral" — this mechanism is *feasible but not deployed* [RAW-CLIP]

## Type 2 — RRP-Drain Buyback (Unintended Net Liquidity Boost)

When money market funds (MMFs) withdraw cash from Fed RRP to buy new Treasury bills, and those bills fund a buyback:

1. MMF holds RRP → reserves parked at Fed, neutralized
2. Treasury issues T-bills → MMF buys bills using RRP withdrawal → reserves flow back into banking system
3. Treasury uses T-bill proceeds to fund buyback of off-the-run bonds
4. Net result: reserves return to banking system, "net liquidity" increases, RRP falls

**Why this is "unintended" Treasury QE:**
- Treasury doesn't need to intend to loosen conditions — the RRP drain automatically boosts net liquidity
- This was the main mechanism of the 2023 net liquidity surge (RRP drain → perceived easing) [RAW-CLIP]

## RRP as "Reserve Neutralizer"

When MMFs invest in RRP:
- MMF's bank destroys its deposit and sends reserves to the Fed
- Fed transforms reserves into an RRP liability on its balance sheet
- Cash is "trapped" until 3:30pm daily — intraday illiquidity
- Net effect: bank deposits and reserves temporarily removed from financial system

RRP drainage = reserve re-injection. This creates the inverse of the Treasury's TGA spending effect. [RAW-CLIP]
