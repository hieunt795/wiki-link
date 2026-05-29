---
node_id: repricing_gap_analysis_nii_eve_impact_001
type: mechanism
title: 'Repricing Gap Analysis: NII and EVE Impact Measurement'
aliases:
- repricing gap
- income gap
- earning gap analysis
- phân tích khoảng cách tái định giá
- khoảng cách tái định giá
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- repricing
- gap_analysis
- NII
- EVE
- IRRBB
- time_bands
confidence: 1
stability: stable
thesis: '[LLM] Repricing gap analysis is a maturity-bucket technique that allocates
  interest-rate-sensitive assets and liabilities into time bands by their next repricing
  date; the net gap in each bucket reveals where mismatches create NII and EVE risk,
  with the weighted sum of all gaps (scaled by modified duration) estimating the EVE
  decline for a 1% rate shock.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch 2, sections 2.1.3 and 2.2.3
  weight: primary
parent_node: null
related:
- node: '[[Duration_Gap_Analysis_Banking_Book]]'
  relation: related_to
- node: '[[Nii_Sensitivity_Forecast_Static_Dynamic_Balance_Sheet]]'
  relation: related_to
- node: '[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Overview

[LLM] Repricing gap analysis allocates all interest-rate-sensitive balance-sheet positions into predefined time buckets based on the *time remaining until next repricing* (for floating-rate instruments) or *time to maturity* (for fixed-rate instruments). Interest rate risk is assumed only up to the next reset date; once reset to market rates, an instrument reprices back to par.

[LLM] Non-maturity positions (sight deposits, savings accounts, mortgages with prepayment options) are assigned to time bands based on behavioral assumptions about their expected repricing date — not their contractual maturity.

## Five-Step Procedure

**Step 1 – Aggregate positions by product class**  
Group all assets, liabilities, and off-balance-sheet items into product categories (bonds, loans, mortgages, term deposits, savings accounts, interbank deposits, derivatives).

**Step 2 – Assign reset periods**  
[LLM] For each product, identify the reset period — the time until the next interest rate reset. Fixed-rate bonds reset only at final maturity; floating-rate loans reset monthly or quarterly; non-maturity deposits are assigned behavioral maturities.

**Step 3 – Allocate to time buckets**  
Distribute the notional amounts of each product into the standard repricing time bands (e.g., <1 month, 1–3 months, 3–6 months, 6–12 months, 1–2 years, 2–3 years, 3–4 years, 4–5 years). This creates a "repricing ladder."

**Step 4 – Calculate net repricing gaps**  
Net repricing gap (in each bucket) = Σ Assets in bucket − Σ Liabilities in bucket. A negative gap (liability-sensitive) means liabilities exceed assets in that bucket; rising rates will raise interest expense more than interest income.

**Step 5 – Weight and aggregate**  
[LLM] Each net repricing gap is multiplied by an estimated modified duration appropriate for that time band (based on the midpoint of the bucket). Summing the weighted gaps across all time bands gives the *total repricing gap*, which estimates the decline in EVE for a 1% (parallel) increase in interest rates. [LLM] In the illustrative model bank, the total repricing gap is 1.74, meaning EVE declines by 1.74 for a 100 bp shock — which is 3.48% of the 50 equity. Under the Basel 200 bp shock, the ratio is 6.96%.

## Illustrative Example (Tata 2025 Model Bank)

| Time bucket (months) | Net gap | Mod. Duration | Weighted gap |
|---|---|---|---|
| <1 | 0 | 0.04 | 0 |
| 1–3 | −150 | 0.16 | −0.24 |
| 3–6 | +100 | 0.36 | +0.36 |
| 6–12 | +150 | 0.72 | +1.08 |
| 12–24 | −100 | 1.39 | −1.39 |
| 24–36 | 0 | 2.25 | 0 |
| 36–48 | 0 | 3.07 | 0 |
| 48–60 | +50 | 3.86 | +1.93 |
| **Total** | | | **1.74** |

## NII Version: Earning Gap

[LLM] The earning gap restricts the repricing gap analysis to positions that reprice within the first year (or a shorter NII horizon), and weights each bucket not by duration but by the *fraction of the year remaining* after the repricing midpoint. This gives the first-year NII impact per 1% shock. [LLM] In the model bank, positions repricing in the 1–3 month bucket produce a periodic earning gap of −150 × 1% × (10/12) = −0.125. Summing across all within-one-year buckets gives the total earning gap of −0.25, implying a NII decline of 1.00 for a 400 bp shock.

## Limitations

[LLM] The repricing gap framework has three main limitations:
1. It applies a single average duration weight to all positions in a time band, ignoring position-specific duration differences within the bucket (resolved by the duration gap approach or full revaluation).
2. It does not capture basis risk — mismatches in the *rate index* (e.g., 1-month vs 6-month EURIBOR) for positions repricing in the same time band.
3. It does not capture optionality — the possible acceleration or deceleration of cashflows due to prepayment or early withdrawal under different rate scenarios.

[LLM] These limitations are recognized in the BCBS 1997 principles and are addressed by more granular EVE simulation and the EBA standardized approach (SA), which includes explicit optionality add-ons.
