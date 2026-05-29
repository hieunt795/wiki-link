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
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
confidence: 1
stability: stable
thesis: 'IFRS 9 replaced IAS 39 hedge accounting by eliminating the ex-post effectiveness
  test requirement (the 80–125% range) and aligning hedge designation with the bank''s
  actual risk management strategy; four asset classification categories determine
  P&L vs OCI treatment; basis risk can be designated as a separate hedged component;
  but portfolio macro hedging remains under IAS 39 pending IASB completion of its
  portfolio hedging project. [LLM]

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
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

IFRS 9 replaced IAS 39 hedge accounting by eliminating the ex-post effectiveness test requirement (the 80–125% range) and aligning hedge designation with the bank's actual risk management strategy. [LLM] Four asset classification categories determine P&L vs OCI treatment; basis risk can now be designated as a separate hedged component; but portfolio macro hedging remains under IAS 39 pending IASB completion of its portfolio hedging project. [LLM]

## Four Asset Classification Categories Under IFRS 9

IFRS 9 introduces four categories for financial assets, replacing the IAS 39 categories: [LLM]

| Category | Measurement | P&L / OCI Impact | ALM Relevance |
|----------|-------------|-----------------|---------------|
| **Amortized cost** | Historical cost less impairment | Interest via P&L; no fair value moves | HTM-equivalent; bonds held to collect cashflows |
| **FVOCI — debt (with recycling)** | Fair value | Unrealized gains/losses through OCI; realized through P&L on sale | AFS-equivalent; liquidity buffer bonds |
| **FVTPL** | Fair value | All changes through P&L | Trading book; derivatives |
| **FVOCI — equity (no recycling)** | Fair value | All gains/losses through OCI; never recycled to P&L | Strategic equity participations |

[LLM]

The classification depends on the business model under which the asset is held and the contractual cash flow characteristics of the instrument (SPPI test — solely payments of principal and interest). [LLM]

## Three Hedge Models Retained Under IFRS 9

IFRS 9 retains the same three hedge types as IAS 39: [LLM]

### 1. Fair Value Hedge

- **Purpose**: Hedge the exposure to changes in fair value of a recognized asset or liability attributable to a specific risk. [LLM]
- **ALM use**: Hedging fixed-rate bonds or fixed-rate loans against interest rate changes using receive-fixed / pay-floating swaps. [LLM]
- **Accounting**: Changes in fair value of both hedged item and hedging instrument are recognized in P&L simultaneously; effective portions offset, ineffectiveness flows through P&L. [LLM]

### 2. Cash Flow Hedge

- **Purpose**: Hedge the variability in cash flows attributable to a specific risk. [LLM]
- **ALM use**: Hedging floating-rate liabilities against rate rises using pay-fixed / receive-floating swaps; hedging future loan originations. [LLM]
- **Accounting**: Effective portion of derivative gain/loss recognized in OCI (cash flow hedge reserve); reclassified to P&L when the hedged item affects P&L. [LLM]

### 3. Net Investment Hedge

- **Purpose**: Hedge the foreign currency risk arising from a net investment in a foreign operation. [LLM]
- **ALM use**: Hedging the structural FX position arising from foreign subsidiaries. [LLM]
- **Accounting**: Effective portion through OCI; recycled to P&L on disposal of the foreign operation. [LLM]

## Key IFRS 9 Changes vs IAS 39

### Change 1: Elimination of Ex-Post Effectiveness Test

Under IAS 39, hedge accounting required the hedge to be 80–125% effective ex-post at each reporting date; failure terminated hedge accounting and required immediate P&L recycling. [LLM] IFRS 9 eliminates this bright-line test: [LLM]
- There is no retrospective quantitative effectiveness threshold. [LLM]
- Instead, there must be an **economic relationship** between the hedged item and the hedging instrument, and the hedge ratio must not be deliberately set to create accounting ineffectiveness. [LLM]
- This allows hedges that slightly deviate from 1:1 to continue as accounting hedges. [LLM]

### Change 2: Risk Component Designation

IFRS 9 permits designation of a **risk component** as the hedged item, rather than the entire instrument. [LLM] This is directly relevant to ALM: [LLM]
- A bank can designate the **EURIBOR component** of a fixed-rate bond as the hedged risk (excluding credit spread and other components). [LLM]
- **Basis risk** (e.g., difference between EURIBOR and ESTR) can be designated as a separate component and excluded from the hedge relationship, reducing reported ineffectiveness. [LLM]

### Change 3: Alignment with Risk Management Strategy

The hedge documentation under IFRS 9 must align with the bank's **risk management objective and strategy** as documented in internal ALM policies. [LLM] This is a more principles-based requirement than IAS 39's rule-based approach, but it requires that the hedge accounting designation mirrors actual risk management decisions. [LLM]

### Change 4: Rebalancing Mechanism

If the hedge ratio changes but the risk management objective remains the same, IFRS 9 allows **rebalancing** of the hedge (adjusting the quantity of hedging instrument) without fully discontinuing hedge accounting. [LLM] IAS 39 required termination and redesignation. [LLM]

## Macro Hedging — Still Under IAS 39

Portfolio-level (macro) hedge accounting — hedging the net interest rate risk across a portfolio of assets and liabilities — is explicitly **excluded from IFRS 9**. [LLM] Banks applying macro hedging (common in ALM for repricing risk) must continue to use **IAS 39** hedge accounting rules, including the 80–125% effectiveness test, until the IASB completes its portfolio hedging project. [LLM] As of 2026, the IASB's dynamic risk management (DRM) project is still ongoing. [LLM]

## Implications for ALM Reporting

The choice of hedge accounting model directly affects how IRRBB appears in financial statements: [LLM]

- **With fair value hedge**: The hedged item (e.g., fixed-rate loan) is marked to market for the designated risk; volatility in P&L is reduced if the hedge is highly effective. [LLM]
- **Without hedge accounting (economic hedge only)**: The derivative is marked to market through P&L; the hedged item is not; this creates P&L volatility even when the economic risk is perfectly hedged. [LLM]
- **Cash flow hedge**: Derivative fair value changes go to OCI rather than P&L; this smooths NII but creates OCI volatility (revaluation reserve). [LLM]

---
*Source: Chapter 12 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
