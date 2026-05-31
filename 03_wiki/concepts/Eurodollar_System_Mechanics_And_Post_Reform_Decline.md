---
node_id: eurodollar_system_mechanics_and_post_reform_decline_001
type: concept
title: Eurodollar System Mechanics And Post-Reform Decline
aliases:
- Eurodollar Market
- Offshore Dollar Banking
- Global Dollar System
- Hệ thống Eurodollar
- Đô la ngoài khơi
domain:
  primary: monetary_policy
tags:
- eurodollar
- dollar_funding
- sofr
- libor
- mmf
- basel_lcr
- global_dollar
confidence: 3
stability: evolving
thesis: The Eurodollar system — offshore dollar banking settled onshore via Fed reserves
  — peaked as the dominant global dollar funding mechanism but was structurally gutted
  by Basel III LCR (2013) and 2014 SEC MMF reform, with unsecured interbank lending
  collapsing and SOFR/secured funding replacing LIBOR/unsecured as the global dollar
  standard.
source_refs:
- path: 02_sources/books/conks/Conks - Global Dollar and Eurodollar Systems.md
  pages: Full document
  weight: primary
parent_node: null
related:
- node: '[[Global Dollar System Eurodollar Architecture]]'
  relation: shared_tag:eurodollar
- node: '[[Fed Policy Rate Shift EFFR to Secured Rate TGCR]]'
  relation: shared_tag:sofr
- node: '[[FHLB EFFR IORB Arbitrage Floor Mechanism]]'
  relation: shared_tag:sofr
- node: '[[Interest Rate Swaps — OIS, Fixed-for-Floating, Clearing, and Basis]]'
  relation: shared_tag:sofr
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:sofr
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The **Eurodollar system** is offshore dollar banking: dollar deposits and loans created outside the US, but ultimately settled onshore through correspondent bank reserves at the Federal Reserve. Despite the name "Euro," it includes all offshore dollar markets globally [RAW-CLIP].

## Core Mechanics
1. **Creation:** A non-US bank (e.g., Deutsche Bank London) accepts a dollar deposit from a corporation → creates a Eurodollar liability
2. **Settlement:** All interbank dollar transfers ultimately settle via Fedwire through US correspondent accounts → the Fed's reserve system is the backbone
3. **Leverage:** Eurodollar banks can lend multiples of their US reserve position via fractional reserve-like layering offshore [LLM]

## The 26+ Dollar Instrument Ecosystem
The "dollar" is not one instrument but a family: Fed Funds, SOFR, Eurodollar futures, FX swaps, offshore deposits, CP, repo, T-bills, and more. European and Japanese banks historically acted as key intermediaries — French banks in particular bridged European and US money markets [RAW-CLIP].

## Structural Collapse (2013-2016)
Two regulatory changes destroyed the unsecured Eurodollar market:

| Reform | Mechanism | Effect |
|--------|-----------|--------|
| Basel III LCR (2013) | Banks must hold HQLA against short-term wholesale funding | Unsecured interbank borrowing became expensive to fund; banks withdrew |
| SEC MMF Reform (2014, effective 2016) | Prime MMFs (main lenders in Eurodollar market) faced gates/fees | Mass shift from prime to government MMFs; destroyed prime MMF demand for bank CP/CDs |

Post-2016: Prime MMF AUM fell from ~$1.5T to ~$0.4T; interbank unsecured Eurodollar lending near zero [RAW-CLIP].

## Legacy (LIBOR) vs Modern (SOFR) Standard
| | LIBOR Era (pre-2023) | SOFR Era (post-2023) |
|--|---------------------|---------------------|
| Rate basis | Unsecured interbank | Secured triparty/GCF repo |
| Credit component | Embedded bank credit risk | Near-zero (Treasury collateral) |
| Panel | 20 contributor banks (surveyed) | Transaction-based (DTCC reported) |
| Dollar market anchor | Eurodollar futures | SOFR futures/swaps |

The LIBOR-to-SOFR transition reflects the underlying structural shift: the "dollar" market moved from trust-based unsecured lending to collateral-based secured lending [RAW-CLIP].

## Global Impact
- **FX Swap Line demand:** Without Eurodollar funding, offshore banks rely on Fed swap lines during stress (as in March 2020)
- **Dollar shortage episodes:** Eurodollar decline made cross-currency basis more volatile; JPY/EUR basis swaps now spike during risk-off events
- **Monetary transmission abroad:** Fed rate changes transmit globally via dollar funding costs even without direct reserve requirement linkage [LLM]


