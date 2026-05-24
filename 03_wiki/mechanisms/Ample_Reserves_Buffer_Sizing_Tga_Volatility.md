---
node_id: ample_reserves_buffer_sizing_tga_volatility_001
type: mechanism
title: Ample Reserves Buffer Sizing TGA Volatility
aliases:
- ample reserves buffer
- reserves buffer sizing
- TGA buffer formula
- buffer du tru hop ly
- Armenter buffer formula
domain:
  primary: monetary_policy
tags:
- fed
- reserves
- tga
- balance_sheet
- ample_reserves
- rate_control
- buffer_sizing
confidence: 1
stability: evolving
thesis: The minimum ample reserves buffer required for rate control can be estimated
  as B = sigma*sqrt(Delta)*z*(epsilon*Delta/2), where sigma is the standard deviation
  of TGA changes over the intervention interval Delta; calibrated to 2021-2025 parameters
  (sigma~00bn/2-week), this yields a buffer of 00-400bn — halving to 00-150bn if TGA
  volatility returned to pre-pandemic levels, implying that TGA management reform
  is the most tractable lever for Fed balance sheet reduction.
source_refs:
- path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
  pages: ''
  weight: primary
related:
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
- node: '[[Fed_Ample_Reserves_Buffer_Sizing_Formula]]'
  relation: duplicate_stub_route
date_created: '2026-05-22'
date_updated: '2026-05-24'
---


## Scope Boundary

[LLM] This node is canonical for the quantitative ample-reserves buffer-sizing formula linked to TGA volatility.

[LLM] [[Fed_Ample_Reserves_Buffer_Sizing_Formula]] is a duplicate stub and should route here unless it is later expanded with distinct source evidence.

[LLM] The qualitative TGA volatility mechanism belongs to [[Tga_Volatility_And_Reserve_Buffer_Demand]].

## Formula
[LLM] Minimum buffer B (in billions) for ample reserves:

  B = sigma * sqrt(Delta) * z*(epsilon * Delta / 2)

Where:
- sigma = std deviation of TGA change over interval Delta (e.g. ~100bn per 2-week period in 2021-25)
- Delta = length between Desk interventions (set Delta=1 by choosing units accordingly)
- epsilon = accepted fault probability per unit time
- z* = normal quantile at epsilon*Delta/2

## Parameter Values (2021-2025)
[LLM] Armenter calibration:
- sigma (2-week TGA std dev): ~00bn
- Delta: 2 weeks (old reserve maintenance period)
- z*: 3 (implies ~99.5% confidence, fault once per 200 months)
- Result: B ~ 3 * 00bn = **00bn** (bracketed to 00-400bn given upside uncertainty)

## TGA Volatility Sensitivity
[LLM] Buffer is LINEAR in sigma:
- Pre-pandemic (2016-2019): sigma(2wk) ~ 0bn -> buffer ~ 00-150bn
- Post-pandemic (2021-25): sigma(2wk) ~ 00bn -> buffer ~ 00-400bn
- Implication: reducing TGA management volatility (Vissing-Jorgensen proposal) could halve required buffer, shrinking Fed balance sheet by ~2pp nominal GDP

## Applicability Limit
[LLM] Formula holds for intervals up to ~2 months (TGA approximates martingale at this frequency). Longer intervals overstate buffer because mean-reversion forces kick in at quarterly frequency.

## Policy Implication
[LLM] The buffer size depends more on TGA volatility than on the precise level of ample reserves. This creates a direct policy lever: Treasury + Fed coordination on TGA management => smaller balance sheet without sacrificing rate control.


