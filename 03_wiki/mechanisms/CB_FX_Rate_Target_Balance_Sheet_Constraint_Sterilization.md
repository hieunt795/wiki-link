---
node_id: cb_fx_rate_target_balance_sheet_constraint_sterilization_001
type: mechanism
title: CB FX Rate Target Balance Sheet Constraint And Sterilization
aliases:
- FX target balance sheet constraint
- sterilization mechanism
- NFA endogeneity under peg
- intervention and sterilization
- ràng buộc bảng cân đối khi target tỷ giá
- cơ chế sterilization
- can thiệp vô hiệu hóa
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- fx_intervention
- sterilization
- nfa
- nda
- reserve_money
- impossible_trinity
- managed_float
- balance_sheet
- em_policy
- capital_flows
- reserve_adequacy
confidence: 4
stability: stable
thesis: 'When a central bank targets an exchange rate (fixed peg, crawling peg, or
  managed band), NFA becomes an endogenous variable determined by BOP flows and intervention
  — not a free policy instrument. The CB retains control only over NDA. Sterilization
  (offsetting NFA changes via NDA) can preserve the monetary base target in the short
  run, but faces two binding limits: (1) reserve depletion when defending against
  depreciation, and (2) quasi-fiscal carrying costs when sterilizing appreciation-driven
  inflows. Sustained sterilization against a persistent shock is unsustainable and,
  if delayed, results in a larger eventual adjustment.

  '
source_refs:
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 2665–2730 (Section 4a: Monetary Policy and External Shocks; Box 4.7:
    Intervention and Sterilization; Table 4.8)'
  weight: primary
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: lines 2241–2244, 2353–2360 (impossible trinity, IT framework and FX)
  weight: primary
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 3699–3715 (capital flows and sterilization), lines 3723–3749 (reserve
    adequacy), lines 2465–2467 (sterilization costs exercise)
  weight: primary
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: lines 216–220 (dual targets, FX intervention as second instrument)
  weight: secondary
parent_node: null
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: identity_foundation
- node: '[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]'
  relation: external_sector_link
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: crisis_endpoint
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: policy_response_framework
- node: '[[CB_Balance_Sheet_Trilemma]]'
  relation: related_constraint
- node: '[[Policy_Trilemma_Efficiency_Frontier_Equivalence]]'
  relation: theoretical_root
date_created: '2026-05-24'
date_updated: '2026-05-24'
steps:
- 'Step 1: reserve depletion when defending against depreciation, and'
- 'Step 2: quasi-fiscal carrying costs when sterilizing appreciation-driven inflows. Sustained sterilization against a persistent shock is unsustainable and, if delayed, results in a larger eventual adjustment'

---

## The Root Constraint: NFA Becomes Endogenous

Under the reserve money identity:

```
RM = NFA + NCG + Cb + OIN
M2 = NFA + NDA
```

When a central bank **freely chooses its balance sheet**, NFA is a policy variable — the CB buys or sells FX reserves at will to hit monetary targets.

When a central bank **commits to an exchange rate target** (any form: fixed peg, crawling peg, managed band), the causation reverses: NFA is *determined* by BOP flows and the intervention obligation. The CB must buy or sell whatever FX the market brings to maintain the target rate. NFA is no longer freely set — it is endogenous.

This leaves the CB with **one degree of freedom: NDA**. The CB can change NDA (via OMO, reserve requirements, lending facilities) to offset unwanted effects on RM. This offsetting operation is called **sterilization**. [RAW-BOOK Lipschitz p.2710–2718]

The impossible trinity formalizes this constraint: a central bank cannot simultaneously maintain (1) a fixed exchange rate, (2) open capital account, and (3) independent monetary policy. Any attempt to achieve all three will fail. [RAW-BOOK Lipschitz p.2241–2244]

---

## Intervention Mechanics: Two Directions

### Case A — Defending Against Depreciation (selling FX)

**Trigger:** BOP deficit, capital outflows, excess demand for foreign currency → domestic currency faces depreciation pressure.

**Intervention:** CB sells FX reserves → receives domestic currency → NFA ↓, RM ↓.

```
CB Balance Sheet (sell FX):
  Assets            Liabilities
  NFA       ↓       Reserve Money  ↓
```

**Without sterilization:** RM contracts → domestic liquidity tightens → interest rates rise → some equilibrating adjustment occurs (higher rates attract inflows, slow domestic demand, reduce imports). This is the market's equilibrating mechanism at work. [RAW-BOOK Lipschitz p.2694]

**With sterilization:** CB simultaneously buys domestic securities (NDA ↑) to reverse the RM contraction.

```
CB Balance Sheet (sell FX + sterilize):
  Assets            Liabilities
  NFA       ↓       Reserve Money  ≈ unchanged
  NCG/Cb    ↑
```

Effect: exchange rate defended, RM unchanged, but FX reserves depleted. No equilibrating adjustment occurs. [RAW-BOOK Lipschitz p.2696]

**Binding limit:** Sterilized intervention against a persistent outflow shock becomes unsustainable when reserves approach a critical minimum. As NFA falls, market confidence erodes, risk premia rise, outflows accelerate — a self-reinforcing dynamic that eventually forces abandonment of the peg. [RAW-BOOK Lipschitz p.2704–2706]

---

### Case B — Defending Against Appreciation (buying FX)

**Trigger:** BOP surplus, capital inflows, excess supply of foreign currency → domestic currency faces appreciation pressure.

**Intervention:** CB buys FX → pays domestic currency → NFA ↑, RM ↑.

```
CB Balance Sheet (buy FX):
  Assets            Liabilities
  NFA       ↑       Reserve Money  ↑
```

**Without sterilization:** RM expands → monetary conditions ease → inflation rises → real appreciation occurs anyway via price level increase rather than nominal exchange rate change.

**With sterilization:** CB issues securities or absorbs liquidity (NDA ↓) to offset RM expansion.

```
CB Balance Sheet (buy FX + sterilize):
  Assets            Liabilities
  NFA       ↑       Reserve Money  ≈ unchanged
  NCG/OIN   ↓  (via T-bill issuance, OMO absorption)
```

Effect: reserves accumulated, RM stable, inflation contained. [RAW-BOOK Lipschitz p.2728]

**Binding limit for sterilizing inflows:** The CB buys *low-yield foreign assets* (typically USD T-bills) while *issuing higher-yield domestic assets* to sterilize. The interest differential is a direct quasi-fiscal cost:

```
Sterilization cost per period =
  r_domestic × sterilization_stock − r_foreign × NFA_accumulated
```

For typical EM (r_domestic > r_foreign): sterilization is loss-making. "Such sterilization can be costly. It entails, in effect, buying low-yield foreign exchange assets (usually US Treasury bills) and selling relatively high-yield domestic assets... thus the sterilization operation reduces the profits (or increases the losses) of the central bank, and reduces (increases) its transfers to (calls on) the government budget." [RAW-BOOK Lipschitz p.2720]

Governments are "usually loath to allow such policies to continue indefinitely." [RAW-BOOK Lipschitz p.2720]

---

## The Sterilization Decision: Four Considerations

| Factor | Description |
|--------|-------------|
| **Shock assessment** | Is the BOP shock temporary or permanent? Sterilization is appropriate for transitory shocks — it buys time for equilibrating adjustments. For permanent shocks, sterilization delays but worsens the eventual adjustment. [RAW-BOOK Lipschitz p.2702] |
| **Reserve buffer** | For depreciation defense: how much FX reserves remain? Once reserves hit a critical floor, intervention must stop — often well before actual depletion, as declining reserves signal vulnerability and attract speculative attacks. [RAW-BOOK Lipschitz p.2706] |
| **Quasi-fiscal cost** | For appreciation defense: interest differential × sterilization volume = recurring CB loss. These reduce seigniorage transfers to government, becoming a fiscal drain. If sustained, government may force the CB to stop. [RAW-BOOK Lipschitz p.2720] |
| **Second-round effects** | Higher domestic rates (from sterilization absorption) attract more capital inflows → more FX purchases needed → more sterilization needed. A positive feedback loop that can make full sterilization impossible. [RAW-BOOK Perry p.267] |

---

## Balance Sheet Trajectory Under Persistent Misalignment

The Lipschitz & Schadler model traces what happens when a CB sterilizes against a *sustained* shock — a BOP deficit combined with fiscal expansion:

**Period 1:** CB sells FX, sterilizes → NFA ↓, NDA ↑, RM stable.
**Period 2:** Same again → NFA ↓↓, NDA ↑↑, RM stable.
**Period n:** "NFA would reach a critical minimum, intervention would no longer be possible, and confidence in the currency would be eroded to the point where risk premia would rise. Financial outflows would then add to exchange market pressure." [RAW-BOOK Lipschitz p.2704]

The diagnostic signal visible *before* crisis: **NFA declining steadily while NDA rising** — same RM, but backed increasingly by domestic claims rather than hard currency. This is a red flag in any CB balance sheet analysis.

**Bulgaria 1994–1996** is the canonical case study. The BNB balance sheet shows NFA collapsing from +12.1 to −234.5 (billion lev) in two years, with NDA expanding to compensate. Hyperinflation and currency collapse followed, ending only with a currency board in July 1997. [RAW-BOOK Lipschitz p.2771–2792]

---

## Exchange Rate Regimes — Constraint Strength

| Regime | NFA Endogeneity | Sterilization Need | Policy Independence |
|--------|----------------|--------------------|---------------------|
| **Hard peg / Currency board** | Full — CB must intervene to maintain exact parity | Not available (NDA fixed too) | Zero |
| **Crawling peg** | Near-full — CB defends the crawl path | Possible but limited by crawl commitment | Minimal |
| **Managed band** | Partial — CB defends only when rate hits band edge | Available within band; sterilization buys time | Moderate within band |
| **Dirty float / lean-against-wind** | Discretionary — CB chooses intervention scale | Full flexibility | High |
| **Pure float** | Zero — NFA fully controlled by CB | No sterilization needed (no intervention) | Full |

For a **currency board**, the constraint is maximally binding: NDA is also endogenous — the board is legally required to back RM 1:1 with foreign assets. Monetary policy is literally absent. The Greenspan-Guidotti rule (NFA/RM ≥ 1) is the credibility threshold for currency boards; falling below it signals potential peg abandonment. [RAW-BOOK IMF p.3745]

For a **managed band** (e.g., ±5% around a center rate): the CB has discretion within the band — NDA is a genuine policy instrument for monetary management. At the band edges, the FX-target constraint becomes binding and sterilization is required to prevent the rate from piercing the band. [RAW-BOOK IMF p.3802]

---

## Reserve Adequacy Interaction

The CB's ability to defend a peg depends on the stock of FX reserves relative to potential claims:

**Traditional rule:** ≥ 3 months of imports (evolved when capital controls were extensive). [RAW-BOOK IMF p.3729]

**Capital-account-open rule (Greenspan-Guidotti):** NFA / RM ≥ 1 — reserves must cover the full monetary base to credibly defend a fixed peg. [RAW-BOOK IMF p.3745]

**Modern IMF ARA metric:** Composite measure weighting exports, M2, short-term debt, portfolio liabilities — calibrated to the specific capital account openness of the country.

Key insight: "At a fundamental level, the credibility of the authorities' economic policies and the confidence that market participants place in them are key to assessing the adequacy of reserves. Indeed, it is credible policies that allow the authorities to augment reserves by borrowing abroad at favourable terms." [RAW-BOOK IMF p.3725]

Reserves are not sufficient on their own — credibility of the broader macro framework determines whether even moderate reserves can sustain a peg.

---

## The Mundell-Fleming Policy Implication

Under a fixed exchange rate with open capital account, **monetary policy is ineffective**:

- CB lowers rates → capital outflows → FX pressure → CB must sell reserves (or let exchange rate depreciate)
- To maintain fixed rate: CB must reverse rate cut → monetary policy self-cancels
- NFA change = −ΔM (money supply changes endogenously to maintain external balance)

Fiscal policy, by contrast, is highly effective under fixed rates: higher government spending attracts foreign financing at the fixed interest rate, with no crowding-out via interest rates. [RAW-BOOK Lipschitz p.2371–2377]

This Mundell-Fleming result is the macroeconomic expression of the same balance-sheet constraint: **under a fixed exchange rate, the money supply is endogenous**, determined by BOP outcomes and sterilization operations, not by the CB's discretion.

---

## Dual-Instrument Resolution for EMEs

Post-GFC practice: many EM central banks operate with **two instruments** — interest rate and FX intervention — to achieve **two targets** — inflation and exchange rate stability. Ostry, Ghosh & Chamon (2012) argue this dual approach *increases* CB credibility in EMEs because FX volatility directly feeds inflation via import prices and balance sheet effects. [RAW-BOOK Perry p.220]

The FIT (Flexible Inflation Targeting) framework formalizes this: FX intervention is not seen as incompatible with inflation targeting, but as a complementary stabilization tool for managing the exchange rate channel of monetary policy transmission. Capital Flow Management (CFM) serves as a third instrument to reduce the volume of flows that require sterilization. [RAW-BOOK Perry p.291–295]

---

## Diagnostic: Reading the CB Balance Sheet for Vulnerability

The pattern to watch for:

```
HEALTHY: NFA rising (or stable), NDA managed for monetary targets → independent monetary policy
STRESS:  NFA declining, NDA rising to compensate → CB defending peg, sterilizing
CRISIS:  NFA at critical minimum, NDA at limits, RM structure deteriorating
         → peg under attack, fiscal dominance risk, potential currency crisis
```

Intervention and sterilization operations are "discernible in the central bank balance sheets. But unless they are dramatically large, it may require some persistence to disentangle them from myriad other transitory influences." [RAW-BOOK Lipschitz p.2722]
