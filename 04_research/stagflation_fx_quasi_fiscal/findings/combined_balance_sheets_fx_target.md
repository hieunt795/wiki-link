---
finding_id: stagflation_fx_qf_bs_001
title: "Kết Hợp Bảng Cân Đối Kế Toán Trong FX Rate Target — 5 Entities, 6 Scenarios"
topic_slug: stagflation_fx_quasi_fiscal
type: T_MODE_DEEP / balance_sheet_tracing
confidence: 3
status: draft
created: 2026-05-25
sources_used:
  - "[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]"
  - "[[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]"
  - "[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]"
  - "[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]"
  - "[[Imf_Macro_Crisis_Vector_Framework]]"
---

## Hệ Thống Accounting Identities — Nền Tảng

Ba identities phải đồng thời thỏa mãn ở mọi scenario:

```
[ID-1] CB Reserve Money:    RM  = NFA  + NCG  + Cb  + OINm
[ID-2] Monetary Survey:     M2  = NFA  + NDC  + OINb
                            NDC = NCG  + CPS
[ID-3] Flow of Funds:       (Sp − Ip) + (Sg − Ig) = CAB
       BOP financing:       CAB + FDI + NFB − ΔNFA = 0
       Banking:             ΔM2 = ΔNFA + ΔNDC + ΔOINb

[RAW-BOOK IMF Macro Box 5.2, Box 5.7, Box 6.4]
```

**Ký hiệu:**
```
CB = Central Bank (Monetary Authorities)
DMB = Deposit Money Banks
GOV = Government
PRIV = Private sector (nonbank)
EXT = External sector (Rest of World)

NFA  = Net Foreign Assets (CB)        NCG = Net Claims on Government (CB)
Cb   = Claims on banks (CB)           CPS = Credit to Private Sector (banking survey)
RM   = Reserve Money                  M2  = Broad Money
OINm = Other items net (CB)           OINb = Other items net (banking survey)
r_d  = domestic interest rate         r_f  = foreign interest rate
```

---

## SCENARIO 0 — BASELINE (Không Có FX Target, Floating Rate)

Trường hợp tham chiếu: CB hoạt động với đầy đủ monetary independence.

```
┌─────────────────────────────────────────────────────────────────────┐
│ CB (Monetary Authorities)                                           │
│  ASSETS              │ LIABILITIES                                 │
│  NFA  = A_f (free)   │ RM   = NFA + NCG + Cb + OINm               │
│  NCG  = A_g          │                                             │
│  Cb   = A_b          │ — CB điều chỉnh NFA tự do via FX sales/buys│
│  OINm = A_o          │ — NCG controlled (no fiscal dominance)      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ DMBs                                                                │
│  ASSETS              │ LIABILITIES                                 │
│  Reserves at CB      │ Deposits (M2 components)                    │
│  Gov bonds           │ Foreign liabilities                         │
│  CPS (loans)         │ Capital                                     │
└─────────────────────────────────────────────────────────────────────┘

Flow of Funds (Eq. 6):
  ΔM2 = ΔNFA + ΔNCG + ΔCPS + ΔOINb

  CB tự do điều chỉnh ΔCb (discount window) và ΔNCG (OMO) để target RM
  Exchange rate absorbs external shocks → NFA is chosen, not endogenous

Monetary autonomy: FULL
FX shock absorption: FULL (exchange rate moves)
Quasi-fiscal cost: ZERO (no sterilization needed)
```

---

## SCENARIO 1 — CAPITAL INFLOWS + FULL STERILIZATION (Appreciation Defense)

**Tình huống:** Dòng vốn vào lớn (FDI, portfolio), CB phải mua FX để giữ tỷ giá,
sau đó sterilize để giữ RM ổn định.

### Step 1A: FX Intervention (CB mua FX)

```
EXT → CB: ngoại tệ chạy vào
CB phải mua → NFA↑, phát hành RM↑

CB Balance Sheet — Step 1A:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          +ΔF         │ RM             +ΔF        │
│ NCG          0           │                           │
│ Cb           0           │                           │
│ OINm         0           │                           │
└──────────────────────────┴───────────────────────────┘

Monetary Survey (Step 1A — before sterilization):
  ΔM2 = +ΔF  (ΔNFA = +ΔF, ΔNDC = 0)
  → M2 mở rộng bằng đúng lượng FX mua vào

Flow of Funds:
  EXT column: ΔNFA = −ΔF (ROW loses reserves)
  CB/Banking column: ΔNFA = +ΔF, ΔM2 = +ΔF ✓
  (Eq. 8): CAB + FDI + NFB = ΔNFA → ΔNFA = +ΔF là counterpart của capital inflows
```

### Step 1B: Sterilization (CB hút lại RM)

```
CB phát hành T-bills / OMO absorption → NDA↓ (OINm↓ hoặc NCG thay đổi)
Hoặc: tăng reserve requirements → DMB deposits at CB↑, RM không đổi về cấu trúc

CB Balance Sheet — Step 1B:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          +ΔF         │ RM             ≈ 0        │
│ NCG          0           │ (T-bills issued by CB:    │
│ Cb           0           │  OINm ↓ by ΔF)            │
│ OINm         −ΔF         │                           │
└──────────────────────────┴───────────────────────────┘

Monetary Survey (Post-sterilization):
  ΔM2 = ΔNFA + ΔNDC + ΔOINb
       = +ΔF  +  0   − ΔF   = 0  ✓
  M2 unchanged, NFA higher, OINb lower

DMB Balance Sheet:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ CB T-bills   +ΔF         │ Deposits       0          │
│ (absorbed by DMBs or     │ (M2 unchanged)            │
│  directly by DMBs)       │                           │
└──────────────────────────┴───────────────────────────┘
```

### The Quasi-Fiscal Cost (Step 1C — Ongoing)

```
CB earns:  r_f × NFA_accumulated  (foreign yield on FX reserves)
CB pays:   r_d × OINm_stock       (domestic yield on sterilization instruments)

Period-by-period P&L:
  QF_cost(t) = r_d × Sterilization_stock(t) − r_f × NFA(t)
             > 0  when r_d > r_f  [RAW-BOOK Lipschitz p.2720]

Accumulated over T periods:
  Total_QF = Σ[t=1→T] (r_d − r_f) × ΔF × t
           = (r_d − r_f) × ΔF × T(T+1)/2  [LLM-E: geometric buildup]

CB P&L in Monetary Survey:
  OINm ↓↓ each period (losses accumulate in OINb/OINm)
  → At some point: OINm < 0 → CB equity negative
  → Transfers to Treasury: CB profit transfer → 0 → negative (call on Treasury)
```

**Flow of Funds impact (Eq. 3 — Government):**
```
Government receives: seigniorage = CB profit transfer ↓ (shrinking each period)
Government side: (Sg − Ig) worsens unless offsetting fiscal adjustment
If government borrows from domestic banks to compensate:
  ΔNDCg ↑ → crowding out CPS ↓ → private credit squeeze [RAW-BOOK IMF Macro p.1943]
```

---

## SCENARIO 2 — DEPRECIATION DEFENSE (Outflow + Selling FX)

**Tình huống:** BOP deficit, capital outflows, CB phải bán FX để giữ tỷ giá.

### Step 2A: CB bán FX (không sterilize)

```
CB bán FX → nhận domestic currency → NFA↓, RM↓

CB Balance Sheet:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          −ΔF         │ RM             −ΔF        │
│ NCG          0           │ (domestic money withdrawn │
│ Cb           0           │  from system)             │
│ OINm         0           │                           │
└──────────────────────────┴───────────────────────────┘

Monetary Survey:
  ΔM2 = ΔNFA + ΔNDC + ΔOINb
       = −ΔF  +  0   +  0   = −ΔF
  M2 contracts → monetary tightening automatic [RAW-BOOK Lipschitz p.2694]

DMB Balance Sheet:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ Reserves at CB  −ΔF      │ Deposits       −ΔF × mm   │
│                           │ (multiplier contraction) │
└──────────────────────────┴───────────────────────────┘

Adjustment mechanism (WITHOUT sterilization):
  RM↓ → liquidity tight → interbank rate↑ → lending rate↑
  → Investment↓, consumption↓ → domestic demand falls
  → Imports↓, BOP improves → equilibrating adjustment [RAW-BOOK Lipschitz p.2694]
  → Exchange rate pressure eases as demand falls
```

### Step 2B: CB sterilize (mua lại domestic assets để giữ RM)

```
CB simultaneously buys NCG (gov bonds from market) to offset RM contraction:

CB Balance Sheet (sterilized):
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          −ΔF         │ RM             ≈ 0        │
│ NCG          +ΔF         │ (NFA↓ offset by NCG↑)    │
│ Cb           0           │                           │
└──────────────────────────┴───────────────────────────┘

Monetary Survey:
  ΔM2 = ΔNFA + ΔNDC + ΔOINb
       = −ΔF  + ΔF   +  0   = 0  ✓
  M2 unchanged — no equilibrating adjustment via monetary channel
  FX reserves depleted, no automatic correction

WARNING SIGNAL BUILDING:
  NFA↓↓ but NCG↑↑ → same RM, same M2
  BUT: backing quality deteriorating
  → NFA/RM ratio falling toward Greenspan-Guidotti floor
  [RAW-BOOK Lipschitz p.2704–2706]
```

### Step 2C: Reserve Depletion Dynamic

```
PERIOD  NFA        NCG        RM      NFA/RM
────────────────────────────────────────────
  T     100        50         150     0.67
  T+1    80        70         150     0.53
  T+2    60        90         150     0.40
  T+3    40       110         150     0.27    ← WARNING ZONE
  T+4    20       130         150     0.13    ← CRITICAL
  T+5     0       150         150     0.00    ← PEG INDEFENSIBLE

When NFA/RM < 1.0 (Greenspan-Guidotti breach):
  CB cannot cover all RM with FX reserves
  Rational agents attack: convert RM to FX at official rate
  → Speculative attack depletes remaining reserves instantly
  [RAW-BOOK IMF Macro p.3451–3459] — Krugman 1979 mechanism
```

---

## SCENARIO 3 — FISCAL EXPANSION + FX DEFENSE SIMULTANEOUS (Dual Deterioration)

**Tình huống:** Chính phủ tăng thâm hụt TRONG KHI CB phải defend FX. Hai lực
kéo ngược nhau trên CB balance sheet.

### Combined Flow (Full T-Account Trace)

```
Government:  Runs fiscal deficit (Ig − Sg) = D > 0
             Finances via: (1) bank credit ΔNDCg, or (2) bond issuance NB
             [IMF Macro Crisis Vector Mode 4]

CB:          Defends FX target against depreciation
             → NFA↓ (selling FX) OR sterilize inflows if inflows exist
```

**Case 3A: Fiscal deficit + BOP deficit (most dangerous)**

```
GOV Balance Sheet (GFS Eq. 3):
  (Sg − Ig) + NFBg + ΔNDCg + NB = 0
  −D         +  0   + ΔNDCg + 0  = 0  →  ΔNDCg = +D  [bank credit to gov]

DMB Balance Sheet (absorbs fiscal):
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ Gov bonds    +D          │ (no new deposits created  │
│ CPS          −D          │  without new money)       │
│ (crowded out)            │                           │
└──────────────────────────┴───────────────────────────┘

CB Balance Sheet (FX defense + CB accommodation):
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          −ΔF         │ RM             ≈ 0        │
│ NCG          +ΔF + ΔF_g  │ (CB buying gov bonds from │
│ (CB buys bonds│           │  banks = indirect fiscal  │
│  from DMBs)  │           │  monetization)            │
└──────────────────────────┴───────────────────────────┘

DUAL DETERIORATION (critical diagnostic):
  NFA↓ from FX defense
  NCG↑ from fiscal accommodation
  → Both moving adversely simultaneously
  → RM stable, M2 stable — headline numbers LOOK FINE
  → But NFA/RM collapsing, NCG/M2 rising
  [RAW-BOOK Lipschitz p.2753]
```

**Monetary Survey — Full Period Trace:**

```
ΔM2 = ΔNFA + ΔNCG + ΔCPS + ΔOINb
     = −ΔF  + (ΔF + ΔF_g) + (−D)   + 0
     = ΔF_g − D

  IF ΔF_g = D (CB accommodation = fiscal deficit):
     ΔM2 = 0  → "stable monetary conditions"
     BUT: this conceals NFA↓ + NCG↑↑ + CPS↓ (crowding out)

  IF ΔF_g > D (over-accommodation):
     ΔM2 > 0  → monetary expansion → inflation
```

**Flow of Funds — All Four Sectors:**

```
(Sp − Ip) + (Sg − Ig) = CAB
  Private: (Sp − Ip) — being crowded out, investment falls → (Sp − Ip) ↑
  Govt:    (Sg − Ig) = −D (deficit)
  → CAB = (Sp − Ip) − D

  If private crowding out is incomplete → CAB worsens → more FX outflows needed
  → More reserve depletion → faster NFA decline

SECTOR INTERACTION MATRIX (Period T):
───────────────────────────────────────────────────────────────────────
Sector      S - I      FDI/NFB     ΔNDC     ΔM2/ΔNFA   Residual
───────────────────────────────────────────────────────────────────────
GOV         −D         0           +D       0           NB = 0
PRIVATE     +D − ε     0           −D+ε     0           CPS crowded
BANKING     0          0           net      ΔNFA(−)+    ΔOINb
EXTERNAL    ε          0           0        +ΔF(−)      CAD = ε
───────────────────────────────────────────────────────────────────────
ROW CHECK: Each row and column = 0 ✓
```

---

## SCENARIO 4 — STERILIZATION COST BUILDUP → CB BALANCE SHEET DETERIORATION

**Tình huống:** Nhiều năm sterilize inflows. Quasi-fiscal losses tích lũy.
CB capital erodes. Government phải recapitalize.

### Multi-Period Balance Sheet Evolution

```
Year 0 (Baseline):
CB: NFA = 100, NCG = 20, Cb = 10, OINm = +5, RM = 135
    Seigniorage transfer to GOV: +3 per year

Year 1 (Sterilization starts):
CB buys FX 30: NFA = 130, OINm = −30 + 5 = −25 (T-bills issued)
QF cost: (7% − 4.5%) × 30 = 0.75
OINm: −25 − 0.75 = −25.75
CB P&L: +0.75 loss → profit transfer to GOV: +3 − 0.75 = +2.25

Year 3 (Sterilization = 80):
QF cost: (7% − 4.5%) × 80 = 2.0/year
OINm: −80 + [capital − cumulative losses]
CB P&L: negative → profit transfer to GOV: 0

Year 5 (Sterilization = 120):
QF cost: (7% − 4.5%) × 120 = 3.0/year
OINm: deeply negative → CB EQUITY NEGATIVE
CB P&L: −3.0/year → CALLS ON GOVERNMENT BUDGET
[RAW-BOOK Lipschitz p.2728]

Government receives NEGATIVE transfer from CB:
GOV financing (Eq. 3): NFBg or ΔNDCg must cover both deficit D AND CB rescue
→ Fiscal pressure compounds: D + QF_cost → total financing need
```

### CB Recapitalization T-Account

```
Government issues bonds (NB) to recapitalize CB:

GOV:  Debt ↑ NB_recap (bonds issued)
DMB:  Gov bonds ↑ NB_recap (absorbed by banks)
CB:   OINm ↑ NB_recap (equity restored via bond injection)

CB Post-Recap:
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          unchanged   │ RM             unchanged   │
│ NCG + bonds  +NB_recap   │ OINm restored  +NB_recap  │
│ (recapitalization        │ → CB equity back to 0+    │
│  bonds on asset side)    │                           │
└──────────────────────────┴───────────────────────────┘

FISCAL IMPACT (GFS):
  Conventional deficit: only future interest on NB_recap flows (NOT the stock)
  True fiscal cost: PV(future interest) = r_d × NB_recap / r_d = NB_recap
  → Full cost concealed from headline deficit [RAW-BOOK IMF Macro p.1841]

DMB (after recap):
  Gov bond portfolio: ↑↑↑ (now holds both original bonds + recap bonds)
  Available for CPS: ↓↓↓ → crowding out WORSENS after recapitalization
```

---

## SCENARIO 5 — FISCAL DOMINANCE ENDPOINT + CRISIS RESOLUTION

**Tình huống:** NFA approaching zero, NCG maxed out. Two outcomes.

### Outcome A: IMF Program + Peg Adjustment

```
TRIGGER: NFA/RM → 0.0; parallel market premium > 10%; capital flight accelerating

STEP 1: Peg abandoned / devaluation (ΔE = depreciation of domestic currency)

CB Balance Sheet (post-devaluation revaluation):
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA in LC    +NFA × ΔE%  │ RM in LC       +NFA × ΔE% │
│ (same FX stock,          │ (RM expands from          │
│  higher LC value)        │  valuation gain on NFA)   │
└──────────────────────────┴───────────────────────────┘

Monetary Survey:
  ΔM2 = ΔNFA (valuation) + ΔNDC + ΔOINb
       = +NFA × ΔE%   + 0    + ΔOINb
  → ONE-TIME M2 expansion from devaluation → inflation spike
  → But: this clears the slate — FX no longer a constraint on monetary policy

STEP 2: Fiscal consolidation
  ΔNDCg → 0 (no more CB accommodation)
  NCG: stops expanding
  M2: now controlled via Cb (discount window) + OMO

STEP 3: Incomes policy (if inertial inflation)
  Wage norm → breaks wage-price spiral
  [RAW-BOOK IMF Macro p.1005 — three-element heterodox program]

Transition path:
  Month 1–3:  Inflation spike (FX pass-through + M2 one-time expansion)
  Month 3–6:  Inflation falls as monetary policy effective again
  Month 6–12: Growth recovers (exchange rate shock absorber restored)
  Year 1–2:   CB balance sheet gradually repaired
```

### Outcome B: Crisis (No IMF Program, Uncontrolled Float)

```
TRIGGER: Speculative attack — NFA hits zero before policy response

CB Balance Sheet (attack exhausts reserves):
┌──────────────────────────┬───────────────────────────┐
│ ASSETS       Δ           │ LIABILITIES    Δ          │
│ NFA          → 0         │ RM             unchanged  │
│ NCG          ↑↑↑ (CB     │ (CB prints to finance     │
│ must print to fund       │  government + LOLR)       │
│ LOLR + gov)              │                           │
└──────────────────────────┴───────────────────────────┘

Monetary Survey (crisis):
  ΔM2 = ΔNFA + ΔNCG + ΔOINb
       = 0    + ↑↑↑  + ↓↓↓  = ↑↑↑ NET
  M2 explodes → hyperinflationary dynamic
  [RAW-BOOK Lipschitz p.2771–2792 — Bulgaria 1994–96 case]

Banking sector:
  FX loans → NPL spike (devaluation destroys borrowers' balance sheets)
  DMB capital → negative → LOLR from CB
  Cb ↑↑↑ → RM ↑↑↑ more

Flow of Funds (crisis):
  (Sg − Ig): fiscal deficit explodes (banking rescue + tax revenue collapses)
  (Sp − Ip): private sector collapses (credit freeze, investment zero)
  CAB: swings to surplus forcibly (import collapse as economy contracts)
  → "Growth" by current account: FORCED, not healthy

Outcome: STAGFLATION → DEPRESSION + HYPERINFLATION
  Bulgaria 1994–96 path: currency board at the end
```

---

## COMBINED VIEW: Sự Truyền Dẫn Xuyên Suốt Toàn Bộ Balance Sheet System

```
ENTITY    ROLE TRONG FX TARGET REGIME        KEY VARIABLE

CB        Endogenous NFA handler             NFA/RM ratio (Greenspan-Guidotti)
          Sterilization operator             OINm (quasi-fiscal cost accumulator)
          Fiscal accommodator (indirect)     NCG (covert monetization)

GOV       Fiscal deficit driver              (Ig − Sg) = D
          Seigniorage recipient              CB profit transfer: normal → 0 → negative
          Implicit CB backstop               Recapitalization: NB_recap

DMBs      Fiscal deficit absorber           Gov bond portfolio / CPS tradeoff
          FX exposure creator               FX loans to PRIV (fear-of-floating source)
          Credit channel transmitter        CPS → investment → growth

PRIV      Credit recipient (crowded out)    CPS availability
          FX exposure holder (unhedged)     FX loan stock (fear-of-floating trigger)
          Wage setter                        Wage-price spiral or restraint

EXT       Capital flow source               Inflows → sterilization need
          Import price setter               Commodity prices → cost-push
          Speculative attack trigger        Shadow rate > peg → attack

INTERACTION MAP:
EXT shock → CB NFA pressure → Sterilization → GOV fiscal drain → DMB crowding
                            OR reserve depletion → NCG expansion → monetization
PRIV FX exposure → Fear of floating → CB cannot devalue → inflation unresolved
GOV fiscal expansion → NCG ↑ → CB accommodation → RM ↑ → M2 ↑ → inflation
All three simultaneously → STAGFLATION TRAP
```

---

## Diagnostic Bảng Cân Đối — Đọc Tín Hiệu Từ Monetary Survey

### Công Thức Giám Sát

```
SIGNAL 1 — Dual Deterioration (P3 precursor):
  ΔNFA < 0  AND  ΔNCG > 0  in same period
  → NFA falling from FX defense
  → NCG rising from fiscal accommodation
  → RM stable: headline CONCEALS the crisis
  Test: ΔRM = ΔNFA + ΔNCG + ΔCb + ΔOINm
        IF ΔRM ≈ 0 but ΔNFA < 0 and ΔNCG > 0 → DUAL DETERIORATION [RAW-BOOK Lipschitz p.2753]

SIGNAL 2 — Quasi-Fiscal Drain:
  OINm trend: declining quarter-over-quarter
  CB profit transfer to GOV: YoY decline
  Test: Seigniorage = r_asset × Assets − r_liab × Liabilities
        IF seigniorage < 0 → CB calling on Treasury [RAW-BOOK Lipschitz p.2720]

SIGNAL 3 — Crowding Out:
  ΔCPS / ΔM2: declining ratio (private credit growing slower than M2)
  ΔNDCg / ΔNDC: rising share of government in total bank credit
  Test: CPS/M2 declining + NCG/M2 rising → fiscal crowding out [RAW-BOOK IMF Macro p.4572]

SIGNAL 4 — Reserve Adequacy:
  NFA / RM: approaching 1.0 (Greenspan-Guidotti threshold)
  M2 / NFA: rising (increasing financial vulnerability)
  Test: IF NFA/RM < 1.0 → CB cannot cover monetary base with FX [RAW-BOOK IMF Macro p.3745]

SIGNAL 5 — Full Stagflation Confirmation:
  All four signals simultaneously:
  ΔNFA < 0, ΔNCG > 0, CPS/M2 ↓, NFA/RM < 1.5 AND:
  CPI > target AND GDP growth < potential
  → STAGFLATION TRAP CONFIRMED [LLM-E composite]
```

### M2 Decomposition — Nguồn Gốc Lạm Phát

```
ΔM2/M2 = (ΔNFA/NFA) × (NFA/M2)     ← FX channel
        + (ΔNCG/NCG) × (NCG/M2)     ← Fiscal/monetization channel
        + (ΔCPS/CPS) × (CPS/M2)     ← Private credit channel
        + (ΔOINb/OINb) × (OINb/M2)  ← Quasi-fiscal/valuation channel
[RAW-BOOK IMF Macro p.4572–4578]

Dưới FX target + quasi-fiscal stress:
  NFA/M2 weight: shrinking (NFA depleting) → FX channel contribution falling
  NCG/M2 weight: rising → fiscal channel increasingly drives M2
  CPS/M2 weight: falling (crowded out)
  OINb/M2: increasingly negative (QF losses)

INFLATION SOURCED TỪNG STAGE:
  Stage 1: NFA channel (inflow-driven M2 expansion, incomplete sterilization)
  Stage 2: NCG channel (fiscal monetization) + import cost-push
  Stage 3: NCG channel dominant + OINb deterioration → unanchored
```

---

## Summary: Kết Hợp Bảng Cân Đối — 6 Scenarios

| Scenario | NFA | NCG | CPS | RM | M2 | Inflation | Growth |
|----------|-----|-----|-----|----|----|-----------|--------|
| 0 — Baseline (float) | Free | Controlled | Free | Targeted | Targeted | Managed | Free |
| 1 — Inflow + sterilize | ↑ | → | crowded | → | → | Cost: QF loss | via crowding |
| 2 — Outflow + sterilize | ↓ | ↑ | ↓ | → | → | Import cost-push | ↓ credit |
| 3 — Fiscal + FX defense | ↓↓ | ↑↑ | ↓↓ | → | concealed | ↑ via NCG | ↓↓ crowding |
| 4 — QF drain + recap | → | ↑ (recap) | ↓ | → | → | NCG-driven | ↓ crowding |
| 5A — IMF exit | valuation ↑ | → 0 | freed | spike→normalize | spike | spike→fall | recovers |
| 5B — Crisis | → 0 | ↑↑↑ | 0 | ↑↑↑ | ↑↑↑ | hyperinflation | collapse |

**Tất cả Scenarios 1–4: RM và M2 đều "ổn định" trên bề mặt — tín hiệu cảnh báo sớm
nằm trong CẤU TRÚC của M2, không phải trong số tổng.**
