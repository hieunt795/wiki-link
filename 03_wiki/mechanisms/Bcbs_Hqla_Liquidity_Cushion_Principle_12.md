---
node_id: bcbs_hqla_liquidity_cushion_p12_001
type: mechanism
title: BCBS HQLA Liquidity Cushion — Principle 12 (2008 Pre-LCR Standard)
aliases:
- BCBS HQLA cushion 2008
- Principle 12 liquidity buffer
- unencumbered high quality liquid assets buffer
- pre-LCR liquidity cushion standard
- đệm tài sản thanh khoản chất lượng cao
- nguyên tắc 12 BCBS đệm thanh khoản
domain:
  primary: banking_regulation
  secondary: financial_stability
tags:
- hqla
- liquidity_cushion
- bcbs
- lrm_framework
- liq_buffer
- pre_lcr
- unencumbered_assets
- stress_insurance
- bcbs144
confidence: 4
stability: stable
thesis: 'BCBS Principle 12 (2008) requires banks to maintain a cushion of unencumbered,
  high quality liquid assets as insurance against a range of liquidity stress scenarios,
  sized to cover contractual and non-contractual outflows including loss of unsecured
  and secured funding. No legal, regulatory or operational impediment may prevent
  using these assets to obtain funding. The principle establishes the qualitative
  precursor to Basel III''s LCR: the same concept of HQLA as a pre-positioned buffer,
  but without a specific ratio or standardised run-off assumptions. The cushion''s
  core must be the most reliably liquid assets (cash, high-quality government bonds);
  the composition may widen for less severe but longer-duration stress.

  '
source_refs:
- path: 02_sources/regulator/bcbs/bcbs144.md
  pages: 'para 123–127 (Principle 12 full text), para 8 (P1: cushion in fundamental
    principle), para 94–95 (P10: stress test → cushion sizing link), para 52 (P5:
    cushion in limit framework)'
  weight: primary
parent_node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
related:
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: parent_framework
- node: '[[Bcbs_Liquidity_Stress_Testing_Principle_10]]'
  relation: cushion_sizing_input
- node: '[[LCR_NSFR_Long_Term_Lending_Penalty]]'
  relation: quantitative_successor_lcr
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## The Core Requirement

```
"A bank should maintain a cushion of unencumbered, high quality liquid assets
to be held as insurance against a range of liquidity stress scenarios, including
those that involve the loss or impairment of unsecured and typically available
secured funding sources. There should be no legal, regulatory or operational
impediment to using these assets to obtain funding."
[RAW-BOOK bcbs144 Principle 12]
```

The cushion is insurance, not the first line of defence.
The first line is day-to-day liquidity management; the cushion backs it up.
[RAW-BOOK bcbs144 para 126]

---

## Sizing the Cushion

```
INPUTS to cushion size (from stress tests):
  ① Contractual cash flow mismatches under stress
  ② Non-contractual outflows (implicit support obligations)
  ③ Loss of unsecured funding sources (wholesale, retail run-off)
  ④ Loss of secured funding — except against "safest, most liquid" assets
  ⑤ Duration and severity of stress assumed
  ⑥ Liquidation/borrowing value of assets under stress (haircuts)

ALIGNMENT: cushion size must match established risk tolerance (P2)
"ensure its liquid asset cushion is sized to maintain sufficient resilience
to unexpected stress while it continues to meet its daily payment and
settlement obligations on a timely basis for the duration of the stress"
[RAW-BOOK bcbs144 para 123–124]
```

Banks must not assume liquid markets for assets that are liquid only in normal times.
[RAW-BOOK bcbs144 para 126]

---

## Composition: Core vs Extended

```
CORE (for most severe stress scenarios):
  → Cash
  → High quality government bonds
  → "Similar instruments"
  → Most reliably liquid in all scenarios
  [RAW-BOOK bcbs144 para 125]

EXTENDED (for less intense but longer-duration stress):
  → Other unencumbered assets marketable without excessive losses/discounts
  → Can be sold or used in repo without distressed pricing

ASSET LIQUIDITY CHARACTERISTICS (general):
  ① Transparency of structure and risk
  ② Ease and certainty of valuation
  ③ Central bank eligibility (necessary but NOT sufficient — CB eligibility ≠ ready market liquidity)
  ④ Market depth relative to bank's holding
  ⑤ Bank's own name recognition in that market
  [RAW-BOOK bcbs144 para 126]
```

**Central bank caution:** Do not assume CB will alter terms or quantity of liquidity provision;
do not overstate amount of cash obtainable against eligible assets. [RAW-BOOK bcbs144 para 127]

---

## No-Impediment Condition

The cushion is only effective if it can be deployed immediately.
Three categories of impediment must be absent:

```
LEGAL: No contractual or legal restriction on pledging or selling
REGULATORY: No supervisory restriction on mobilisation in stress
OPERATIONAL: Assets physically accessible; documentation in place;
             settlement can be executed in timeframes needed
[RAW-BOOK bcbs144 Principle 12, para 126]

→ Cross-border pledging requires operational arrangements tested in advance
→ Assets held at custodians must have known mobilisation timeframes (P9)
→ Assets in tied positions (hedges) must be distinguished from free HQLA
[RAW-BOOK bcbs144 para 90]
```

---

## Relationship to Basel III LCR

This principle is the qualitative precursor:

```
BCBS 2008 Principle 12          →    Basel III LCR (2013/2015)
  HQLA cushion: qualitative           LCR = HQLA_stock / 30d_net_outflows ≥ 100%
  "range of stress scenarios"         Defined 30-day stress scenario
  "sized to meet outflows"            Standardised run-off factors by liability type
  Core = gov bonds + cash             Level 1 HQLA (0% haircut) vs Level 2 (haircut)
  Extended = other liquid assets      Level 2A, Level 2B HQLA
  No impediment requirement           Unencumbered, immediately available
  Not the first line of defence       LCR is a minimum; banks hold surplus
  Proportional to bank                LCR applied to internationally active banks
[LLM — derived from Principle 12 text + Basel III LCR standard comparison]
```

The key innovation from 2008 to 2013 was adding quantitative run-off assumptions:
the 2008 standard required banks to estimate their own stress scenarios; Basel III
prescribed standardised scenarios to enable cross-bank comparison and supervisory benchmarking.
