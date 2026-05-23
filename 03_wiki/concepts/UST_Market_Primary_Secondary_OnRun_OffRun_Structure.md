---
node_id: ust_market_structure_onrun_offrun_001
type: concept
title: UST Market Primary Secondary OnRun OffRun Structure
aliases:
- on-the-run Treasury
- off-the-run Treasury
- primary Treasury market
- secondary Treasury market
- UST market structure
- trái phiếu kho bạc on-the-run off-the-run
domain:
  primary: financial_markets
tags:
- ust
- treasury
- on_the_run
- off_the_run
- primary_dealer
- secondary_market
- liquidity
confidence: 1
stability: stable
thesis: The U.S. Treasury market has two structurally distinct layers — the primary market (initial auction, globally liquid, dealer-intermediated) and the secondary market (secondary trading, concentrated in on-the-run bonds, with off-the-run bonds mostly held to maturity and prone to illiquidity) — with structural blindspots and monopoly power in the secondary layer that primary-market tools cannot address.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batch 3 (chars ~17854-26638)
  weight: primary
related:
- node: '[[Treasury Buybacks Sovereign Debt Liquidity Intervention]]'
  relation: context
- node: '[[NBFI Sovereign Market Supervisory Gap]]'
  relation: related_concept
- node: '[[Sovereign Debt Market Discipline Price Discovery Role]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Primary Market

Where investors buy bonds directly from the U.S. government at auction (via primary dealers as underwriters):
- Remains liquid and globally in-demand
- Primary dealers absorb full auction supply, then distribute to secondary market buyers
- The world can't get enough of auctions even at high issuance volumes (~$550B/quarter as of 2022) [RAW-CLIP]

## Secondary Market: On-the-Run vs Off-the-Run

**On-the-run (OTR):** The most recently issued Treasury of each maturity tenor
- Concentrated liquidity; dominates daily trading volume
- Tight bid-ask spreads; high market depth [RAW-CLIP]

**Off-the-run (OFR):** All previously issued Treasuries of that maturity
- Mostly held to maturity by institutional investors; rarely traded
- Prone to illiquidity during stress; wider bid-ask spreads
- When stress forces off-the-run selling, price discovery breaks down [RAW-CLIP]

## The Secondary Market "Dark Spot"

The secondary market, particularly the off-the-run segment, contains structural blindspots:
- Monopoly power concentrations among dealer intermediaries
- Regulatory gaps in reporting and oversight (FINRA/TRACE coverage incomplete)
- Fed's repo/money-market liquidity tools do not directly address secondary off-the-run illiquidity [RAW-CLIP]

## Primary Dealers as Market Plumbers

Primary dealers act as the structural intermediaries ("plumbers") between the Treasury and secondary market buyers:
1. Absorb full auction allocation at primary
2. Hold inventory on balance sheet
3. Distribute to real-money buyers, hedge funds, foreign official sector
4. Provide two-way markets in secondary trading

When balance sheet constraints limit dealer capacity, the primary-to-secondary transmission breaks and issuance cannot reach end buyers efficiently. [LLM]
