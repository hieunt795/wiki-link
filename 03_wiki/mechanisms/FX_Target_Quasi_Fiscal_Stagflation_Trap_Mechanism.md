---
node_id: fx_target_quasi_fiscal_stagflation_trap_001
type: mechanism
title: FX Rate Target + Quasi-Fiscal Operations — Stagflation Trap Mechanism
aliases:
- FX target stagflation trap
- quasi-fiscal stagflation
- regime-structural stagflation EME
- đình lạm kiểu neo tỷ giá
- bẫy đình lạm FX target
- đình lạm cấu trúc chính sách EME
- tỷ giá mục tiêu chi phí bán tài chính đình lạm
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- stagflation
- fx_target
- quasi_fiscal
- sterilization
- fiscal_dominance
- em_policy
- policy_trap
- impossible_trinity
- fear_of_floating
- inflation_persistence
confidence: 3
stability: stable
thesis: 'Stagflation under an FX rate target is regime-structural, not shock-driven:
  the FX commitment simultaneously generates persistent inflation (by disabling the
  exchange rate as a cost-push shock absorber and enabling monetary accommodation)
  and suppresses growth (via quasi-fiscal drain on fiscal space, crowding out of private
  credit, and elevated domestic interest rates from sterilization). The trap is self-reinforcing:
  sterilization costs accumulate as quasi-fiscal losses, eroding seigniorage transfers
  to government, which must either cut spending (deepening stagnation) or accommodate
  via NCG expansion (deepening inflation). Fear of floating locks both channels shut
  simultaneously. Policy cannot solve inflation and stagnation with the same instrument
  when that instrument is neutered by the FX commitment.

  '
source_refs:
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 2241–2244 (impossible trinity), lines 2371–2377 (Mundell-Fleming:
    monetary policy ineffective under fixed FX), lines 2694–2728 (sterilization mechanics
    and quasi-fiscal cost), lines 2730–2763 (fiscal dominance: no scope for independent
    monetary policy), lines 2753 (dual deterioration: NFA↓ + NCG↑), lines 2757 (fiscal
    dominance vicious circle), lines 3693–3814 (fear of floating, FX mismatch buildup)'
  weight: primary
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 878–927 (four inflation types: cost-push, inertial), lines 1941–1945
    (four deficit financing modes → four crisis types), lines 2280–2292 (Box 3.7 quasi-fiscal
    operations taxonomy), lines 3451–3459 (speculative attack under fixed peg, Krugman
    1979), lines 4867 (inertial inflation definition)'
  weight: primary
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: 'lines 265–273 (offset coefficient α=0.7, sterilization coefficient β=0.5,
    Indonesia 2000–2010: α > β → net loss of monetary autonomy), lines 289–293 (sterilization
    cost of reserve accumulation)'
  weight: supporting
parent_node: null
related:
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: upstream_mechanism
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: quasi_fiscal_channel
- node: '[[Fear_Of_Floating_Stagflation_Amplifier_Mechanism]]'
  relation: lock_in_mechanism
- node: '[[Stagflation_Regime_Diagnostic_Framework]]'
  relation: regime_classification
- node: '[[Heterodox_Stabilization_Three_Element_Program]]'
  relation: exit_path
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: quantifies_monetary_autonomy_loss
- node: '[[Imf_Macro_Crisis_Vector_Framework]]'
  relation: crisis_vector_context
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## What Makes This Stagflation Regime-Structural

Classical stagflation (1970s) originates from an external supply shock hitting an economy
with full monetary flexibility. The CB faces a genuine tradeoff: fight inflation (tighten,
accept more unemployment) or support growth (ease, accept more inflation).

FX-target stagflation has no such tradeoff — it is a **policy trap** where the CB cannot
move in either direction without triggering a different crisis:

```
Fight inflation (rate hike)?
  → Capital inflows increase (rate differential widens)
  → Appreciation pressure → CB must buy more FX
  → NFA↑, RM↑ → monetary easing effect offsets the hike
  → Net effect: near-zero monetary tightening [RAW-BOOK Lipschitz p.2371]
  → AND: quasi-fiscal cost of sterilizing the new inflows rises further

Support growth (rate cut)?
  → Capital outflows (rate differential narrows or reverses)
  → Depreciation pressure → CB must sell FX
  → NFA↓ → reserves deplete
  → Fear of floating: depreciation would trigger banking insolvencies
  → Rate cut blocked [LLM — derived from Lipschitz p.3693–3814 fear mechanism]

Indonesia evidence:
  Offset coefficient α = 0.7: 70% of every CB tightening action was offset
  by induced capital inflows [RAW-BOOK Perry p.269]
  → A 100bp rate hike delivered only 30bp of effective domestic tightening
  → Sterilization of the induced inflows added further quasi-fiscal cost
```

---

## Three Transmission Pathways

### Pathway 1 — External Shock Pass-Through (Inflation)

Under FX target, exchange rate cannot serve as shock absorber:

```
Commodity price↑ / Import cost↑ (external cost-push):
  Floating rate → currency appreciation → import prices in local currency fall
                → Shock partly absorbed, CPI impact smaller

  FX target     → CB prevents appreciation (buys FX) AND prevents depreciation
                → Import prices pass through fully to domestic CPI
                → [RAW-BOOK IMF Macro p.878–927]: cost-push → inertial inflation
                  "a change in the relative price of a key good can initiate a process
                   that leads to generalized inflation" [RAW-BOOK IMF Macro p.878]
                → Wage contracts index to past CPI → spiral embeds
```

### Pathway 2 — Quasi-Fiscal Drain (Stagnation)

```
Sterilization of inflows:
  CB earns r_f on FX reserves, pays r_d on sterilization instruments
  QF cost per period = (r_d − r_f) × sterilization_stock  [RAW-BOOK Lipschitz p.2720]

  Four channels draining growth simultaneously:
  ① Fiscal channel: seigniorage transfer to Treasury falls → government cuts spending
                    OR borrows more → crowding out private credit
  ② Credit channel: sterilization absorbs DMB liquidity → lending rates elevated
                    → Investment↓ [RAW-BOOK IMF Macro p.1943 Mode 4]
  ③ Offset-feedback: rate hike → more inflows → more sterilization needed (higher α)
                     [RAW-BOOK Perry p.269]
  ④ Real wage squeeze: nominal wages suppressed, inflation persists → real wages↓
                       → Consumption↓ [LLM — derived from channels 1+2 interaction]
```

### Pathway 3 — Fiscal Dominance Endpoint (Both Simultaneously)

```
Sustained Pathway 1+2 → CB balance sheet deteriorates:
  NFA↓ (FX defense draining reserves)
  NCG↑ (CB accommodating fiscal deficit to prevent rate spike)
  → DUAL DETERIORATION: "NFA declining steadily while NDA rising"
    [RAW-BOOK Lipschitz p.2704]
    → Same RM, same M2 — but backing quality deteriorating

  At fiscal dominance: "there is no scope for independent monetary policy"
    [RAW-BOOK Lipschitz p.2757]
  → Rate held below neutral → inflation unanchored (Pathway 1 accelerates)
  → Government forced to cut spending (reserves near critical minimum)
     → stagnation accelerates
  → "vicious circle of self-perpetuating depreciation, increasing inflation,
     and rising inflation expectations" [RAW-BOOK Lipschitz p.2757]
```

---

## Self-Reinforcing Dynamic

```
Sterilization costs↑ → CB losses↑ → seigniorage to Treasury↓
    ↓
Treasury: cut spending (growth↓) OR borrow more (NCG↑ → monetization → inflation↑)
    ↓
Either route → (a) stagnation deepens OR (b) inflation deepens
    ↓
Fear of floating: cannot adjust exchange rate → neither channel resolved
    ↓
Sterilization costs↑ further (larger NFA stock, larger QF carry loss)
    ↓ [loop]
```

The loop ends only via external shock (sudden stop → forced float) or
deliberate policy regime change (three-element heterodox program).
[LLM — derived from Lipschitz p.2757–2792 full sequence]

---

## Differential Diagnosis: FX-Type vs Classical Stagflation

| Dimension | Classical (supply shock) | FX-Target Type |
|-----------|--------------------------|----------------|
| **Inflation source** | External supply shock | Cost-push pass-through + covert monetization |
| **CB constraint** | Tradeoff: can choose | Lock: cannot move either way |
| **Growth channel** | Real income squeeze from costs | Crowding out + fiscal drain + high rates |
| **Duration** | Shock-dependent (ends when shock passes) | Regime-dependent (persists until regime changes) |
| **Policy exit** | Volcker-style tightening | Regime change: FX adjustment + fiscal + incomes policy |
| **Self-reinforcing?** | Partially (wage-price spiral) | Fully (QF costs → fiscal drain → monetization) |
| **Historical case** | US/EU 1973–1982 | Bulgaria 1994–96 (extreme); generic EME fear-of-floating |

---

## Diagnostic: CB Balance Sheet Signals

```
EARLY WARNING (6–18 months before visible stagflation):
  NFA/RM ratio: declining toward 1.0 [RAW-BOOK IMF Macro p.3745]
  CB profit transfer to Treasury: YoY decline [RAW-BOOK Lipschitz p.2948]
  OMO absorption stock / GDP: rising [RAW-BOOK Perry p.293]
  NCG/M2 share: rising quarter-over-quarter [RAW-BOOK IMF Macro p.4572]

CRISIS PRECURSOR (concurrent signals):
  NFA↓ AND NCG↑ simultaneously = DUAL DETERIORATION [RAW-BOOK Lipschitz p.2753]
  CPS/M2 share falling = crowding out of private credit
  Policy rate below neutral despite inflation above target = fiscal dominance emerging

STAGFLATION CONFIRMATION:
  CPI > target (persistent, not one-off) AND
  GDP growth < potential AND
  Both of the above with no policy instrument free to address either
```
