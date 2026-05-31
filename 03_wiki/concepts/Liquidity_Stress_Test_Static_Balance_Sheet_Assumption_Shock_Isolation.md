---
node_id: liquidity_stress_test_static_balance_sheet_assumption_shock_isolation_001
type: concept
title: Liquidity Stress Test Static Balance Sheet Assumption Shock Isolation
aliases:
- static balance sheet assumption
- shock isolation liquidity stress
- giả định bảng cân đối tĩnh
- ECB/SSM liquidity stress methodology
domain:
  primary: alm
tags:
- liquidity_stress_testing
- methodology
- static_balance_sheet
- ecb_ssm
- fsi
confidence: 3
stability: stable
thesis: 'BIS FSI Insights No. 59 §35 + Table 2: the ECB/SSM sector-wide liquidity
  stress test uses a static balance sheet assumption — no bank reactions after the
  reference date, no new sources of inflows, no contract renegotiations, no management
  responses. Purpose: assess the intensity of the initial shock impact before mitigating
  actions, and enable clean cross-bank comparability. Static assumption is unrealistic
  but intentional — it provides an upper bound for inherent vulnerability under the
  shock. Alternative: dynamic approaches (BCB uses bank-specific scenarios; Riksbank/SCB
  maintains broadly static but replaces some term assets/liabilities). EBA GL/2018/04
  §188 formally defines "static balance sheet" as: constant balance sheet + unchanged/stable
  business model throughout projection period, permitting inclusion of new assets/liabilities
  only insofar as they bear the same characteristics as excluded ones.'
source_refs:
- path: 02_sources/regulator/bcbs/insights59.md
  pages: '§35, Table 2 (ECB/SSM approach), §36'
  weight: primary
- path: 02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md
  pages: '§188 (static balance sheet definition)'
  weight: secondary
parent_node: null
related:
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
- liquidity_stress_test_nccf_survival_horizon_output_metrics_001
- stress_testing_management_actions_before_after_presentation_conservative_rules_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

## Definition

**Static balance sheet assumption** (EBA GL/2018/04 §188):
> "...the impact of the stress test scenarios is to be measured on the assumption of a 'constant balance sheet' and of an 'unchanged or stable business model' throughout the projection period, enhancing the comparability of results across institutions."

Permits inclusion of new assets/liabilities **only** if they bear the same main characteristics (maturities, risk profiles) as excluded ones — i.e. like-for-like replacement only, no new business growth.

---

## Operationalisation: ECB/SSM Sector-Wide LST

**Source:** BIS FSI Insights No. 59 §35:

> "the ECB/SSM assumes a static balance sheet in its stress test exercise. This means that no bank reactions are taken into account and, in particular, **no new sources of inflows** after the reference date, **no renegotiations of contracts** and **no revaluation of management's responses** can take place."

**In practice (Table 2, ECB/SSM):**
- All haircuts applied instantaneously at t=0
- Preset run-off rates for sight deposits (conservative)
- Term assets/liabilities: only small fraction assumed to be replaced at maturity; replacement coefficient lower for flightier funding (FI deposits vs commercial deposits)

---

## Purpose and Trade-off

| Benefit | Trade-off |
|---|---|
| Clean cross-bank comparability | Unrealistic — management always reacts |
| Isolates pure shock intensity (upper bound) | May overstate survival difficulty |
| Enables system-wide aggregation | Misses dynamic amplification from collective management responses |
| Supervisory tool for identifying vulnerabilities | Not suitable as stand-alone pass/fail for bank-level adequacy |

---

## Contrast: Dynamic Balance Sheet Approaches

| Authority | Approach | Notes |
|---|---|---|
| ECB/SSM | Static — no management actions | Comparable; top-down by SSM |
| SCB (Riksbank) | Static-leaning — small replacement of term items | Broadly comparable; 6-month horizon |
| BCB (Brazil) | Dynamic — bank-specific scenarios, historical calibration | Not directly comparable; BCB aggregates |
| ILAAP (bank-run) | Dynamic — management actions allowed, must be presented "before and after" (EBA GL §197) | Bank-specific; must document action feasibility |

---

## Relationship to NCCF / Survival Horizon

Static B/S assumption → pre-management-action NCCF → **survival horizon (pre-CBC)**

The gap between pre-CBC and post-CBC survival horizon quantifies the value added by management actions.
Static assumption is the baseline; the "before management actions" panel in ILAAP results uses the same principle.

