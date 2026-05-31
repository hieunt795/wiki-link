---
node_id: imf_quota_sdr_reserve_tranche_credit_tranche_accounting_001
type: concept
title: IMF Quota, SDR, Reserve Tranche, and Credit Tranche — Balance Sheet Accounting
aliases:
- IMF quota accounting
- SDR accounting
- reserve tranche IMF
- credit tranche IMF
- use of Fund credit
- reserve position in the Fund RPF
- hạn ngạch IMF
- SDR phân bổ
- phần dự trữ IMF
- hạn mức tín dụng IMF
- kế toán giao dịch IMF
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- imf
- quota
- sdr
- reserve_tranche
- credit_tranche
- reserve_position_fund
- nfa
- monetary_authorities
- balance_sheet
- international_reserves
- imf_macro_accounting
confidence: 3
stability: stable
thesis: 'IMF transactions affect a member country''s monetary authority balance sheet
  through specific accounting conventions. The reserve position in the Fund (RPF) equals
  quota minus IMF holdings of member currency in excess of reserve tranche; RPF is
  a foreign asset. Use of Fund credit (UFC) is a foreign liability. A new SDR allocation
  is unique: it increases NFA (new SDR holdings) with no matching increase in liabilities
  (SDR counterpart goes to Other Items Net as a capital item), making SDR allocations
  a net expansion of the monetary authority balance sheet. Credit tranche purchases
  increase foreign exchange (asset) and IMF No. 1 Account balance (liability), leaving
  NFA unchanged but increasing UFC (foreign liabilities). The reserve tranche drawdown
  converts RPF (foreign asset) into foreign exchange (also a foreign asset) — NFA
  is unchanged.'
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 5237–5341 (Appendix — IMF transactions, quota definition, reserve
    tranche, credit tranche, SDR concepts, illustrative T-account examples for quota
    payment, reserve tranche drawdown, credit tranche purchase)
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: IMF_transactions_recorded_in_MA_balance_sheet_affecting_NFA
- node: '[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]'
  relation: IMF_transactions_also_recorded_in_BOP_reserve_account
- node: '[[Ma_Balance_Sheet_Oin_Other_Items_Net_Absorber_Mechanics]]'
  relation: SDR_allocation_counterpart_absorbed_into_OIN_capital_item
date_created: '2026-05-31'
date_updated: '2026-05-31'
---

## Overview: Why IMF Transactions Need Special Accounting Treatment

Transactions between a member country and the IMF are recorded in the balance sheet of the monetary authorities (often the central bank serves as the IMF's designated depository). These transactions have specific accounting treatments that affect net foreign assets (NFA), reserve money, and the capital account in non-obvious ways.

"Transactions between a member country and the IMF are recorded in the balance sheet of the monetary authorities." [RAW-BOOK IMF-macro Box 5.4 p.4423]

The three IMF accounts maintained with the member's depository [RAW-BOOK IMF-macro p.5243]:

| Account | Use |
|---------|-----|
| IMF No. 1 Account | Operational transactions (purchases, repurchases, repayment of borrowing) |
| IMF No. 2 Account | Administrative transactions (payment of publications, etc.) |
| IMF Securities Account | Non-negotiable, non-interest-bearing securities substituted for currency in quota payment; cashable on demand |

---

## Key Concepts and Definitions

### Quota
Upon joining the Fund, a country is assigned a quota — the size of its financial commitment and basis for borrowing rights. Paid in:
- At least 75% in national currency
- Up to 25% in a reserve asset (convertible currency)

[RAW-BOOK IMF-macro p.5241]

### Reserve Position in the Fund (RPF)
The reserve position in the Fund equals:

```
RPF = Quota − IMF holdings of member's currency (excluding holdings from UFC)

Alternatively:
RPF = quota payment in reserve assets + Fund's net use of member's currency (lending to others)

Characteristics:
  - Part of the member's external reserves (like gold or foreign exchange)
  - Purchasable at any time unconditionally
  - Not subject to charges
  - Not required to be repurchased
  - Has the characteristics of a reserve asset
```

[RAW-BOOK IMF-macro p.5265]

### Credit Tranches
Available in four tranches, each equal to 25% of a member's quota:

```
Reserve tranche (tranche 0): Purchases not regarded as use of Fund credit
First credit tranche:         Raises IMF holdings of member's currency by 25% of quota
Upper credit tranches (2-4):  Each 25% of quota; higher conditionality required

Additional facilities: Compensatory and contingency financing, buffer stock financing,
                       Extended Fund Facility (EFF)
```

[RAW-BOOK IMF-macro p.5267]

### SDR (Special Drawing Rights)
SDRs are international reserve assets allocated by the IMF. The accounting treatment is unique because a new allocation creates foreign assets with no matching increase in conventional liabilities — the counterpart appears in the capital/reserves section ("Other Items Net").

---

## T-Account Illustrations

### 1. Quota Payment (100 SDR quota: 25% in foreign exchange, 75% in national currency)

**Decomposed payment:**

```
Monetary Authorities
  Assets                          Liabilities
  Foreign exchange:    −25        IMF No. 1 Account:  +75
  (Quota payment:     +100)
  Reserve position RPF: +25
```

**Simplified net view:**

```
Monetary Authorities
  Assets                          Liabilities
  RPF:    +25                     (Net: exchange -25, RPF +25 → NFA unchanged)
```

**Effect on NFA:**
NFA changes as follows:
- Foreign exchange falls by 25 (paid to IMF)
- RPF rises by 25 (counterpart: reserve position)
- Net NFA unchanged

"This is reflected in changes in the balance sheet of the monetary authorities as follows... the increase in the country's reserve position with the IMF is offset by a decline in the country's foreign exchange position." [RAW-BOOK IMF-macro p.5282-5287]

Accounting formula:

```
RPF = Quota − (IMF No. 1 Account balance − holdings reflecting UFC)

Initially: RPF = 100 − 75 = 25  (= 25% paid in reserve assets)
```

---

### 2. Reserve Tranche Drawdown

A country can draw its entire reserve tranche at any time without conditionality.

```
Before drawdown:
  IMF No. 1 Account: 75 (MA's local currency held by IMF)
  RPF: 25

Drawdown of 25:
  + Foreign exchange: +25 (IMF releases reserve assets)
  IMF No. 1 Account: 100 (IMF needs member's currency, debits No. 1 Account further)

After drawdown:
  Foreign exchange: 25 → 0
  RPF: RPF = Quota − IMF holdings (ex UFC) = 100 − 100 = 0
```

**Effect on NFA:**
- Before: RPF = 25 (foreign asset)
- After: Foreign exchange gained 25, RPF falls to 0
- Net NFA unchanged — one type of foreign asset replaces another

[RAW-BOOK IMF-macro p.5295-5309]

---

### 3. Credit Tranche Purchase of SDR 40

A credit tranche purchase means the country uses IMF resources (a loan), classified as "Use of Fund Credit" (UFC).

```
Before purchase:
  Foreign exchange: 0
  RPF: 0 (after full reserve tranche draw)
  IMF No. 1 Account (liability): 100

Purchase of SDR 40:
  Monetary Authorities
    Assets                          Liabilities
    + Foreign exchange: +40         IMF No. 1 Account: +140 (IMF debits more local currency)
                                    Use of Fund Credit (UFC): +40

After purchase:
  RPF = Quota − (IMF holdings − UFC) = 100 − (140 − 40) = 0
  UFC = 40 (new foreign liability)
```

**Effect on NFA:**
- Foreign exchange rises +40 (new asset from IMF loan)
- UFC rises +40 (new foreign liability)
- Net NFA unchanged (+40 asset − 40 liability = 0)

"Note that use of IMF credit includes the country's use of IMF resources beyond the reserve tranche, and is included in foreign liabilities." [RAW-BOOK IMF-macro Box 5.4 p.4423]

[RAW-BOOK IMF-macro p.5311-5330]

---

### 4. New SDR Allocation (Unique Case — NFA Increases)

An SDR allocation by the IMF is the one transaction that expands NFA without a matching conventional liability:

```
New SDR allocation of, say, 50:
  Monetary Authorities
    Assets                          Liabilities
    + SDR holdings: +50             SDR counterpart (capital item in OIN): +50
```

"In contrast, a new allocation of SDRs increases the net foreign assets of the country, because the increase in assets is not matched by an increase in liabilities [in the standard sense]." [RAW-BOOK IMF-macro Box 5.4 p.4423]

**Effect on NFA:**
- SDR holdings (foreign asset) rise +50
- The counterpart in the capital account ("SDR allocations") appears in "Other Items Net" as a capital liability — but this is a permanent allocation, not a foreign exchange liability
- Net NFA: +50 (SDR holdings) minus SDR allocation counterpart treatment in NFA definition
- Under most IMF accounting, the SDR counterpart is classified in the capital account (OIN), not as a foreign liability → NFA rises by the allocation amount

This makes SDR allocations analogous to "printing reserve assets" for members — expanding international liquidity without requiring repayment.

---

## Summary Table: NFA Effects of IMF Transactions

| Transaction | NFA Effect | Mechanism |
|-------------|-----------|-----------|
| Quota payment (25% FX, 75% local currency) | Unchanged | Foreign exchange ↓, RPF ↑ by same amount |
| Reserve tranche drawdown | Unchanged | RPF ↓, Foreign exchange ↑ by same amount |
| Credit tranche purchase | Unchanged | Foreign exchange ↑, UFC (foreign liability) ↑ |
| New SDR allocation | Increases by allocation amount | SDR holdings ↑, counterpart in OIN (capital) not a foreign liability |
| SDR cancellation or use | Decreases | SDR holdings ↓ |

---

## Policy Relevance

**International reserves reporting:** The NFA of the monetary authorities is broader than official international reserves. NFA includes assets "that are not regarded as available if a balance of payments problem develops." For example, bilateral payment agreement claims and inconvertible foreign currency holdings are in NFA but not in official reserves. [RAW-BOOK IMF-macro p.4342]

**RPF as a reserve asset:** The reserve position in the Fund counts toward a country's official international reserves. Drawing the reserve tranche does not reduce international reserves — it converts one reserve asset (RPF) into another (foreign exchange).

**UFC as foreign debt:** Use of Fund credit beyond the reserve tranche is a foreign liability subject to repurchase obligations and charges. It is included in the foreign liabilities of the monetary authorities and is excluded from international reserves.

**IMF program monitoring:** In IMF financial programs, the floor on Net International Reserves (NIR) typically includes the RPF (as a reserve asset) and excludes UFC (as a liability against reserves). Program design must account for these accounting conventions precisely to avoid mismeasuring reserve adequacy.
