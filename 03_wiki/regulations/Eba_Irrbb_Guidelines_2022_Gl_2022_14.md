---
node_id: eba_irrbb_guidelines_2022_gl_2022_14_001
type: regulation
jurisdiction: international
issuer: eba
title: EBA IRRBB Guidelines 2022 (EBA/GL/2022/14) and Supervisory Outlier Tests
aliases:
- EBA GL 2022/14
- EBA IRRBB guidelines 2022
- SOT EVE
- SOT NII
- hướng dẫn EBA về rủi ro lãi suất 2022
- kiểm tra ngoại lệ giám sát EVE NII
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- EBA
- IRRBB
- SOT
- EVE
- NII
- CSRBB
- regulation
- supervisory_outlier_test
confidence: 1
stability: stable
thesis: '[LLM] EBA/GL/2022/14 (October 2022) updated the EU IRRBB regulatory framework
  by adding the first NII supervisory outlier test (SOT), introducing CSRBB as an
  explicit risk category, tightening NMD behavioral caps, and mandating standardized
  and simplified standardized approaches; the two SOTs — EVE (>15% of Tier 1 capital)
  and NII (>5% of Tier 1 capital) — create a simultaneous compliance constraint that
  banks must optimize jointly.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch 5, sections 5.1.3, 5.2, 5.3, 5.4, 5.5
  weight: primary
parent_node: null
related:
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: implements
- node: '[[Eve_Calculation_Mechanics_Discount_And_Shock]]'
  relation: related_to
- node: '[[Nii_Sensitivity_Forecast_Static_Dynamic_Balance_Sheet]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Regulatory Context

[LLM] EBA/GL/2022/14 was published on October 20, 2022, mandated by Article 84(6) of CRD IV (Directive 2013/36/EU). It replaced EBA/GL/2018/02 and came into force in 2023. Two accompanying Regulatory Technical Standards (RTS) — EBA/RTS/2022/09 and EBA/RTS/2022/10 — were implemented via Commission Delegated Regulations 2024/856 and 2024/857, entering into force on May 14, 2024. [LLM] The full reporting regime (Commission Implementing Regulation 2024/855) has been applicable since October 2024.

## What Changed vs EBA/GL/2018/02

[LLM] The 2022 framework introduced three major changes relative to the 2018 guidelines:

1. **New NII Supervisory Outlier Test (SOT)**: The 2018 guidelines focused almost exclusively on the EVE perspective; the NII SOT is entirely new. The NII SOT flags a bank as an outlier when ΔNII / Tier 1 capital exceeds 5% under a parallel shock up or down scenario, calculated over a one-year horizon on a constant balance sheet.

2. **CSRBB formally integrated**: Credit spread risk arising from the banking book (CSRBB) is explicitly included in the guideline scope and must be assessed and monitored alongside IRRBB.

3. **NMD behavioral caps tightened**: A five-year cap on the weighted average repricing maturity is applied to non-maturity retail and wholesale deposits from non-financial counterparties (some categories in the 2018 guidelines allowed longer assumptions in certain cases).

## Supervisory Outlier Tests (SOTs) — Summary

### SOT on EVE (unchanged from 2018, recalibrated floor)

- **Trigger**: ΔEVE exceeds 15% of Tier 1 capital under any of the six shock scenarios.
- **Six scenarios** (specified in CRD V 2019 and confirmed in RTS/2022/10): parallel shock up, parallel shock down, steepener (short rates down / long rates up), flattener (short rates up / long rates down), short rates shock up, short rates shock down.
- **Balance sheet assumption**: Run-off — existing positions mature and are not replaced.
- **Floor**: A maturity-dependent post-shock rate floor, starting at −150 bps for immediate maturities and rising linearly by 3 bps per year to 0% at 50-year maturity (recalibrated from −100 bps / 5 bps per year in EBA 2018a, reflecting that in late 2020 and early 2022 the baseline rate fell below the old floor).
- **Commercial margins**: May be excluded.

### SOT on NII (new in 2022)

- **Trigger**: ΔNII / Tier 1 capital exceeds 5% under parallel shock up or parallel shock down.
- **Horizon**: One-year NII calculation.
- **Balance sheet assumption**: Constant (static) — maturing positions are replaced by instruments with comparable features.
- **Commercial margins**: Must be included.
- **Floor**: No linear floor is currently applied to the NII SOT.

## Standardized Approaches (SA and S-SA)

[LLM] RTS/2022/09 specifies two standardized calculation methodologies as fallbacks or alternatives to banks' internal measurement systems (IMS):

- **Standardized Approach (SA)**: Calculates EVE change by subtracting EVE in the baseline from EVE in the shock scenario. For NII, it sums three components: (1) interest payments fixed before repricing, (2) projected risk-free return after repricing on a constant balance sheet, and (3) projected commercial margin after margin reset. Includes an add-on for automatic optionality. [LLM] The SA is designed for the most accurate standardized representation of risk.

- **Simplified Standardized Approach (S-SA)**: Designed for small and non-complex institutions. Simplifications include treatment of NMD core deposits, cashflow granularity, automatic option volatility add-on, and commercial margin granularity. [LLM] National competent authorities (NCAs) may override the S-SA and require the full SA if they consider the simplified approach inadequate.

## Simultaneous Compliance Problem

[LLM] A key insight from Tata (2025) Ch 5.4: the EVE SOT and NII SOT create partially conflicting constraints on the optimal composition of fixed-rate assets for a bank with large sight deposit positions:

- EVE SOT imposes upper and lower bounds on the share of fixed-rate assets as a function of asset duration (too much fixed-rate creates EVE risk; too little also creates EVE risk in the downward shock).
- NII SOT imposes a minimum amount of fixed-rate assets (needed to stabilize NII in a rate-decline scenario).

[LLM] The "feasible zone" — combinations of fixed-rate asset share and duration that satisfy both SOTs simultaneously — may be very narrow and may shift over time with volume changes. Banks must solve a constrained optimization (Fig. 5.2 in Tata 2025) to find compliant portfolio compositions.

## Behavioral Modeling Requirements

[LLM] EBA/GL/2022/14 requires banks to report detailed behavioral modeling parameters in supervisory templates, including:

- Average weighted repricing dates for each NMD category, and core volume identification.
- Pass-through rate (PTR): the fraction of an interest rate shock assumed to be passed through to NMD rates.
- Prepayment and early redemption rates, and their sensitivity to the rate environment.
- Treatment of the 0% floor for retail deposits in negative rate scenarios.

[LLM] Banks must also provide qualitative disclosures on which approach (SA, S-SA, or IMS) is used for each SOT, and on the methods used to determine NMD behavioral repricing dates.

## CSRBB Requirements

[LLM] The 2022 guideline requires banks to: (1) identify exposures to CSRBB from all banking book positions; (2) monitor and manage CSRBB using appropriate metrics; (3) ensure CSRBB is explicitly assessed in the SREP process. [LLM] Unlike IRRBB, there is no standardized approach or supervisory outlier test for CSRBB in the 2022 framework — banks are required to develop internal approaches proportionate to their CSRBB exposure.
