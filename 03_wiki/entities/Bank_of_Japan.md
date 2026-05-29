---
node_id: entity_boj_001
type: entity
title: Bank of Japan (BoJ)
aliases:
- BoJ
- BOJ
- 日本銀行
- Ngân hàng Trung ương Nhật Bản
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
  - fiscal_policy
tags:
- central-bank
- japan
- ycc
- qe
- unconventional-policy
confidence: 3
stability: evolving
entity_type: central_bank
jurisdiction: JP
established: 1882
mandate: Price stability (2% inflation target) and financial system stability
thesis: 'The Bank of Japan is notable for operating the world''s most extensive unconventional
  monetary policy regime: Quantitative and Qualitative Easing (QQE) from 2013, Yield
  Curve Control (YCC) from 2016, culminating in a 2024 exit from negative rates and
  YCC cap removal. Its decade-long zero-rate policy enabled Japan''s consolidated
  public sector to operate a sovereign carry trade at 91% of GDP in bank reserves,
  compressing household duration and engineering implicit financial repression.

  '
source_refs:
- path: 02_sources/Clipping/What about Japan_ (Part I).md
  weight: primary
- path: 02_sources/Clipping/What about Japan_ (Part II).md
  weight: primary
- path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
  weight: supporting
parent_node: null
related:
- node: '[[Japan_Sovereign_Carry_Trade_Framework]]'
  relation: implements
- node: '[[Japan_Filp_To_Qe_Structural_Succession]]'
  relation: implements
- node: '[[BOJ_QQE_YCC_Policy_2013_2024]]'
  relation: executed
- node: '[[Duration_Targeting_Convergence_And_Yield_Trap]]'
  relation: related_to
- node: '[[Financial_Repression_Via_Reserve_Creation]]'
  relation: implements
date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The Bank of Japan, the oldest central bank in Asia (est. 1882), sets monetary policy through its Policy Board. Its operational history is distinctive: conventional easing exhausted by the late 1990s, it pioneered **Quantitative Easing (QE)** in 2001–2006, then launched **Quantitative and Qualitative Easing (QQE)** under Governor Kuroda in April 2013 — the most aggressive peacetime balance sheet expansion by any G7 central bank relative to GDP.

## Balance Sheet Scale

By end-2023, BoJ assets exceeded 130% of Japanese GDP. Bank reserves stood at **91% of GDP** — the liability counterpart to JGB purchases. The consolidated public sector (government + BoJ + public pension funds) effectively ran a sovereign carry trade: borrow floating at BoJ-controlled near-zero rates, invest in long-duration domestic equities (39% of GDP) and unhedged foreign securities (57% of GDP). Annualised excess return over funding costs: 4.66% (2013–2023). [RAW-CLIP What about Japan Part I]

## YCC and Its Exit

Yield Curve Control (YCC), introduced September 2016, pegged the 10-year JGB yield at ~0% (±0.1%, later widened to ±0.5%, then ±1.0%). The BoJ became the buyer of last resort for JGBs, distorting price discovery. The March 2024 YCC exit — raising the policy rate from -0.1% to 0–0.1% and removing the 10-year yield cap — ended eight years of explicit yield targeting. By April 2026, the policy rate stood at 0.75% (= IOER). [RAW-CLIP CB Commentary April 2026]

## Financial Repression Mechanism

QE structurally stripped duration out of private hands: when the BoJ buys JGBs and pays with reserves, it converts fixed-rate long-duration bonds into floating-rate near-zero-duration liabilities. [LLM] Japanese households, who park ~70% of financial wealth in deposits (duration ≈ 0), absorbed the duration removal without benefit — while equity-holding wealthier households captured the capital gains from falling discount rates. This wealth transfer mechanism is documented in [[Financial_Repression_Distributional_Welfare_Effects]] and [[Japan_Sovereign_Carry_Trade_Framework]].

## Policy Status (2026)

In April 2026, the BoJ held its policy rate at 0.75% amid Hormuz supply shock uncertainty. Governor Ueda's framework: treat headline energy-driven inflation as transitory unless it produces "secondary effects" in underlying inflation. The BoJ is watching for whether the shock feeds wages and services prices. [RAW-CLIP CB Commentary April 2026]
