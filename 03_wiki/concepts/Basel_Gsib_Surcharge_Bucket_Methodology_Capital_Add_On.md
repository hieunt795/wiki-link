---
node_id: basel_gsib_surcharge_bucket_methodology_capital_add_on_001
type: concept
title: 'Basel G-SIB Surcharge: 5-Category Score, Bucket Methodology, and CET1 Add-On'
aliases:
- G-SIB surcharge
- G-SIB higher loss absorbency
- systemic importance buffer
- phụ phí G-SIB
- ngân hàng tầm quan trọng hệ thống toàn cầu
- HLA G-SIB
domain:
  primary: basel_risk
tags:
- gsib
- systemic_risk
- capital_surcharge
- indicator_based
- cet1
- higher_loss_absorbency
- bucket_methodology
- basel3
confidence: 3
stability: stable
thesis: 'G-SIBs are identified annually via a 12-indicator scoring methodology across
  5 equal-weighted categories (size, cross-jurisdictional activity, interconnectedness,
  substitutability, complexity); banks scoring ≥130 bps are designated G-SIBs and
  allocated to Buckets 1–5 (1.0%–3.5% CET1 add-on), with an empty Bucket 5 (3.5%)
  serving as an anti-gaming deterrent — if populated, a new bucket at 4.5% is created;
  the add-on extends the capital conservation buffer and triggers the same MDA distribution
  restriction mechanism when breached.

  '
source_refs:
- path: 02_sources/regulator/bcbs/BaselFramework.md
  pages: SCO40 (indicator-based methodology, 5 categories, 12 indicators, bucketing
    approach SCO40.19-22), RBC40.1-5 (higher loss absorbency implementation, bucket
    table)
  weight: primary
parent_node: null
related:
- node: '[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]'
  relation: additional_buffer_layer
- node: '[[Basel_Ccyb_Countercyclical_Buffer_Macroprudential_Activation]]'
  relation: buffer_stack_peer
- node: '[[Basel_Iii_Leverage_Ratio_Non_Rwa_Capital_Constraint]]'
  relation: gsib_leverage_add_on
- node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
  relation: constraint_system_component
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## Overview

The G-SIB framework addresses the "too-big-to-fail" negative externalities of globally systemically important banks: their failure would damage the global economy, create moral hazard through implicit government support, and generate cross-border spillovers. The response is higher going-concern loss-absorbing capacity (CET1) rather than just ex-post resolution. (SCO40.1-3)

**Objective:** Reduce the probability of failure of G-SIBs — not reduce the impact of failure (that is the FSB resolution framework's domain). (SCO40.6)

## Indicator-Based Measurement (SCO40.4-18)

Systemic importance is scored using **12 indicators across 5 equally weighted categories** (20% each). For each indicator, a bank's score = (bank's indicator value / total sample indicator value) × 10,000, expressed in basis points. Overall score = simple average of 5 category scores.

| Category (weight) | Individual Indicator | Indicator Weight |
|---|---|---|
| **Cross-jurisdictional activity (20%)** | Cross-jurisdictional claims | 10% |
| | Cross-jurisdictional liabilities | 10% |
| **Size (20%)** | Total exposures (leverage ratio measure, incl. insurance) | 20% |
| **Interconnectedness (20%)** | Intra-financial system assets | 6.67% |
| | Intra-financial system liabilities | 6.67% |
| | Securities outstanding | 6.67% |
| **Substitutability/infrastructure (20%)** | Assets under custody | 6.67% |
| | Payments activity | 6.67% |
| | Underwritten transactions (debt/equity) | 3.33% |
| | Trading volume | 3.33% |
| **Complexity (20%)** | Notional OTC derivatives outstanding | 6.67% |
| | Level 3 assets | 6.67% |
| | Trading and available-for-sale securities | 6.67% |

**Substitutability cap:** The substitutability category score is capped at **500 bps** to prevent dominant payment/custody banks from receiving a disproportionately higher G-SIB classification score than the Committee intended. (SCO40.8)

**Sample:** The 75 largest global banks by leverage ratio exposure measure (plus prior-year G-SIBs and supervisory judgment additions) comprise the annual assessment sample. (SCO40.19)

## Bucketing and Higher Loss Absorbency (RBC40.1-5)

Banks with scores ≥130 bps are designated G-SIBs. Buckets are 100 bps wide:

| Bucket | Score Range | CET1 Add-On |
|---|---|---|
| 5 | 530–629 bps | **3.5%** (empty — anti-gaming deterrent) |
| 4 | 430–529 bps | 2.5% |
| 3 | 330–429 bps | 2.0% |
| 2 | 230–329 bps | 1.5% |
| 1 | 130–229 bps | 1.0% |

**Empty Bucket 5 mechanism:** Bucket 5 is intentionally kept empty. If any bank's score exceeds 629 bps, a new Bucket 6 is created with a **4.5% CET1 add-on**, maintaining the incentive structure to avoid growing more systemically important. (RBC40.5)

The add-on must be met with **CET1 only** — no AT1 or Tier 2 substitution. (RBC40.1)

## Implementation: Extension of Capital Conservation Buffer (RBC40.2)

The G-SIB surcharge is implemented as an extension of the Capital Conservation Buffer, using the same MDA distribution restriction mechanism:
- For a Bucket 2 G-SIB (1.5% surcharge): unrestricted distribution threshold = 4.5% + 2.5% (CConB) + 1.5% (G-SIB) = **8.5% CET1**
- MDA constraint table applies with four equal quartile bands across the total buffer range

Breaching the surcharge triggers distribution restrictions (dividends, buybacks, discretionary bonuses) — it is not a formal supervisory intervention until the capital remediation plan stage. (RBC40.3)

## Leverage Ratio Add-On for G-SIBs

G-SIBs also face a leverage ratio buffer of **50% of their G-SIB risk-based CET1 buffer** (see LEV40). A Bucket 2 G-SIB with 1.5% CET1 surcharge faces an additional 0.75% leverage ratio buffer on top of the 3% minimum. This makes the leverage ratio doubly binding for G-SIBs engaged in large-scale low-risk-weight activities (repo, government bonds).

## Adjustment Dynamics (RBC40.6)

- **Score increases to higher bucket:** Bank has **12 months** to meet the higher buffer requirement.
- **Score falls to lower bucket:** Immediate release of the previously required higher buffer (national authorities may delay at their discretion).
- Annual reassessment by the Committee; bucket reassignments applied accordingly.

## D-SIB Framework (RBC40.7-23)

Domestic Systemically Important Banks (D-SIBs) follow a complementary framework set by national authorities. Key principles:
- D-SIB surcharge also met with CET1 only
- D-SIB and G-SIB requirements are not additive: the higher of the two applies
- Home authority imposes at consolidated level; host authority may impose on significant subsidiaries (no double-counting)

## Related Concepts

`[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]` describes the base capital stack onto which the G-SIB add-on is layered. `[[Basel_Ccyb_Countercyclical_Buffer_Macroprudential_Activation]]` is the third buffer layer on top of the conservation buffer. `[[Basel_Iii_Leverage_Ratio_Non_Rwa_Capital_Constraint]]` covers the leverage ratio add-on that G-SIBs face at LEV40.
