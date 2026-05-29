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
parent_node: null
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
date_updated: '2026-05-25'
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

## Monetary Authorities Balance Sheet (Box 5.2 — Analytical Form)
```
ASSETS                                    LIABILITIES
──────────────────────────────────────────────────────────────────────
NFA  Net Foreign Assets                   RM  Reserve Money
  + Gold holdings                           Currency outside banks (CY)
  + Foreign exchange reserves               DMB cash in vault
  + Reserve position in IMF                 DMB deposits at MA
  + SDR holdings
  − Short-term foreign liabilities        Government deposits
    (deposits of foreign CBs,               (Treasury accounts at CB)
     swap facilities, overdrafts)
  − Use of IMF credit                     Foreign liabilities
                                            Use of IMF credit
NCG  Net Claims on Government               Other short-term foreign debt
  + Government securities held
  + Direct loans to Treasury             Capital accounts + OINm
  − Government deposits at MA              Physical assets of CB
                                            Capital and reserves
Cb   Claims on DMBs                         Valuation adjustments
  (discount window lending,                  Unclassified items
   repo/liquidity facilities)

CPS  Claims on Private Sector
  (direct CB lending, rare in
   modern central banking)

OINm Other Items Net
  (physical assets, capital,
   valuation adjustments)
──────────────────────────────────────────────────────────────────────
Identity: NFA + NCG + Cb + CPS + OINm = RM + Govt deposits + Foreign liabilities
```
[RAW-BOOK IMF Macro Box 5.2 p.4336–4353]

## Deposit Money Banks Balance Sheet (Box 5.5 — Analytical Form)
```
ASSETS                                    LIABILITIES
──────────────────────────────────────────────────────────────────────
Reserves                                  Demand Deposits (DD)
  Cash in vault                             Sight deposits
  Deposits with Monetary Authorities        Checking accounts

Foreign Assets                            Quasi-money (QM)
  Claims on nonresident banks               Time deposits
  Claims on nonresident nonbanks            Savings deposits
                                            Foreign currency deposits
Claims on Government
  Treasury bills                          Money Market Instruments
  Other government securities               Certificates of deposit
  Loans and advances to govt                Promissory notes

Claims on Nonfinancial                    Bonds
  Public Enterprises
                                          Restricted Deposits
Claims on Private Sector (CPS)              Import prepayments
  Discounts, loans, mortgages               Other restricted deposits
  Investments, overdrafts
                                          Foreign Liabilities
Claims on Nonmonetary
  Financial Institutions                  Government Deposits

                                          Credit from Monetary Authorities
                                            (discount window borrowing)

                                          Liabilities to Nonmonetary
                                            Financial Institutions

                                          Capital Accounts
──────────────────────────────────────────────────────────────────────
Identity: Reserves + Foreign Assets + Claims = Deposits + Liabilities + Capital
```
[RAW-BOOK IMF Macro Box 5.5 p.4432–4530]

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

### Monetary Survey Balance Sheet (Box 5.7 — Consolidated)
MA and DMB balance sheets are consolidated; interbank positions cancel out.

```
ASSETS                                    LIABILITIES
──────────────────────────────────────────────────────────────────────
NFA  Net Foreign Assets                   M1  Narrow Money
  = MA NFA                                  CY  Currency outside banks
  + DMB net foreign assets                  DD  Demand deposits
    (net of interbank claims)

NCG  Net Claims on Government             QM  Quasi-money
  = MA claims on govt                       Time deposits
  + DMB claims on govt                      Savings deposits
  − Govt deposits at MA                     Foreign currency deposits
  − Govt deposits at DMBs                     of residents

CPS  Claims on Private Sector           ──────────────────────────────
  = MA CPS + all DMB credit             M2 = M1 + QM
    to nongovernment private            NDA = NDC + OINb
    sector                              NDC = NCG + CPS

OINb Other Items Net (banking)          M2 = NFA + NDA
  = Residual; absorbs valuation           (Money market instruments,
    adjustments, capital accounts,         bonds, restricted deposits
    unclassified interbank items           included where applicable)
──────────────────────────────────────────────────────────────────────
Identity: NFA + NCG + CPS + OINb = M2
```
[RAW-BOOK IMF Macro Box 5.7 p.4546–4580]

**Formal zero-sum form (Box 6.4, Equation 6) [RAW-BOOK IMF Macro Box 6.4 p.5503–5504]:**

```
Banking sector identity (Eq. 6):
  ΔM2 = ΔNFA + ΔNDC + ΔOINb
  ΔM2 − ΔNFA − ΔNDC − ΔOINb = 0                  ... (6)

Where:
  ΔM2   = Change in broad money (liabilities side of monetary survey)
  ΔNFA  = Change in net foreign assets (includes MA + DMB FX positions)
  ΔNDC  = Change in net domestic credit = ΔNCGnet + ΔCPS
           (NCGnet = claims on govt net of govt deposits; CPS = credit to private)
  ΔOINb = Change in other items net (banking sector residual; absorbs
           valuation adjustments, unclassified items, capital accounts)

Banking sector saving-investment gap (by convention):
  Sb − Ib = 0   (banking sector has zero real transactions)
  → Only financial intermediation; no autonomous saving or investment
```

**Flow direction interpretation:**
```
ΔNFA ↑ (reserve accumulation)  →  ΔM2 ↑  (monetary expansion from FX inflows)
ΔNCGnet ↑ (more credit to govt) →  ΔM2 ↑  (monetization of deficit)
ΔCPS ↑ (more credit to private) →  ΔM2 ↑  (private credit expansion)
ΔOINb ↓ (capital losses, write-offs) → ΔM2 ↓ (contraction from losses)
```

**NDA ceiling derivation (financial programming):**
```
From Eq. 6: ΔNDA = ΔM2 − ΔNFA
  → ΔNDA ≤ ΔM2(target) − ΔNFA(program)
  → ΔNDA ceiling = programmed money demand growth − target reserve change

This is the IMF NDA ceiling in financial programming: ensures domestic credit
creation is consistent with the money demand and reserve accumulation targets.
```

### M2 Growth Decomposition
Each component of the monetary survey contributes to M2 growth in proportion to its share [RAW-BOOK IMF Macro p.4572–4578]:

```
ΔM2/M2 = (ΔNFA/NFA) × (NFA/M2)
        + (ΔNCG/NCG) × (NCG/M2)
        + (ΔCPS/CPS) × (CPS/M2)
        + (ΔOINb/OINb) × (OINb/M2)

Interpretation:
  → Each term = growth rate of component × weight in M2
  → NFA/M2 = openness weight: high in open/dollarized economies
  → NCG/M2 = fiscal monetization weight: elevated during CB deficit financing
  → CPS/M2 = private credit weight: dominant in financially developed economies
  → OINb/M2 = residual / valuation effect weight

Policy use: decompose observed M2 growth into its sources to isolate
  whether expansion is FX-driven (ΔNFA), fiscal (ΔNCG), or private credit (ΔCPS).
```

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


