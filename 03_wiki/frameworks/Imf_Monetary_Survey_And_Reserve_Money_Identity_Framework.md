---
node_id: imf_monetary_survey_and_reserve_money_identity_framework_001
type: framework
title: IMF Monetary Survey And Reserve Money Identity Framework
aliases:
- Monetary Survey
- Reserve Money Identity
- M2 = NFA + NDA
- IMF Financial Programming Framework
- Điều tra tiền tệ IMF
- Đồng nhất thức tiền cơ sở
domain:
  primary: monetary_policy
tags:
- imf
- monetary_survey
- reserve_money
- nfa
- nda
- m2
- financial_programming
- monetary_authorities
- dmb
confidence: 4
stability: evolving
thesis: The IMF Monetary Survey consolidates Monetary Authorities and Deposit Money
  Banks into a single balance sheet where M2 = NFA + NDA (net foreign assets plus
  net domestic credit), and reserve money growth is driven by changes in NFA, net
  claims on government, claims on banks, and other net items — the core identity underlying
  IMF financial programming.
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'Chapter 5: Monetary Accounts and Analysis'
  weight: primary
related:
- node: '[[IMF Balance of Payments Framework and External Account Analysis]]'
  relation: shared_tag:imf
- node: '[[IMF Flow Of Funds 4-Sector Consistency Framework]]'
  relation: shared_tag:imf
- node: '[[IMF GFS Fiscal Accounting Framework Deficit Measurement And Sustainability]]'
  relation: shared_tag:imf
- node: '[[IMF Monetary Analysis Quantity Theory Velocity And Exchange Rate Regimes]]'
  relation: shared_tag:imf
- node: '[[IMF SNA Real Sector Accounting GDP Identities And Sectoral Accounts]]'
  relation: shared_tag:imf
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The **Monetary Survey** is the consolidated balance sheet of the entire banking system (Monetary Authorities + Deposit Money Banks). It is the foundational tool of IMF financial programming, linking monetary policy to GDP, inflation, and the balance of payments [RAW-CLIP].

## The Three-Level Financial System
```
Level 1: Monetary Authorities (MA) balance sheet + DMBs balance sheets (separate)
Level 2: Monetary Survey = consolidated MA + all DMBs
Level 3: Financial Survey = Monetary Survey + Other Financial Institutions (OFIs)
```
The monetary survey focuses on the banking sector because: (1) monetary liabilities strongly influence aggregate nominal spending; (2) data are available even in developing economies; (3) banks typically account for the bulk of financial assets in less developed markets [RAW-CLIP].

## The Monetary Authorities Balance Sheet (Analytical Form)
```
ASSETS                              LIABILITIES
Net Foreign Assets (NFA)            Reserve Money (RM)
  Gold, FX, SDRs, IMF reserve pos.    Currency issued (in banks + outside)
  Less: foreign liabilities           DMBs' deposits at MA
Net Claims on Government (NCG)      Government deposits
  Government securities + loans     Foreign liabilities
  Less: government deposits           Use of IMF credit
Claims on DMBs (Cb)                 Capital accounts + OIN(net)
Claims on Private Sector
Other Items Net (OINm)
```
[RAW-CLIP]

## Reserve Money Identity
The balance sheet constraint gives the fundamental identity:

```
Reserve Money (RM) = NFA + NCG + Cb + OINm
```

In flow terms:
```
ΔRM = ΔNFA + ΔNCG + ΔCb + ΔOINm
```

This means reserve money expands when: (1) foreign reserves increase (BoP surplus); (2) CB lends more to government; (3) CB lends more to banks (discount window); (4) other net assets increase [RAW-CLIP].

## Monetary Survey Identity (M2 = NFA + NDA)
Consolidating MA and DMBs, interbank positions cancel out. The result:

```
M2 = NFA + NDA
NDA = NDC + OIN(b)
NDC = NCG + CPS (Claims on Private Sector)
```

Therefore:
```
M2 = NFA + NCG + CPS + OIN(b)
```

This is the core IMF monetary programming identity: **broad money is fully determined by net foreign assets plus net domestic credit** [RAW-CLIP].

## Money Definitions
- **Reserve Money (RM / M0):** Currency issued + DMBs' deposits at MA
- **M1 (Narrow Money):** Currency outside banks + Demand deposits
- **M2 (Broad Money):** M1 + Quasi-money (time, savings, foreign currency deposits) + money market instruments

## Five Monetary Policy Instruments (via Reserve Money)
1. **FX Intervention:** CB buys FX → NFA rises → RM rises (sterilization reverses via OMO)
2. **Open Market Operations:** CB buys government securities → NCG rises → RM rises
3. **Deficit Financing:** Government borrows from CB → spends → NCG rises → RM rises (1:1 money printing)
4. **Discount Window:** CB lends to DMBs → Cb rises → RM rises; rate affects demand for borrowing
5. **Reserve Requirements:** Higher RR → same RM supports fewer deposits (reduces money multiplier) [RAW-CLIP]

## Money Multiplier and Fractional Reserve
DMBs hold only a fraction of deposits as reserves (fractional reserve system). The money multiplier:
```
m = M2 / RM
```
Changes in RM propagate through the multiplier to affect M2. DMBs' demand for excess reserves is influenced by: payment system efficiency, discount rate, and uncertainty [RAW-CLIP].

## Central Bank Independence and Reserve Money Control
Control over reserve money is incomplete because:
- **NFA** reflects BoP outcomes (partly exogenous)
- **NCG** in many countries is determined by fiscal needs (passive monetization of deficit)
- **Cb** (discount window) is most directly controllable

An independent central bank's key attribute: ability to refuse to monetize the fiscal deficit by controlling NCG [RAW-CLIP].

## Accounting Principles
- **Stocks vs flows:** Balance sheets are stocks; analysis focuses on period-to-period changes
- **Cash vs accrual:** IFS records on cash basis; most bank transactions settled immediately so distinction is minor
- **Currency conversion:** Foreign-currency items converted at end-period exchange rate
- **Consolidation:** Interbank items (due from/to other banks) are netted; not mere aggregation [RAW-CLIP]


