---
node_id: credit_spread_risk_banking_book_csrbb_001
type: concept
title: Credit Spread Risk in the Banking Book (CSRBB)
aliases:
- CSRBB
- credit spread risk banking book
- hazard rate model CSRBB
- OAS banking book
- reduced-form credit model ALM
- rủi ro chênh lệch tín dụng sổ ngân hàng
- CSRBB mô hình tỷ lệ rủi ro
- OAS sổ ngân hàng
domain:
  primary: alm
  secondary: []
tags:
- credit-spread
- hazard-rate
- reduced-form
- duration
confidence: 3
stability: stable
thesis: 'CSRBB is the sensitivity of banking book economic value to changes in credit
  spreads, included for the first time in BCBS IRRBB standards (2016). Three modelling
  approaches each imply different effective durations: the cashflow/hazard rate model
  captures duration shortening from default-contingent early termination; the credit-spread-adjusted
  discount model overstates duration by ignoring reduced asset lifetime; the OAS model
  produces the longest (most overstated) duration. Preferred method depends on data
  availability and portfolio default risk profile.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 11: Credit Spread Risk in the Banking Book'
parent_node: null
related:
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[Hedge_Accounting_IFRS9_ALM]]'
  relation: related_to
- node: '[[Interest_Rate_Basis_Risk_Measurement_ALM]]'
  relation: related_to
- node: '[[CSRBB]]'
  relation: related_to
- node: '[[OAS]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[IFRS9]]'
  relation: related_to
- node: '[[LGD]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

ALM risk management has traditionally focused on interest rate risk, but BCBS IRRBB standards published in 2016 include credit spread risk as an additional component, as changes in credit spreads could amplify the risk arising from IRRBB. [RAW-Elkenbracht-Huizing ch.11 p.1]

BCBS standards define CSRBB scope as: only market credit risk and liquidity risk are included; idiosyncratic credit risk and duration risk are excluded. Creating a credit spread free of other components is a challenge because it is usually impossible to distinguish these elements in market prices. [RAW-Elkenbracht-Huizing ch.11 p.1]

## Reduced-Form Valuation Framework

Under the reduced-form approach (Jarrow and Turnbull 1995; Duffie and Singleton 1999), the price of a claim with default risk is expressed as the present value of the promised payoff discounted at the **default-adjusted short rate**: [RAW-Elkenbracht-Huizing ch.11 p.2]

> **R_t ≈ r_t + λ_t × L_t**

Where λ_t is the hazard rate (conditional default probability at time t) and L_t is the LGD. The credit spread equals λ_t × L_t — the expected loss rate per period. A high recovery rate (low LGD) produces a reduced equivalent credit spread. [RAW-Elkenbracht-Huizing ch.11 p.2]

## Three Modelling Approaches and Duration Effects

The impact of credit spreads on Market Value of Equity (MVE) can be modelled via three approaches that are equivalent in market value but **differ in duration sensitivity**: [RAW-Elkenbracht-Huizing ch.11 p.3]

### 1. Cashflow / Hazard Rate Model

Adjusts cashflows by defaults and recovery — a default results in early termination of the asset, reducing the outstanding balance and resulting in a **shorter duration**. For products with a high default risk, this is the most suitable approach as the tolerance for variation is smallest. High recovery rate produces a shorter duration, as a greater proportion of the asset's value is paid off earlier. [RAW-Elkenbracht-Huizing ch.11 p.3]

### 2. Credit-Spread-Adjusted Discount Model

Incorporates recovery as a reduced spread, but **fails to capture the reduced lifetime of the asset** (ignores lost interest). This omission causes the model to **overstate duration** — duration grows as recovery increases, because the method does not distinguish the reduced lifetime. [RAW-Elkenbracht-Huizing ch.11 p.3]

### 3. OAS Model

Incorporates credit and prepayment aspects only via adjustment to the discount rate on contractual cashflows. As the OAS model only reflects the forfeited income or P&L consequence of a default, it is **not sensitive to the reduction in lifetime** from prepayments or defaults. This produces a **substantially longer duration** than the other approaches. Best applied for products with clear market prices. [RAW-Elkenbracht-Huizing ch.11 p.3]

## Macroeconomic Drivers of Default

Key macroeconomic variables in credit default models: [RAW-Elkenbracht-Huizing ch.11 p.3]

- **Unemployment rates** — higher unemployment → higher default probability
- **House prices / LTV** — price falls reduce borrower's disincentive to default and reduce creditor recovery
- **GDP growth** — contraction in economy drives adverse changes in unemployment and credit quality

The value of factoring in the interest rate–credit correlation for MVE sensitivity is "questionable" due to lagging effects, but is more important for stress testing and capital requirements. [RAW-Elkenbracht-Huizing ch.11 p.3]

## IFRS 9 and Double-Counting

IFRS 9 raises the question of consistency between behavioural assumptions for IRRBB and forward-looking provisions. If MVE results have already been adjusted for credit quality, the IFRS 9 provision is effectively already incorporated. Hedging both IFRS 9 provisions AND credit-spread-adjusted MVE figures would result in **increased valuation volatility rather than a reduction**, due to double counting. Any hedging should reflect one or the other, not both. [RAW-Elkenbracht-Huizing ch.11 p.2]

Care must be taken to avoid double counting with existing credit capital requirements on any assets introduced into the capital framework. [RAW-Elkenbracht-Huizing ch.11 p.4]

## Implementation Guidance

- For products **with clear market prices**: OAS approach preferred.
- For products **without market prices**: credit spread curves by sector, rating, or geography.
- For portfolios with **high default risk**: cashflow estimation method most suitable (lower tolerance for variation). [RAW-Elkenbracht-Huizing ch.11 p.4]

Calibrating the spread without market prices: use historical PD and recovery, or prevailing lending rates as a proxy adjusted by appropriate issuer spread. [RAW-Elkenbracht-Huizing ch.11 p.4]
