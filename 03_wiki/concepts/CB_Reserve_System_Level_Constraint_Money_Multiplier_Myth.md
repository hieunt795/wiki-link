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
confidence: 4
stability: stable
thesis: "Two foundational misconceptions about commercial bank reserves: (1) individual banks appear to choose between reserves and other assets, but at the system level total reserves are entirely determined by the central bank's balance sheet identities — no individual bank action can reduce system-wide reserves; (2) banks do not require reserves to lend — the money multiplier (reserves → lending) has causality reversed; broad money expands with economic activity and narrow money is subsequently supplied by the CB to meet requirements."
source_refs:
- path: 02_sources/books/central_bank_balance_sheet/Central_Bank_Balance_Sheet.md
  pages: pp. 11-14 (Misconception 1 and Misconception 2 sections)
  weight: primary
related:
- node: "[[CB_Reserve_Requirements_Taxonomy_Surplus_Shortage_Liquidity]]"
  relation: companion
- node: "[[Fed Balance Sheet Size And Policy Rate Independence]]"
  relation: related_concept
- node: "[[FHLB Foreign Bank EFFR IORB Arbitrage Fed Funds Market]]"
  relation: related_mechanism
date_created: "2026-05-23"
date_updated: "2026-05-24"
---

## Misconception 1 — Reserves as an Individual vs System Choice

Individual bank action: A bank can buy assets, reduce its own reserve balance. But as established by Keister and McAndrews (2009):
- The seller's bank is credited by the same amount.
- If the seller has no reserve account, their clearing bank is credited.
- Even buying foreign assets: the bank providing foreign currency receives the domestic reserves.
- Net result: **reserves remain in the system** regardless of individual bank actions [RAW-BOOK p.12].

The only action that genuinely changes system-wide reserves is the central bank's own balance sheet changes. When the ECB's deposit facility swelled after its 3-year LTROs (2010-11), the commentary blamed "bank hoarding" — this was analytically incorrect; increased use of the deposit facility reflected increased central bank provision of reserves, not commercial bank decisions [RAW-BOOK p.12].

The only way commercial banks could independently reduce system-wide reserves is by exchanging them for banknotes — but this does not reduce the monetary base, merely alters its composition [RAW-BOOK p.12].

## Misconception 2 — Money Multiplier Causality Is Reversed

Traditional money multiplier story: CB provides reserves → banks "multiply" them into loans.

In reality, the process is decoupled:
1. Bank makes a loan → lengthens its balance sheet by increasing loans as assets and deposits as liabilities. This initial process has **no impact on reserves** [RAW-BOOK p.13].
2. Borrower spends the deposit → reserves move between banks to settle the transaction, but the total quantity of reserves is unchanged [RAW-BOOK p.12].
3. Reserve requirements (if any) are met by the central bank providing necessary liquidity to meet the demand.

**Key refutation**: As noted by Gray (2011), 80% of central banks that impose reserve requirements do so in a **lagged manner** (based on lending in a previous period). Under a genuine money multiplier, new credit creation would be impossible under a lagged system. Instead, CB frameworks ensure sufficient reserves are available to meet exogenous short-term demand [RAW-BOOK p.13].

Commercial banks lend when it is profitable: return on loan > cost of funding (market rate set by CB). Reserve availability is not a binding constraint. If the CB controls interbank market conditions, lending decisions are independent of the quantity of reserves (Martin, McAndrews, Skeie 2013) [RAW-BOOK p.13].

**Reverse Causality**: Any observed stable multiplier relationship actually reflects broad money adjusting with economic activity, while narrow money (reserves) is subsequently adjusted by the central bank to meet requirements [RAW-BOOK p.13].

## Additional Costs That Shape Lending Decisions

Beyond funding cost, actual lending determinants include (Beau, Hill, Hussain and Nixon 2014; Carney 2012):
- Regulatory capital and liquidity buffer (LCR/NSFR) requirements.
- Administrative costs and interest rate risk hedging (swaps).
- Credit risk assessment and borrower "credit hungriness" [RAW-BOOK p.14].

"Commercial banks through history have shown that they are more than capable of expanding lending at times of high interest rates and contracting lending even when rates are low" [RAW-BOOK p.14].

Reserve availability is therefore neither a binding constraint nor a direct policy lever for bank lending volume. [LLM]
