---
node_id: duration_targeting_convergence_and_yield_trap_001
type: mechanism
title: Duration Targeting Convergence And Yield Trap
aliases:
- DT Convergence
- Effective Maturity Rule
- Gravitational Pull
- Yield Trap
- Bẫy lãi suất DT
domain:
  primary: financial_markets
tags:
- duration
- fixed_income
- immunization
- yield_convergence
- bond_return
confidence: 3
stability: evolving
thesis: At the 'effective maturity' horizon (≈ 2× duration target), cumulative accrual
  gains and cumulative price effects exactly offset each other regardless of yield
  direction, creating a convergence to initial yield — and trapping the investor in
  the yield environment at portfolio inception.
source_refs:
- path: 02_sources/books/homer_leibowitz_yield_book/Homer_Leibowitz_Inside_the_Yield_Book.md
  pages: Chapter 1-2
  weight: primary
parent_node: null
related:
- node: '[[Duration Targeting Bond Portfolio Framework]]'
  relation: shared_tag:duration
- node: '[[Bond Accrual Price Effect Interaction]]'
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


## Core Mechanism: Effective Maturity
For a Duration-Targeted (DT) portfolio with constant duration D, the **effective maturity** is approximately:

> **H_eff ≈ 2 × D**

At this horizon, the cumulative gain from reinvesting coupons at changed rates exactly offsets the cumulative capital gain or loss from duration exposure. Total return converges to the initial yield Y₀ [RAW-CLIP].

## Mathematical Intuition
- **Accrual component** grows roughly as ≈ Y₀ × H (linear in horizon)
- **Price component** = –D × ΔY at any point; but this is "paid back" via reinvestment over the remaining horizon
- At H = 2D: the "price debt" accumulated in early periods is exactly repaid by reinvestment gains in later periods [RAW-CLIP]

## Statistical Immunization Window
Within the **stability window** (roughly H < 6-9 years for a 5-year DT portfolio), total return volatility compresses to approximately **±90bps** around initial yield regardless of yield path variance. This is called "Statistical Immunization" [RAW-CLIP].

## The Yield Trap
The convergence property creates a structural trap:

> A DT investor who initiates a portfolio at yield Y₀ cannot escape Y₀ as their approximate terminal return — regardless of how rates move subsequently.

This has important implications:
- Investors initiating in low-yield environments are "locked in" to low returns at effective maturity horizon [RAW-CLIP]
- Active duration extension bets (increasing D) can break the trap but introduce new duration risk
- The only exit is to abandon the DT strategy entirely [LLM]

## Policy Relevance: Japan / ZIRP Context
Japanese life insurers and pension funds that initiated DT portfolios in the 2000-2015 ZIRP era were structurally "trapped" at near-zero yields. Even with subsequent JGB yield normalization (2022-2026), the convergence mechanism means prior-period DT returns cannot be "earned back" — the loss is locked in [LLM].


