---
node_id: mon_pol_trans_short_long_frictions_mec_001
type: mechanism
title: Monetary Policy Transmission Short Long Rate Frictions
aliases:
  - Transmission Frictions
  - Những điểm nghẽn truyền dẫn từ lãi suất ngắn hạn sang dài hạn
  - Short-to-Long Rate Transmission

domain:
  primary: monetary_policy
  secondary: [macro_outlook]
tags: [transmission, interest_rate_channel, yield_curve, term_premium]

confidence: 3
stability: stable

thesis: >
  Transmission from short-term policy rates to medium- and long-term yields is non-linear and subject to structural frictions, including asymmetric effectiveness across business cycles and shifts in market expectations that can decouple policy actions from long-term rate movements.

source_refs:
  - path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
    pages: "Section 2"
    weight: primary

related:
  - node: "[[Monetary_Policy_Transmission_Mechanisms_Framework]]"
    relation: detail_of
  - node: "[[DV01_Duration_Convexity_Fixed_Income]]"
    relation: analytics_for

date_created: 2026-05-20
date_updated: 2026-05-20
---

## Overview
Monetary policy assumes that changes in very short-term (overnight) rates will influence the medium- to long-term rates (e.g., 10-year yields) that drive economic decisions on investment, housing, and consumption. However, this transmission channel is often weak or obstructed by structural factors [RAW-CLIP].

## Key Frictions and Limiting Factors

### 1. Asymmetric Effectiveness
The impact of interest rate changes is not uniform across economic conditions:
- **Boom vs. Recession:** Effectiveness is generally higher during economic booms or periods of high total debt than during recessions or low-debt situations [RAW-CLIP].
- **Borrower Constraints:** In high-debt environments, rate hikes have a more immediate impact on expenditure via higher interest burdens [LLM].

### 2. Declining Efficiency
Since the 1980s, the efficiency of long-term rates in influencing expenditure has declined [RAW-CLIP]. This may be due to shifts in the composition of the economy or changes in how businesses finance investment (e.g., moving from bank loans to capital markets) [LLM].

### 3. Decoupling of Short and Long Rates
Short-term policy rates and 10-year yields do not always move in tandem. Long rates are driven by a variety of market factors independent of current policy:
- **Expectations:** Investor expectations on future growth and inflation.
- **Fiscal Outlook:** Concerns about government debt levels and future supply of bonds.
- **Foreign Flows:** Global capital flows searching for yield or safe assets.
- **Term Premium:** The additional compensation investors require for holding longer-maturity debt [RAW-CLIP].

## Canonical Examples of Transmission Failure

### The "Greenspan Conundrum" (2004)
A classic example where the Fed raised the Fed Funds Rate by 150 basis points, but 10-year yields remained virtually unchanged [RAW-CLIP]. This decoupling illustrated the power of global liquidity and market expectations over domestic policy rates.

### Recent Episodes (2024-2025)
In September 2024 and October 2025, instances occurred where the Fed cut policy rates, yet 10-year yields began to rise [RAW-CLIP]. This reflects a scenario where market concerns (e.g., fiscal deficits or inflation expectations) override the signal from the central bank's short-term rate adjustment.

## Policy Responses to Frictions
To overcome these frictions, central banks have increasingly resorted to "unconventional" measures:
- **Forward Guidance:** Directly attempting to influence future rate expectations.
- **Quantitative Easing (QE):** Directly purchasing long-term securities to compress term premiums and lower long-term yields [RAW-CLIP].
