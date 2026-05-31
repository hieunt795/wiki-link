---
node_id: alm_low_negative_interest_rate_environment_001
type: concept
title: ALM in a Low/Negative Interest Rate Environment
aliases:
- low rate ALM
- negative rate ALM
- deposit beta ALM
- floor risk banking book
- margin compression low rates
- ALM lãi suất thấp âm
- rủi ro sàn tiền gửi
- beta tiền gửi lãi suất thấp
- nén biên lãi suất môi trường lãi thấp
domain:
  primary: alm
  secondary: []
tags:
- low-rate
- negative-rate
- deposit-beta
- floor-risk
- margin-compression
- swaption
- interest-rate-floor
confidence: 3
stability: stable
thesis: 'In a low/negative interest rate environment, ALM functions face new challenges:
  customers may behave differently (challenging product modelling assumptions), certain
  products reveal inherent optionalities, and the objective of stabilising NII becomes
  difficult to achieve. A bank cannot easily protect against ΔEVe impact and simultaneously
  stabilise NII — the composition that reduces NII volatility in a normal environment
  does not work in zero/negative rate environments.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 10: ALM in a Low/Negative Interest Rate Environment'
parent_node: null
related:
- node: '[[NMD_Stochastic_Three_Factor_Model]]'
  relation: related_to
- node: '[[NMD_Decay_Model_Volume_Segmentation]]'
  relation: related_to
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[ILAAP_Supervisory_Liquidity_Framework]]'
  relation: related_to
- node: '[[NII]]'
  relation: related_to
- node: '[[EVE]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

ALM includes the management of interest rate risk arising from a bank's business activities. In cases of very low or even negative interest rates, bank risks present new challenges. ALM functions are typically tasked with stabilising NII banking book revenues — in an environment of negative yields this objective becomes difficult to achieve. [RAW-Elkenbracht-Huizing ch.10 p.1]

## Deposit Beta and the Two Balance Sheet Types

**Deposit beta (depositβ):** expresses deposit rate changes relative to market interest rate changes. [RAW-Elkenbracht-Huizing ch.10 p.1]

Two extreme cases:
- **β = 1:** highly sensitive to market rates — a 1bp market rate increase causes a 1bp customer rate increase, otherwise customers shift/withdraw.
- **β = 0:** current accounts — customers are insensitive to market rate changes.

**Balance sheet A (NII-stable):** funded with 80 O/N deposits (β=1), 10 deposits (β=0), 10 equity. Deposits with β=0 and equity invested in a 10Y asset at 5% coupon. Baseline NII = 0.9 at t₀. ΔEVe in +100bp: approximately −1.81; in −100bp: approximately +2.01.

**Balance sheet B (EVE-stable):** all liabilities (both deposit types) and equity invested in O/N assets. Lower baseline NII = 0.1. ΔEVe ≈ 0 under rate shocks; NII varies with rate changes. [RAW-Elkenbracht-Huizing ch.10 p.2]

## Why Low/Negative Rates Break Balance Sheet A

Applying the same interest rate shocks in a low-rate environment (O/N yield already at 0%, 10Y at 2%) reveals: [RAW-Elkenbracht-Huizing ch.10 p.2]

- **Balance sheet A in −100bp shock:** ΔnII = **−0.8** (NII falls from 0.4 to −0.4). The balance sheet composition that reduces NII volatility in a normal environment does **not work** when rates are at zero or negative. The driver: banks with large retail deposits cannot charge customers negative rates, but the deposit base is invested in money market products or central bank accounts that can trade at negative rates.
- **Balance sheet B in −100bp shock:** ΔnII = **−1.0**, much higher than in the positive rate example, due to the asymmetric payout profile.

Key conclusion: **there is no clear recommendation** between A and B — the answer depends on the business model and risk appetite of the bank. Banks need to balance ΔnII and ΔeVE effects. [RAW-Elkenbracht-Huizing ch.10 p.2]

## Embedded Options in Customer Business (Low Rate Context)

The chapter discusses embedded options in customer business, their impacts on modelling, and possible countermeasures to manage IRRBB for low interest rates. Key regulatory reference included: under German law (Bürgerliches Gesetzbuch Section 489), borrowers may terminate fixed-rate loan contracts after 10 years giving 6 months' notice, and variable-rate contracts at any time giving 3 months' notice — this creates prepayment option risk that becomes particularly costly in low rate environments. [RAW-Elkenbracht-Huizing ch.10 p.3]

The chapter also covers stress testing in negative rate environments, regulatory developments (including removal of the 0% floor in IRRBB stress scenarios), and the effects of technological and competitive changes on banks' risk management in low rate environments.
