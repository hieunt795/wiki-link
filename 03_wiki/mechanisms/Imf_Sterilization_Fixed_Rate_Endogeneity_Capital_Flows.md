---
node_id: imf_sterilization_fixed_rate_endogeneity_capital_flows_001
type: mechanism
title: IMF Sterilization — Fixed Exchange Rate Endogeneity, Capital Flows, and Sterilization Limits
aliases:
- sterilization operations
- FX endogeneity under peg
- money supply endogeneity fixed rate
- sterilization limits
- capital inflow sterilization
- currency board no sterilization
- can thiệp vô hiệu hóa
- tiền tệ nội sinh tỷ giá cố định
- giới hạn sterilization
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- sterilization
- fixed_exchange_rate
- endogenous_money
- capital_flows
- nfa
- nda
- currency_board
- monetary_autonomy
- impossible_trinity
- bop_monetary_approach
- imf_macro_accounting
steps:
- 'Step 1: Under a fixed exchange rate, the CB commits to buy/sell domestic currency
  at a predetermined fixed price.'
- 'Step 2: Any BOP surplus or deficit forces a change in NFA (reserve change) to maintain
  the peg.'
- 'Step 3: The NFA change automatically changes reserve money (RM = NFA + NDA + OIN),
  making the money supply endogenous to BOP outcomes.'
- 'Step 4: If the CB attempts to tighten (raise domestic credit), the money contraction
  attracts capital inflows; the inflows force FX purchases → NFA rises → RM rises
  → the tightening is frustrated.'
- 'Step 5: Sterilization counteracts Step 3 by offsetting ΔNFA with an equal and opposite
  ΔNDA (OMO), keeping RM unchanged.'
- 'Step 6: Sterilization limits bind through: (a) absence of deep securities market
  for OMO; (b) accumulating interest cost as CB sells securities to fund FX purchases;
  (c) Mundell-Fleming — under full capital mobility, sterilization is impossible as
  any interest differential is instantly arbitraged away.'
confidence: 3
stability: stable
thesis: 'Under a fixed exchange rate regime, the money supply is endogenous — the
  central bank cannot simultaneously fix the exchange rate and independently control
  the money supply. The only way to offset BOP-driven money creation is sterilization:
  an OMO that sells government securities to mop up excess reserve money created by
  FX purchases, keeping RM unchanged despite the NFA change. Sterilization can work
  temporarily but faces three binding limits: (1) it requires a functioning securities
  market; (2) the interest cost of holding excess foreign reserves while paying domestic
  bond yields escalates rapidly; (3) under high capital mobility, any interest differential
  that makes sterilization viable induces further capital inflows, perpetuating the
  cycle. Currency boards institutionalize zero sterilization: RM can only be created
  if fully backed by foreign exchange, making adjustment automatic but potentially
  painful if wages and prices are inflexible.'
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 4794–4865 (fixed rate and money supply endogeneity, sterilization mechanics,
    sterilization limits, currency boards Estonia/Lithuania, floating rate monetary
    autonomy, capital flows under alternative regimes, Figure 5.5)
  weight: primary
parent_node: null
related:
- node: '[[Imf_FX_Regime_Monetary_Accounts_Balance_Sheet_Endogeneity]]'
  relation: endogeneity_result_generalizes_to_managed_rate_regimes
- node: '[[Imf_Five_Monetary_Policy_Instruments_Reserve_Money_Control]]'
  relation: sterilization_is_instrument_1_offset_by_instrument_2
- node: '[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]'
  relation: NDA_ceiling_is_the_sterilization_constraint_in_IMF_programs
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: complements_ALM_focused_sterilization_analysis
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: sterilization_offset_coefficient_quantifies_effectiveness
date_created: '2026-05-31'
date_updated: '2026-05-31'
---

## The Core Problem: Money Supply Endogeneity Under Fixed Rates

Under a fixed exchange rate regime, the monetary authorities stand ready to buy or sell domestic currency for foreign currencies at a predetermined fixed price. This commitment makes the money supply endogenous — it is determined by the system, not by the CB's discretion.

"Adopting a fixed exchange rate regime therefore dedicates monetary policy to the goal of ensuring that the officially fixed level of the exchange rate is also the equilibrium level. The central bank is then committed to adjusting the money supply to the level needed to ensure that the exchange market clears at the predetermined fixed exchange rate. The monetary authorities are therefore unable to control the money supply; in this sense, by agreeing to fix the exchange rate, they relinquish control over the money supply." [RAW-BOOK IMF-macro p.4794]

---

## Mechanism: How Domestic Credit Expansion Is Frustrated Under a Peg

```
CB under fixed rate tries to expand domestic credit (raise NDA):

Step 1: NDA rises (CB buys government securities or lends to banks)
     → RM rises
     → Money supply rises
     → Aggregate spending rises
     → Import demand rises (current account deficit worsens)
     → Downward pressure on the exchange rate

Step 2: Exchange rate threatens to depreciate below the peg
     → CB must sell foreign exchange (buy domestic currency)
     → NFA falls by the same amount NDA rose

Step 3: Net effect:
     ΔNFA = −ΔNDA
     ΔRM = ΔNFA + ΔNDA = 0 (money supply unchanged)

The credit expansion is fully reversed through the balance of payments
```

"Under a fixed exchange rate regime, the effects of the central bank's efforts to expand domestic credit go beyond domestic prices and output. An increase in aggregate spending leads to a rise in the current account deficit and puts downward pressure on the exchange rate. The central bank must counter this pressure by selling foreign exchange, resulting in a drop in net foreign assets. The central bank's attempt to increase the money supply is thereby frustrated." [RAW-BOOK IMF-macro p.4796]

---

## Sterilization: Mechanism and Accounting

Sterilization is the CB's attempt to offset the automatic BOP-driven money creation/destruction, preserving the chosen RM level despite FX intervention.

**Scenario: BOP surplus (reserve inflow) → CB buys FX:**

```
Without sterilization:
  + ΔNFA = +100 (CB buys USD)
  + ΔRM = +100 (DMBs deposit the local currency payment at CB)

With sterilization (OMO sale):
  + ΔNFA = +100 (FX purchase)
  - ΔNDA = -100 (CB sells government securities in OMO)
  Net ΔRM = 0 → monetary conditions unchanged
```

"A sale of foreign exchange that reduces the monetary authorities' net foreign assets is offset by an open market purchase of securities that raises the monetary authorities' net domestic assets, diluting the impact on reserve money and the money supply. With sterilization, the direct link between an external imbalance and the equilibrating change in the money supply is broken." [RAW-BOOK IMF-macro p.4828]

---

## Three Limits of Sterilization

### Limit 1 — Market Infrastructure

Sterilization requires the CB to sell/buy government securities in the secondary market. In most early transition economies, this market did not exist — there were no treasury bills or interbank markets, so OMO was not feasible. Without a securities market, sterilization is not available as a tool. [RAW-BOOK IMF-macro p.4828]

### Limit 2 — Escalating Interest Cost

When the CB sterilizes a capital inflow (buys FX → sells domestic securities):

```
CB accumulates: Foreign reserves (NFA) earning foreign interest rate r*
CB issues:      Domestic government securities paying domestic interest rate r

If r > r* (common when the CB is trying to attract capital), the CB pays:
  Annual carry cost = (r − r*) × sterilized_stock

As the stock of sterilized inflows grows (persistent capital inflow episode):
  → Carry cost grows → CB quasi-fiscal loss → pressure to stop sterilization
```

"The basic weakness [of sterilization] is its dependence on the kind of broad and well-functioning securities market that is not available in many transition economies. More fundamentally, sterilization is limited by the cost of interest payments on the government securities purchased, a cost that can escalate rapidly if the central bank sells too many securities to offset a large foreign exchange inflow." [RAW-BOOK IMF-macro p.4828]

### Limit 3 — Capital Mobility Arbitrage

Under perfect capital mobility, the domestic-foreign interest rate differential is immediately arbitraged:

```
Step 1: CB sterilizes → domestic interest rate maintained above foreign rate
Step 2: Interest differential attracts capital inflows (carry trade)
Step 3: Capital inflow creates new NFA increase → CB must sterilize again
Step 4: Cycle repeats — sterilization perpetuates the capital inflow it tries to offset
Step 5: Eventually CB must:
  (a) Allow some nominal exchange rate appreciation, or
  (b) Allow some monetary expansion (partial sterilization), or
  (c) Accumulate unsustainable quasi-fiscal losses and abandon sterilization
```

"In practice, most countries have responded by undertaking a combination of actions involving (i) a partial intervention to buy some of the capital inflow, thereby allowing some nominal exchange rate appreciation; (ii) partial sterilization to offset part of the impact of the increased net foreign assets on the monetary base; and (iii) some increase in the monetary base and inflation and consequently real exchange rate appreciation." [RAW-BOOK IMF-macro p.4864]

---

## Currency Boards: Institutionalized Zero Sterilization

Currency boards (Estonia 1992, Lithuania 1994 as transition examples) represent the extreme form of a fixed exchange rate with no sterilization option:

```
Currency board rule:
  RM can ONLY be created if backed 100% by foreign exchange holdings
  → NFA = RM at all times (no NDA cushion)
  → Sterilization is ruled out by design

Consequence:
  All adjustment is automatic:
    BOP surplus → NFA + RM rise → money supply rises → prices adjust → real appreciation → adjustment
    BOP deficit → NFA + RM fall → money supply falls → credit tightening → prices adjust (if flexible) OR
                                                           → output/employment falls (if wages rigid)
```

"Currency boards in transition economies essentially create a fixed exchange rate system with no option for sterilization, because reserve money can be created only if it is fully backed by holdings of foreign exchange. Since sterilization is ruled out, adjustments are automatic but not painless. Adjustment will eventually raise nominal and real interest rates and put downward pressure on prices: if prices, and especially wages, are not flexible, output and employment fall." [RAW-BOOK IMF-macro p.4850]

**Benefit**: Imports credibility of the anchor currency's central bank. Eliminates exchange rate risk (for the peg duration). Enforces monetary discipline automatically.

**Cost**: Surrenders monetary control; exchange rate cannot be used as adjustment mechanism; adjustment falls entirely on domestic prices and wages.

---

## Floating Exchange Rate: Monetary Autonomy Restored

Under a pure float, the CB does not intervene → no change in NFA → RM is fully under CB control:

```
Pure float mechanics:
  CB expands credit (raises NDA) → RM rises
  Money supply rises → spending rises → imports rise
  But: no FX intervention required (exchange rate depreciates freely)
  → NFA unchanged → RM gain from NDA expansion is retained

  Exchange rate depreciation becomes an additional transmission channel:
    RM ↑ → exchange rate depreciates → import prices rise → additional inflation channel
    (important in small open economies dependent on critical imports)
```

"With a floating exchange rate regime, the monetary authorities have full control over the domestic money supply and therefore can determine the domestic inflation rate. Excessive credit creation manifests itself through an additional channel (the depreciation of the exchange rate)." [RAW-BOOK IMF-macro p.4852]

**Pure float is largely hypothetical**: Most floating rate countries intervene when the rate moves too far from equilibrium ("dirty float"), implying partial sterilization remains relevant. [RAW-BOOK IMF-macro p.4852]

---

## Summary: Three Regime Comparison

| Regime | RM Endogeneity | Sterilization Available | Monetary Policy Autonomy |
|--------|----------------|------------------------|--------------------------|
| Fixed rate (peg) | High — BOP-driven | Yes, but limited by market and cost | None (must maintain peg) |
| Currency board | Complete — 100% FX-backed | None (prohibited by rule) | None (by design) |
| Managed float | Partial | Yes, common practice | Partial (depends on capital mobility) |
| Pure float | None | Not needed | Full |
| Float + capital mobility | None | Not needed | Full |
| Fixed + capital mobility | Complete | Not feasible (Mundell-Fleming) | None |
