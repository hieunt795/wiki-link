---
node_id: concept_fi_rv_001
type: concept
title: "Fixed Income Relative Value Framework"
aliases:
  - fixed income RV
  - FIRV
  - relative value analysis
  - bond relative value
  - phân tích giá trị tương đối thu nhập cố định

domain:
  primary: financial_markets
tags:
  - fixed-income
  - relative-value
  - carry
  - roll
  - bond-pricing
  - trading-framework

confidence: 2
stability: stable

thesis: >
  Fixed income relative value (RV) is the systematic identification and monetisation of
  price discrepancies between economically similar instruments along four dimensions:
  carry (income earned per unit of risk), roll-down (P&L from yield curve passage of
  time), richness/cheapness (deviation from fitted curve), and duration-neutral spread
  trades. RV positions are constructed to isolate a single mispricing while hedging
  all other exposures.

source_refs:
  - path: 02_sources/books/huggins_schaller_relative_value/Huggins_Schaller_Fixed_Income_RV.md
    weight: primary
  - path: 02_sources/books/tuckman_serrat_fixed_income/Tuckman_Serrat_Fixed_Income_2022.md
    weight: supporting

related:
  - node: "[[Swap_Carry_And_Roll_Down_Analysis]]"
    relation: component_of
  - node: "[[Asset_Swap_Mechanics_And_Spread]]"
    relation: component_of
  - node: "[[DV01_Duration_Convexity_Fixed_Income]]"
    relation: uses
  - node: "[[Interest_Rate_Swaps_OIS_Fixed_Floating]]"
    relation: instrument_for

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

Fixed income relative value analysis, as systematised by Huggins & Schaller (2nd ed., 2024), decomposes the total return of a fixed income position into four measurable components and uses that decomposition to isolate and trade specific mispricings:

1. **Carry**: The income earned from holding a position — coupon received minus financing cost (repo rate). Carry is the baseline return assuming no price change and no yield curve shift.

2. **Roll-down**: The gain (or loss) from the passage of time on a positively (or negatively) sloped yield curve. As a bond approaches maturity, it rolls down the yield curve: a 10-year bond becomes a 9-year bond one year later. If the curve is upward-sloping, the yield falls and the price rises. Roll-down can be computed separately from carry. [LLM]

3. **Richness / Cheapness**: Deviation of a bond's yield from a fitted benchmark curve (e.g., spline or Nelson-Siegel fitted to on-the-run Treasuries). "Cheap" bonds yield more than the curve predicts; "rich" bonds yield less. The convergence of cheap-to-rich is the RV trade thesis. [LLM]

4. **Duration-neutral spread trades**: Pairing long and short positions across instruments with offsetting DV01 exposures, so the combined position has near-zero sensitivity to parallel yield curve shifts while retaining exposure to the spread between specific instruments. [RAW-BOOK Huggins_Schaller_Fixed_Income_RV]

## Core Trade Structures

**On-the-run / Off-the-run spread:** Newly issued Treasuries (on-the-run) trade rich to older issues (off-the-run) due to liquidity premium and index inclusion flows. The OTR/OFR spread is one of the most liquid RV trades.

**Swap spread trade:** Receive fixed on an IRS while being long the equivalent Treasury. The swap spread (Treasury yield minus swap rate) reflects balance sheet costs, credit supply, and regulatory constraints. See [[Asset_Swap_Mechanics_And_Spread]] and [[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]].

**Butterfly trade:** Long the body of the yield curve (e.g., 5-year), short the wings (2-year + 10-year) in DV01-neutral proportions. Expresses a view on curvature (2s5s10s butterfly) without parallel rate exposure. [LLM]

## RV vs Directional

RV analysis explicitly separates **alpha** (spread return from identified mispricing) from **beta** (directional exposure to rate levels). An RV trader structures positions to earn only alpha — duration-hedged, convexity-controlled. This requires precise DV01 and convexity measurement (see [[DV01_Duration_Convexity_Fixed_Income]]) and ongoing mark-to-market of carry/roll decomposition.

## Carry + Roll as RV Decision Input

Huggins & Schaller emphasise carry + roll as the first screen: before assessing richness/cheapness, compute the total carry + roll for each instrument on a comparable risk basis. A bond that appears cheap on yield but has negative carry + roll requires the mispricing to close faster than the carry bleeds. See [[Swap_Carry_And_Roll_Down_Analysis]] for the swap-specific application.
