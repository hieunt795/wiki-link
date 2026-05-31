---
node_id: liquidity_stress_test_nccf_survival_horizon_output_metrics_001
type: concept
title: Liquidity Stress Test NCCF and Survival Horizon Output Metrics
aliases:
- NCCF liquidity stress
- net cumulative cash flow stress test
- survival horizon liquidity
- lowest cumulative net cash flow point
- chân trời sống sót thanh khoản
- dòng tiền tích lũy ròng kiểm tra căng thẳng
domain:
  primary: alm
tags:
- liquidity_stress_testing
- nccf
- survival_horizon
- counterbalancing_capacity
- eba
- methodology
confidence: 3
stability: stable
thesis: 'EBA GL/2018/04 §159-161 defines two primary LST output metrics: (1) Net Cumulative
  Cash Flow (NCCF) — the time-series output; for each scenario and stress level, the
  institution projects inflows and outflows per future period and identifies the lowest
  cumulative NCF point within the assessed time horizon; (2) Survival horizon — derived
  from counterbalancing capacity (CBC); the first time period at which CBC is exhausted,
  reported before and after deployment of management actions. NCCF is the core methodology;
  survival horizon is the scalar summary. LCR is a special case: a standardised 30-day
  NCCF under bcbs238 scenario. LCR ≥ 100% does not imply survival horizon ≥ 30 days
  because the two use different scenarios and behavioural assumptions.'
source_refs:
- path: 02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md
  pages: '§155, §159-162'
  weight: primary
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§19 (LCR scenario)'
  weight: secondary
parent_node: null
related:
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
- liquidity_stress_three_scenario_types_idiosyncratic_market_wide_combined_eba_001
- ilaap_recovery_plan_management_actions_no_double_counting_001
- basel_iii_lcr_hqla_cashflow_mechanics_001
date_created: '2026-05-29'
date_updated: '2026-05-29'
---

## 1. Net Cumulative Cash Flow (NCCF) — Core Methodology

**Source:** EBA GL/2018/04 §159

The main methodology for calculating LST impact is the **net cash flow profile**:

```
For each scenario × time horizon:
  NCF(t) = Inflows(t) − Outflows(t)          ← period net flow
  NCCF(T) = Σ NCF(t) for t = 1 to T          ← cumulative

Key output: lowest cumulative point of NCCF within the assessed time period
```

**Time horizons required** (§155):

| Phase | Horizon | Purpose |
|---|---|---|
| Short acute | Overnight → 30 days | Survive without business model change |
| Prolonged | 3 → 12 months | Sustained less-acute stress |
| Intraday | Separate test | Intraday payment/settlement obligations |

§156 further requires: combine short/medium liquidity stress with funding risk stress, minimum 12-month time horizon.

---

## 2. Survival Horizon — Scalar Summary Metric

**Source:** EBA GL/2018/04 §160(c)

> "The survival horizon of the institution as derived from its counterbalancing capacity, i.e. the institution's ability to hold, or have access to, excess liquidity over short-term, medium-term and long-term time horizons in response to stress scenarios... and stressed cash flows, taken jointly, before and after the impact of counterbalancing measures."

**Definition:** First time period t at which Counterbalancing Capacity (CBC) is exhausted under the stress scenario.

**Two versions always reported:**

```
Survival horizon (pre-CBC):  pure structural — no management action
Survival horizon (post-CBC): deployed CBC — reflects all available tools

Gap between the two = value of management action capacity
```

---

## 3. Counterbalancing Capacity (CBC)

**Source:** EBA GL §160(b)

CBC = HQLA buffer (post-haircut) + unencumbered monetisable assets + pre-arranged CB repo access

**Conservative approach rule** (§161): CB counterbalancing effects (monetary policy) must be treated conservatively — access cannot be assumed unless pre-arranged and operationally tested. The available liquidity buffer assessment must also quantify the proportion of encumbered assets.

---

## 4. Interpretation Framework

| Metric | What it answers | Regulatory parallel |
|---|---|---|
| NCCF(t) time series | When does the gap appear? How deep at each horizon? | LCR 30-day single point |
| Lowest NCCF point | Maximum cumulative funding need under scenario | LCR denominator analogue |
| Survival horizon (pre-CBC) | How long bank survives with no management action | — |
| Survival horizon (post-CBC) | How long bank survives deploying all CBC tools | ILAAP adequacy test |

---

## 5. Relationship to LCR

LCR is a **standardised special case** of NCCF:
- Fixed 30-day horizon
- Standardised bcbs238 scenario (combined idiosyncratic + market-wide shock per §19)
- Standardised haircuts and run-off rates — not institution-specific calibration

**LCR ≥ 100% ≠ survival horizon ≥ 30 days** because:
- LCR scenario is more severe in some dimensions (standardised 100% FI outflows)
- ILAAP scenarios may capture institution-specific vulnerabilities LCR doesn't
- Behavioural assumptions differ: LCR uses fixed floors; ILAAP uses institution-calibrated rates
