---
node_id: duration_targeting_bond_portfolio_framework_001
type: framework
title: Duration Targeting Bond Portfolio Framework
aliases:
- DT Framework
- Duration-Targeted Portfolio
- Chiến lược nhắm mục tiêu duration
domain:
  primary: financial_markets
tags:
- duration
- bond_portfolio
- immunization
- fixed_income
- rebalancing
confidence: 3
stability: evolving
thesis: Institutional bond portfolios implicitly or explicitly maintain a stable duration
  target via periodic rebalancing, creating a predictable convergence toward initial
  yield at the 'effective maturity' horizon (≈ 2× duration target), regardless of
  the yield path taken.
source_refs:
- path: 02_sources/books/homer_leibowitz_yield_book/Homer_Leibowitz_Inside_the_Yield_Book.md
  pages: Introduction, Chapter 1
  weight: primary
parent_node: null
related:
- node: '[[Bond Accrual Price Effect Interaction]]'
  relation: shared_tag:duration
- node: '[[Duration Targeting Convergence And Yield Trap]]'
  relation: shared_tag:duration
- node: '[[DV01, Duration, and Convexity — Fixed Income Risk Measures]]'
  relation: shared_tag:duration
- node: '[[Financial Repression Distributional Welfare Effects]]'
  relation: shared_tag:duration
- node: '[[QE Duration Extraction from Private Sector]]'
  relation: shared_tag:duration
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
Proposed and analyzed by Homer & Leibowitz, the **Duration Targeting (DT)** framework describes the dominant approach used by institutional bond managers. Rather than buying and holding to a fixed maturity, DT portfolios rebalance continuously to maintain a constant duration — meaning exposure to interest rate risk is stable over time [RAW-CLIP].

## Three Archetypes of Bond Management
1. **Buy-and-Hold (BH):** Fixed maturity, duration drifts as time passes, no rebalancing. Returns converge to initial yield only at exact maturity date.
2. **Immunized Portfolio:** Liability-matching; duration matched to specific liability horizon. A specialized DT case.
3. **Duration-Targeted (DT):** The most common institutional approach. Portfolio duration is kept constant via periodic rebalancing (selling bonds that have shortened and buying longer ones) [RAW-CLIP].

## The "Gravitational Pull" Property
A DT portfolio at horizon H = effective maturity (≈ 2 × duration target D) generates a total return that **converges to the initial yield** regardless of the intervening yield path [RAW-CLIP].

- If yields fall → price gains offset by reinvestment losses at lower coupons → net return ≈ initial yield
- If yields rise → price losses offset by reinvestment gains at higher coupons → net return ≈ initial yield
- This "gravitational pull" is the core insight: DT investors cannot permanently exploit rate moves within their horizon [LLM]

## Trendline (TL) Model
Homer & Leibowitz develop the **Trendline Model** — a linear yield path formulation that enables closed-form total return calculation for DT portfolios. The return depends only on:
- Initial yield Y₀
- Duration target D
- Investment horizon H
- Terminal yield Y_T

This model enables decomposing returns into accrual and price components analytically [RAW-CLIP].

## Institutional Prevalence
Most large institutional bond portfolios (pension funds, insurance companies, sovereign wealth funds) are implicitly DT portfolios because duration mandates or liability-matching requirements force periodic rebalancing. The framework thus applies to the majority of fixed-income AUM [LLM].


