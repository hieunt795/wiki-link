---
node_id: treasury_buybacks_sovereign_debt_001
type: mechanism
title: Treasury Buybacks Sovereign Debt Liquidity Intervention
aliases:
- Treasury buybacks liquidity
- UST secondary market repurchase
- sovereign debt liquidity intervention
- illiquidity spiral
- vòng xoáy thiếu thanh khoản
- mua lại trái phiếu kho bạc
domain:
  primary: fiscal_policy
  secondary: financial_markets
tags:
- treasury
- buybacks
- ust
- liquidity
- sovereign_debt
- illiquidity_spiral
- intervention
confidence: 1
stability: stable
thesis: When Treasury market illiquidity escalates, the U.S. Treasury's first-line intervention (before full YCC) is secondary-market buybacks — repurchasing off-the-run bonds via primary dealers to compress the illiquidity premium, reduce interest expense, and break the illiquidity spiral (volatility → illiquidity → more volatility doom loop) without requiring Fed balance sheet expansion.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batch 1 (chars ~0-9000)
  weight: primary
related:
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: complements
- node: '[[NBFI Sovereign Market Supervisory Gap]]'
  relation: context
- node: '[[Sovereign Debt Market Discipline Price Discovery Role]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Illiquidity Spiral (Conks Framework)

The doom loop in sovereign bond markets:
1. Volatility increases → bid-ask spreads widen → market depth collapses
2. Thinning depth → more price impact per trade → more volatility
3. Loop reinforces: **volatility → illiquidity → more volatility**

This spiral is self-reinforcing without external intervention. [RAW-CLIP]

## Treasury Buybacks Mechanism

When the illiquidity spiral threatens market functioning, the U.S. Treasury can repurchase bonds in the secondary market via primary dealers (e.g., JPMorgan, Nomura):

**Funding sources:**
- Proceeds from new bond sales (net supply-neutral if coupon issuance continues)
- Draw from TGA (Treasury's bank account at the Fed)

**Transmission:**
1. Treasury buys off-the-run bonds → removes illiquid securities from market
2. Higher bond prices → lower yields → reduced interest expense on outstanding debt
3. Bid-ask spreads compress → market depth restores → volatility recedes [RAW-CLIP]

## Why Buybacks Before YCC

The intervention ladder (from least to most interventionist):
1. **Treasury buybacks** — fiscal tool; no monetary expansion required; politically easier
2. **Operation Twist-style swap** — Fed extends duration without balance sheet growth
3. **Outright QE** — Fed buys bonds, expands balance sheet
4. **Explicit YCC** — last resort; requires indefinite commitment; risks credibility loss

Monetary authorities prefer buybacks precisely because they do not require Fed balance sheet expansion and are reversible. [LLM]
