---
node_id: external_debt_sustainability_and_reserve_adequacy_framework_001
type: framework
title: External Debt Sustainability and Reserve Adequacy Framework
aliases:
- External Debt Sustainability
- Reserve Adequacy
- Debt Service Ratio
- Import Cover
- tinh ben vung no nuoc ngoai
- du tru ngoai hoi du thich
domain:
  primary: macro_outlook
tags:
- external-debt
- reserve-adequacy
- bop
- imf
- sustainability
- debt-service
confidence: 4
stability: evolving
thesis: The IMF external debt sustainability framework links debt stock dynamics (D_t
  = D_{t-1} + disbursements − amortization + valuation adjustments) to ratio indicators
  of solvency (debt/GDP, debt/exports) and liquidity (debt service/exports, import
  coverage of reserves). Reserve adequacy requires ≥3 months import cover at minimum,
  but ultimately depends on policy credibility, not ratios alone.
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: Ch.4, pp.110-115
  weight: primary
parent_node: null
related: []
date_created: '2026-05-31'
date_updated: '2026-05-31'
components:
- 'Debt stock equation: D_t = D_{t-1} + B_t − A_t + valuation adjustments'
- 'Debt solvency indicators: Debt/GDP, Debt/Exports'
- 'Debt liquidity indicator: Debt Service/Exports (> 25% = warning)'
- 'Reserve import cover: Gross Reserves / Monthly Imports ≥ 3 months'
- 'Policy credibility dimension: adequate ratios may be insufficient if credibility
  is low'
application_domain: macro_outlook
---

## Overview

The IMF external debt sustainability framework tracks how a country's foreign debt stock evolves over time and whether the country can service it. It links the **flow** dimension (debt-creating transactions in the BOP financial account) to the **stock** dimension (outstanding debt), and provides ratio indicators to assess both solvency (can debt be repaid?) and liquidity (can near-term payments be made?). [RAW-BOOK Ch.4, pp.110-115]

## Components

**Debt Stock Equation**: the fundamental accounting identity linking debt flows to debt stocks:

  D_t = D_{t-1} + B_t − A_t + Valuation Adjustments

Where:
- D_t = gross external debt stock at end of period t
- B_t = new disbursements (gross borrowing)
- A_t = amortization (principal repayments)
- Valuation adjustments: debt in foreign currencies changes in domestic-currency value when the exchange rate moves; interest arrears capitalized add to D_t

This equation means the BOP financial account flows and the debt stock must be consistent — a check on data quality. [RAW-BOOK Ch.4, p.110]

**Debt Solvency Indicators** (long-run capacity to repay):
- Debt/GDP: compares debt stock to economic output capacity
- Debt/Exports: compares stock to annual FX earnings; captures whether exports can ultimately service debt

**Debt Liquidity Indicators** (near-term payment capacity):
- Debt Service/Exports: (interest + amortization) / export receipts
  - Rule of thumb: > 25% is a warning signal
- Short-term debt/Total debt: proportion of debt due within one year (rollover risk)

**Reserve Adequacy Indicators**:
- Import cover: Gross International Reserves / Monthly Import Bill ≥ 3 months (conventional minimum); ≥ 6 months is comfortable [RAW-BOOK Ch.4, p.113-114]
- Greenspan-Guidotti rule: Reserves ≥ Short-term external debt (covers one year of external rollover risk) [LLM — named rule; source describes the concept]

## Core Identity

Within the BOP framework:
- CA deficit = net inflow via FA (borrowing or FDI)
- Debt-creating flows in FA increase D_t; equity (FDI) does not increase debt
- Sustainable: CA deficit is financed by FDI + long-term debt at r < g (growth)
- Unsustainable: CA deficit financed by short-term debt at r > g → debt/GDP rising without bound

## How to Apply

Step 1: Construct debt stock using the accumulation equation; verify against BOP financial account flows.
Step 2: Identify currency composition of debt → compute valuation adjustments under FX stress scenario.
Step 3: Compute debt service schedule (interest + amortization by year) → debt service ratio.
Step 4: Compare gross reserves to import coverage (3-month rule) and to short-term debt due.
Step 5: Assess credibility dimension: even adequate reserves can be insufficient if policy credibility is low (capital flight can deplete reserves faster than the import-cover metric suggests). [RAW-BOOK Ch.4, p.115]

## Limitations

Import coverage is a static metric — it assumes BOP flows continue as projected. It does not capture sudden stops or capital flow reversals, which can drain reserves in days. [LLM]

The debt/GDP ratio is sensitive to both nominal GDP (denominator can be inflated) and valuation (foreign debt stock in domestic currency units rises when currency depreciates — the "original sin" problem). [LLM]

## Evidence and Sources

[RAW-BOOK Ch.4, pp.110-115] Ouanes and Thakur: debt stock equation (Eq.4.5), debt service indicators, reserve adequacy metrics including the 3-month import rule and the credibility dimension (Poland 1991 example).

## Related Concepts

[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]] provides the BOP accounting framework from which debt-creating flows are drawn. [[Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design]] addresses exchange rate sustainability, the complement to debt sustainability.

