---
node_id: stress_testing_management_actions_before_after_presentation_conservative_rules_001
type: concept
title: Stress Testing Management Actions Before After Presentation Conservative Rules
aliases:
- management actions stress test
- before after management actions ST
- hanh dong quan ly kiem tra cang thang
- EBA management actions stress
domain:
  primary: alm
tags:
- eba
- stress_testing
- management_actions
- icaap
- ilaap
- '2018'
confidence: 3
stability: stable
thesis: 'EBA GL/2018/04 §194-199 requires: (1) Results must be presented before AND
  after management actions (§197). "Before" includes strategy/growth assumptions but
  excludes actions unavailable under stress (winding down a business line, raising
  capital — §197). (2) Actions must be consistent with stated strategies/policies,
  e.g. dividend policy (§196). (3) Conservative about feasibility — recognise that
  stress scenarios impair access to markets and counterparties (§196). (4) Distinguish
  immediate vs contingent actions with pre-defined triggers (§196). (5) Acceptable
  action categories (§198): review risk appetite/limits, risk mitigation techniques,
  liquidity/funding/capital policies, reduce shareholder distributions, change strategy/business
  plan, raise capital or funding. Note: EBA GL does not use the term "double-counting"
  explicitly; the no-double-count rule for ICAAP/ILAAP actions derives from SSM ILAAP
  Guide (ECB, 2018) requirement to integrate capital and liquidity feedback loops.'
source_refs:
- path: 02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md
  pages: '§194-199 (4.8.2 Management actions)'
  weight: primary
parent_node: null
related:
- ilaap_recovery_plan_management_actions_no_double_counting_001
- stress_testing_solvency_liquidity_interaction_icaap_ilaap_integration_001
- liquidity_stress_test_nccf_survival_horizon_output_metrics_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

Management actions in stress testing — EBA GL/2018/04 §194-199:

## Presentation Rule: Before and After (§197)

Stress test results must always show **two versions**:

**Before management actions:**
- Include: strategy assumptions, growth projections, associated revenue
- Exclude: actions unavailable under stress (raising capital in a stressed market, winding down business lines) — §197 explicitly carves these out

**After management actions:**
- Show quantitative and qualitative impact of each action
- Document differentiated actions per scenario and adjusted to scenario severity (§199)

---

## Rules for Acceptable Actions (§196, §198)

**Feasibility constraint (§196):** Institutions must be conservative about their ability to execute actions in stress — stressed markets reduce liquidity, raise costs, and may make certain actions impossible.

**Trigger discipline (§196):** Distinguish:
- **Immediate actions**: taken at stress onset, no external trigger needed
- **Contingent actions**: activated only when specific, pre-defined events occur

**Policy consistency (§196):** Actions must be consistent with stated strategies and policies (e.g. dividend policy per CRD Article 141 maximum distributable amount).

**EBA-listed acceptable categories (§198):**
1. Review internal risk appetite and risk limits
2. Review risk mitigation techniques
3. Revise liquidity/funding or capital adequacy policies
4. Reduce distributions to shareholders
5. Change overall strategy, business plan, risk appetite
6. Raise capital or funding

---

## Double-Counting: ICAAP ↔ ILAAP

The EBA GL does not use "double-counting" explicitly. The rule derives from:
- **EBA GL §267(e-f)**: "solvency-liquidity adverse loops" and "interlinkages between solvency and liquidity stress tests" must be documented
- **SSM ILAAP Guide (ECB, 2018) Example 7.1**: ICAAP and ILAAP stress tests must integrate capital and liquidity feedback loops — losses from asset liquidation increase funding costs which worsen solvency; and vice versa
- Implication: an action (e.g. asset sale) deployed in ILAAP stress reduces CBC; the same asset cannot also be credited as capital buffer recovery in ICAAP

