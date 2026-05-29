---
node_id: currency_substitution_dollarization_001
type: concept
title: Currency Substitution and Dollarization — Monetary Control Implications
aliases:
- currency substitution
- dollarization
- FX deposits
- dollarization ratio
- monetary control under dollarization
- đô la hóa
- thay thế tiền tệ
- tiền gửi ngoại tệ
- kiểm soát tiền tệ đô la hóa
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- dollarization
- currency_substitution
- monetary_control
- fx_deposits
- transition_economy
- em_policy
- inflation
- imf_macro_accounting
confidence: 3
stability: stable
thesis: 'Currency substitution occurs when residents hold FX assets (deposits, cash)
  as a substitute for domestic money, driven by high inflation, exchange rate instability,
  or institutional distrust of the CB. FX deposits/M2 ratios reached 30-60% in peak
  transition economies. Dollarization undermines CB monetary control: base money (RM)
  no longer fully determines M2 because FX deposits lie partly outside the domestic
  money multiplier chain. Attempts to reverse dollarization by force (banning FX deposits)
  typically backfire by driving FX holdings offshore, further shrinking the domestic
  monetary base. [LLM]

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 4778–4820 (currency substitution definition, dollarization ratio, transition
    economy peak, monetary control implications, anti-dollarization backfire)
  weight: primary
parent_node: null
related:
- node: '[[Imf_Money_Multiplier_Ratio_Decomposition_Three_Agent]]'
  relation: dollarization_compresses_domestic_multiplier
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: dollarized_system_amplifies_fx_target_constraints
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: dollarization_amplifies_balance_sheet_crisis_risk
- node: '[[Hyperinflation_Dynamics_Cagan_Real_Money_Collapse]]'
  relation: hyperinflation_triggers_flight_to_fx
- node: '[[Transition_Economy_Monetary_Special_Issues]]'
  relation: dollarization_is_dominant_transition_economy_problem
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Definition and Measurement

**Currency substitution** (broad): Residents use foreign currency for any of the three money functions:
- Store of value (FX savings deposits)
- Medium of exchange (FX cash transactions)
- Unit of account (FX-denominated contracts, wages, prices)

**Dollarization ratio** (standard IMF measure):

```
Dollarization ratio = FX deposits / M2
                    = FX deposits / (domestic deposits + FX deposits + currency)

Where FX deposits = resident holdings of FX-denominated bank deposits
```

[RAW-BOOK IMF p.4778]

Threshold interpretations:
- < 10%: Low dollarization — CB retains most monetary control
- 10-30%: Moderate — significant FX exposure but manageable
- 30-60%: High — peak range for transition economies during disinflation
- > 60%: Severe — CB monetary transmission effectively broken; de facto dollarization

**Peak levels in transition economies**: Bolivia, Peru, Vietnam, former Soviet states reached 30-60% during high-inflation periods of the 1990s. [RAW-BOOK IMF p.4785]

---

## Why Dollarization Occurs: Triggers

```
Primary trigger: Inflation → loss of domestic money as store of value

Domestic inflation ↑
→ Real return on domestic deposits → negative
→ FX assets preserve real value
→ Public shifts savings to FX deposits / USD cash

Secondary trigger: Exchange rate instability
→ Even if inflation is moderate, large FX volatility destroys domestic
  asset value unpredictably
→ FX holding provides exchange rate hedge

Tertiary trigger: Institutional distrust
→ History of forced conversion, confiscation, devaluation
→ Public learns to distrust domestic banking system
→ FX deposits shift offshore (capital flight)
```

[RAW-BOOK IMF p.4782–4790]

The trigger is **asymmetric and persistent**: dollarization rises faster during inflation spikes than it falls during stabilization. This is because re-denomination costs are high and trust rebuilds slowly even after inflation falls.

---

## Monetary Control Breakdown

Dollarization breaks the standard RM→M2 transmission chain:

```
Standard (no dollarization):
  H (reserve money) → mm → M2 (domestic)
  CB controls H → CB influences M2

With dollarization:
  H → mm → M2_domestic
  FX deposits → M2_FX (determined by BOP, FX supply, CB FX policy)
  
  M2_total = M2_domestic + M2_FX
  
  CB controls only H and hence M2_domestic
  M2_FX is exogenous to CB (determined by capital flows, FX rate, offshore conditions)
```

[RAW-BOOK IMF p.4792]

**Three specific breakdowns:**

**1. Multiplier compression**
FX deposits do not generate domestic reserve requirements (in most systems). Residents shifting domestic to FX deposits:
- Reduces `D` (demand deposits) → `c` effectively rises in the multiplier formula
- Reduces the reserve-creating deposit base → mm falls for given `H`

**2. Interest rate transmission weakening**
When 40-60% of financial assets are in FX, domestic policy rate changes affect a shrinking share of the monetary stock. The pass-through of rate changes to spending and inflation is proportionally weaker.

**3. Liquidity channel disruption**
In a banking crisis, a CB can lend domestic currency freely as LOLR. But if bank liabilities are predominantly FX, the CB cannot create FX reserves on demand — LOLR function is crippled. [LLM — standard LOLR under dollarization problem]

---

## Why Anti-Dollarization Measures Backfire

Forced de-dollarization (banning or restricting FX deposits) has a systematic failure mode:

```
Policy: Ban FX deposits in domestic banking system
→ Public cannot hold FX savings locally
→ Response: Move FX savings to:
    (a) Offshore accounts (capital flight)
    (b) FX cash holdings (mattress banking)
    (c) Real assets (property, gold)
→ Result: FX assets are still held — just outside the banking system
→ Domestic monetary base SHRINKS (FX deposits were on bank balance sheets;
   cash/offshore holdings are not)
→ Monetary control worsens, not improves
```

[RAW-BOOK IMF p.4810]

"The attempt to forcibly de-dollarize may drive deposits offshore, shrinking the domestic deposit base and worsening, not improving, the monetary control problem." [RAW-BOOK IMF p.4812]

**Successful de-dollarization path**: Not legal prohibition but:
1. Credible disinflation (stabilization program) → rebuilds domestic currency real return
2. Positive real domestic interest rates → makes domestic deposits attractive
3. Time + credibility → trust rebuilds gradually over 5-10 years
4. Financial deepening → more domestic instruments available as FX alternatives

**Country examples of gradual success**: Peru (1990s-2000s): dollarization ratio fell from ~60% to ~30% over 15 years of credible IT + financial development, NOT through restrictions. [LLM — standard case, consistent with IMF framework]

---

## FX Regime Interaction

The exchange rate regime directly affects dollarization dynamics:

| Regime | Dollarization tendency | Mechanism |
|--------|----------------------|-----------|
| **Hard peg / currency board** | Stabilizes or reduces dollarization | Credibility eliminates FX risk; domestic currency trusted |
| **Managed float** | Moderate dollarization | Some FX risk → partial hedging via FX deposits |
| **Free float (low credibility)** | High dollarization | Large FX swings → FX deposits as insurance |
| **Free float (high credibility/IT)** | Low and declining | Stable purchasing power → domestic deposits adequate |

[LLM — from IMF framework and standard open economy macro]

For EMEs: the relationship is non-linear. A highly credible IT framework with a freely floating currency can achieve lower dollarization than a managed float. But a managed float with a history of large devaluations generates MORE dollarization than a hard peg, because FX deposits protect against the risk of a future peg collapse.

---

## Monetary Survey Implications

When computing monetary aggregates in dollarized economies, the IMF recommends:

```
Narrow M:  Exclude FX deposits (pure domestic liquidity measure)
Broad M2:  Include FX deposits at current exchange rate

If the CB targets M2:
  - Changes in FX rate mechanically change M2 even if no new deposits
  - A devaluation → FX deposits worth more in domestic currency → M2 jumps
  - CB must account for "valuation effect" in M2 targeting

If CB targets base money (H):
  - FX deposit swings are exogenous to the RM target
  - Large dollarization → M2 becomes unreliable policy anchor
```

[RAW-BOOK IMF p.4815]

The valuation effect means that a devaluation under high dollarization creates an **automatic monetary loosening** (M2 rises mechanically) even if the CB does nothing — amplifying the inflationary effect of devaluation and creating a perverse feedback loop with FX-indexed debt. [connects to [[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]]
