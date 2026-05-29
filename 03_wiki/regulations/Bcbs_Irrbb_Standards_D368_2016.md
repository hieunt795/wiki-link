---
node_id: bcbs_irrbb_standards_d368_2016_001
type: regulation
jurisdiction: international
issuer: bcbs
title: BCBS IRRBB Standards (d368) — 12-Principle Framework, April 2016
aliases:
- BCBS d368 IRRBB 2016
- IRRBB 12 principles 2016
- BCBS IRRBB standards
- Interest Rate Risk Banking Book d368
- tiêu chuẩn rủi ro lãi suất sổ ngân hàng BCBS
- IRRBB 12 nguyên tắc 2016
domain:
  primary: banking_regulation
  secondary: interest_rate_risk
tags:
- irrbb
- bcbs
- regulatory_standard
- eve
- nii
- pillar_2
- outlier_test
- six_shock_scenarios
- nmd
- csrbb
- d368
- basel
confidence: 4
stability: stable
thesis: 'BCBS d368 (April 2016) establishes the current IRRBB regulatory framework
  under Pillar 2 (Supervisory Review Process), replacing the 2004 IRR Principles.
  The framework defines three IRRBB sub-types (gap, basis, option risk) and requires
  banks to measure and disclose ΔEVE and ΔNII under six prescribed interest rate shock
  scenarios. Twelve principles cover: bank management of IRRBB (P1–P7), disclosure
  (P8), capital adequacy in ICAAP (P9), supervisory assessment (P10–P12). The outlier
  test — ΔEVE > 15% of Tier 1 capital under any prescribed scenario — triggers supervisory
  review. A supervisory standardised framework (Section IV) may be mandated for banks
  with inadequate internal measurement systems.

  '
source_refs:
- path: 02_sources/regulator/bcbs/d368.md
  pages: 'para 1–7 (executive summary), para 8–10 (IRRBB definition, CSRBB), para
    11 (EVE vs NII), para 12–32 (P1 identification, P2 governance), para 33–43 (P4
    EVE/NII measurement, shock scenarios), para 44–51 (P5 behavioural assumptions),
    para 52–65 (P6 model governance), para 66–68 (P7 reporting), para 69–71 (P8 disclosure),
    para 72–76 (P9 ICAAP capital), para 77–87 (P10–P11 supervisory), para 88–95 (P12
    outlier test), para 96–98 (scope + timeline), para 99–115 (standardised framework:
    bucketing, NMDs Table 2), Table B (six shock scenarios)'
  weight: primary
parent_node: null
related:
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: detailed_content_node
- node: '[[Bcbs_Irrbb_Nmd_Standardised_Framework]]'
  relation: nmd_treatment_detail
- node: '[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]'
  relation: nmd_valuation_connection
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: related_bcbs_standard
- node: '[[Maturity_Gap_Analysis_Interest_Rate_Risk_Banking_Book]]'
  relation: gap_analysis_mechanism
- node: '[[Bank_Alm_Banking_Book_Risk_Management_Framework]]'
  relation: bank_implementation
- node: '[[Behavioralization_Non_Maturity_Deposit_Alm_Prepayment_Early_Withdrawal_Modeling]]'
  relation: behavioral_assumptions
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Regulatory Architecture

**Pillar assignment:** Pillar 2 (SREP/ICAAP) — NOT Pillar 1 minimum capital.
BCBS concluded that "the heterogeneous nature of IRRBB would be more appropriately
captured in Pillar 2." [RAW-BOOK d368 para 3]

**Scope:** Internationally active banks on a consolidated basis; national discretion
to apply to other institutions. [RAW-BOOK d368 para 5, 96]

**Implementation deadline:** 2018 (disclosures based on 31 Dec 2017 data). [RAW-BOOK d368 para 7, 98]

---

## Three IRRBB Sub-Types

```
(a) GAP RISK:
  → Arises from term structure of banking book instruments
  → Timing mismatches in rate changes
  → PARALLEL risk: yield curve shifts consistently across maturities
  → NON-PARALLEL risk: differential shifts by period (twists, steepening, flattening)
  [RAW-BOOK d368 para 9a]

(b) BASIS RISK:
  → Impact of relative changes between interest rate indices
  → Same tenors, different benchmarks (eg SOFR-indexed asset vs prime-rate liability)
  → Imperfect correlation between indices in stress
  [RAW-BOOK d368 para 9b]

(c) OPTION RISK:
  → Arises from option derivatives OR optional elements embedded in products
  → Bank or customer can alter level and timing of cash flows
  → Sub-categories:
    - AUTOMATIC option risk: triggered mechanically (eg caps, floors, callable bonds)
    - BEHAVIOURAL option risk: customer exercises based on economic incentive
      (eg mortgage prepayment, NMD withdrawal, term deposit early redemption)
  [RAW-BOOK d368 para 9c]

CSRBB (Credit Spread Risk in Banking Book):
  → NOT an IRRBB sub-type, but must be monitored and assessed
  → "Any kind of asset/liability spread risk of credit-risky instruments that is not
     explained by IRRBB and by the expected credit/jump to default risk"
  → Treated as a related risk, monitored within IRRBB framework
  [RAW-BOOK d368 para 10]
```

---

## 12-Principle Overview

```
PRINCIPLES FOR BANKS (P1–P9):
  P1: Identify, measure, monitor and control all three IRRBB sub-types + CSRBB
  P2: Governing body responsible for IRRBB management framework; ALCO delegation
  P3: Risk appetite in EVE AND earnings terms; policy limits consistent with risk appetite
  P4: Measure IRRBB via BOTH EVE and earnings-based measures; use six prescribed scenarios
  P5: Key behavioural/modelling assumptions: documented, rigorous, updated annually
      → NMDs, prepayments, early redemption, embedded options
  P6: Model governance: independent validation, backtesting, version control, documentation
  P7: Regular reporting to governing body at least semi-annually
  P8: Mandatory public disclosure of ΔEVE and ΔNII under six prescribed scenarios (annually)
      Tables A (qualitative) and B (quantitative, fixed format) [RAW-BOOK d368 para 69–70]
  P9: Capital adequacy for IRRBB considered in ICAAP [RAW-BOOK d368 para 72–76]

PRINCIPLES FOR SUPERVISORS (P10–P12):
  P10: Collect information; monitor trends; identify outlier banks
  P11: Regular assessment; specialist resources; cross-border cooperation
  P12: OUTLIER TEST: publish criteria; if ΔEVE > 15% of Tier 1 → supervisory action required
  [RAW-BOOK d368 para 6, 88]
```

---

## Six Prescribed Interest Rate Shock Scenarios

All banks must disclose ΔEVE and ΔNII for each of these six scenarios:
[RAW-BOOK d368 Table B, para 35, 69]

```
1. PARALLEL UP       — All tenors shift up by identical amount
2. PARALLEL DOWN     — All tenors shift down by identical amount
3. STEEPENER         — Short rates fall, long rates rise (yield curve steepens)
4. FLATTENER         — Short rates rise, long rates fall (yield curve flattens)
5. SHORT RATE UP     — Short-end rates rise, long-end unchanged/minimal move
6. SHORT RATE DOWN   — Short-end rates fall, long-end unchanged/minimal move

Disclosure format (Table B):
  → ΔEVE and ΔNII per scenario, current period T and prior period T-1
  → Maximum ΔEVE across all six scenarios → compared to 15% Tier 1 outlier threshold
  → Annual frequency, as at financial year-end

ΔEVE calculation basis:
  → Run-off balance sheet (no new business)
  → Instantaneous shock
  → Exclude own equity from computation
  → Option: include or disclose commercial margins in cash flows

ΔNII calculation basis:
  → Constant balance sheet (maturing cash flows replaced with identical features)
  → Instantaneous shock
  → Rolling 12-month forward period [RAW-BOOK d368 para 70]
```

---

## Outlier Test (Principle 12)

```
MANDATORY MINIMUM TEST:
  Maximum ΔEVE (worst of six prescribed scenarios) > 15% of Tier 1 capital
  → Bank flagged as outlier: "potentially having undue IRRBB"
  → Triggers supervisory review
  [RAW-BOOK d368 para 88]

SUPERVISORS MAY ADD:
  → Alternative capital measure (CET1, capital above minimum requirements)
  → Earnings-based outlier test (ΔNII exceeds earnings sustainability threshold)
  → Additional tests must be ≥ as stringent as 15% Tier 1 standard
  [RAW-BOOK d368 para 89]

SUPERVISORY ACTIONS UPON OUTLIER DESIGNATION:
  ① Reduce IRRBB exposures (eg by hedging)
  ② Raise additional capital
  ③ Set constraints on internal risk parameters
  ④ Improve risk management framework
  [RAW-BOOK d368 para 94]

STRONG PRESUMPTION:
  "There is a strong presumption for supervisory and/or regulatory capital
   consequences, when a review of a bank's IRRBB exposure reveals inadequate
   management or excessive risk relative to a bank's capital, earnings or
   general risk profile." [RAW-BOOK d368 para 58/exec summary]
```

---

## Standardised Framework (Section IV) — When Mandated

Supervisors can mandate (or banks can voluntarily adopt) the standardised framework
when internal measurement systems (IMS) are assessed as inadequate.

```
FIVE-STAGE EVE CALCULATION:
  Stage 1: Categorise positions → amenable / less amenable / not amenable to standardisation
  Stage 2: Slot cash flows into 19 predefined time buckets (O/N to >20Y)
           Exceptions: NMDs, prepayable loans, early-redeemable term deposits
  Stage 3: Calculate ΔEVE per scenario per currency
  Stage 4: Add-ons for automatic interest rate options (caps, floors, callables)
           Sold options: full revaluation + 25% relative volatility increase
  Stage 5: IRRBB EVE = maximum EVE reduction across all 6 scenarios (worst case)
  [RAW-BOOK d368 para 100–104]

19 TIME BUCKETS: O/N, O/N–1M, 1–3M, 3–6M, 6–9M, 9M–1Y, 1–1.5Y, 1.5–2Y,
  2–3Y, 3–4Y, 4–5Y, 5–6Y, 6–7Y, 7–8Y, 8–9Y, 9–10Y, 10–15Y, 15–20Y, >20Y
  [RAW-BOOK d368 Table 1]

NMD TREATMENT: Separate core vs non-core; Table 2 caps (see Bcbs_Irrbb_Nmd_Standardised_Framework)
```

---

## ICAAP Capital Adequacy (Principle 9)

```
IRRBB capital must be assessed in ICAAP — not just for outlier test:
  → Banks develop own capital allocation methodologies for IRRBB
  → Capital must cover BOTH EVE risk (embedded losses) AND earnings risk
  → Capital adequacy factors [RAW-BOOK d368 para 75]:
    ① Size and tenor of internal IRRBB limits + whether limits are binding
    ② Hedging effectiveness and cost
    ③ Sensitivity of IMS to key modelling assumptions
    ④ Basis risk (positions priced off different indices)
    ⑤ FX currency mismatches
    ⑥ Embedded losses (positions already in loss at current rates)
    ⑦ Capital distribution across legal entities in consolidation group
    ⑧ Drivers of underlying risk
    ⑨ Circumstances under which risk might crystallise

"Banks should not only rely on supervisory assessments of capital adequacy for
IRRBB, but should also develop their own methodologies" [RAW-BOOK d368 para 73]
```
