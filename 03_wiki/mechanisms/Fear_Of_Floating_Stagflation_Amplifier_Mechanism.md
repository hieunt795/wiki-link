---
node_id: fear_of_floating_stagflation_amplifier_001
type: mechanism
title: Fear-Of-Floating As Stagflation Amplifier — FX Exposure Lock-In
aliases:
- fear of floating stagflation
- FX mismatch policy lock
- unhedged FX exposure policy trap
- stagflation amplifier FX regime
- sợ thả nổi và bẫy đình lạm
- khuếch đại đình lạm qua rủi ro tỷ giá
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- fear_of_floating
- stagflation
- fx_mismatch
- balance_sheet_crisis
- em_policy
- fx_intervention
- monetary_autonomy
- policy_trap
confidence: 4
stability: stable
thesis: 'Fear of floating — the authorities'' inability to allow exchange rate depreciation
  because unhedged FX exposures in banking and nonbank sectors would trigger mass
  insolvencies — converts a standard BOP adjustment problem into a stagflation trap.
  The CB is locked: cannot depreciate (banking collapse), cannot raise rates freely
  (growth collapses), cannot cut rates (reserves bleed). Inflation persists because
  the FX channel is disabled as a shock absorber; growth stagnates because monetary
  and fiscal space is consumed by peg defense. The mechanism is self-reinforcing:
  the longer the peg is defended, the larger the unhedged FX exposure buildup, and
  the higher the eventual cost of adjustment.

  '
source_refs:
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 3693–3814 (Chapter 6 Section 3: Anatomy of an EM Balance Sheet Crisis
    — fear of floating, FX mismatch buildup, implicit guarantee, malign configuration)'
  weight: primary
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 2241–2244 (impossible trinity), lines 2371–2377 (Mundell-Fleming:
    monetary policy ineffective under fixed FX + open CA)'
  weight: primary
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 3451–3459 (Krugman 1979: speculative attack mechanism), lines 878–927
    (cost-push inflation persistence)'
  weight: supporting
parent_node: '[[FX_Target_Quasi_Fiscal_Stagflation_Trap_Mechanism]]'
related:
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: source_concept
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: constraint_mechanism
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: fiscal_cost_companion
- node: '[[Stagflation_Regime_Diagnostic_Framework]]'
  relation: regime_outcome
- node: '[[FX_Target_Quasi_Fiscal_Stagflation_Trap_Mechanism]]'
  relation: component_of
date_created: '2026-05-25'
date_updated: '2026-05-25'
steps:
- 'Step 1: Fear of floating — the authorities'' inability to allow exchange rate depreciation because unhedged FX exposures in banking and nonbank sectors would trigger mass insolvencies — converts a standard BOP adjustment problem into a stagflation trap. The CB is locked: cannot depreciate (banking collapse), cannot raise rates freely (growth collapses), cannot cut rates (reserves bleed). Inflation persists because the FX channel is disabled as a shock absorber'
- 'Step 2: growth stagnates because monetary and fiscal space is consumed by peg defense. The mechanism is self-reinforcing: the longer the peg is defended, the larger the unhedged FX exposure buildup, and the higher the eventual cost of adjustment'

---

## The Lock-In Mechanism: From Peg Defense to Stagflation

Fear of floating begins as a balance sheet problem and ends as a policy paralysis:

```
BUILDUP PHASE (years 1–N under FX target):
  Limited FX flexibility → borrowers perceive implicit exchange rate guarantee
  → Borrow in FX without hedging (FX loans cheaper than local currency loans)
  → Banks fund credit expansion via short-term FX borrowing
  → FX exposure accumulates: banking sector (FX liabilities) + nonbank (FX mortgages)
  [RAW-BOOK Lipschitz p.3693–3814]

LOCK-IN POINT (trigger event: BOP pressure, sudden stop, commodity shock):
  Authorities face the depreciation option:
    IF depreciate → FX borrowers: debt service in local currency↑ → mass insolvency
                 → Bank NPL spike → capital loss → solvency crisis
                 → Government must recapitalize banks → fiscal deterioration
  → FEAR: authorities defend peg at cost of reserves rather than allowing depreciation
```

**The "malign configuration" [RAW-BOOK Lipschitz p.3814]:**

```
BENIGN: FX exposure concentrated in exporters (natural hedge)
  → Depreciation tolerable; CB can provide liquidity from reserves ✓

MALIGN: FX exposure in domestic consumers / developers / banks
  → No FX revenues to service FX debt
  → Depreciation → solvency crisis → bank runs → fiscal rescue
  → Authorities CANNOT allow depreciation regardless of macro fundamentals ✗
```

---

## How Fear of Floating Generates Stagflation

The peg defense disables both instruments of stabilization simultaneously:

**Inflation channel — FX rate cannot absorb shocks:**

```
External cost-push shock (commodity prices, import inflation):
  Floating rate: domestic currency appreciates → import prices fall → shock absorbed
  FX target (fear blocks depreciation AND appreciation):
    → Full pass-through of import cost shock into domestic CPI
    → No exchange rate buffer
    → Inertial embedding: wage contracts index to past CPI → spiral
  [RAW-BOOK Lipschitz p.2694] + [RAW-BOOK IMF Macro p.878–927]
```

**Stagnation channel — policy rate paralyzed:**

```
Mundell-Fleming under fixed FX + open capital account:
  Rate hike → capital inflows → appreciation pressure → CB must buy FX
            → NFA↑, RM↑ → easing effect cancels the hike
  Rate cut  → capital outflows → depreciation pressure → CB must sell FX
            → NFA↓, RM↓ → reserves bleed
  → Policy rate CANNOT be used for domestic stabilization [RAW-BOOK Lipschitz p.2371]

Stagnation therefore comes from:
  (a) Fiscal squeeze (quasi-fiscal costs drain government space)
  (b) Credit squeeze (sterilization → high domestic rates → investment↓)
  (c) Real sector: export sector suppressed, import-competing sector damaged
```

**Self-reinforcing dynamic:**

```
Longer peg defense → more FX exposure buildup → higher eventual adjustment cost
→ Authorities become EVEN MORE reluctant to devalue
→ Inflation persists longer without FX adjustment
→ Stagnation deepens as fiscal/credit space consumed
[LLM — derived from Lipschitz p.3693–3814 buildup mechanism]
```

---

## Policy Escape Conditions

Fear of floating is escapable only when the FX mismatch stock is reduced:

```
Pre-crisis escape (preferred):
  (1) Macroprudential: LTV caps on FX lending, capital requirements on FX liabilities
  (2) Gradual FX flexibility introduction → borrowers experience rate volatility → self-limit FX exposure
  (3) Bankruptcy reform → dispels implicit guarantee → market discipline
  [RAW-BOOK Lipschitz p.3814 — diagnostic criteria and mitigants]

Post-buildup escape (costly):
  Accept the balance sheet crisis via managed depreciation + banking sector support
  → Short-term: NPL spike, fiscal cost of bank recapitalization
  → Long-term: FX mismatch cleared → exchange rate restored as shock absorber
  → Combined with IMF program for external financing during adjustment
```

**Irreducible minimum:** Some real income loss is unavoidable once the unhedged stock
is large. The only question is whether it is taken as a managed adjustment or a
disorderly crisis. Delay increases the total cost. [LLM — policy logic from Lipschitz]
