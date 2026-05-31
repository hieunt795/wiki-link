---
node_id: nmd_stochastic_three_factor_model_001
type: framework
title: NMD Stochastic Three-Factor Model
aliases:
- NMD stochastic model
- three-factor deposit model
- Vasicek deposit volume model
- NMD Cholesky Monte Carlo
- mô hình ba nhân tố ngẫu nhiên tiền gửi NMD
- Monte Carlo tiền gửi không kỳ hạn
- rủi ro nén biên lãi suất tiền gửi
domain:
  primary: alm
  secondary: []
tags:
- stochastic-model
- credit-spread
- Monte-Carlo
- margin-compression
- floor-risk
- replicating-portfolio
confidence: 3
stability: stable
thesis: 'The Bohn stochastic three-factor NMD model drives deposit value via correlated
  short rate, credit spread, and deposit volume processes; a Cholesky decomposition
  of the correlation matrix captures interdependencies; the risk appetite confidence
  level φ defines the replicating portfolio as the interest-rate hedge covering deposit
  funding costs at the φ-percentile; margin compression risk — from market rates
  falling to the client-rate floor — requires raising hedge ratios before rates breach
  zero.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 6: Non-Maturity Deposits — A Stochastic Model Approach (Bohn)'
parent_node: null
related:
- node: '[[NMD_Decay_Model_Volume_Segmentation]]'
  relation: related_to
- node: '[[ALM_Low_Negative_Interest_Rate_Environment]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[NMD]]'
  relation: related_to
- node: '[[Vasicek]]'
  relation: related_to
- node: '[[Cholesky]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

This chapter (Bohn, BCG) introduces an approach to hedging non-maturing deposits under stochastic deposit volumes, interest rates and credit spreads. The method captures: (1) outflows from unexpected weakening of a financial institution's creditworthiness; (2) **negative convexity from margin compression risk** — the risk of market rates falling close to or below a floor for interest rates paid to clients. The approach manages the **economic value** of client deposit portfolios. [RAW-Elkenbracht-Huizing ch.6 p.1]

## Three Stochastic Factors

The economy is modelled with three stochastic factors: the short-term interest rate, the credit spread of the deposit-taking institution, and the deposit volume. Their **interdependencies** are captured in a correlation matrix CORR with three cross-correlations: [RAW-Elkenbracht-Huizing ch.6 p.3]

- ρ_{r,c}: correlation between changes in interest rates and credit spreads
- ρ_{r,D}: correlation between changes in interest rates and deposit volumes
- ρ_{c,D}: correlation between changes in credit spreads and deposit volumes

As these correlation parameters cannot be derived from market prices, they are best estimated from historical time series. A **Cholesky decomposition** of CORR yields matrix G such that GG^T = CORR; its elements specify the stochastic processes for each factor. [RAW-Elkenbracht-Huizing ch.6 p.3]

## Risk Appetite Parameter φ and the Replicating Portfolio

The bank defines its risk appetite by limiting the probability of deposit balance D(t) falling below the invested hedge amount A(t): [RAW-Elkenbracht-Huizing ch.6 p.2]

> P[D(t) < A(t)] ≤ φ

The factor **φ** represents the bank's risk aversion with respect to liquidity shortfalls. Key calibration guidance: [RAW-Elkenbracht-Huizing ch.6 p.2]

- Confidence levels between φ = 0.01 and φ = 0.1 appear in line with **conservative risk appetite**.
- φ = 0.5 implies an **unchanged balance development**, resulting in a **perpetual replicating portfolio**.

The replicating portfolio A(t) is constructed with a "horizontal" view of tranches that can be rolled over continuously — converting the vertical profile of maturing balances into fixed tranches per maturity bucket. The rollover frequency can be annual, semi-annual, quarterly, or monthly. [RAW-Elkenbracht-Huizing ch.6 p.2]

When client rate elasticity with respect to market rate changes is above zero, the notional amount of the replicating portfolio must be adjusted (away from 100% notional hedge). [RAW-Elkenbracht-Huizing ch.6 p.2]

## Margin Compression Risk and Hedge Ratio Adjustment

**Margin compression risk** = the risk that the net interest margin is reduced due to a floor in client rates while the hedge rate drops with market rate levels. [RAW-Elkenbracht-Huizing ch.6 p.1]

The approach allows the ALM manager to **adjust hedge ratios in an environment of high interest rates** — not just when rates are low and the net interest margin is directly threatened. This is the key insight: raising hedge ratios ahead of reaching the floor, rather than reacting when already there. [RAW-Elkenbracht-Huizing ch.6 p.1]

## Application to Decay Models

The chapter also illustrates applications to decay models, linking the stochastic volume modelling to the decay approach of Chapter 5 (Soulellis). The stochastic approach captures the uncertainty in future deposit volumes that the deterministic decay model takes as given. [RAW-Elkenbracht-Huizing ch.6 p.1]
