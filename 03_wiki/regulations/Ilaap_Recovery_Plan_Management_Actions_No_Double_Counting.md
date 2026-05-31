---
node_id: ilaap_recovery_plan_management_actions_no_double_counting_001
type: regulation
title: Ilaap Recovery Plan Management Actions No Double Counting
aliases:
- ILAAP recovery plan overlap
- double counting crisis capacity
- tránh trùng lắp kế hoạch phục hồi ILAAP
- management actions double-counting
domain:
  primary: alm
tags:
- ilaap
- recovery_planning
- management_actions
- ecb
- governance
confidence: 3
stability: stable
thesis: 'SSM ILAAP Guide (ECB, 2018) Principle 2 / Example 2.2 (§187-189): ILAAP management
  actions and recovery plan options must be consistent and non-overlapping. Actions
  already deployed under the ILAAP reduce the available recovery capacity — if an
  institution has already raised funding under its ILAAP, the same funding capacity
  cannot be counted again in the recovery plan. Rule: any material ILAAP management
  action must be reflected without delay in a re-assessment of recovery plan feasibility.
  The bank''s total crisis response capacity = ILAAP actions + ADDITIONAL (not-yet-used)
  recovery options. Source uses the word "double-counting" explicitly: "in order to
  avoid overlaps between recovery options and ILAAP management actions, which might
  lead to double-counting" (§187).'
source_refs:
- path: 02_sources/regulator/bcbs/ECB Guide to the internal liquidity adequacy assessment process (ILAAP).md
  pages: 'Principle 2, Example 2.2 §183-189 (Consistency between ILAAP and recovery plan)'
  weight: primary
parent_node: null
related:
- stress_testing_management_actions_before_after_presentation_conservative_rules_001
- stress_testing_solvency_liquidity_interaction_icaap_ilaap_integration_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

## The Double-Counting Problem

**Source:** SSM ILAAP Guide (ECB, 2018) Principle 2, Example 2.2 §187-189

> "...in order to avoid overlaps between recovery options and ILAAP management actions, which might lead to **'double-counting'**, material management actions taken under the ILAAP are expected to be reflected without delay in a re-assessment of the feasibility and effectiveness of the recovery options included in the recovery plan." (§187)

> "For instance, the capacity of an institution to raise funding in a recovery situation may be severely affected if the institution has already raised funding under its ILAAP in a situation that does not fall under the recovery plan. This could impact the types and volume of extra funding that could be raised as well as the specification of issuance conditions." (§189)

---

## Mechanics

**ILAAP management actions** = pre-recovery interventions under adverse-but-not-crisis conditions:
- Tapping wholesale funding markets
- Selling liquid assets at market prices
- Reducing RWA / shrinking the loan book
- Activating committed credit lines

**Recovery plan options** = post-trigger crisis measures (after recovery indicators are breached):
- Emergency asset sales (fire sale)
- Capital raises (rights issue, AT1 issuance)
- Structural measures (business line disposal, subsidiary sale)
- Extraordinary CB support

**The rule:**
```
If Action X is used under ILAAP → Action X is no longer available in Recovery Plan
Total crisis response capacity = ILAAP capacity + ADDITIONAL (unused) recovery options

NOT: ILAAP capacity + ALL recovery options (double count)
```

---

## Consistency Requirement (§183-185)

ILAAP and recovery plan must be consistent across the **continuum of liquidity deterioration**:

- Liquidity indicators in the recovery plan (triggers) must be consistently reflected in the ILAAP scenarios
- ILAAP must manage the institution **above** recovery plan indicator thresholds by a prudent margin under normal conditions
- Scenarios in both ILAAP and recovery plan must address the institution's **key vulnerabilities** specifically

---

## Why This Matters in Practice

A bank that counts "emergency bond issuance" as both:
- An ILAAP management action (to survive a 6-month severe scenario), AND
- A recovery plan option (to restore viability after breach of recovery triggers)

...is **overestimating its total crisis capacity**. If it has already tapped markets under ILAAP, market access in a recovery scenario will be impaired (higher spreads, smaller issuance size, reputational damage from having already issued under stress).

