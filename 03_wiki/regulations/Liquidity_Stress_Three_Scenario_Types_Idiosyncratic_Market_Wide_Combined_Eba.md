---
node_id: liquidity_stress_three_scenario_types_idiosyncratic_market_wide_combined_eba_001
type: regulation
title: Liquidity Stress Three Scenario Types Idiosyncratic Market Wide Combined Eba
aliases:
- liquidity stress three scenarios
- idiosyncratic market combined scenarios
- ba kich ban cang thang thanh khoan
- EBA 2018 liquidity scenarios
domain:
  primary: alm
tags:
- eba
- stress_testing
- liquidity_risk
- idiosyncratic
- market_wide
- combined
confidence: 3
stability: stable
thesis: 'EBA GL/2018/04 §154 requires three mandatory liquidity stress scenarios: (1)
  Idiosyncratic — institution-specific events (rating downgrade, default of largest
  funding counterparty, loss of market access, loss of currency convertibility, default
  of counterparty providing largest inflows); (2) Market-wide — impact on a group of
  institutions or the financial sector (deterioration in funding market conditions or
  macroeconomic environment, rating downgrades of countries where institution operates);
  (3) Combined — simultaneous idiosyncratic + market-wide, the most severe configuration;
  also the calibration scenario for the LCR (bcbs238 §19). Scenarios are applied across
  multiple time horizons (overnight to ≥12 months: §155) with adverse behavioural
  assumptions designed per scenario and time horizon (§157). Key output: lowest
  cumulative NCF point within assessed time period per scenario (§159).'
source_refs:
- path: 02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md
  pages: '§154-159'
  weight: primary
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§19 (combined scenario = LCR calibration)'
  weight: secondary
parent_node: null
related:
- bcbs_liquidity_stress_testing_p10_001
- liquidity_stress_test_nccf_survival_horizon_output_metrics_001
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

Three mandatory liquidity stress scenarios per EBA GL/2018/04 §154:

## Scenario Types

**① Idiosyncratic** — institution-specific events while system functions normally:
- Rating downgrade (triggers collateral calls, contingent outflows)
- Default of the largest funding counterparty
- Loss of market access (unsecured wholesale, CP, CD markets)
- Loss of currency convertibility
- Default of counterparty providing largest cash inflows

**② Market-wide** — systemic stress affecting a group of institutions or the financial sector:
- Deterioration in funding market conditions (repo, unsecured interbank)
- Macroeconomic environment deterioration (credit spread widening, asset price falls)
- Rating downgrades of sovereigns/countries in which the institution operates

**③ Combined** — simultaneous idiosyncratic + market-wide (most severe):
- Represents the worst-case plausible scenario
- Also the calibration scenario for the LCR (bcbs238 §19: "combined idiosyncratic and market-wide shock")
- Must be included in all ILAAP liquidity stress programmes

---

## Time Horizons and Behavioural Assumptions

Per §155-157:
- **Overnight → 30 days**: short acute phase — no business model change assumed
- **3 → 12 months**: prolonged phase — less acute but sustained
- **Intraday**: separate test for payment/settlement obligations
- For each scenario × time horizon: design specific adverse behavioural assumptions (deposit run-off rates, wholesale rollover, contingent outflows) — not one-size-fits-all

---

## Cross-reference: BCBS Principle 10 (2008)

BCBS Principle 10 (bcbs144 §99) uses a 2×2 matrix:
- Short-term vs protracted × institution-specific vs market-wide
- EBA §154 simplifies to 3 mandatory types; the protracted dimension is captured in the 3-12 month horizon requirement (§155)
- Both require combined scenarios as the most severe configuration

