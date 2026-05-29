---
node_id: imf_fx_regime_monetary_accounts_balance_sheet_endogeneity_001
type: mechanism
title: IMF FX Regime Balance Sheet — Monetary Accounts Perspective (Chapter 5)
aliases:
- IMF FX regime monetary accounts
- exchange rate regime balance sheet endogeneity
- fixed rate money supply endogenous
- capital inflows three regime analytics
- IMF Chapter 5 FX target balance sheet
- tỷ giá cố định và nội sinh cung tiền
- bảng cân đối tỷ giá theo IMF Chapter 5
- tính nội sinh tiền cơ sở dưới chế độ tỷ giá cố định
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- fx_regime
- nfa_endogeneity
- reserve_money
- sterilization
- fixed_exchange_rate
- currency_board
- capital_flows
- monetary_survey
- imf_macro_accounting
- dollarization
- monetary_autonomy
- impossible_trinity
confidence: 4
stability: stable
thesis: 'Under a fixed exchange rate regime, the central bank''s monetary accounts
  identity (RM = NFA + NCG + Cb + OIN) loses its normal causality: NFA becomes endogenous
  — determined by BOP flows and the intervention obligation — and money supply adjusts
  to clear the exchange market rather than serving as a policy instrument. This is
  the IMF Chapter 5 formulation of the same constraint captured in the impossible
  trinity: fixing the exchange rate surrenders monetary control. Sterilization can
  delay but not sustain monetary independence because of two limits — the depth of
  the securities market and the fiscal cost of the interest differential. The three
  real-world responses to capital inflows (partial intervention, partial sterilization,
  some monetary expansion) describe the middle ground between the pure fixed and pure
  float extremes.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 4382–4402 (Section: Interpretation of Balance Sheet Changes — five
    instruments for controlling reserve money: FX intervention, OMO, deficit financing,
    discount window, reserve requirements); lines 4794–4853 (Special Issues in Monetary
    Analysis — exchange rate regimes and monetary analysis: fixed rate endogeneity,
    sterilization limits, currency board, floating rate autonomy); lines 4854–4865
    (Role of capital flows: perfect capital mobility under fixed rate, three-component
    real world response, Figure 5.5)

    '
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: identity_foundation — this node explains what happens to that identity
    under FX target
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: companion_mechanism — Lipschitz formulation of the same constraint; richer
    on intervention T-accounts
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: fiscal_cost_mechanism — sterilization interest cost channel
- node: '[[Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design]]'
  relation: regime_design — crawling peg as intermediate solution
- node: '[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]'
  relation: policy_application — NDA ceiling derived under fixed rate assumption
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: quantitative_measurement — offset and sterilization coefficients measure
    what this node describes
- node: '[[Policy_Trilemma_Efficiency_Frontier_Equivalence]]'
  relation: theoretical_root
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## The Core IMF Formulation: Balance Sheet Causality Reversal

Under the reserve money identity:

```
RM = NFA + NCG + Cb + OIN
```

In normal (no FX target) operation, the CB freely chooses NFA — buys or sells FX at discretion — and uses NDA (NCG + Cb + OIN) as the primary monetary policy instrument.

When a CB **commits to a fixed exchange rate**, the causality reverses:

> "Under a fixed exchange rate system, the monetary authorities stand ready to buy or sell the domestic currency for foreign currencies at a predetermined fixed price. Whenever the market exchange rate threatens to depart from this fixed rate, the monetary authorities buy or sell foreign exchange for the local currency to ensure that the rate remains at the fixed level. In terms of the monetary authorities' balance sheet, **net foreign assets adjust in line with the foreign exchange intervention, and the monetary base and money supply adjust in line with net foreign assets**. Adopting a fixed exchange rate regime therefore dedicates monetary policy to the goal of ensuring that the officially fixed level of the exchange rate is also the equilibrium level. The central bank is then committed to adjusting the money supply to the level needed to ensure that the exchange market clears at the predetermined fixed exchange rate. **The monetary authorities are therefore unable to control the money supply**; in this sense, by agreeing to fix the exchange rate, they relinquish control over the money supply." [RAW-BOOK IMF Macro p.4794]

```
NORMAL (no FX target):             FIXED EXCHANGE RATE:
  NFA = policy variable            NFA = endogenous (determined by BOP + intervention)
  NDA = primary instrument         NDA = can be used for sterilization only
  RM  = target                     RM  = residual (adjusts to clear FX market)
  → Money supply controlled        → Money supply endogenous
```

## The Five Instruments for Controlling Reserve Money

The IMF framework identifies five direct instruments (Box 5.2 / Section: Interpretation of Balance Sheet Changes) [RAW-BOOK IMF Macro p.4382–4402]:

| Instrument | Mechanism | Balance Sheet Effect |
|------------|-----------|---------------------|
| **FX Intervention** | Buy/sell FX reserves | NFA ↑↓, RM ↑↓ (1:1) |
| **Open Market Operations** | Buy/sell government securities in secondary market | NCG ↑↓, RM ↑↓ (1:1) |
| **Government Deficit Financing** | CB lends to government; government spends → RM rises when deposits transferred to private sector | NCG ↑, RM ↑ (1:1); "monetization of deficit" |
| **Discount Window (Rediscount)** | CB lends to banks at policy rate; rate change affects demand for CB credit | Cb ↑↓, RM ↑↓; most directly controlled instrument |
| **Reserve Requirements** | Change in mandatory reserve ratio forces banks to hold more/less reserves | RM ↑ (higher RRR forces higher deposits at CB); money multiplier ↓ |

**Key insight:** "It is clear that if the purchase of an asset (e.g., government securities, foreign exchange) is offset by the selling of another asset, the monetary base will not change. In this case we say that the initial action has been **sterilized**, in the sense that its impact on the monetary base and hence on overall liquidity conditions in the economy has been offset." [RAW-BOOK IMF Macro footnote 71 p.4388]

Sterilization = using one instrument (OMO / NCG) to offset the RM effect of another instrument (FX intervention / NFA). Under a fixed rate, the CB gives up discretion over FX intervention — so sterilization via NDA is the only residual instrument.

---

## Sterilization Under Fixed Rate: Mechanism and Limits

When the CB intervenes (e.g., buys FX to resist appreciation → NFA ↑ → RM ↑), sterilization uses OMO to reverse the RM effect:

```
Step 1 — FX Intervention:
  NFA ↑  → RM ↑  (monetary expansion from FX purchase)

Step 2 — Sterilization OMO:
  NCG ↓  → RM ↓  (sell government securities, drain RM)

Net effect on RM: ≈ 0  (sterilization "worked")
Net effect on balance sheet: NFA ↑, NCG ↓, NDA ↓, RM unchanged
```

The IMF identifies **two binding limits** on this approach [RAW-BOOK IMF Macro p.4828]:

**Limit 1 — Securities market depth:**
> "Sterilization can work only for a short period. Its basic weakness is its dependence on the kind of broad and well-functioning securities market that is not available in many transition economies." [RAW-BOOK IMF Macro p.4828]

In shallow markets, large OMO sales drive up domestic interest rates sharply (thin absorption capacity), attracting more capital inflows, requiring more FX purchases, requiring more sterilization — a self-reinforcing loop.

**Limit 2 — Interest cost escalation:**
> "More fundamentally, sterilization is limited by the cost of interest payments on the government securities purchased, a cost that can escalate rapidly if the central bank sells too many securities to offset a large foreign exchange inflow." [RAW-BOOK IMF Macro p.4828]

When CB sells domestic T-bills at r_domestic > r_foreign (yield on accumulated FX reserves):
```
Net carry cost per period = r_domestic × sterilization_stock − r_foreign × NFA_accumulated
                           = NEGATIVE (for typical EM)
```
This becomes a quasi-fiscal loss → seigniorage transfer inverts → government funding drain.

---

## Exchange Rate Regime Spectrum: Balance Sheet Implications

### Fixed Peg (Hard)
```
CB Balance Sheet under fixed peg:
  NFA = fully endogenous (must intervene to maintain exact parity)
  NDA = sterilization-only instrument (no independent monetary policy)
  RM  = fully determined by external balance
  
Policy implication: "Adopting a fixed exchange rate regime dedicates monetary policy
to the goal of ensuring that the officially fixed level of the exchange rate is also
the equilibrium level." [RAW-BOOK IMF Macro p.4794]
```

Corollary (financial programming): "Using domestic credit ceilings to improve the balance of payments within the financial programming framework is a simple corollary of this analysis. Under a fixed exchange rate regime, **the money supply is rendered endogenous** — that is, it is determined by the system — rather than being an instrument of policy." [RAW-BOOK IMF Macro p.4810]

### Currency Board
Maximum constraint — sterilization is **legally impossible**:

> "Currency boards in transition economies (such as those adopted by Estonia and, more recently, Lithuania) essentially create a fixed exchange rate system with **no option for sterilization, because reserve money can be created only if it is fully backed by holdings of foreign exchange**. Since sterilization is ruled out, adjustments are automatic but not painless. Adjustment will eventually raise nominal and real interest rates and put downward pressure on prices: if prices, and especially wages, are not flexible, output and employment fall." [RAW-BOOK IMF Macro p.4850]

```
Currency Board balance sheet constraint:
  NFA_cb / RM_cb ≥ 1.0   (Greenspan-Guidotti rule, currency board interpretation)
  → RM can only expand if NFA expands 1:1
  → NDA is legally fixed (cannot be used for sterilization)
  → Monetary policy = 0 (no independent policy possible)
  
Adjustment mechanism (no sterilization):
  BOP deficit → NFA ↓ → RM ↓ → liquidity tightens → r_domestic ↑ → prices ↓
  (deflation and unemployment, not exchange rate adjustment)
```

### Floating Exchange Rate
Full monetary autonomy — CB chooses NFA freely:

> "With a floating exchange rate regime, the monetary authorities have full control over the domestic money supply and therefore can determine the domestic inflation rate. Excessive credit creation manifests itself through an additional channel (the depreciation of the exchange rate). In most small, open economies dependent on critical imports, the exchange rate therefore provides an additional channel between the money stock and inflation." [RAW-BOOK IMF Macro p.4852]

```
Float balance sheet logic:
  NFA = discretionary (CB decides whether/how much to intervene)
  NDA = full policy instrument
  RM  = fully controlled
  
BOP adjustment mechanism:
  CA deficit → excess FX demand → domestic currency depreciates
  → No CB intervention → NFA unchanged
  → Depreciation restores trade competitiveness automatically
```

---

## Capital Flows: Fixed vs. Float Comparison (Figure 5.5 Analytics)

The IMF identifies the capital flow transmission as **the key test** of monetary autonomy under alternative regimes [RAW-BOOK IMF Macro p.4854–4865]:

### Under Fixed Exchange Rate + Open Capital Account

> "Under perfect capital mobility, the slightest difference between interest rates prevailing in domestic and foreign capital markets provokes very large capital flows. When a fixed exchange rate is added, a central bank **cannot hope to influence the level of domestic interest rates**. Any attempt by the central bank to tighten monetary policy will induce a huge capital inflow into the country, forcing the central bank to intervene in the exchange market in order to keep the domestic currency from appreciating. The increase in net foreign assets offsets the initial money contraction, forcing domestic interest rates down to the world level." [RAW-BOOK IMF Macro p.4862]

```
CB tightens (ΔNDA ↓, raises r_domestic):
  r_domestic > r_foreign → capital inflows → FX excess supply
  → CB must buy FX (fixed rate obligation) → ΔNFA ↑
  → ΔNFA offsets ΔNDA → RM unchanged → r_domestic back to r_foreign
  
Net result: Monetary tightening fully offset by capital inflow response.
Policy implication: Interest rate policy IMPOTENT under fixed rate with open capital account.
```

### Under Floating Exchange Rate + Open Capital Account

> "Under a floating exchange rate regime, the absence of intervention by the monetary authorities implies no change in net foreign assets, and the current account deficit is equal to private and official capital inflows. **The link between the money supply and the balance of payments is broken**, and the central bank regains control over the money supply." [RAW-BOOK IMF Macro p.4864]

```
CB tightens (ΔNDA ↓, raises r_domestic):
  r_domestic > r_foreign → capital inflows → domestic currency appreciates
  → No CB intervention → ΔNFA = 0
  → Tightening transmitted fully to domestic conditions
  → Appreciated exchange rate reduces inflation via import prices (additional channel)
  
Net result: Monetary tightening fully effective; exchange rate acts as additional transmission channel.
```

### Real-World Middle Ground: Three-Component Response

> "In practice, most countries have responded by undertaking a combination of actions involving (i) **a partial intervention** to buy some of the capital inflow, thereby allowing some nominal exchange rate appreciation; (ii) **partial sterilization** to offset part of the impact of the increased net foreign assets on the monetary base; and (iii) some **increase in the monetary base and inflation** and consequently real exchange rate appreciation." [RAW-BOOK IMF Macro p.4864]

```
REAL WORLD RESPONSE TO CAPITAL INFLOWS:

Component (i) — Partial FX intervention:
  CB buys some FX (not all) → ΔNFA ↑ (partial) → some monetary expansion
  Exchange rate still appreciates partially (not held fixed)

Component (ii) — Partial sterilization:
  CB sells T-bills → ΔNDA ↓ → partially offsets component (i) RM expansion
  Limit: securities market depth + interest cost

Component (iii) — Accept some monetary expansion:
  Residual ΔNFA not sterilized → ΔRM ↑ → some inflation → real appreciation via prices
  
Combined result:
  → Some nominal appreciation (less than full float)
  → Some reserve accumulation (less than full peg)
  → Some domestic monetary expansion (less than full sterilization failure)
  → Tripod between exchange rate, reserves, and inflation management
```

---

## Dollarization: The Currency Substitution Complication

Currency substitution (dollarization) undermines FX target effectiveness from a different angle [RAW-BOOK IMF Macro p.4784–4793]:

> "Currency substitution substantially undermines the authorities' ability to conduct monetary policy, as the foreign currency component of the total money supply **cannot be directly controlled**." [RAW-BOOK IMF Macro p.4788]

```
Balance sheet implication of dollarization:
  M2 = M1_domestic + Quasi-money_domestic + FX_deposits_domestic (residents)
  
  FX_deposits are in M2 but:
    (a) Not directly controllable by CB reserve requirements (if unremunerated or exempt)
    (b) Respond to inflation expectations and exchange rate expectations, not CB rate
    (c) When local currency depreciates → FX_deposits rise in local currency value
       → M2 rises WITHOUT any monetary expansion → valuation effect in monetary survey
```

This connects to the IMF valuation adjustment problem [see [[Imf_Monetary_Survey_Valuation_Adjustment_Transaction_Flow_Decomposition]]]:
- Depreciation → FX deposits (local currency value) ↑ → M2 ↑ → looks like monetary expansion
- But is pure revaluation, not transaction-based money creation
- OIN absorbs the adjustment in the monetary survey

**The anti-dollarization limits from IMF:**
> "Combating dollarization with artificial measures, such as issuing indexed domestic financial instruments or forcing the conversion of foreign assets, merely magnifies the eventual inflation 'explosion.' Normally, sound financial and fiscal policies will increase holdings of assets denominated in domestic currency without government mandates." [RAW-BOOK IMF Macro p.4788]

---

## Three-Way Regime Comparison: Balance Sheet Summary

```
BALANCE SHEET INSTRUMENT MATRIX BY REGIME:

                    Fixed Peg    Currency Board   Managed Float   Pure Float
NFA                 Endogenous   Fully endogenous Discretionary   Discretionary
NDA (sterilization) Available    NOT available    Available       Available
RM                  Endogenous   Endogenous       Partially        Controlled
                    (adjusts to  (= NFA, 1:1)     controlled
                     FX market)
Monetary autonomy   None         Zero             Partial         Full
FX intervention     Mandatory    Mandatory 1:1    Discretionary   None

KEY BALANCE SHEET SIGNAL:
  Fully endogenous NFA: peg absorbs all BOP shocks into RM
  Fully controlled NDA: sterilization can offset, with fiscal limits
  Combination: actual monetary outcomes = mix of both
```

---

## Connection to IMF Financial Programming (NDA Ceiling)

The NDA ceiling in IMF programs is the **operational translation** of this analysis [RAW-BOOK IMF Macro p.4810]:

```
Under fixed exchange rate:
  ΔM2 = ΔNFA + ΔNDA
  ΔM2_target is determined by money demand (quantity theory)
  ΔNFA_program is the target change in reserves (BoP objective)

→ ΔNDA ≤ ΔM2_target − ΔNFA_program   ← NDA ceiling

If ΔNFA falls short of program (BoP weaker than expected):
  → ΔNDA ceiling tightens automatically
  → Forces domestic credit contraction to preserve M2 target
  
If ΔNFA exceeds program (strong reserves):
  → ΔNDA ceiling loosens
  → CB can allow more domestic credit (or accumulate more reserves)

This is the "monetary approach to the balance of payments" (MABP):
under a fixed rate, monetary policy must subordinate itself to reserve targets.
```

---

## Diagnostic Checklist (IMF Chapter 5 Perspective)

```
SIGNAL: NFA declining while NCG rising, RM stable
  → Classic sterilized intervention against depreciation pressure
  → CB defending peg, buying time
  → Check: how long can NDA expand before hitting ceiling?

SIGNAL: NFA rising, NDA declining, RM stable
  → Sterilized appreciation defense (buying FX, absorbing RM)
  → Sterilization quasi-fiscal cost accumulating
  → Check: interest differential × sterilization stock = quarterly CB loss

SIGNAL: NFA rising, NDA not fully declining, RM expanding
  → Partial sterilization only (real world middle ground)
  → Monetary expansion leaking through; inflation risk rising
  → Check: what share of NFA expansion is being sterilized? (β coefficient)

SIGNAL: M2 rising but NDA stable
  → NFA driving M2 expansion (FX inflow-driven)
  → Strong BoP not fully sterilized → monetary easing via FX channel
  → Benign if CPI stable; risk if capacity constraints bite

SIGNAL: M2 rising faster than NFA + NDA would suggest
  → Check dollarization: FX deposit revaluation may inflate M2
  → Check OIN: valuation adjustments absorbed there
  → True monetary expansion may be smaller than headline M2 growth suggests
```
