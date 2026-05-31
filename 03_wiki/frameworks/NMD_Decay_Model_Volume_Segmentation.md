---
node_id: nmd_decay_model_volume_segmentation_001
type: framework
title: NMD Decay Model and Volume Segmentation
aliases:
- NMD decay model
- non-maturity deposit behavioralization
- deposit average life estimation
- deposit volume segmentation
- mô hình suy giảm tiền gửi không kỳ hạn
- phân khúc khối lượng tiền gửi NMD
- tuổi thọ trung bình tiền gửi
domain:
  primary: alm
  secondary: []
tags:
- non-maturity-deposits
- decay-model
- behavioralization
- deposit-segmentation
- average-life
- logistic-regression
confidence: 3
stability: stable
thesis: 'Deposit decay modeling estimates the expected remaining life of non-maturity
  deposits (NMDs) by defining "end of life" via logistic regression on threshold-breach
  variables, computing average life via annual midpoint or monthly granular techniques,
  and segmenting the portfolio so that within-segment behavior is homogeneous while
  cross-segment behavioral variance is maximized, enabling each segment to be independently
  modeled and replicated.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 5: Non-Maturity Deposits — A Decay Model Approach (Soulellis)'
parent_node: null
related:
- node: '[[NMD_Stochastic_Three_Factor_Model]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[ALM_Low_Negative_Interest_Rate_Environment]]'
  relation: related_to
- node: '[[NMD]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

Accurate liabilities or deposit-based expected life modelling is widely considered a prerequisite to sound asset-liability management, and its importance in mitigating interest rate risk is undisputed. The key challenge distinguishing NMD modelling from mortgage modelling: deposit balance behaviour is **not necessarily monotonically decreasing** — a savings deposit balance may increase or decrease at any point, driven by macroeconomic conditions, product/pricing structure, and competition. [RAW-Elkenbracht-Huizing ch.5 p.1]

## Four Philosophical Drivers of Deposit Behavior

Four key themes concern a depositor and drive balance stability: [RAW-Elkenbracht-Huizing ch.5 p.1]

1. **Rate of return** — the most important driver; rate-balance elasticity is positively correlated, possibly linear or exponential over a rate interval, but cannot increase into perpetuity due to finite supply of liquid cash in the system.
2. **Liquidity / terms and conditions** — customers avoid excessive withdrawal fees or rates that fall below a balance threshold.
3. **Safety and reputation** — investors want assurance that funds are protected and the institution will not become insolvent.
4. **Service level** — speedy account access, multiple channels (branch, internet, mobile), and relationship quality.

## Defining "End of Life" for a Deposit Cohort

Defining when a deposit account is no longer "alive" is a key modelling step. Dormancy or very low balance levels coupled with inactivity over a significant time period suggest the account has effectively ended its life — but determining the threshold is subjective. [RAW-Elkenbracht-Huizing ch.5 p.2]

**Logistic regression approach:** Build a model that predicts the likelihood of future balance inflows. Example variable set: [RAW-Elkenbracht-Huizing ch.5 p.2]

- B_50_3: balance < £50 for 3 consecutive months
- B_50_6: balance < £50 for 6 consecutive months
- B_5_3 / B_5_6: balance < £5 for 3/6 months
- RCB3/6/12: percentage change in balance over last 3/6/12 months

The regression yields parameter estimates that define a decision logic: if these conditions are met, the account's life can be officially pronounced over. Accounts triggering multiple binary variables AND fast decay rates over 12 months are the most likely end-of-life candidates. [RAW-Elkenbracht-Huizing ch.5 p.2]

## Average Life Calculation

The expected average life calculation depends on: (1) a continuous balance function B(t) over observed and forecasted time; (2) the number of discrete time intervals introduced. Two approaches: [RAW-Elkenbracht-Huizing ch.5 p.3]

**Annual midpoint method:** Divide the cohort into annual intervals; the fraction of balances that survive at each cumulative point is weighted by the midpoint of each year. Produces a "weighted" average life across annual buckets.

**Monthly granular method:** Uses monthly time intervals for finer precision — required when the replicating portfolio uses instruments with sub-annual maturities.

## Segmentation

The chapter provides comprehensive guidance on designing a segmentation scheme to ensure within-segment behavioral homogeneity while maximizing cross-segment variance. Segmentation considerations include product structure, pricing, withdrawal terms, account type, and client characteristics. [RAW-Elkenbracht-Huizing ch.5 p.4]

Key factors driving balance behavior within the multivariate approach: rate of return relative to alternatives, introductory/promotional periods (as main effect or interaction variable), macroeconomic data, product structure's impact on balance behavior, safety/security of the institution, service levels, and lagged terms. [RAW-Elkenbracht-Huizing ch.5 p.4]

## Model Validation Requirements

The chapter specifies validation requirements: [RAW-Elkenbracht-Huizing ch.5 p.5]

- Fit statistics
- Parameter significance (p-values)
- Test for multicollinearity presence
- Residual analysis
- Accuracy levels: development vs. validation samples
- Model stability under stressed scenario testing

Ongoing model monitoring/calibration is required to maintain accuracy over time. [RAW-Elkenbracht-Huizing ch.5 p.5]
