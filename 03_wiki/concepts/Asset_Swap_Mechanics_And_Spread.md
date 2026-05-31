---
node_id: asset_swap_mechanics_and_spread_001
type: concept
title: Asset Swap Mechanics And Spread
aliases:
- Asset Swap
- Asset Swap Spread
- Par Asset Swap
- Yield/Yield Asset Swap
- Hoán đổi tài sản
domain:
  primary: financial_markets
tags:
- swaps
- asset_swap
- credit_spread
- fixed_income
- relative_value
- libor
confidence: 4
stability: evolving
thesis: An asset swap packages a fixed-rate bond purchase with a pay-fixed receive-floating
  interest rate swap, transforming the bond into a synthetic floater; the resulting
  asset swap spread (LIBOR + spread) isolates the bond's credit spread from interest
  rate risk, making it a credit-pure relative value metric.
source_refs:
- path: 02_sources/books/howard_corb_swaps/Howard_Corb_Interest_Rate_Swaps.md
  pages: Chapter 2.5.2, Chapter 8.4
  weight: primary
parent_node: null
related:
- node: '[[Swap Carry And Roll Down Analysis]]'
  relation: shared_tag:swaps
- node: '[[Duration Targeting Bond Portfolio Framework]]'
  relation: shared_tag:fixed_income
- node: '[[Bond Accrual Price Effect Interaction]]'
  relation: shared_tag:fixed_income
- node: '[[Duration Targeting Convergence And Yield Trap]]'
  relation: shared_tag:fixed_income
- node: '[[Eurodollar System Mechanics And Post-Reform Decline]]'
  relation: shared_tag:libor
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Structure
An **asset swap** is a two-part package:
1. Investor **buys a fixed-rate bond** (takes credit exposure).
2. Investor **pays fixed in an IRS** matching the bond's maturity → receives LIBOR ± spread.

The result: investor holds a synthetic floating-rate note with **zero duration** (interest rate risk hedged by the swap) but **full credit exposure** to the bond issuer [RAW-CLIP].

## Two Common Methodologies

**1. Par Asset Swap (traditional):**
- The swap includes an upfront payment to bring the all-in cost to par.
- If bond dirty price < par → dealer pays upfront to investor.
- If bond dirty price > par → investor pays upfront to dealer.
- Fixed leg matches bond coupons exactly (amount + dates).
- Result: investor pays par total and receives LIBOR + asset swap spread [RAW-CLIP].

**2. Yield/Yield Asset Swap (market standard today):**
- No upfront payment; swap notional = bond face value.
- Fixed leg coupon ≠ bond coupon (mismatch accepted).
- Asset swap spread = Bond yield – Swap rate (same maturity).
- Simpler to execute; fixed leg is a standard IRS [RAW-CLIP].

## Asset Swap Spread Interpretation
**High spread** → bond is **cheap** relative to swap curve ("cheap on LIBOR basis") — the bond offers more yield than an equivalent IRS, suggesting excess credit premium [RAW-CLIP].

**Low/negative spread** → bond is **rich** relative to swap curve — typical for AAA/agency bonds that trade through LIBOR [LLM].

## What Risk Remains After Asset Swap?
1. **Credit risk:** The investor still owns the bond's default/spread risk.
2. **Swap spread risk:** If the swap spread on the offsetting IRS widens, the package benefits (fixed payer benefits from spread widening). If swap spreads tighten, the package loses [RAW-CLIP].
3. **Basis between bond credit spread and swap spread:** The hedge is imperfect if the bond's credit spread is not correlated with generic swap spreads [LLM].

## Use Cases
- **Credit investors** seeking pure credit exposure without interest rate duration.
- **Relative value:** Comparing asset swap spreads across same-issuer bonds with different maturities or across issuers in the same sector.
- **New issue hedging:** Corporations issuing fixed debt can use forward starting swaps; investors can immediately asset swap to LIBOR exposure.
- **Mortgage basis trades:** Buy mortgages, pay fixed in swaps to isolate prepayment/spread risk [RAW-CLIP].


