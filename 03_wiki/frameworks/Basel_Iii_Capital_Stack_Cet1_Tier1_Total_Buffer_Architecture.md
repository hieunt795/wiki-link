---
node_id: basel_iii_capital_stack_cet1_tier1_total_buffer_architecture_001
type: framework
title: 'Basel III Capital Stack: CET1, Tier1, Total + Buffer Architecture'
aliases:
- Basel III capital adequacy
- CET1 minimum requirement
- capital conservation buffer
- Basel III capital stack
- Cấu trúc vốn Basel III
- yêu cầu vốn tối thiểu Basel
domain:
  primary: basel_risk
tags:
- capital_adequacy
- cet1
- tier1
- tier2
- at1
- basel3
- capital_buffer
- mda
- regulatory_capital
confidence: 3
stability: stable
thesis: 'Basel III establishes a three-tier capital hierarchy (CET1, AT1, Tier 2)
  with hard minimums (CET1 ≥ 4.5%, Tier 1 ≥ 6%, Total ≥ 8% of RWA) layered beneath
  a Capital Conservation Buffer of 2.5% CET1; breaching the buffer triggers Maximum
  Distributable Amount (MDA) constraints that mechanically restrict dividends, buybacks,
  and discretionary bonuses in proportion to the shortfall, creating a graduated capital
  restoration regime without formal insolvency.

  '
source_refs:
- path: 02_sources/regulator/bcbs/BaselFramework.md
  pages: CAP10 (Definition of eligible capital), RBC20 (Minimum risk-based capital
    requirements), RBC30 (Buffers above regulatory minimum)
  weight: primary
parent_node: null
related:
- node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
  relation: detailed_mechanics
- node: '[[Basel_Iv_Output_Floor_72pct_Internal_Model_Constraint]]'
  relation: rwa_floor_complement
- node: '[[Basel_Gsib_Surcharge_Bucket_Methodology_Capital_Add_On]]'
  relation: additional_buffer_layer
- node: '[[Basel_Ccyb_Countercyclical_Buffer_Macroprudential_Activation]]'
  relation: macroprudential_buffer_extension
- node: '[[Bcbs_Irrbb_Standards_D368_2016]]'
  relation: pillar2_complement
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## Overview

Basel III capital regulation imposes a **three-layer architecture**: hard minimum floors, a mandatory conservation buffer, and discretionary macroprudential buffers on top. The entire framework is denominated in **Common Equity Tier 1 (CET1)** — the highest-quality, loss-absorbing capital — as its anchor metric.

## Capital Categories (CAP10)

**Common Equity Tier 1 (going-concern):**
- Common shares + retained earnings + AOCI + minority interest
- 14 qualifying criteria: perpetual, most subordinated, no incentive to redeem, full discretion to cancel dividends
- CET1 = loss-absorbing while bank is a going concern

**Additional Tier 1 (going-concern):**
- Perpetual instruments (no maturity date, no step-ups)
- Full discretion to cancel coupon at all times (non-payment ≠ event of default)
- Mandatory write-off or conversion trigger: CET1 < 5.125%
- Classified as liabilities under IFRS but regulatory treatment is equity-like

**Tier 2 (gone-concern):**
- Subordinated debt with minimum 5-year original maturity
- Provides loss absorption in resolution/liquidation only
- Not available for going-concern losses

## Minimum Requirements (RBC20)

```
CET1 ≥ 4.5% of RWA
Tier 1 ≥ 6.0% of RWA       (CET1 + AT1)
Total ≥ 8.0% of RWA       (Tier 1 + Tier 2)
```

These are **hard floors** — breach triggers supervisory intervention. The RWA used is `MAX(model RWA, 72.5% × SA-RWA)` due to the output floor (see `[[Basel_Iv_Output_Floor_72pct_Internal_Model_Constraint]]`).

## Capital Conservation Buffer (RBC30)

A 2.5% CET1 buffer sits **above** the 4.5% minimum, bringing the effective CET1 threshold for unrestricted distributions to **7.0%**.

**MDA constraint table** (earnings = distributable profit pre-deduction):

| CET1 ratio | Max distributions (% of earnings) |
|---|---|
| 4.5% – 5.125% | 0% (100% retention) |
| 5.125% – 5.75% | 20% |
| 5.75% – 6.375% | 40% |
| 6.375% – 7.0% | 60% |
| > 7.0% | 100% (no constraint) |

Key design principle: constraints apply only to **distributions**, not to operations. Banks can continue lending even in the buffer range — the regime avoids creating a de facto new minimum that would trigger a cliff-edge.

## Buffer Extension Mechanics

When the Countercyclical Capital Buffer (CCyB) is active, the conservation buffer expands:
- A 2.5% CCyB extends the "unrestricted distribution" threshold from 7.0% to **9.5%**
- G-SIB surcharge adds a further 1%–3.5% on top

The MDA constraint table scales proportionally with the total buffer size — the four equal quartile bands always apply, regardless of the buffer level.

## Interaction with AT1 / Tier 2

CET1 must **first satisfy** the 6% Tier 1 and 8% Total requirements before the remainder contributes to the conservation buffer. A bank with 8% CET1, 0 AT1, 0 Tier 2 meets minimum capital but has **zero** conservation buffer → subject to 100% distribution restriction. [RAW-BOOK BaselFramework RBC30.4 fn]

## Related Concepts

The capital stack is the foundation from which all other Basel requirements extend. `[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]` provides the integrated view of how capital + liquidity constraints interact. `[[Basel_Iv_Output_Floor_72pct_Internal_Model_Constraint]]` explains the RWA floor that determines the denominator. `[[Basel_Gsib_Surcharge_Bucket_Methodology_Capital_Add_On]]` and `[[Basel_Ccyb_Countercyclical_Buffer_Macroprudential_Activation]]` are the additional buffer layers that extend the CConB.
