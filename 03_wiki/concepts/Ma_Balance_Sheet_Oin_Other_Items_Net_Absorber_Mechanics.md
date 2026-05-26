---
node_id: ma_balance_sheet_oin_other_items_net_absorber_mechanics_001
type: concept
title: MA Balance Sheet OIN Other Items Net Absorber Mechanics
aliases:
- OIN monetary authority
- other items net CB
- OINm
- OINb
- balance sheet absorber
- valuation adjustment OIN
- khoản mục khác ròng NHTW
- OIN bảng cân đối NHTW
- số dư kế toán NHTW
- điều chỉnh định giá lại OIN
domain:
  primary: monetary_policy
tags:
- oin
- balance_sheet
- valuation_adjustment
- quasi_fiscal
- recapitalization
- monetary_survey
- reserve_money
- cb_capital
- revaluation
- absorber
- monetary_authority
- em_policy
confidence: 3
stability: evolving
thesis: 'OIN (Other Items Net) is the mandatory residual in the MA identity RM = NFA
  + NCG + Cb + OIN: any change in assets or liabilities that does not alter RM flows
  into OIN, making it a balance-sheet absorber that simultaneously captures (1) FX
  revaluation gains/losses on NFA when exchange rates change without actual transactions,
  (2) cumulative quasi-fiscal losses from sterilization as retained earnings decline,
  and (3) recapitalization injections when government restores CB capital. Negative
  OINm signals CB capital exhaustion and a latent fiscal cost that precedes formal
  recapitalization; in M2 decomposition, the OINb weight (ΔOINb/OINb × OINb/M2) isolates
  the quasi-fiscal and valuation component of broad money growth from genuine credit
  expansion.'
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md
  pages: 'Box 5.2 p.4336–4353 (OINm components); Box 5.8 p.4651 (valuation → OIN); p.4572–4578 (M2 decomposition OINb weight); p.1841 (recapitalization fiscal treatment)'
  weight: primary
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 2720–2728 (sterilization losses → OINm decline); lines 2745–2753 (OINm exhaustion dual deterioration)'
  weight: primary
related:
- node: '[[IMF Monetary Survey And Reserve Money Identity Framework]]'
  relation: identity_foundation — OIN is the fourth term of RM = NFA + NCG + Cb + OIN
- node: '[[IMF Monetary Survey — Valuation Adjustment and Transaction Flow Decomposition]]'
  relation: valuation_channel — FX revaluation flows into OIN via VAj mechanism
- node: '[[CB FX Target — Five-Entity Combined Balance Sheet Trace (T-Account Scenarios)]]'
  relation: applied_context — OINm decline in Scenario A; OINm exhaustion in Scenario D
- node: '[[CB Quasi-Fiscal Mechanism — Sterilization Costs, Seigniorage, and the Fiscal-Monetary Nexus]]'
  relation: loss_source — QF losses accumulate in OINm as retained earnings fall
- node: '[[CB FX Rate Target Balance Sheet Constraint And Sterilization]]'
  relation: parent_mechanism — sterilization is the primary driver of OINm decline under FX target
- node: '[[IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)]]'
  relation: regime_context — under FX target, OIN is the only NDA component freely adjustable
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## Three Mechanisms That Move OIN

**1 — Valuation adjustment (FX revaluation):**
Exchange rate change → NFA in LCU changes → RM unchanged (no transaction) → ΔOIN absorbs the difference. Depreciation: ΔOIN = −VAj (negative, surplus side). Appreciation: ΔOIN = +VAj (positive, deficit side). [RAW-BOOK IMF Macro Box 5.8 p.4651]

**2 — Quasi-fiscal loss accumulation:**
Each sterilization period: CB earns r_f on NFA < pays r_d on sterilization stock → net loss → retained earnings ↓ → OINm ↓. When OINm = 0, seigniorage transfer to Treasury = 0. When OINm < 0, CB is insolvent in accounting terms; Treasury must recapitalize. [RAW-BOOK Lipschitz p.2720–2728]

**3 — Recapitalization:**
Government issues recap bonds → injects into CB capital → OINm ↑ restored. Fiscal cost concealed in headline deficit (only annual interest flows recorded); true cost = full NB_recap stock. [RAW-BOOK IMF Macro p.1841]

## OINm as Diagnostic Signal

| OINm trend | Interpretation |
|---|---|
| Rising steadily | CB profitable; seigniorage transfer positive |
| Flat despite large NFA | Valuation gains offset by QF losses — net zero |
| Slowly declining | Sterilization cost > earnings; latent fiscal stress |
| Approaching zero | CB capital near-exhausted; recap imminent |
| Negative | Accounting insolvency; fiscal contingency materializing |
| Large sudden jump ↑ | Recapitalization just occurred |

