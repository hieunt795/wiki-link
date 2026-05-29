---
node_id: irrbb_standardised_versus_internal_model_approach_001
type: framework
title: IRRBB Standardised vs Internal Model Approach — Practitioner Perspective
aliases:
- IRRBB SA vs IMA
- IRRBB Pillar 2 principles
- BCBS 12 principles IRRBB
- supervisory outlier test SOT
- tiêu chuẩn IRRBB Basel Pillar 2
- phương pháp nội bộ rủi ro lãi suất sổ ngân hàng
- kiểm tra ngoại lệ giám sát SOT
domain:
  primary: alm
  secondary: []
tags:
- supervisory-outlier-test
- standardised-approach
- internal-model
- regulatory-shocks
confidence: 3
stability: stable
thesis: 'BCBS 2016 (d368) adopted a principles-based Pillar 2 framework rather than
  a mandatory Pillar 1 standardised capital charge for IRRBB — regulators and practitioners
  largely agreed this was the appropriate approach given the complexity and heterogeneity
  of banking business models. The framework structures 12 principles requiring measurement
  of both EVE and NII, and introduces a supervisory outlier test (SOT) where EVE
  decline exceeding 15% of Tier 1 capital triggers supervisory review.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 3: Interest Rate Risk Management — The Practitioner''s Perspective'
parent_node: null
related:
- node: '[[Bcbs_Irrbb_Standards_2016]]'
  relation: related_to
- node: '[[ALM_Enterprise_Risk_Management_Framework]]'
  relation: related_to
- node: '[[ILAAP_Supervisory_Liquidity_Framework]]'
  relation: related_to
- node: '[[Interest_Rate_Basis_Risk_Measurement_ALM]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[BCBS]]'
  relation: related_to
- node: '[[Pillar2]]'
  relation: related_to
- node: '[[EVE]]'
  relation: related_to
- node: '[[NII]]'
  relation: related_to
- node: '[[SOT]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Pillar 1 vs Pillar 2 — How the Debate Resolved

The BCBS proposed two approaches for industry consultation: a standardised Pillar 1 (simplified and conservative) method versus a principles-based Pillar 2 approach. The standardised Pillar 1 methodology was designed to protect banks from an interest rate hike scenario. However, given the **complexity and heterogeneity of banking business models and IRRBB**, any standardised methodology would have resulted in punitive requirements while still failing to address all potential risks. [RAW-Elkenbracht-Huizing ch.3 p.1]

After thorough analysis during the consultation period, regulators and practitioners largely agreed that IRRBB best practice should take the form of a **principles-based approach**. BCBS issued the revised IRRBB principles (BCBS 368) in April 2016. [RAW-Elkenbracht-Huizing ch.3 p.1]

The principles-based Pillar 2 methodology enhanced the original principles set out in 2004 (Basel Committee on Banking Supervision 2004) and focused on: implementing additional governance requirements to derive proprietary models and assumptions; setting out compulsory standardised disclosures and regulatory oversight. [RAW-Elkenbracht-Huizing ch.3 p.1]

## IRRBB Definition and Behavioral Assumptions

IRRBB is defined as "the current or prospective risk to the bank's capital and earnings arising from adverse movements in interest rates that affect the bank's banking book positions." [RAW-Elkenbracht-Huizing ch.3 p.1]

IRRBB measurement is **highly dependent on assumptions about client behaviours**. Key balance-sheet items requiring behavioral assumptions: [RAW-Elkenbracht-Huizing ch.3 p.2]

- **Current accounts and savings deposits:** when client rates do not move with market rates, rate changes affect future margin on the deposit portfolio.
- **Fixed-rate loans and mortgages:** client's option to prepay reduces the duration of the fixed income stream.
- **Credit card receivables and overdrafts:** ability to raise client rates may be limited at very high market rates; retail vs. corporate overdrafts priced differently.
- **Fixed-rate loan commitments:** client's ability to draw on commitments at fixed rates reduces net interest margin when rates rise (also applies to pipeline/launch risk).
- **Capital:** different interest rate tenors assumed for capital depending on business model and balance-sheet structure.

The key focus shifted from the traditional emphasis on control of exposures towards the management of **structural risks under uncertainty** by understanding the impact of assumption risk (Principle 5). [RAW-Elkenbracht-Huizing ch.3 p.2]

## The 12 BCBS Principles — Structural Grouping

BCBS 368 articulated the updated framework in **twelve principles** (Figure 3.1). The technical challenges in prescribing standardised methodologies resulted in the inclusion of Principles 5, 8 and 12. The other nine principles were broadly a new representation of the previous 2004 principles. [RAW-Elkenbracht-Huizing ch.3 p.3]

**Risk identification (Principles 1–3):**
- P1: Identify, measure, monitor and control IRRBB — including gap risk (repricing mismatches), basis risk (different rate indexes), and option risk (customer alteration of cashflow profiles). CSRBB must also be monitored and assessed.
- P2: Board responsibility for IRRBB oversight; board must have at least one member/advisor with IRRBB understanding; independent audit review.
- P3: Risk appetite articulated in terms of both economic value AND earnings metrics.

**Measuring methodology (Principles 4–6):**
- **EVE** = present value of assets minus present value of liabilities. Assumes no ongoing business activity — a simplified gone-concern equity valuation. Change in EVE due to rate movement = EVE sensitivity.
- **NII** = projected revenue driven by interest rate margin. Incorporates new business origination. Change in NII projections = NII sensitivity.
- P5: Governance of modelling assumptions — the key focus moved to managing structural risks under uncertainty through assumption risk understanding.

**Reporting and regulatory requirements (Principles 7–12)** — including compulsory standardised disclosures (P8) and capitalisation requirements (P9). [RAW-Elkenbracht-Huizing ch.3 p.3]

## Enterprise-Wide Stress Testing as an Alternative

Enterprise-wide stress testing (EWST) emerged as an alternative to address IRRBB complexities by conducting earnings simulation across inter-risk type relationships. US Comprehensive Capital Analysis and Review (CCAR) was first introduced in Dodd-Frank regulation in 2010, using EWST to analyse capital origination adequacy. [RAW-Elkenbracht-Huizing ch.3 p.2]
