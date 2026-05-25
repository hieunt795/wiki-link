---
node_id: bcbs_irrbb_nmd_standardised_framework_001
type: mechanism
title: BCBS IRRBB NMD Standardised Framework — Core/Non-Core Separation and Table 2 Caps
aliases:
  - BCBS NMD IRRBB treatment
  - d368 NMD behavioural assumptions
  - non-maturity deposit core cap IRRBB
  - NMD Table 2 IRRBB caps
  - tiền gửi không kỳ hạn IRRBB phân loại lõi
  - NMD phân loại lõi phi lõi giới hạn
domain:
  primary: banking_regulation
  secondary: interest_rate_risk
tags:
  - nmd
  - non_maturity_deposit
  - irrbb
  - behavioural_assumptions
  - core_deposits
  - bcbs
  - d368
  - standardised_framework
  - eve
  - alm
confidence: 4
stability: stable
thesis: >
  BCBS d368 standardised framework (Section IV) requires banks to separate NMDs into
  core and non-core portions by category, subject to prescribed caps on the proportion
  of core deposits and maximum average repricing maturity per category. The two-step
  separation: (1) stable vs non-stable (based on 10-year observed volume changes);
  (2) core vs non-core within stable (portion unlikely to reprice under significant
  rate changes). Non-core NMDs are slotted overnight; core NMDs are distributed up
  to the category's maximum average maturity. The caps — retail transactional 90%/5yr,
  retail non-transactional 70%/4.5yr, wholesale 50%/4yr — directly determine the
  maximum EVE sensitivity reduction a bank can claim from NMD stability assumptions.
source_refs:
  - path: 02_sources/regulator/bcbs/d368.md
    pages: "para 44–46 (P5: NMD behavioural assumptions), para 109–115 (standardised framework NMD treatment: categories, separation, slotting), Table 2 (NMD core caps and average maturity limits), para 112 (10-year observation, stable/non-stable/core definition)"
    weight: primary
related:
  - node: "[[Bcbs_Irrbb_Standards_D368_2016]]"
    relation: parent_regulatory_standard
  - node: "[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]"
    relation: nmd_valuation_complement
  - node: "[[Irrbb_Eve_Nii_Dual_Metric_Framework]]"
    relation: eve_measurement_context
  - node: "[[Bcbs_Liquidity_Internal_Pricing_Ftp_Principle_4]]"
    relation: ftp_nmd_connection
date_created: "2026-05-25"
date_updated: "2026-05-25"
---

## Why NMDs Are the Critical IRRBB Behavioural Assumption

```
"NMDs — Behavioural assumptions for deposits that have no specific repricing date
can be a major determinant of IRRBB exposures under the economic value and
earnings-based measures."
[RAW-BOOK d368 para 45(iv)]

The NMD modelling problem:
  → Demand deposits, savings accounts, current accounts: no contractual maturity
  → Contractual assumption: overnight maturity → zero IRRBB from NMDs
  → Economic reality: stable deposits held for years → substantial IRRBB
  → Bank assigns a repricing maturity → this maturity DETERMINES EVE sensitivity

If NMDs modelled as 5yr average repricing:
  → A 1% rate shock creates large EVE loss (long-duration liability vs shorter assets)
If NMDs modelled as overnight:
  → Nearly zero EVE sensitivity from NMDs
→ NMD assumptions can move ΔEVE by multiples of Tier 1 capital
```

---

## Two-Step Separation Procedure

```
STEP 1 — Stable vs Non-Stable:
  Stable NMD portion = portion that remains undrawn with high likelihood
  Measurement: "observed volume changes over the past 10 years"
  → 10-year historical observation required — captures a full rate cycle

  Non-stable NMDs:
  → Treated as volatile; must be modelled as outflows under stress
  → Slotted overnight in standardised framework

  [RAW-BOOK d368 para 112]

STEP 2 — Core vs Non-Core (within stable portion):
  Core deposits = proportion of stable NMDs "unlikely to reprice even under
  significant changes in the interest rate environment"
  → The "stickiest" portion — will remain at below-market rates even when
    alternative rates rise substantially
  → Non-core stable = stable in volume but rate-sensitive (will reprice with market)

  Key distinction:
    STABLE → won't leave the bank (volume stability)
    CORE → won't demand higher rates AND won't leave (rate insensitivity)

  [RAW-BOOK d368 para 112]
```

---

## Table 2: NMD Caps by Category

Prescribed caps on what banks can claim as core deposits, and maximum average maturity:
[RAW-BOOK d368 Table 2]

```
┌──────────────────────────────┬─────────────────────────┬────────────────────────────────┐
│ NMD Category                 │ Cap on proportion of    │ Cap on average maturity of     │
│                              │ core deposits (%)       │ core deposits (years)          │
├──────────────────────────────┼─────────────────────────┼────────────────────────────────┤
│ Retail / Transactional       │ 90%                     │ 5 years                        │
│ Retail / Non-transactional   │ 70%                     │ 4.5 years                      │
│ Wholesale                    │ 50%                     │ 4 years                        │
└──────────────────────────────┴─────────────────────────┴────────────────────────────────┘
```

**Category definitions:**
```
RETAIL DEPOSITS:
  → Deposits placed with a bank by an individual person
  → Small business customers managed as retail (aggregated < €1 million) → treated as retail

RETAIL / TRANSACTIONAL:
  → Regular transactions carried out in the account (eg salary credited regularly)
  → OR non-interest bearing deposits
  → Most stable category → highest core cap (90%) + longest maturity (5yr)

RETAIL / NON-TRANSACTIONAL:
  → Retail deposits NOT meeting transactional criteria
  → More rate-sensitive than transactional → lower core cap (70%), shorter maturity (4.5yr)

WHOLESALE:
  → Legal entities, sole proprietorships, partnerships
  → Most institutionally driven rate sensitivity → lowest cap (50%), shortest maturity (4yr)

[RAW-BOOK d368 para 111]
```

---

## Cash Flow Slotting for NMDs

```
NON-CORE NMDs:
  → Treated as overnight deposits
  → Slotted into overnight/shortest time bucket (k=1)
  [RAW-BOOK d368 para 114]

CORE NMDs:
  → Distributed across time buckets up to the category's maximum average maturity
  → Bank determines slotting procedure for each category
  → Constraint: average maturity ≤ cap in Table 2
  → Banks must also disclose (in Table A):
    ① Average repricing maturity assigned to NMDs
    ② Longest repricing maturity assigned to NMDs
  [RAW-BOOK d368 para 115, Table A]
```

---

## Impact on ΔEVE Calculation

```
MAXIMUM DURATION PROFILE from full core utilisation:
  Retail transactional:    90% × 5yr = 4.5yr effective duration (maximum)
  Retail non-transactional: 70% × 4.5yr = 3.15yr effective duration (maximum)
  Wholesale:               50% × 4yr = 2yr effective duration (maximum)

EVSE SENSITIVITY DIRECTION:
  NMDs are liabilities → longer repricing maturity = LESS EVE sensitivity (hedges assets)
  Bank with long-duration NMDs: negative liability duration → offsets long-duration assets
  → NMD duration assumption REDUCES ΔEVE exposure

CROSS-CHECK (required by Principle 5):
  Banks should periodically compare EVE from internal IMS vs standardised framework
  → If IMS gives substantially lower ΔEVE: assumption justification required
  → "Banks should analyse its depositor base in order to identify the proportion of
     core deposits" — empirical analysis, not assumption-only
  [RAW-BOOK d368 para 45(iv), para 49]
```

---

## Governing Assumptions for Internal Models (Principle 5)

Beyond the standardised caps, banks using internal models must:

```
KEY DIMENSIONS FOR NMD BEHAVIOURAL ASSUMPTION:
  ① Responsiveness of product rates to changes in market interest rates (pass-through)
  ② Current level of interest rates (low rates environment: deposits stickier)
  ③ Spread between bank's offer rate and market rate
  ④ Competition from other firms (more competitive = less sticky)
  ⑤ Bank's geographical location
  ⑥ Demographic and customer characteristics of depositor base
  [RAW-BOOK d368 Table in para 46]

GOVERNANCE REQUIREMENTS:
  → "Banks should document, monitor and regularly update key assumptions"
  → Review at least ANNUALLY (more frequently in rapidly changing market conditions)
  → Sensitivity analysis on EVE and NII to changes in NMD assumptions
  → Model validation: backtesting of NMD stability assumptions against actual data
  [RAW-BOOK d368 para 45(iv), para 51, para 59]
```

---

## Connection to FTP (Funds Transfer Pricing)

The NMD repricing maturity assumption used for IRRBB is the same parameter that
drives the FTP credit for NMD funding:

```
IF core NMDs assigned 5-year repricing maturity (retail transactional maximum):
  → IRRBB: 5-year liability reduces long-duration asset EVE sensitivity
  → FTP:   Business line gathering these deposits receives 5-year rate FTP credit

IF core NMDs assigned 2-year repricing maturity (conservative internal view):
  → IRRBB: Less duration offset from NMDs → higher ΔEVE exposure
  → FTP:   Deposit-gathering gets only 2-year rate credit → smaller funding benefit

The IRRBB assumption and FTP credit must be internally consistent.
Using different maturities for IRRBB vs FTP creates regulatory arbitrage / incentive distortion.
[LLM — policy logic from d368 para 45 NMD assumptions + bcbs144 P4 FTP requirement]
```
