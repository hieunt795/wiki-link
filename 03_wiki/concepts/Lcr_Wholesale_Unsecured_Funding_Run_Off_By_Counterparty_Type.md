---
node_id: lcr_wholesale_unsecured_funding_run_off_by_counterparty_type_001
type: concept
title: Lcr Wholesale Unsecured Funding Run Off By Counterparty Type
aliases:
- wholesale funding run-off
- LCR wholesale outflows
- operational deposits 25%
- tỷ lệ rút vốn bán buôn LCR
- wholesale counterparty outflow rates
domain:
  primary: alm
tags:
- lcr
- wholesale_funding
- run_off_rate
- outflow_rates
- alm
- bcbs
confidence: 3
stability: evolving
thesis: 'LCR wholesale unsecured funding outflows (bcbs238 §87-104) are calibrated
  by counterparty type: (a) Small business (≤€1M): retail treatment 5%/10% (§89);
  (b) Operational deposits — clearing, custody, cash management: 25% for qualifying
  operational portion only; non-operational portion at 40% or 100% depending on
  counterparty (§93-98); (c) Non-financial corporates, sovereigns, PSEs, multilaterals:
  40% for non-operational deposits; (d) Financial institutions and central banks
  (non-operational): 100%; (e) Other legal entities: 100%. Term deposits callable
  only after >30 days: 0% (§87). Operational deposits at other institutions carry
  0% inflow assumption for the depositing bank (§98).'
source_refs:
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§87-104'
  weight: primary
parent_node: null
related:
- lcr_retail_deposit_run_off_rates_stable_less_stable_categories_001
- lcr_secured_funding_run_off_by_collateral_quality_asset_level_001
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

Wholesale unsecured funding run-off rates under LCR 30-day stress (bcbs238 §87-104):

**Tiered by counterparty type and operational relationship:**

| Counterparty | Deposit type | Run-off rate |
|---|---|---|
| Small business (≤€1M) | Stable | 5% |
| Small business (≤€1M) | Less stable | 10%+ |
| Any wholesale counterparty | Term deposit >30d callable notice | 0% |
| Clearing/custody/cash mgmt (qualifying operational) | Operational portion | 25% |
| Clearing/custody/cash mgmt | Non-operational portion | 40% |
| Non-financial corporates, sovereigns, PSEs, MDBs | Non-operational | 40% |
| Financial institutions, central banks | Non-operational | 100% |
| Other legal entities | All | 100% |

**Qualifying operational deposits (§93-95):**
- Activity: clearing, custody, or cash management
- Customer reliant on the bank as independent third-party intermediary for normal banking over 30 days
- Deposits must be by-products of underlying services, not sought for interest income
- Excess over operational need → treated at counterparty-appropriate rate (40% or 100%)

**Operational deposit held AT another institution (§98):**
- 0% inflow assumption for the depositing bank — these funds are operationally locked and not available to repay other outflows

