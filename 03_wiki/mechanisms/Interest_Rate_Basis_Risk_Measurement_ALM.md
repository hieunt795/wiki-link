---
node_id: interest_rate_basis_risk_measurement_alm_001
type: mechanism
title: Interest Rate Basis Risk Measurement in ALM
aliases:
- basis risk ALM
- multi-curve ALM framework
- EURIBOR OIS basis spread
- tenor basis swap ALM
- rủi ro cơ sở lãi suất ALM
- đa đường cong chiết khấu ALM
- chênh lệch EURIBOR OIS
domain:
  primary: alm
  secondary: []
tags:
- basis-risk
- node: '[[IRRBB]]'
  relation: related_to
- multi-curve
- node: '[[EURIBOR]]'
  relation: related_to
- node: '[[OIS]]'
  relation: related_to
- tenor-basis
- gap-analysis
- key-rate-duration
- node: '[[NII]]'
  relation: related_to
- node: '[[PV01]]'
  relation: related_to
confidence: 1
stability: stable
thesis: 'Post-2008, basis spreads between EURIBOR tenors and between IBOR and OIS
  became material and persistent, requiring ALM to shift from a single-curve to a
  multi-curve framework where OIS rates are used for discounting and separate forward
  curves are constructed per tenor; gap-based NII sensitivity and key-rate duration
  arrays (6–10 buckets) are then applied to manage non-parallel rate shocks and tenor-specific
  repricing mismatches. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 4: Basis Risk and Key Rate Durations in ALM'
parent_node: null
related:
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[NMD_Decay_Model_Volume_Segmentation]]'
  relation: related_to
- node: '[[Hedge_Accounting_IFRS9_ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

Post-2008, basis spreads between EURIBOR tenors and between IBOR and OIS became material and persistent, requiring ALM to shift from a single-curve to a multi-curve framework. [LLM] OIS rates serve as the risk-free discounting curve while separate forward curves are constructed per IBOR tenor; gap-based NII sensitivity and key-rate duration arrays capture non-parallel rate shocks and tenor-specific repricing mismatches. [LLM]

## Why Basis Spreads Became Material Post-2008

Before the 2008 financial crisis, EURIBOR and OIS rates tracked each other closely, and the basis between 3M and 6M EURIBOR was negligible. [LLM] The crisis revealed counterparty credit risk embedded in interbank lending rates: [LLM]

- **IBOR vs OIS spread:** EURIBOR/LIBOR reflect unsecured lending risk; OIS reflects nearly risk-free overnight rates. During stress, the IBOR-OIS spread widened to hundreds of basis points, becoming a permanent feature of the curve. [LLM]
- **Tenor basis:** 6M EURIBOR vs 3M EURIBOR: the 6M rate commands a term premium for unsecured lending, creating a non-zero tenor basis that varies with credit market conditions. [LLM]
- **Consequence for ALM:** Loans priced off 6M EURIBOR funded by liabilities repricing at 3M or OIS introduced basis risk that was previously unmodeled. [LLM]

## Multi-Curve Construction

The post-2008 multi-curve framework separates discounting from forward-rate projection: [LLM]

| Curve | Purpose | Instruments used |
|-------|---------|-----------------|
| **OIS curve** | Risk-free discounting (all cashflows) | OIS swaps, central bank rate expectations |
| **3M forward curve** | Project 3M IBOR-linked cashflows | 3M IBOR FRAs, 3M IBOR swaps vs OIS |
| **6M forward curve** | Project 6M IBOR-linked cashflows | 6M IBOR swaps vs OIS, tenor basis swaps |

[LLM]

Each forward curve is built separately then used to project cashflows, which are discounted on the OIS curve. [LLM] This eliminates the pre-crisis assumption that all IBOR tenors share a single curve. [LLM]

## Gap Analysis and NII Sensitivity Formula

The standard repricing gap formula for NII sensitivity remains: [LLM]

> **ΔNII = GAPᵢ × T × Δr**

Where: [LLM]
- GAPᵢ = rate-sensitive assets minus rate-sensitive liabilities in time bucket i [LLM]
- T = fraction of year remaining in bucket i [LLM]
- Δr = parallel rate shift (e.g., +100bp) [LLM]

In a multi-curve environment, separate gap reports are maintained per repricing index (3M EURIBOR gap, 6M EURIBOR gap, OIS gap, fixed-rate gap), enabling basis-specific NII sensitivity analysis. [LLM]

## Basis Swap Sensitivity Array

To hedge or measure basis exposure, ALM constructs a **basis swap sensitivity array**: [LLM]

- For each maturity bucket (e.g., 1Y, 2Y, 3Y, 5Y, 7Y, 10Y), compute the PV01 of the basis position (6M vs 3M basis swap notional at that maturity). [LLM]
- The array shows where the bank is long or short basis across the yield curve. [LLM]
- Hedging uses tenor basis swaps: pay 6M EURIBOR, receive 3M EURIBOR plus basis spread. [LLM]

## Key-Rate Duration Framework

Parallel rate shock analysis (single ΔNII or ΔEVE) is insufficient for basis risk and non-parallel yield curve scenarios. [LLM] Key-rate durations (KRD) provide a more granular view: [LLM]

- The yield curve is divided into **6–10 maturity buckets** (e.g., 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 15Y, 20Y+). [LLM]
- For each bucket, compute the EVE sensitivity to a 1bp shift in that bucket's rate holding all others constant (partial PV01). [LLM]
- The KRD array captures steepener/flattener risk (P5 regulatory shock) that a single duration number cannot detect. [LLM]
- ALCO reviews the KRD array to identify concentrated exposures in specific maturity segments and to guide macro hedge allocation. [LLM]

## Interaction with BCBS IRRBB Regulatory Shocks

The six BCBS regulatory shocks (parallel up/down, steepener, flattener, short-rate up, short-rate down) all generate different KRD-weighted impacts. [LLM] A bank that passes the parallel-shock SOT may still fail if it has a concentrated steepener exposure. [LLM] Key-rate analysis is therefore essential for full compliance with the spirit of BCBS Principles 4–6. [LLM]

---
*Source: Chapter 4 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
