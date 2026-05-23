---
node_id: japan_sovereign_carry_trade_frm_001
type: framework
title: Japan Sovereign Carry Trade Framework
aliases:
- Japan Public Sector SWF
- Mô hình "Carry Trade" của khu vực công Nhật Bản
- Borrow-Short Invest-Long Sovereign Model
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
  - fiscal_policy
tags:
- japan
- boj
- carry_trade
- duration_mismatch
- swf
confidence: 3
stability: stable
thesis: 'The Japanese public sector (government + BoJ + pension funds) operates as
  a giant, leveraged sovereign wealth fund that borrows at floating short-term rates
  (bank reserves) to fund long-duration risky assets (equities and foreign securities),
  creating a massive sensitivity to rising interest rates.

  '
source_refs:
- path: 02_sources/Clipping/What about Japan_ (Part I).md
  pages: Full document
  weight: primary
- path: 02_sources/Clipping/What about Japan_ (Part II).md
  pages: Full document
  weight: secondary
related:
- node: '[[Central_Bank_Balance_Sheet_Structure_Liabilities_Assets]]'
  relation: specialized_case
- node: '[[JGB_Yield_Spillover_Transmission]]'
  relation: risk_trigger
- node: '[[Financial Repression Distributional Welfare Effects]]'
  relation: shared_tag:japan
- node: '[[Financial Repression via Reserve Creation]]'
  relation: shared_tag:japan
- node: '[[Japan FILP to QE Structural Succession]]'
  relation: shared_tag:japan
- node: '[[QE Duration Extraction from Private Sector]]'
  relation: shared_tag:japan
- node: '[[Yen Intervention Liquidity Drain Mechanism]]'
  relation: shared_tag:japan
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Overview
As of 2023-2026, the consolidated Japanese public sector balance sheet has been identified not merely as a debt-laden entity, but as a massive **Sovereign Carry Trade**. By consolidating the BoJ, public pension funds (GPIF), and financial institutions, a single budget constraint emerges that exploits interest rate differentials [RAW-CLIP].

## Mechanics of the Carry Trade

### 1. Funding (The Liabilities)
- **Floating Rate Debt:** The BoJ flooded the system with bank reserves (91% of GDP by 2023). These are essentially overnight, floating-rate liabilities with near-zero cost during the YCC era [RAW-CLIP].
- **Duration Shortening:** QE converted long-term government bonds into short-term reserves, effectively adding a giant "fixed-for-floating swap" to the public balance sheet [RAW-CLIP].

### 2. Deployment (The Assets)
The borrowed funds are invested in long-duration, high-risk assets:
- **Domestic Equities:** 39% of GDP.
- **Unhedged Foreign Securities:** 57% of GDP (largely US Treasuries and global stocks) [RAW-CLIP].

## The Excess Return Era (2013-2023)
Between 2013 and 2023, this sovereign carry trade earned an annualized excess return of **4.66%** above funding costs, totaling **6.25% of GDP** [RAW-CLIP]. This "profit" helped mask Japan's underlying fiscal unsustainability.

## Structural Vulnerabilities in 2026
As the BoJ normalizes (policy rate at 0.75% in April 2026) and JGB yields rise (>200bps since 2022), the framework enters a "Capital Loss" phase:
- **Funding Cost Surge:** Interest paid on the 91% of GDP in bank reserves rises immediately with every BoJ hike [RAW-CLIP].
- **Asset Devaluation:** Rising rates cause capital losses on the long-duration equity and bond portfolios [RAW-CLIP].
- **Duration Mismatch:** Japan is funding 75-year duration assets (equities) with overnight liabilities, creating extreme sensitivity to real rate shocks [RAW-CLIP].

## Global Impact: The "Japan Dump"
To cover rising funding costs or stabilize the Yen, the Japanese public sector is structurally incentivized to liquidate its unhedged foreign securities (primarily US Treasuries). This creates a persistent "wall of selling" in global markets as the carry trade unwinds [LLM].

