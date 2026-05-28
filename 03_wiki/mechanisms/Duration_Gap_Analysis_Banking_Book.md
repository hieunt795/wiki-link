---
node_id: duration_gap_analysis_banking_book_001
type: mechanism
title: "Duration Gap Analysis in the Banking Book"
aliases:
  - duration gap
  - funding gap
  - maturity gap (duration-based)
  - phân tích khoảng cách thời lượng
  - khoảng cách thời lượng ngân hàng

domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - duration
  - EVE
  - IRRBB
  - modified_duration
  - banking_book

confidence: 1
stability: stable

thesis: >
  [LLM] The duration gap measures the net interest rate sensitivity of a bank's economic value by comparing the weighted-average modified duration of assets to that of liabilities (scaled by the liability/asset ratio); a positive duration gap means rising rates reduce EVE, and the estimated EVE loss equals duration_gap × total_assets × Δr.

source_refs:
  - path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
    pages: "Ch 2, section 2.1.4; Ch 4, section 4.3.3; Ch 2, section 2.2.5"
    weight: primary

related:
  - node: "[[Eve_Calculation_Mechanics_Discount_And_Shock]]"
    relation: related_to
  - node: "[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]"
    relation: related_to
  - node: "[[Irrbb_Eve_Nii_Dual_Metric_Framework]]"
    relation: component_of

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Definition and Formula

Duration gap (D_gap) = D_A − (L/A) × D_L

where:
- D_A = position-weighted average modified duration of assets
- D_L = position-weighted average modified duration of liabilities (excluding equity)
- L/A = total liabilities divided by total assets (the liability-to-asset ratio)

[LLM] The EVE sensitivity to a rate change Δr is then approximated as:

ΔEVE ≈ −D_gap × A × Δr

where A is total assets. [LLM] This is the banking-book analogue of the bond price-yield relationship: ΔP ≈ −P × ModD × Δi, applied at the balance-sheet level.

## Worked Example (Tata 2025 Model Bank)

[LLM] Using the illustrative model bank (total assets = 500, equity = 50, liabilities = 450):

| Product | Modified Duration |
|---|---|
| Bonds (50) | 4.45 |
| Loans (300) | 0.50 |
| Mortgages (150) | 1.00 |
| Term deposits (150) | 0.25 |
| Savings accounts (200) | 0.50 |
| Interbank deposits (100) | 2.00 |

D_A = (50×4.45 + 300×0.50 + 150×1.00) / 500 = 1.195  
D_L = (150×0.25 + 200×0.50 + 100×2.00) / 450 = 0.903  
D_gap = 1.195 − (450/500) × 0.903 = 1.195 − 0.812 = 0.383

[LLM] With a duration gap of 0.383, a 1% rise in rates causes a loss of 0.383% × 500 = 1.915, which is 3.83% of the 50 equity. The Basel 200 bp shock doubles this to approximately 7.66%. This is slightly higher than the repricing gap method estimate (6.96%) for the same balance sheet, illustrating that the two methods are approximations that converge but do not give identical results.

## Key Properties

[LLM] Modified duration estimates used in the duration gap must reflect *behavioral* maturity, not contractual maturity. For non-maturity deposits (sight deposits, savings accounts), behavioral duration is typically modeled as substantially longer than the overnight contractual maturity. Misjudging this behavioral duration — as occurred at Silicon Valley Bank — is a primary source of ALM failure.

[LLM] The duration gap is sensitive to balance sheet composition:
- Asset-heavy banks with long-duration fixed-rate bonds or mortgage portfolios will have large positive duration gaps.
- Banks that fund long assets with short liabilities (classic maturity transformation) will have positive duration gaps, meaning they lose EVE when rates rise.
- A duration gap of zero achieves EVE immunization, but this typically introduces NII risk (see EVE-NII trade-off).

## SVB Case Application

[LLM] At Silicon Valley Bank (year-end 2022), the HTM securities book had an estimated duration of 6.25 years (implied by the USD 15.2 bn unrealized loss on a USD 95 bn portfolio for a 2.7% rate rise). [LLM] The bank's deposit base consisted of approximately 45% tech startup and VC-related deposits, likely with behavioral duration of 1 year or less given their transactional nature. Tata (2025) estimates SVB's duration gap at approximately 3 years, implying an EVE loss of USD 209 bn × 2% × 3 = USD 12.5 bn under the Basel 200 bp shock — exceeding 100% of the bank's equity of USD 12 bn. [LLM] To pass the EVE outlier test (ΔEVE < 15% of Tier 1 capital under 200 bps), SVB's deposit duration would have needed to be at least 3.7 years — an unreasonable behavioral assumption given the depositor base.

## Relationship to Repricing Gap

[LLM] The repricing gap and duration gap approaches produce similar but not identical EVE estimates. The repricing gap applies an average modified duration weight to positions grouped by time bucket, whereas the duration gap calculates precise position-level durations and aggregates them. [LLM] The duration gap is more precise but requires individual duration estimates; the repricing gap is simpler and is the basis for the EBA standardized approach (SA) methodology.
