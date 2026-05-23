---
node_id: ptf_treasury_market_making_001
type: mechanism
title: PTF Principal Trading Firms Treasury Market Making
aliases:
- principal trading firms
- PTF Treasury
- HFT market makers Treasury
- công ty giao dịch chính
domain:
  primary: financial_markets
tags:
- ptf
- treasury
- market_making
- hft
- electronic_trading
- g-sib
- dealer
- liquidity
confidence: 1
stability: stable
thesis: Post-Basel III, Principal Trading Firms (PTFs) using HFT strategies on electronic platforms displaced large G-SIB banks as the dominant Treasury market makers — because PTFs are not subject to G-SIB capital constraints and can intermediate large volumes without the regulatory penalty that caused banks like JPMorgan to exit tri-party repo, creating a faster but more opaque and fragile market-making ecosystem.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batch 4 (chars ~26638-35400)
  weight: primary
related:
- node: '[[UST Market Primary Secondary OnRun OffRun Structure]]'
  relation: extends
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: context
- node: '[[NBFI Sovereign Market Supervisory Gap]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Why PTFs Displaced Banks in Treasury Market Making

**Pre-Basel III:** Large G-SIB banks (JPMorgan, Goldman, etc.) were the primary market makers for Treasuries and repo.

**Post-Basel III/Dodd-Frank:** Capital requirements (SLR, NSFR, LCR) made balance-sheet-intensive market-making unprofitable for G-SIBs:
- JPMorgan closed its tri-party repo business entirely due to regulatory capital penalties
- Banks pulled back from risk-taking and two-way market-making [RAW-CLIP]

**PTF entry:** Principal Trading Firms (PTFs) are non-bank entities not classified as G-SIBs:
- Use proprietary HFT algorithms on electronic trading platforms
- Not subject to G-SIB capital surcharges, SLR, or Basel III risk weights
- Profit from bid-ask spread while trading USTs, MBS, and other securities
- Have gradually captured dominant Treasury market-making share [RAW-CLIP]

## Market Implications

**Positive:** PTFs provide continuous electronic liquidity; narrower spreads in normal times.

**Negative:** PTF risk appetite is highly correlated — during stress events, all PTFs withdraw simultaneously:
- PTFs have no obligation to make markets (unlike primary dealers, who have auction obligations)
- Their exit during stress creates sudden liquidity vacuum (no backstop buyer)
- Concentration risk: a few PTF firms provide most of the marginal liquidity
- System is faster but more fragile than bank-dealer-dominated structure [LLM]

## Regulatory Gap

PTFs operate in an opaque regulatory space:
- Not subject to Fed oversight like primary dealers
- Not subject to G-SIB capital rules
- Not required to report positions to FINRA/TRACE with same granularity as bank dealers
- The structural power shift from banks to PTFs has created supervisory blindspots [RAW-CLIP]
