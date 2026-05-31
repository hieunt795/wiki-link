---
node_id: stress_testing_solvency_liquidity_interaction_icaap_ilaap_integration_001
type: regulation
title: Stress Testing Solvency Liquidity Interaction Icaap Ilaap Integration
aliases:
- solvency liquidity stress link
- ICAAP ILAAP stress integration
- tuong tac von va thanh khoan stress
- capital liquidity feedback
domain:
  primary: alm
tags:
- eba
- stress_testing
- icaap
- ilaap
- solvency_liquidity_link
- '2018'
confidence: 3
stability: stable
thesis: 'EBA GL/2018/04 §187-193 + SSM ILAAP Guide (ECB, 2018) require explicit integration
  of ICAAP and ILAAP stress tests through two feedback loops: (A) solvency→liquidity:
  capital ratio deterioration triggers market perception effects — higher CDS spreads,
  withdrawal of wholesale funding, collateral haircut increases; (B) liquidity→solvency:
  forced asset sales (fire sales) generate mark-to-market losses and P&L hits, eroding
  capital. Requirements: ICAAP stress ≥2-year horizon (§189d); consistent management
  action assumptions across both (SSM ILAAP Guide Example 7.1 — losses from asset
  liquidation increase funding costs which worsen solvency); results before and after
  management actions (§197); funding cost increases from liquidity stress must feed
  into P&L projections in ICAAP (EBA GL §163).'
source_refs:
- path: 02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md
  pages: '§187-193 (4.8.1), §163, §267(e-f)'
  weight: primary
- path: 02_sources/regulator/bcbs/ECB Guide to the internal liquidity adequacy assessment process (ILAAP).md
  pages: 'Example 7.1 (ICAAP/ILAAP stress interaction), §30 (ILAAP-RAF-recovery plan link)'
  weight: secondary
parent_node: null
related:
- stress_testing_management_actions_before_after_presentation_conservative_rules_001
- ilaap_recovery_plan_management_actions_no_double_counting_001
- liquidity_stress_test_nccf_survival_horizon_output_metrics_001
- integrated_stress_testing_capital_liquidity_link_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

## Two Feedback Loops

**A: Solvency → Liquidity** (capital deterioration triggers liquidity outflows):
- CDS spread widening → unsecured wholesale funding more expensive or unavailable
- Credit rating downgrade → contractual collateral calls, derivative margin triggers
- Public perception of capital weakness → retail and corporate deposit withdrawals
- Interbank counterparties reduce exposure limits → repo and interbank funding withdrawal

**B: Liquidity → Solvency** (liquidity stress creates capital losses):
- Fire sales of assets below book value → mark-to-market losses on remaining portfolio
- Asset liquidation → realised losses → P&L deterioration → capital erosion
- Increased funding costs (wider spreads) → NII compression → lower earnings
- EBA GL §163: "institutions should assess the impact of increasing funding costs on P&L"

---

## ICAAP/ILAAP Integration Requirements

**EBA GL §187-193:**
- Both assess sufficiency: ICAAP = capital resources; ILAAP = liquidity resources
- §188: Test reliability of capital plans AND liquidity plans under stress — transferability of both is assessed
- §189c: Comprehensive institution-wide stress test covers both simultaneously
- **§189d: ICAAP stress tests must cover ≥2-year forward-looking period**; ILAAP stress: overnight to 12 months (§155)
- §190: Consistent with risk appetite and business strategy; institutions must demonstrate they can rebuild liquidity positions after using buffers

**SSM ILAAP Guide, Example 7.1 (ECB, 2018):**
> "The institution is expected to assess the potential impact of relevant scenarios, integrating capital and liquidity impacts and potential feedback loops, taking into account, in particular, losses arising from the liquidation of assets or increases in funding costs during periods of stress."

---

## Practical Integration: What Must Be Documented

```
ICAAP scenario → capital impact → funding cost effect → ILAAP cash flow adjustment
ILAAP scenario → forced asset sale → P&L loss → ICAAP capital deduction

The loops must be:
  ① Quantified (at least in directional terms with sensitivity analysis)
  ② Documented in both the ICAAP and ILAAP submissions
  ③ Reflected in management action consistency — an asset sold in ILAAP
     cannot simultaneously be the capital recovery asset in ICAAP
```

**EBA GL §267(e-f):** Stress testing programme review must assess:
- "How to incorporate possible solvency-liquidity adverse loops"
- "The adequacy of possible interlinkages between solvency stress tests and liquidity stress tests"

