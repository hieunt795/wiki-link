---
node_id: imf_five_monetary_policy_instruments_reserve_money_control_001
type: framework
title: IMF Five Monetary Policy Instruments for Reserve Money Control
aliases:
- five monetary policy instruments
- reserve money instruments
- FX intervention monetary effect
- open market operations reserve money
- discount window reserve money
- reserve requirements monetary control
- deficit monetization printing money
- năm công cụ chính sách tiền tệ
- kiểm soát tiền cơ sở
domain:
  primary: monetary_policy
  secondary: []
tags:
- reserve_money
- monetary_instruments
- fx_intervention
- open_market_operations
- discount_rate
- reserve_requirements
- deficit_financing
- monetary_base
- monetary_authorities
- imf_macro_accounting
confidence: 3
stability: stable
thesis: 'The monetary authorities control reserve money (high-powered money / monetary
  base) through five direct instruments: (1) FX intervention — purchases of foreign
  exchange increase NFA and reserve money; (2) open market operations — purchases
  of government securities from the public increase reserve money; (3) financing the
  government deficit — when the government spends borrowed CB funds, net credit to
  government rises one-for-one with reserve money (equivalent to printing money);
  (4) discount window — changes in the rate or quantity of CB lending to deposit money
  banks affect reserve money, with the discount rate being the most controllable lever;
  (5) reserve requirements — increasing required reserves forces banks to hold more
  reserves for the same deposit base, mechanically expanding reserve money while simultaneously
  reducing the money multiplier. Any purchase of one asset offset by a sale of another
  (sterilization) leaves reserve money unchanged.'
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 4384–4401 (five instruments — FX intervention, OMO, deficit financing,
    discount window, reserve requirements), lines 4352–4380 (reserve money identity,
    balance sheet constraint, growth decomposition)
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: instruments_change_asset_side_of_MA_balance_sheet_affecting_RM
- node: '[[Imf_Money_Multiplier_Ratio_Decomposition_Three_Agent]]'
  relation: reserve_requirements_change_both_RM_and_multiplier
- node: '[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]'
  relation: NDA_ceiling_constrains_instruments_2_3_4
- node: '[[Imf_FX_Regime_Monetary_Accounts_Balance_Sheet_Endogeneity]]'
  relation: under_fixed_rate_instrument_1_becomes_endogenous
- node: '[[Imf_Sterilization_Fixed_Rate_Endogeneity_Capital_Flows]]'
  relation: sterilization_is_instrument_1_plus_instrument_2_offsetting
date_created: '2026-05-31'
date_updated: '2026-05-31'
---

## Overview: Reserve Money as the Fulcrum

The monetary authorities are the monopoly supplier of reserve money (RM), also called high-powered money or the monetary base. Because RM = Currency issued + DMB reserves, and M2 = mm × RM, reserve money control is the primary route through which the CB controls broad money and hence inflation and aggregate demand.

"By virtue of being the monopoly supplier of reserve money, the monetary authorities are the undisputed arbiter of monetary policy and monetary conditions in the economy." [RAW-BOOK IMF-macro p.4332]

The balance sheet identity of the monetary authorities (MA) is:

```
ASSETS                        LIABILITIES
Net Foreign Assets (NFA)      Reserve Money (RM)
Claims on Government (NCG)    Government Deposits
Claims on DMBs (CDB)          Foreign Liabilities
Claims on Private (CPS)       Capital Accounts
Other Items Net (OIN)

Identity: NFA + NCG + CDB + CPS + OIN = RM (net of other liabilities)

In growth form:
ΔRM/RM = w_NFA × ΔNFA/NFA + w_NCG × ΔNCG/NCG + w_CDB × ΔCDB/CDB + ...
(weighted contributions of each asset class to RM growth)
```

[RAW-BOOK IMF-macro p.4354-4378]

---

## Instrument 1 — Foreign Exchange Intervention

The MA intervenes in the FX market to defend the exchange rate or achieve a desired level of international reserves.

**Mechanics when MA buys FX (e.g., USD) from a domestic resident:**

```
MA balance sheet:
  + NFA (foreign assets rise)
  + RM (reserve money rises — the resident deposits the payment check at a DMB,
         which deposits it at the MA → DMB reserves at MA rise)

Net effect: ΔNFA = +X → ΔRM = +X (one-for-one, no sterilization)
```

**Mechanics when MA sells FX:**

```
  - NFA (foreign assets fall)
  - RM (reserve money falls)
```

"When the central bank purchases foreign exchange from a domestic resident and pays for it by writing a check against itself (or equivalently by printing money), it increases reserve money. Its balance sheet shows an increase in foreign assets and a corresponding rise in reserve money." [RAW-BOOK IMF-macro p.4392]

**Key caveat:** Under a fixed exchange rate regime, NFA adjusts endogenously to BOP outcomes. The MA cannot simultaneously fix the exchange rate and fully control RM through this channel. Changes in NFA from BOP outcomes "cannot generally be considered to be a fully policy-controlled variable." [RAW-BOOK IMF-macro p.4380]

**Sterilization:** If the MA offsets a FX purchase with an OMO sale (Instrument 2), the net effect on RM is zero. "If the purchase of an asset is offset by the selling of another asset, the monetary base will not change. In this case we say that the initial action has been sterilized." [RAW-BOOK IMF-macro p.4388 fn7]

---

## Instrument 2 — Open Market Operations (OMO)

OMO consists of buying and selling government securities (typically in the secondary market) to change the stock of the monetary base. This is "one of the preferred methods of changing the stock of the monetary base." [RAW-BOOK IMF-macro p.4394]

**Purchase of government securities from the public:**

```
MA balance sheet:
  + Claims on Government (securities holdings rise)
  + RM:
      (a) if paid in newly printed currency → currency in circulation rises
      (b) if paid by MA check → DMBs deposit the check at the MA → DMB reserves rise

In both cases: ΔNCG(OMO) = +X → ΔRM = +X
```

**Sale of government securities to the public:**

```
  - Claims on Government
  - RM (DMBs' deposits at MA fall as banks pay for the securities)
```

OMO requires a functioning secondary market in government securities. In many transition economies in early stages of reform, this market does not exist — limiting OMO as an instrument and forcing reliance on Instruments 4 and 5. [RAW-BOOK IMF-macro p.4882]

---

## Instrument 3 — Financing the Government Deficit

When the government borrows directly from the central bank:

**Step 1 — Government borrows from CB:**

```
MA balance sheet:
  + Claims on Government (gross claims rise)
  + Government Deposits (government holds the loan proceeds at CB)

Net NCG = Claims - Government Deposits → no change yet in net NCG
```

**Step 2 — Government spends the borrowed money (e.g., pays civil servants):**

```
MA balance sheet:
  - Government Deposits (government draws down its CB account)
  + RM: private sector recipients deposit payments at DMBs → DMB reserves at MA rise

Net NCG = Claims - (lower) Government Deposits → rises one-for-one
ΔRM = +1 for each unit of government spending from CB credit
```

"A fiscal deficit financed by borrowing from the central bank thus results in a one-for-one increase in reserve money. For this reason, financing a deficit by borrowing is equivalent to financing a deficit by issuing currency (frequently referred to as deficit financing by printing money, or simply as the monetization of the deficit)." [RAW-BOOK IMF-macro p.4398]

**Hallmark of central bank independence:** The CB's ability to refuse government lending is the defining characteristic of monetary policy independence. Where the CB cannot refuse, fiscal dominance is complete. "The central bank's ability to control the reserve money it creates by refusing to lend to the government is therefore one hallmark of an independent central bank." [RAW-BOOK IMF-macro p.4398]

---

## Instrument 4 — Discount Window (Rediscount Policy)

The discount mechanism encompasses arrangements designed to influence the level of CB credit to the banking system. The most important component is the interest rate charged — the discount rate.

**Higher discount rate:**

```
  → Cost of DMB borrowing from CB rises
  → DMBs reduce borrowing from CB
  → DMBs also increase excess reserves (precautionary, to avoid costly CB borrowing)
  → Net: CDB (claims on DMBs) falls → RM falls

Signal: Signals intention to tighten monetary conditions
```

**Lower discount rate:**

```
  → Cost of CB borrowing falls
  → DMBs borrow more from CB
  → CDB rises → RM rises
```

"By making such borrowing more costly, it tends to reduce bank borrowing from the central bank, while at the same time inducing banks to increase their holding of excess reserves. Thus, it tends to reduce central bank assets and hence reserve money." [RAW-BOOK IMF-macro p.4400]

**Most controllable instrument:** "The central bank's credit to deposit money banks is in practice the source of reserve money most directly under its control." [RAW-BOOK IMF-macro p.4400 fn9] In established financial markets, discount lending is typically limited to short-term liquidity support and LOLR in crises.

Other discount window parameters: types of eligible collateral, maximum credit per borrower. [RAW-BOOK IMF-macro p.4403 fn8]

---

## Instrument 5 — Reserve Requirements

The CB mandates that DMBs hold a percentage of their deposits as reserves (either as vault cash or as deposits at the MA).

**Increase in reserve requirement:**

```
  → DMBs must hold more reserves per unit of deposits
  → For the same deposit level, total required reserves rise → RM rises mechanically
  → BUT: ability to create new money falls (multiplier effect is reduced)

Effect on multiplier:
  mm = (1 + c) / (c + r)
  Higher r → denominator rises → mm falls

Net: RM rises, mm falls, M2 may fall or be unchanged depending on magnitudes
```

"An increase in the reserve requirement will force the banking system to hold a larger level of reserves for the same level of deposits, thus increasing reserve money. At the same time, however, it will reduce the ability of the banking system to create money." [RAW-BOOK IMF-macro p.4401]

**Decomposed reserve requirement (IMF formulation):**

```
RM = CY + rd×DD + rt×TD + re×DD

Where:
  rd = required reserve ratio on demand deposits
  rt = required reserve ratio on time/savings deposits
  re = excess reserves as ratio to demand deposits (endogenous behavior of DMBs)

This decomposition shows three agents determine RM:
  1. MA: sets rd and rt
  2. DMBs: choose re (excess reserves, sensitive to discount rate and payment system efficiency)
  3. Public: determines c (currency ratio) and b (time/demand deposit split)
```

[RAW-BOOK IMF-macro p.4728-4756]

---

## Practical Controllability Hierarchy

The five instruments differ in the degree to which the MA can unilaterally control reserve money:

| Instrument | MA Control | Why Constrained |
|------------|-----------|-----------------|
| Discount window (Instrument 4) | Highest direct control | MA sets rate and eligibility; banks may or may not borrow |
| Reserve requirements (Instrument 5) | High — regulatory mandate | Changes affect RM mechanically; but have large side effects on multiplier |
| OMO (Instrument 2) | High — if market exists | Requires liquid secondary securities market |
| Deficit financing (Instrument 3) | Medium — depends on CB independence | In many countries, CB cannot refuse government; politically constrained |
| FX intervention (Instrument 1) | Low — driven by BOP | NFA is largely a residual of BOP outcomes under fixed rate regime |

"The monetary authorities' control over reserve money tends to be incomplete. For example, changes in net foreign assets, which are a reflection of the balance of payments outcome, cannot generally be considered to be a fully policy-controlled variable. Also, variations in claims on the government are, in many countries, adjusted passively to the government's budgetary position, especially in countries without an independent central bank." [RAW-BOOK IMF-macro p.4380]

---

## Worked Identity: Reserve Money Growth Decomposition

From the MA balance sheet identity, reserve money growth is the weighted sum of asset contributions:

```
ΔRM/RM = (ΔNFA/RM) + (ΔNCG/RM) + (ΔCDB/RM) + (ΔCPS/RM) + (ΔOIN/RM)

Where each Δ/RM term is the contribution (not the growth rate) of each asset class
to total reserve money growth. Weights are lagged asset shares in RM.
```

[RAW-BOOK IMF-macro p.4364-4378]

This decomposition is the standard diagnostic tool in IMF monetary programs: which instrument/counterpart is driving reserve money growth, and is it controllable?
