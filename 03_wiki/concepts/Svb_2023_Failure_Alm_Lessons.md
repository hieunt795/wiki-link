---
node_id: svb_2023_failure_alm_lessons_001
type: concept
title: SVB 2023 Failure — ALM Lessons
aliases:
- SVB failure
- Silicon Valley Bank 2023
- SVB duration mismatch
- SVB HTM portfolio failure
- sự sụp đổ SVB 2023
- bài học quản lý ALM từ SVB
- rủi ro thời hạn danh mục HTM
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- SVB
- duration-mismatch
- HTM-portfolio
- concentration-risk
- governance-failure
confidence: 3
stability: stable
thesis: '"Silicon Valley Bank failed because of a textbook case of mismanagement
  by the bank. Its senior leadership failed to manage basic interest rate and liquidity
  risk. Its board of directors failed to oversee senior leadership and hold them
  accountable. And Federal Reserve supervisors failed to take forceful enough action."
  (Michael S. Barr, Vice Chair for Supervision, Federal Reserve). Hidden USD 15.2bn
  unrealized loss in USD 95bn HTM portfolio; duration gap ~3 years; >88% uninsured
  concentrated depositor base; 8 months without a CRO.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch4, SVB Case Study (lines 2557–2675)
parent_node: null
related:
- node: '[[Eve_Calculation_Mechanics_Discount_And_Shock]]'
  relation: related_to
- node: '[[NMD_Stochastic_Three_Factor_Model]]'
  relation: related_to
- node: '[[Integrated_Stress_Testing_Capital_Liquidity_Link]]'
  relation: related_to
- node: '[[ALM_Enterprise_Risk_Management_Framework]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- node: '[[NMD]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Background

SVB was founded in 1983 in Santa Clara, California, focused on clients in innovation, entrepreneurship, and technology industries. By 2022, SVB's assets exceeded USD 200bn (16th largest US bank). SVB experienced a rapid influx of deposits from venture capital and technology clients during a period of exceptionally low interest rates; these deposits were largely invested in securities with longer maturities. [RAW-Tata ch.4 §4.1]

**March 8, 2023:** SVB reported losses of USD 1.8bn on sale of USD 21bn fixed income securities. Customers attempted to withdraw USD 142bn in deposits. **March 10, 2023:** SVB collapsed and was seized by its regulator. **March 17, 2023:** SVBFG filed Chapter 11. [RAW-Tata ch.4]

## Early Warning Signs

1. **Vacant CRO:** CRO Laura Izurieta resigned April 29, 2022. SVB had no CRO for eight months until Kim Olson assumed the role December 27, 2022. [RAW-Tata ch.4 §4.2]

2. **Minimal hedging:** Only USD 15.3bn (~12.3%) of the USD 124bn bond portfolio was hedged with pay-fixed/receive-floating interest rate swaps at end-2021.

3. **Hedge unwind:** ~USD 11bn of the USD 15.3bn swap positions were unwound in H1 2022 — not because the portfolio was shrinking, but "to juice its P&L in the short term." By end-2022, only USD 0.5bn in hedges remained (0.4% of portfolio).

4. **Uninsured deposit concentration:** At end-2021, uninsured deposits were USD 166bn — more than **88% of total non-maturity deposits** and an 87% increase from USD 88.6bn a year earlier. Non-FDIC-insured deposits (above USD 250k per depositor) are subject to rapid withdrawal at any sign of counterparty credit risk. [RAW-Tata ch.4 §4.2]

## Balance Sheet Analysis (ALM Lens)

**GAAP vs. economic reality:** SVB's year-end 2022 balance sheet showed equity of ~USD 12bn (5.7% of total assets of USD 212bn). Hidden within the HTM book: **USD 15.2bn unrealized GAAP loss** — implying a 2.7% rate increase caused this, and a **duration of 6.25 years on the USD 95bn HTM book**. Without GAAP accounting, the bank's equity would have been completely wiped out by EoY 2022. The AFS book contributed an additional ~USD 1.7bn loss. [RAW-Tata ch.4 §4.3.1]

**NII perspective:** SVB appeared healthy from NII: USD 4.5bn for 2022; average interest income 2.73%; average interest expense 0.57%; NIM 2.15%. [RAW-Tata ch.4 §4.3.2]

**Duration gap:** ~45% of deposits were from tech startups and VCs who temporarily "park" money — implying short behavioral duration. The **duration gap was ~3 years**. A 3-year duration gap × USD 209bn × 2% ≈ USD 12.5bn loss — more than 100% of equity under a 200bp Basel shock. To avoid being an "outlier bank" under the EVE supervisory outlier test, the duration of deposits would have to be greater than **3.7 years** — "a highly unreasonable assumption." [RAW-Tata ch.4 §4.3.3]

**Q1 2023:** Investors attempted to withdraw USD 42bn in a single day.

## Behavioral Model Failure

SVB's depositor base was concentrated in technology startups whose deposit behavior is driven by two correlated interest-rate-sensitive factors:
1. The general level of interest rates affects how much investors allocate to PE/VC funds (low rates → "chase yield" → more VC activity → more deposits at SVB).
2. The level of interest rates affects VC funds' ability to invest in start-ups (higher rates → fewer deals → withdrawal of parked capital from SVB).

These two factors don't even have the same causal relationship, making modeling complex. SVB "made model changes that reduced the level of risk depicted by the model (…) management changed assumptions rather than the balance sheet to alter reported risks. In April 2022, [SVB] made a poorly supported change in assumption to increase the duration of its deposits based on a deposit study conducted by a consultant." The assumptions were unsubstantiated given rapid deposit growth, lack of historical data, rapid rate increases, and the uniqueness of SVB's client base. [RAW-Tata ch.4 §4.3.4, citing Barr 2023]

## Lessons Learned

Per Michael S. Barr (Fed Vice Chair for Supervision): "Silicon Valley Bank failed because of a textbook case of mismanagement by the bank." Key lessons: [RAW-Tata ch.4 §4.4]

- Accounting (HTM classification) can conceal unrealized losses — making **prudent ALM even more important**.
- Proper governance is imperative — flying blind for 8 months without a CRO "did not reflect well on SVB's board and management; in this case, supervisors failed to catch the lack of governance."
- Heavy concentration in SVB's customer base (mostly VC-backed tech companies) "should have received more supervisory attention" — modeling assumptions for highly correlated NMDs from a small group of similar depositors "should have been questioned and challenged."
- Despite claims to the contrary, "large (and unhedged) maturity mismatches on banks' balance sheets pose a great potential danger."
