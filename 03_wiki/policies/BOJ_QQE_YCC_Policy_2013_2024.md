---
node_id: policy_boj_qqe_ycc_001
type: policy
title: "BoJ Quantitative and Qualitative Easing + Yield Curve Control (2013–2024)"
aliases:
  - BOJ QQE
  - Abenomics monetary pillar
  - YCC policy Japan
  - BoJ YCC
  - chính sách kiểm soát đường cong lợi suất Nhật Bản
  - nới lỏng định lượng và định tính Nhật Bản

domain:
  primary: monetary_policy
  secondary:
    - financial_markets
    - fiscal_policy
tags:
  - japan
  - ycc
  - qe
  - unconventional-policy
  - balance-sheet
  - financial-repression

confidence: 4
stability: stable

jurisdiction: JP
period: "2013–2024"
policy_type: unconventional_monetary
instruments:
  - "JGB purchases (unlimited at fixed yield under YCC)"
  - "ETF and J-REIT purchases"
  - "Negative interest rate policy (NIRP): -0.1% on excess reserves (2016–2024)"
  - "Yield Curve Control: 10-year JGB yield target at ~0% (±band, widened over time)"
outcome: >
  BoJ balance sheet expanded to >130% of GDP; bank reserves reached 91% of GDP.
  Inflation target of 2% achieved by 2023 (imported inflation + wage dynamics).
  YCC exit completed March 2024: NIRP ended, 10-year cap removed, policy rate raised
  to 0–0.1%. Sovereign carry trade unwound partially as yen funding costs rose.

thesis: >
  The BoJ's QQE + YCC regime was the most extensive unconventional monetary program
  by any G7 central bank: unlimited JGB purchases at fixed yields (YCC) converted the
  BoJ into buyer of last resort for Japanese sovereign debt, enabled a consolidated
  public sector sovereign carry trade at 91% of GDP, and enforced financial repression
  by stripping duration from private portfolios and suppressing household savings returns.

source_refs:
  - path: 02_sources/Clipping/What about Japan_ (Part I).md
    weight: primary
  - path: 02_sources/Clipping/What about Japan_ (Part II).md
    weight: primary
  - path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
    weight: supporting

related:
  - node: "[[Bank_of_Japan]]"
    relation: executed_by
  - node: "[[Japan_Sovereign_Carry_Trade_Framework]]"
    relation: enables
  - node: "[[Japan_Filp_To_Qe_Structural_Succession]]"
    relation: succeeds
  - node: "[[Financial_Repression_Via_Reserve_Creation]]"
    relation: instance_of
  - node: "[[Financial_Repression_Distributional_Welfare_Effects]]"
    relation: produces
  - node: "[[Duration_Targeting_Convergence_And_Yield_Trap]]"
    relation: related_to
  - node: "[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]"
    relation: contrasts_with

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The BoJ's QQE + YCC program spanned three phases:

**Phase 1 — QQE (April 2013):** Governor Kuroda launched "Quantitative and Qualitative Monetary Easing" — doubling the monetary base within two years via JGB purchases. Targets: 2% inflation within two years. Instruments: JGB purchases at ¥50 trillion/year, extended maturity of purchases, ETF/J-REIT buying. [RAW-CLIP What about Japan Part I]

**Phase 2 — NIRP (January 2016):** Negative interest rate policy applied a -0.1% rate on a marginal tier of excess reserves, in a three-tier system. Effect: pushed short rates below zero while leaving bulk of reserves at zero.

**Phase 3 — YCC (September 2016):** The BoJ explicitly targeted the 10-year JGB yield at approximately 0%, with an allowable band (initially ±0.1%, widened to ±0.25%, ±0.5%, ±1.0% through successive adjustments). The BoJ committed to unlimited JGB purchases at the fixed yield — effectively becoming buyer of last resort. By 2023, BoJ held >50% of outstanding JGBs.

## Sovereign Carry Trade Mechanics

Through QQE + YCC, Japan's consolidated public sector accumulated:
- **Liabilities**: 91% of GDP in bank reserves (floating-rate, near-zero cost)
- **Assets**: 39% of GDP in domestic equities + 57% of GDP in unhedged foreign securities (long-duration, high-risk)

Annualised excess return over funding cost: **4.66%** (2013–2023), totalling 6.25% of GDP over the decade. This carry trade was sustainable only while the BoJ controlled short rates. [RAW-CLIP What about Japan Part I]

## Duration Stripping and Financial Repression

Each BoJ JGB purchase replaced a long-duration fixed-rate bond in private hands with a short-duration floating-rate reserve. Japanese households — 67% with no securities, parking wealth in bank deposits (duration ≈ 0) — received no benefit from falling discount rates. Equity-holding wealthier households captured the capital gains. [RAW-CLIP What about Japan Part II]

The mechanism: QQE stripped duration out of the market → households left holding zero-duration deposits → government/BoJ captured all duration risk premium. A wealth transfer from depositors to the consolidated public sector and equity holders. See [[Financial_Repression_Distributional_Welfare_Effects]].

## Exit (2024)

The March 2024 BoJ meeting ended the era:
- NIRP abolished (policy rate raised to 0–0.1%)
- YCC cap removed (10-year yield allowed to float freely)
- ETF purchases stopped

By April 2026, policy rate stood at 0.75% (= IORB equivalent). The carry trade is partially unwinding: rising yen funding costs are compressing the sovereign spread. [RAW-CLIP CB Commentary April 2026]
