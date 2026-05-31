---
node_id: lcr_secured_funding_run_off_by_collateral_quality_asset_level_001
type: concept
title: Lcr Secured Funding Run Off By Collateral Quality Asset Level
aliases:
- secured funding run-off
- LCR repo run-off
- collateral quality run-off rates
- tỷ lệ rút vốn repo LCR theo tài sản đảm bảo
domain:
  primary: alm
tags:
- lcr
- secured_funding
- repo
- collateral
- run_off_rate
- alm
- bcbs
confidence: 3
stability: evolving
thesis: 'LCR secured funding run-off (bcbs238 §112-115): maturing secured transactions
  (repos, securities lending) assumed to roll over at rates depending on collateral
  quality: 0% for Level 1 HQLA or central bank counterparty; 15% for Level 2A collateral;
  25% for Level 2B RMBS or for funding with domestic sovereign/PSE/MDB counterparty
  where collateral is not L1/L2A (PSE RW ≤20% only); 50% for other Level 2B collateral;
  100% for all others. Correction vs LLM stub: the 25% counterparty bucket is not
  generic "central bank/sovereign" — it applies only to domestic sovereign, qualifying
  PSEs (RW ≤20%), or MDBs as counterparty with non-HQLA collateral. Level 1 HQLA
  repo is self-funding in stress (0% run-off); non-HQLA repo funding disappears entirely
  (100%).'
source_refs:
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§112-115'
  weight: primary
parent_node: null
related:
- lcr_retail_deposit_run_off_rates_stable_less_stable_categories_001
- lcr_wholesale_unsecured_funding_run_off_by_counterparty_type_001
- hqla_classification_level1_level2a_level2b_001
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

Secured funding run-off rates under LCR 30-day stress (bcbs238 §112-115):

**Definition (§112):** Secured funding = liabilities collateralised by legal rights to designated assets in the event of bankruptcy/insolvency. Covers repos, securities lending, collateral swap outflows.

**Run-off rate table (bcbs238 §115 Table):**

| Collateral / Counterparty | Run-off rate |
|---|---|
| Level 1 HQLA collateral (any counterparty) OR central bank counterparty | **0%** |
| Level 2A collateral | **15%** |
| Level 2B RMBS collateral | **25%** |
| Domestic sovereign / qualifying PSE (RW ≤20%) / MDB counterparty with non-L1/L2A collateral | **25%** |
| Other Level 2B collateral | **50%** |
| Margin lending backed by non-HQLA | **50%** |
| All others (including non-HQLA with private sector counterparty) | **100%** |

**Key mechanism — self-funding incentive:**
- A repo book collateralised entirely with Level 1 HQLA runs off at 0% → the bank can always roll this funding in stress
- Non-HQLA repo (e.g., corporate bonds as collateral with non-sovereign counterparty) → 100% assumed non-rollover → effective funding disappears
- This creates a strong structural incentive to use HQLA as repo collateral and hold Level 1 assets on balance sheet

**Scope:** Applies to maturing transactions within the 30-day horizon. Transactions with contractual maturity beyond 30 days: excluded (0% assumed outflow).

