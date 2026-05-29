---
node_id: hedge_accounting_ifrs9_alm_banking_book_001
type: mechanism
title: Hedge Accounting IFRS 9 for ALM Banking Book
aliases:
- IFRS 9 hedge accounting
- IAS 39 replacement hedge accounting
- fair value hedge banking book
- cash flow hedge ALM
- kế toán phòng ngừa rủi ro IFRS 9
- IAS 39 thay thế kế toán phòng ngừa
- phòng ngừa giá trị hợp lý ngân hàng
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- IFRS9
- hedge-accounting
- IAS39
- fair-value-hedge
- cash-flow-hedge
- OCI
confidence: 3
stability: stable
thesis: 'IFRS 9 replaced IAS 39 hedge accounting (final rules published July 24,
  2014; EU endorsed November 29, 2016) by eliminating the ex-post 80–120% effectiveness
  test, extending hedged items to include derivatives in documented hedge groups,
  and aligning hedge designation with actual risk management strategy. Four asset
  classification categories determine P&L vs OCI treatment. Portfolio macro hedging
  remains under IAS 39 pending IASB portfolio hedging project completion.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 12: Hedge Accounting (IFRS 9 and ALM)'
parent_node: null
related:
- node: '[[Eve_Calculation_Mechanics_Discount_And_Shock]]'
  relation: related_to
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: related_to
- node: '[[ALM_Hedging_Strategy_Design]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Context: IAS 39 → IFRS 9

Hedge accounting principles were incorporated into IAS 39 to eliminate valuation asymmetries from different accounting treatment of a hedge and hedged item. The rules were characterised by many administrative obligations and limitations that restricted use in banks. [RAW-Elkenbracht-Huizing ch.12 p.1]

In 2009 a project was set up to replace IAS 39 with IFRS 9. The final hedge accounting rules were published **July 24, 2014**, endorsed by the EU **November 29, 2016**. [RAW-Elkenbracht-Huizing ch.12 p.1]

## Four Asset Classification Categories Under IFRS 9

IFRS 9 distinguishes four categories of financial assets (IFRS 9, Paragraph 4.1): [RAW-Elkenbracht-Huizing ch.12 p.2]

1. **Amortised cost** — comparable to former loans and receivables; objective is to collect contractual cashflows (solely payments of principal and interest).
2. **FVOCI debt instruments** — cumulate gains/losses in OCI; reclassified to P&L upon derecognition (comparable to former available-for-sale).
3. **FVPL** — debt, equity instruments and **all derivatives** measured at fair value through P&L (trading).
4. **FVOCI equity** — at fair value through OCI **without recycling** in P&L.

No "held-to-maturity" category in IFRS 9. Classification based on two criteria: (1) the bank's **business model** for managing the financial assets; (2) the individual **contractual cashflow characteristics**. [RAW-Elkenbracht-Huizing ch.12 p.2]

For hedge accounting, only financial instruments at amortised cost or FVOCI can be designated hedged items. [RAW-Elkenbracht-Huizing ch.12 p.2]

## Key Changes in IFRS 9 Hedge Accounting vs IAS 39

Changes were driven by the need to simplify rules and align with risk management methods: [RAW-Elkenbracht-Huizing ch.12 p.3]

- **Extension of hedged items** to include derivatives within a group of hedged items — real hedges now documentable (not permitted under IAS 39).
- **Simplification:** ex-post efficiency tests no longer required; the **80–120% range for hedge effectiveness removed**.
- Recognition of hedging costs in **OCI as well as P&L** — reduces P&L volatility.
- Documented hedge accounting for **product groups and net positions**.
- Integration with high-level risk strategy — violation of the risk strategy may compromise hedge accounting.
- More disclosure requirements than IAS 39.

**Unchanged general mechanics** from IAS 39: accounting models for fair value hedge, cash flow hedge, and net investment hedge retained; hedge effectiveness measured and ineffectiveness recognised in P&L; hedge documentation still required; hedge accounting remains optional; only external deals can be designated hedged instruments. [RAW-Elkenbracht-Huizing ch.12 p.3]

## Risk Management Strategy Requirement

For hedge accounting, the bank must describe the expected/experienced risks and their risk management in a **risk management strategy at board level**, documented in risk management guidelines or policy. The risk management guidelines are also part of IFRS 7 disclosure. [RAW-Elkenbracht-Huizing ch.12 p.3]

Risk management objectives must be aligned to the high-level risk strategy. A risk management objective that does not conform to the strategy can prevent accounting of the documented hedge — or, in existing documented hedge groups, a change in objective can **force termination** of a hedge relationship affecting the P&L account. **Voluntary termination of a documented hedge relationship is no longer permitted** without severe changes in the risk management strategy. [RAW-Elkenbracht-Huizing ch.12 p.3]

## Macro Hedging — Still Under IAS 39

At the time of writing, the macro-hedging model (where amounts of both hedging instrument and hedged item can change constantly) was **still being deliberated by the IASB**. The chapter therefore focuses on the final "general hedge accounting model." Banks applying macro hedging continue to use IAS 39. [RAW-Elkenbracht-Huizing ch.12 p.1]
