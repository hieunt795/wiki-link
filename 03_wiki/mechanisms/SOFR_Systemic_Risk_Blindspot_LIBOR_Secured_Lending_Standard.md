---
node_id: sofr_systemic_blindspot_libor_001
type: mechanism
title: SOFR Systemic Risk Blindspot LIBOR Secured Lending Standard
aliases:
- SOFR hides systemic risk
- LIBOR to SOFR transition drawback
- secured lending standard blindspot
- SOFR vs LIBOR stress signal
- điểm mù rủi ro hệ thống của SOFR
domain:
  primary: financial_markets
  secondary: monetary_policy
tags:
- sofr
- libor
- secured_lending
- systemic_risk
- rfr
- stress_indicator
- repo
confidence: 1
stability: stable
thesis: SOFR's replacement of LIBOR resolved benchmark manipulation risk but introduced
  a new systemic blindspot — because SOFR is secured (repo-backed), it does not spike
  during bank funding stress the way LIBOR did, making it a poor early-warning signal
  of unsecured credit stress; meanwhile the global secured lending standard (RFRs
  replacing IBORs in derivatives, bonds, and loans) has tightened the linkage between
  private finance and sovereign balance sheets.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batches 7-9 (chars ~45000-70000)
  weight: primary
parent_node: null
related:
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: related_mechanism
- node: '[[Fed Policy Rate Shift EFFR To Secured Rate TGCR]]'
  relation: extends
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Why LIBOR Failed

LIBOR was a panel-based, unsecured benchmark:
- Banks submitted estimated unsecured interbank borrowing rates daily
- August 2007: LIBOR detached from Fed Funds during the subprime crisis — banks understated submissions to appear financially sound
- Post-2008: LIBOR manipulation scandal (traders exploited 1bp moves for millions in profits)
- 2017: ARRC selected SOFR as LIBOR's replacement; fully deprecated June 2023 [RAW-CLIP]

## SOFR's Systemic Risk Blindspot

SOFR measures the overnight secured repo rate (Tri-Party + GCF + DVP):
- Because repos are collateralized by USTs, SOFR barely budges during bank credit stress — collateral quality hides interbank stress
- **COVID case**: LIBOR spiked sharply above Fed Funds (signaling unsecured stress); SOFR barely moved
- SOFR cannot differentiate: "calm because banks are healthy" vs. "calm because repo collateral is covering up the stress"

As a result, SOFR provides a **false sense of security** during credit crises. Alternatives like Bloomberg BSBY (a credit-sensitive benchmark) tracked LIBOR's COVID spike closely — suggesting it could be a better early-warning signal. [RAW-CLIP]

## The Global Secured Lending Standard

Post-LIBOR benchmark transition:
- **US**: SOFR (overnight secured repo rate)
- **UK**: SONIA (overnight unsecured, but near risk-free)
- **Canada**: CORRA; **Australia**: AONIA; **Eurozone**: ESTR
- These Risk-Free Rates (RFRs) now underpin trillions in derivatives, bonds, and loans [RAW-CLIP]

**Structural implication**: As the global benchmark standard shifted from unsecured (LIBOR) to secured (RFR), private finance became more tightly coupled to the supply and quality of sovereign collateral (USTs, gilts, etc.). When collateral is scarce, repo markets freeze — precisely when you need them most. [LLM]

## Collateral Shortage as SOFR Risk

Rehypothecation daisy chains — where the same UST collateral is reused across multiple repo legs — work only in calm conditions:
- When stress hits, holders hoard collateral → daisy chains unwind → SOFR spikes
- This is a post-LIBOR mechanism of systemic contagion, invisible in normal times [RAW-CLIP]
