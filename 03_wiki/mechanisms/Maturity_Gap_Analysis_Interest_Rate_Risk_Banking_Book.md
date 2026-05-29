---
node_id: maturity_gap_analysis_interest_rate_risk_banking_book_001
type: mechanism
title: Maturity Gap Analysis Interest Rate Risk Banking Book
aliases:
- repricing gap analysis
- IRRBB gap analysis
- EVE NII sensitivity
- maturity bucket repricing
- phân tích khe hở tái định giá
- gap analysis IRRBB
- interest rate sensitivity banking book
domain:
  primary: alm
tags:
- irrbb
- gap_analysis
- eve
- nii
- repricing_risk
- banking_book
- alm
- basel_irrbb
confidence: 1
stability: evolving
thesis: '[LLM] Maturity gap analysis measures IRRBB by bucketing rate-sensitive assets
  and liabilities into repricing time bands; a positive gap (assets reprice faster
  than liabilities) generates net interest income risk when rates fall, while a negative
  gap generates risk when rates rise. The EVE (Economic Value of Equity) perspective
  computes the present value sensitivity of the entire balance sheet to a parallel
  rate shift, while the NII (Net Interest Income) perspective measures earnings impact
  over a 12-month horizon — Basel IRRBB standards (d368/BCBS) require both.'
source_refs:
- path: 02_sources/books/alm/A - Asset liability optimization.md
  pages: ''
  weight: primary
parent_node: '[[Bank_Alm_Banking_Book_Risk_Management_Framework]]'
related:
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: measured_by
- node: '[[Bank_Alm_Banking_Book_Risk_Management_Framework]]'
  relation: parent_framework
- node: '[[Bcbs_Irrbb_Standards_D368_2016]]'
  relation: regulatory_requirement
- node: '[[Ftp_As_Unified_Balance_Sheet_Control_Mechanism_Transmission_To_Risk_Factors]]'
  relation: ftp_gap_interaction
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

[LLM] Auto-generated stub from A - Asset liability optimization.md. Review and expand.

