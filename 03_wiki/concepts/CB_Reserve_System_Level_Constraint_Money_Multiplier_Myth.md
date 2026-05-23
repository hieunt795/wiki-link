---
node_id: cb_reserve_system_constraint_multiplier_myth_001
type: concept
title: CB Reserve System Level Constraint And Money Multiplier Myth
aliases:
- reserve system level constraint
- money multiplier myth
- banks don't need reserves to lend
- reserves determined by CB identity
- huyền thoại số nhân tiền tệ
- ràng buộc cấp hệ thống của dự trữ
domain:
  primary: monetary_policy
  secondary: banking
tags:
- reserves
- money_multiplier
- central_bank
- balance_sheet
- credit_creation
- misconception
confidence: 1
stability: stable
thesis: "Two foundational misconceptions about commercial bank reserves: (1) individual banks appear to choose between reserves and other assets, but at the system level total reserves are entirely determined by the central bank's balance sheet identities — no individual bank action can reduce system-wide reserves; (2) banks do not require reserves to lend — the money multiplier (reserves → lending) has causality reversed; broad money expands with economic activity and narrow money is subsequently supplied by the CB to meet requirements."
source_refs:
- path: 02_sources/books/central_bank_balance_sheet/Central_Bank_Balance_Sheet.md
  pages: lines 256-305 (Misconception 1 and Misconception 2 sections)
  weight: primary
related:
- node: '[[Required Reserves Taxonomy CB Liquidity Framework]]'
  relation: companion
- node: '[[Fed Balance Sheet Size And Policy Rate Independence]]'
  relation: related_concept
- node: '[[FHLB Foreign Bank EFFR IORB Arbitrage Fed Funds Market]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Misconception 1 — Reserves as an Individual vs System Choice

Individual bank action: A bank can buy assets, reduce its own reserve balance. But:
- The seller's bank is credited by the same amount
- If the seller has no reserve account, their clearing bank is credited
- Even buying foreign assets: the bank providing foreign currency receives the domestic reserves
- Net result: **reserves remain in the system** regardless of individual bank actions [RAW-CLIP]

The only action that genuinely changes system-wide reserves is the central bank's own balance sheet changes. When the ECB's deposit facility swelled after its 3-year LTROs (2010-11), the commentary blamed "bank hoarding" — this was wrong; banks received more reserves because the ECB supplied more, and hoarding simply redistributed them. [RAW-CLIP]

The only way commercial banks could independently reduce system-wide reserves is by exchanging them for banknotes — but this doesn't reduce the monetary base, only changes its composition. [RAW-CLIP]

## Misconception 2 — Money Multiplier Causality Is Reversed

Traditional money multiplier story: CB provides reserves → banks "multiply" them into loans.

What actually happens:
1. Bank makes a loan → creates a deposit (asset-liability extension on the bank's balance sheet, NO reserve impact)
2. Borrower spends the deposit → reserves shift between banks (no net change in system reserves)
3. Reserve requirement applies only to the reserve distribution, not the creation of credit [RAW-CLIP]

**Key refutation**: 80% of reserve-requiring central banks apply requirements in a **lagged manner** — current requirements are based on prior-period lending. Under a genuine money multiplier, new credit would be impossible under lagged reserves. Instead, CB guarantees it will supply adequate reserves to meet the resulting requirement. [RAW-CLIP]

Commercial banks lend when: return on loan > cost of funding (market rate set by CB). Reserve availability does not enter the decision. If the CB controls interbank conditions, lending decisions are independent of reserve quantity (Martin, McAndrews, Skeie 2013). [RAW-CLIP]

**The observable money multiplier is reverse causality**: broad money adjusts with economic activity; narrow money (reserves) is adjusted by the CB afterward to meet imposed requirements. [RAW-CLIP]

## Additional Costs That Shape Lending Decisions

Beyond funding cost, actual lending costs include (Carney 2012):
- Regulatory capital and liquidity buffer requirements
- Administrative and hedging costs (interest rate swaps for fixed-rate loans)
- Credit risk assessment and borrower credit-hunger [RAW-CLIP]

"Commercial banks through history have shown that they are more than capable of expanding lending at times of high interest rates and contracting lending even when rates are low." [RAW-CLIP]
