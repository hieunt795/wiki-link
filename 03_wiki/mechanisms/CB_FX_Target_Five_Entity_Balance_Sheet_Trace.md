---
node_id: cb_fx_target_five_entity_balance_sheet_trace_001
type: mechanism
title: CB FX Target — Five-Entity Combined Balance Sheet Trace (T-Account Scenarios)
aliases:
- FX target combined balance sheets
- five-entity T-account FX
- dual deterioration T-account
- quasi-fiscal T-account trace
- bảng cân đối kết hợp dưới tỷ giá mục tiêu
- truy tài khoản T xuyên suốt năm thực thể
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- balance_sheet
- t_account
- fx_intervention
- sterilization
- dual_deterioration
- monetary_survey
- flow_of_funds
- quasi_fiscal
- crowding_out
- em_policy
confidence: 3
stability: stable
thesis: 'Every FX intervention and sterilization operation propagates simultaneously
  across five balance sheets — CB, DMBs, Government, Private sector, and External
  — linked by three accounting identities (RM = NFA + NCG + Cb + OINm; M2 = NFA +
  NDC + OINb; (Sp−Ip) + (Sg−Ig) = CAB). The critical diagnostic insight is that M2
  and RM remain stable in appearance throughout the buildup phases (sterilization
  cancels the FX effect), while the actual stress accumulates in the structure of
  M2: NFA/M2 falling, NCG/M2 rising, CPS/M2 falling. Dual deterioration — NFA↓ + NCG↑
  simultaneously in the same period — is the leading signal of a regime under maximum
  stress, visible from the CB balance sheet before it manifests as crisis.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'Box 5.2 (MA balance sheet analytical form), Box 5.7 (Monetary Survey consolidated:
    M2 = NFA + NDC + OINb), Box 6.4 Eq.6 (ΔM2 = ΔNFA + ΔNDC + ΔOINb), Box 6.4 Eqs.2–5
    (government, private, banking, external sector identities), p.4572–4578 (M2 decomposition
    by component), p.1841 (recapitalization fiscal treatment), p.2288 (quasi-fiscal
    taxonomy), p.3745 (Greenspan-Guidotti NFA/RM floor)'
  weight: primary
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: 'lines 2694–2710 (depreciation defense T-account), lines 2720–2728 (sterilization
    quasi-fiscal cost), lines 2745–2753 (NCG + NFA dual deterioration mechanism),
    lines 2771–2792 (Bulgaria 1994–96: NFA +12.1 → −234.5, hyperinflation sequence)'
  weight: primary
parent_node: null
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: identity_foundation
- node: '[[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]'
  relation: flow_of_funds_framework
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: upstream_mechanism
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: quasi_fiscal_channel
- node: '[[FX_Target_Quasi_Fiscal_Stagflation_Trap_Mechanism]]'
  relation: macro_outcome
date_created: '2026-05-25'
date_updated: '2026-05-25'
steps:
- 'Step 1: Every FX intervention and sterilization operation propagates simultaneously across five balance sheets — CB, DMBs, Government, Private sector, and External — linked by three accounting identities (RM = NFA + NCG + Cb + OINm'
- 'Step 2: (Sp−Ip) + (Sg−Ig) = CAB). The critical diagnostic insight is that M2 and RM remain stable in appearance throughout the buildup phases (sterilization cancels the FX effect), while the actual stress accumulates in the structure of M2: NFA/M2 falling, NCG/M2 rising, CPS/M2 falling. Dual deterioration — NFA↓ + NCG↑ simultaneously in the same period — is the leading signal of a regime under maximum stress, visible from the CB balance sheet before it manifests as crisis'

---

## Accounting Identities — Three Must Hold Simultaneously

```
[ID-1] CB:      RM  = NFA + NCG + Cb + OINm       [RAW-BOOK IMF Macro Box 5.2]
[ID-2] Survey:  M2  = NFA + NDC + OINb             [RAW-BOOK IMF Macro Box 5.7]
                NDC = NCG + CPS
                ΔM2 = ΔNFA + ΔNDC + ΔOINb         [RAW-BOOK IMF Macro Box 6.4 Eq.6]
[ID-3] FoF:     (Sp − Ip) + (Sg − Ig) = CAB        [RAW-BOOK IMF Macro Box 6.4]
                CAB + FDI + NFB − ΔNFA = 0
```

The banking sector has zero real saving-investment balance by convention —
its only role is financial intermediation between sectors. [RAW-BOOK IMF Macro p.5503]

---

## SCENARIO A — Inflow + Full Sterilization (Appreciation Defense)

**Step 1 — FX intervention (CB buys FX):**

```
CB:      NFA +ΔF │ RM +ΔF          M2 = +ΔF before sterilization
EXT:     ΔNFA −ΔF                  (ROW loses reserves)
```

**Step 2 — Sterilization (CB issues T-bills, absorbs RM):**

```
CB:      NFA +ΔF │ RM    ≈ 0       OINm ↓ by ΔF (T-bills issued)
         OINm −ΔF│

Monetary Survey:
  ΔM2 = +ΔF (ΔNFA) + 0 (ΔNDC) − ΔF (ΔOINb) = 0  ✓
  M2 UNCHANGED — but NFA higher, OINb lower

DMBs: absorb CB T-bills → liquid assets shift from reserves to T-bills
```

**Step 3 — Quasi-fiscal cost (ongoing, each period):**

```
CB P&L:  Earns r_f × NFA_stock
         Pays  r_d × sterilization_stock
         Net:  (r_f − r_d) × stock = NEGATIVE when r_d > r_f
               [RAW-BOOK Lipschitz p.2720]

OINm:    Declines each period as losses accumulate
CB profit transfer to Treasury: falling → turning negative
```

**Flow of Funds impact:**

```
Government (Eq.3): seigniorage revenue ↓ → deficit ↑ (if no offsetting adjustment)
                   → ΔNDCg ↑ to compensate → DMBs shift toward gov bonds → CPS↓
```

---

## SCENARIO B — Outflow + Sterilization (Depreciation Defense)

**Without sterilization — automatic adjustment:**

```
CB:      NFA −ΔF │ RM −ΔF
M2 contracts → liquidity tightens → rates↑ → demand↓ → BOP improves
[RAW-BOOK Lipschitz p.2694]
```

**With sterilization — equilibrating mechanism blocked:**

```
CB:      NFA  −ΔF │ RM   ≈ 0
         NCG  +ΔF │ (buys domestic bonds to offset RM contraction)

ΔM2 = −ΔF + ΔF + 0 = 0  ✓
M2 stable, but NFA declining, NCG rising

RESERVE DEPLETION TABLE [RAW-BOOK Lipschitz p.2704–2706]:
Period   NFA    NCG    RM    NFA/RM
T        100     50   150    0.67
T+2       60     90   150    0.40
T+4       20    130   150    0.13  ← WARNING ZONE
T+5        0    150   150    0.00  ← PEG INDEFENSIBLE

Greenspan-Guidotti breach (NFA/RM < 1.0): CB cannot redeem RM at peg
→ Rational speculative attack [RAW-BOOK IMF Macro p.3745, p.3451–3459]
```

---

## SCENARIO C — Fiscal Deficit + FX Defense (Dual Deterioration)

Government runs deficit D, financed via bank credit; CB simultaneously defends peg.

```
GOV:     Issues bonds → DMBs absorb → ΔNDCg = +D
DMBs:    Gov bonds ↑D │ CPS ↓D (crowded out — same deposit base, shifted allocation)

CB accommodation (indirect monetization):
  CB buys gov bonds from DMBs (secondary market OMO) → NCG ↑ΔF_g
  CB sells FX for peg defense → NFA ↓ΔF

CB:      NFA   −ΔF    │ RM     ≈ 0
         NCG   +ΔF    │
                +ΔF_g │ (accommodation)

Full Monetary Survey:
  ΔM2 = ΔNFA + ΔNCG + ΔCPS + ΔOINb
       = −ΔF + (ΔF + ΔF_g) + (−D) + 0
       = ΔF_g − D

  If ΔF_g = D: ΔM2 = 0  → "stable monetary conditions" CONCEALING:
    NFA↓↓, NCG↑↑, CPS↓↓

DUAL DETERIORATION SIGNAL:
  NFA↓ from FX defense AND NCG↑ from fiscal accommodation
  in the SAME reporting period
  "In effect, the higher government deficit is being financed by a drawdown in
   central bank reserves" [RAW-BOOK Lipschitz p.2753]
```

**Flow of Funds (all four sectors — Eq. 2–8):**

```
GOV:      (Sg − Ig) = −D;  ΔNDCg = +D;  NB = 0
PRIVATE:  (Sp − Ip) offset by −ΔCPS = +D (crowded out, investment falls)
BANKING:  ΔM2 = ΔNFA + ΔNDC + ΔOINb = 0 (identity holds)
EXTERNAL: CAD worsens → −ΔNFA = −ΔF feeds through to BOP identity ✓

Horizontal check: each row sums to zero ✓
[RAW-BOOK IMF Macro Box 6.4]
```

---

## SCENARIO D — CB Recapitalization

CB losses exhaust capital (OINm deeply negative). Government must act.

```
GOV issues recapitalization bonds NB_recap → injects equity into CB:

GOV:     Debt ↑ NB_recap (bonds issued to market or DMBs)
DMBs:    Gov bonds ↑ NB_recap (absorbed — further crowds out CPS)
CB:      OINm ↑ NB_recap (equity restored)

CB post-recap:
  NFA  unchanged │ RM    unchanged
  NCG  ↑NB_recap │ OINm  restored to 0

FISCAL TREATMENT [RAW-BOOK IMF Macro p.1841]:
  Conventional GFS deficit: only future interest on NB_recap flows
  True fiscal cost: PV of all future interest = NB_recap (full stock)
  → Recap concealed from headline deficit; shows only as future interest expense

DMB impact: gov bond portfolio ↑↑↑ → CPS ↓↓↓ → crowding out WORST at this stage
```

---

## SCENARIO E — Crisis + Forced Float (Outcome B: Uncontrolled)

```
NFA → 0; speculative attack exhausts remaining reserves instantly
[RAW-BOOK IMF Macro p.3459 — Krugman mechanism: attack precedes actual exhaustion]

Post-attack CB balance sheet:
  NFA  →0   │ RM  unchanged initially
  NCG  ↑↑↑  │ (CB must print to fund gov + LOLR for banks)

ΔM2 = 0 (ΔNFA) + ↑↑↑ (ΔNCG) + ↓ (ΔOINb from bank losses) = ↑↑↑ NET
→ M2 explosion → hyperinflation

Bulgaria 1994–96:
  NFA: +12.1 → −234.5 billion lev over 2 years
  NCG: expanding to compensate → RM ≈ stable until attack
  Post-attack: hyperinflation + economic collapse → currency board July 1997
  [RAW-BOOK Lipschitz p.2771–2792]
```

---

## M2 Decomposition: Reading the Structure, Not Just the Total

```
ΔM2/M2 = (ΔNFA/NFA) × (NFA/M2)    ← FX channel weight
        + (ΔNCG/NCG) × (NCG/M2)    ← Fiscal/monetization weight
        + (ΔCPS/CPS) × (CPS/M2)    ← Private credit weight
        + (ΔOINb/OINb) × (OINb/M2) ← QF loss / valuation weight
[RAW-BOOK IMF Macro p.4572–4578]

HEALTHY regime:    NFA/M2 rising; NCG/M2 stable; CPS/M2 stable or rising
STRESS building:   NFA/M2 ↓; NCG/M2 ↑; CPS/M2 ↓ — M2 total may look fine
CRISIS precursor:  NCG/M2 dominant; NFA/M2 minimal; OINb/M2 increasingly negative

KEY INSIGHT: Total M2 and RM are lagging indicators.
The stress is visible in the composition BEFORE the total moves.
[LLM — derived from IMF decomposition identity + Lipschitz deterioration sequence]
```

---

## Scenario Summary Matrix

| Scenario | ΔNFA | ΔNCG | ΔCPS | ΔM2 | Diagnostic signal |
|----------|------|------|------|-----|-------------------|
| **A** — Inflow + sterilize | ↑ | → | ↓ (crowd) | ≈0 | OINm declining (QF cost) |
| **B** — Outflow + sterilize | ↓ | ↑ | ↓ | ≈0 | NFA/RM declining |
| **C** — Fiscal + FX defense | ↓↓ | ↑↑ | ↓↓ | ≈0 | **Dual deterioration** |
| **D** — Recapitalization | → | ↑(recap) | ↓↓ | → | Gov debt ↑; CPS worst |
| **E** — Crisis | →0 | ↑↑↑ | 0 | ↑↑↑ | Hyperinflation trigger |

**All scenarios A–D: M2 ≈ stable.** Crisis is in the structure, not the total.
