---
node_id: lcr_retail_deposit_run_off_rates_stable_less_stable_categories_001
type: concept
title: Lcr Retail Deposit Run Off Rates Stable Less Stable Categories
aliases:
- retail deposit run-off
- LCR stable deposit 5%
- less stable deposit 10%
- tỷ lệ rút tiền tiền gửi bán lẻ LCR
- deposit run-off rate
domain:
  primary: alm
tags:
- lcr
- run_off_rate
- retail_deposits
- deposit_insurance
- alm
- bcbs
confidence: 3
stability: evolving
thesis: 'The LCR (bcbs238 §73-84) defines two retail deposit categories with different
  30-day outflow assumptions: (1) Stable deposits — 5% standard run-off rate; 3% if
  the jurisdiction has a qualifying deposit insurance scheme (prefunded via periodic
  levies, binding coverage, well-funded, high public awareness — §78). Deposit insurance
  alone does not make a deposit stable (§77). (2) Less stable deposits — minimum 10%,
  with supervisors free to add higher buckets for online-only, foreign currency, or
  high-value deposits (§79). Term deposits with residual maturity >30 days and no
  legal right of early withdrawal (or with material early-withdrawal penalty): excluded
  from outflows (§82). Small business deposits (≤€1M, managed as retail): same
  treatment as retail (§89).'
source_refs:
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§73-84, §89'
  weight: primary
parent_node: null
related:
- lcr_wholesale_unsecured_funding_run_off_by_counterparty_type_001
- lcr_secured_funding_run_off_by_collateral_quality_asset_level_001
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

Retail deposit run-off rates under the LCR 30-day stress scenario (bcbs238 §73-84):

**Stable deposits (§75-78):**
- Standard run-off: **5%**
- Qualifying DIS rate: **3%** — only if jurisdiction meets all 5 criteria: prefunded via periodic bank levies, legally binding coverage, well-funded, high public awareness, prompt payout
- Eligibility: fully insured AND (depositor has other established relationship making withdrawal unlikely OR deposit is transactional/salary account)
- Deposit insurance alone is insufficient to qualify a deposit as stable (§77)

**Less stable deposits (§79-80):**
- Minimum run-off: **10%**
- Supervisors may add additional buckets with higher rates for: online-only accounts, foreign-currency deposits, high-value deposits, deposits from non-resident customers
- If a bank cannot identify which deposits are stable (e.g., cannot determine DIS coverage), the full amount goes into the less stable bucket (§80)

**Term deposits >30 days (§82):**
- Run-off: **0%** — excluded from total outflows if depositor has no legal right to withdraw within 30 days, or if early withdrawal triggers a material penalty (materially greater than interest forfeited)

**Small business deposits (§89):**
- Deposits from small business customers (≤€1M threshold, managed as retail): same 5%/10% treatment as retail, not wholesale

