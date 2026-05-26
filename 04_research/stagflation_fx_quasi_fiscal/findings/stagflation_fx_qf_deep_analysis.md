---
finding_id: stagflation_fx_qf_deep_001
title: "T_MODE_DEEP — Stagflation Under FX Rate Target + Quasi-Fiscal: Full Mechanism Map"
topic_slug: stagflation_fx_quasi_fiscal
type: T_MODE_DEEP
analysis_mode: T_MODE_DEEP
confidence: 3
status: confirmed
created: 2026-05-25
updated: 2026-05-26
sources_used:
  - "[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]"
  - "[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]"
  - "[[Imf_FX_Regime_Monetary_Accounts_Balance_Sheet_Endogeneity]]"
  - "[[Stagflation_Regime_Diagnostic_Framework]]"
  - "[[Stagflation_Policy_Response_Tradeoff_Framework]]"
  - "[[Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design]]"
  - "[[Imf_Macro_Crisis_Vector_Framework]]"
  - "[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]"
  - "[[Incomes_Policy_Wage_Controls_Stabilization_Programs]]"
  - "[[Enhanced_Taylor_Rule_EME_FX_Augmented]]"
  - "[[Imf_Inflation_Analysis_Cpi_Gdp_Deflator_Four_Types_Core]]"
  - "[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]"
  - "[[Cost_Push_Inflation_Persistence_Mechanism]]"
new_raw_passages_confirmed_2026_05_26:
  - "IMF-macro p.890+920-921: cost-push cannot persist IF monetary policy refuses to accommodate → under FX target CB cannot refuse → direct mechanism source for Tầng I"
  - "IMF-macro p.923 fn: inertial inflation perpetuated through contracts/indexation"
  - "IMF-macro p.982-990+992fn17: incomes policy role — break inertia + support FX anchor credibility"
  - "IMF-macro p.1021: Poland three-element program explicitly described"
  - "Lipschitz p.2720: sterilization cost mechanism (low-yield FX vs high-yield domestic)"
  - "Lipschitz p.2757: fiscal dominance definition + vicious circle passage"
  - "Lipschitz p.2791 Box 4.8: 'A vicious circle of depreciation, monetary accommodation, and inflation ensued' — Bulgaria direct case"
remaining_llm_e:
  - "Timing leads (T-12, T-8, T-6 months) — need empirical source"
  - "Sterilization cost 0.5% GDP figure — LLM-E from assumed parameters"
  - "Crowding out multiplier magnitude"
  - "CB profit transfer decline threshold >15%"
---

# TOP-DOWN ENTRY

**Regime đang xét:** 🟢 CURRENT — EME với FX rate target (managed band / crawling peg / dirty float
với fear of floating) kết hợp quasi-fiscal operations đáng kể (sterilization stock, CB losses,
NCG accommodation, policy bank subsidized lending).

**Core claim [LLM-E]:** Đây là bẫy chính sách self-reinforcing. Stagflation xuất hiện không phải
do cú sốc thuần túy từ bên ngoài mà do *cấu trúc regime* vô hiệu hóa cả monetary lẫn fiscal
policy theo hai hướng ngược nhau — một cái tạo lạm phát, cái kia tạo đình đốn — đồng thời.

---

## LENS 1 — POLICY: Tại Sao FX Target Khóa Chính Sách Tiền Tệ Hai Chiều

**Mechanism:**

```
Standard central bank có 2 degrees of freedom:
  (i) Policy rate  → inflation/growth management
  (ii) Balance sheet (NDA) → liquidity management

Khi CB commit FX target:
  NFA becomes ENDOGENOUS (driven by BOP + intervention obligation)
  → NDA là instrument duy nhất còn lại
  → Nhưng NDA phải lo sterilization → NDA không còn free instrument nữa
  → Effective degrees of freedom: ZERO [RAW-BOOK Lipschitz p.2241–2244]
```

**Hệ quả chính sách:**

Kịch bản **A — Inflation xuất hiện** (e.g. cost-push, commodity shock):
- Tăng lãi suất để chống lạm phát → dòng vốn vào tăng → appreciation pressure → CB phải mua
  thêm FX → NFA↑, RM↑ → monetary easing effect → counteracts the rate hike
- Kết quả: rate hike KHÔNG effective trong điều kiện FX target + open capital account [LLM-E]
- Worse: nếu CB sterilize inflows → quasi-fiscal cost↑ → fiscal drain → không gian chính sách thu hẹp hơn

Kịch bản **B — Growth yếu / stagnation:**
- Cắt lãi suất để kích thích → capital outflows → depreciation pressure → CB phải bán FX → NFA↓
- Nếu reserves thấp → không thể cắt rate → tăng trưởng tiếp tục yếu
- Enhanced Taylor rule cho EME: `i_t = i* + α(π−π*) + β(y−y*) + γ_e × e_t` — với FX target,
  γ_e coefficient cao → FX term dominates → rate policy bị neo theo FX, không theo inflation/output
  [RAW-BOOK Perry p.279]

**Mundell-Fleming kết luận:** Dưới fixed FX + open capital account: monetary policy is
ineffective for domestic stabilization. [RAW-BOOK Lipschitz p.2371]

→ **Policy lock**: Không thể vừa fight inflation vừa support growth với cùng một instrument.

---

## LENS 2 — MACRO: Ba Tầng Stagflation — Đồng Thời Không Phải Tuần Tự

Stagflation "kiểu FX target" khác stagflation cổ điển 1970s ở chỗ nó là **regime-structural**,
không phải shock-driven. Ba tầng hoạt động song song:

### Tầng I — Inflation Persistence: FX Target Không Hấp Thụ Được External Shocks

```
External shock: commodity price↑, import cost↑, global inflation↑
    ↓
Floating rate: domestic currency appreciates → import prices fall in local terms
             → shock partly absorbed by exchange rate
    ↓
FX target regime: CB prevents appreciation → exchange rate FIXED
             → Full pass-through of commodity/import shock into domestic CPI
             → Cost-push inflation không bị giảm nhẹ bởi tỷ giá
             → Inertial embedding: wage contracts index to past CPI → spiral begins
[RAW-BOOK IMF Macro p.878–927] + [RAW-BOOK Lipschitz p.2720]
```

Đây là inflation persistence mechanism đặc thù của FX target: tỷ giá không làm nhiệm vụ
shock absorber. IMF inflation taxonomy: cost-push → inertial khi không có non-accommodating policy.
[RAW-BOOK IMF Macro p.4867]

### Tầng II — Stagnation: Bốn Kênh Drain Từ Quasi-Fiscal

**Kênh QF-1 — Direct fiscal drain từ sterilization carry:**
```
Sterilization cost (annual) = r_domestic × QF_stock − r_foreign × NFA_accumulated
→ Với typical EME: (7% − 4.5%) × 20% GDP = 0.5% GDP/năm [LLM-E]
→ Tương đương fiscal drag 0.5% GDP → government buộc cắt chi tiêu public
→ Multiplier effect: ΔG × fiscal multiplier → GDP impact > 0.5% [LLM-E]
[RAW-BOOK Lipschitz p.2720] [RAW-BOOK IMF Macro p.2288]
```

**Kênh QF-2 — Crowding out via NCG expansion:**
```
Nếu government bù đắp fiscal drain bằng cách tăng vay ngân hàng:
NCG↑ → banks reduce credit to private sector (CPS↓) → đầu tư tư nhân giảm
OR: CB accommodates → RM↑ → monetization → Kênh lạm phát (vòng lặp)
[RAW-BOOK IMF Macro p.1943–1945] — Mode 4 of fiscal crisis vector
```

**Kênh QF-3 — High real interest rates từ sterilization absorption:**
```
CB sterilize inflows → phát hành T-bills → domestic interest rate pressure↑
Higher r_domestic → higher lending rates → credit expensive → investment↓ → growth↓
Paradox: CB sterilize để giữ RM ổn định, nhưng effect là tighten domestic credit market
[RAW-BOOK Perry p.267] — second-round effects
```

**Kênh QF-4 — Real wage squeeze từ inflation + fiscal compression:**
```
Nominal wages: bị kìm hãm bởi austerity / incomes policy (nếu có)
Real wages: = nominal wages / CPI → fall as inflation persists + nominal frozen
Real disposable income↓ → consumption↓ → domestic demand↓ → growth↓ [LLM-E]
```

### Tầng III — The Trap: Fear of Floating Locks In Both

**Cơ chế "fear of floating" [RAW-BOOK Lipschitz p.3693–3814]:**

Sau nhiều năm FX target, khu vực ngân hàng và nonbank tích lũy FX exposure lớn vì:
- Implicit exchange rate guarantee → borrowers không hedge
- FX loans rẻ hơn VND/local loans → tư nhân vay ngoại tệ

Hệ quả:
```
Nếu CB LET rate depreciate:
  FX borrowers: mismatch → higher debt service in local currency
  Banks: NPL spike → capital loss → solvency risk
  Government: phải recapitalize banks → fiscal deterioration
  → Fear of floating: authorities BAN NHÀ KHÔNG THỂ thả nổi kể cả khi muốn
  [RAW-BOOK Lipschitz p.53] — the malign configuration
```

Kết quả: CB bị kẹt ở đây:
- Cannot depreciate → inflation không được địa chỉ từ supply side
- Cannot raise rates significantly → stagnation deepens
- Cannot cut rates → reserves bleed
- Cannot use fiscal → quasi-fiscal costs đã hút hết không gian

**Matrix of impossibilities [LLM-E]:**

```
Policy action     | Inflation effect | Growth effect | FX effect  | Feasible?
─────────────────────────────────────────────────────────────────────────────
Rate hike         | Reduces (slow)   | Contracts (-) | Attracts + | Partial
Rate cut          | Worsens (+)      | Stimulates(+) | Outflow(-) | Blocked
Fiscal expand     | Worsens (+)      | Stimulates(+) | Reserve-   | Blocked
Fiscal tighten    | Reduces(minor)   | Contracts (-) | Neutral    | Painful
Peg devalue       | Worsens SHARP(+) | Mixed (J-crv) | Resolves   | Fear blocks
Sterilize more    | Neutral          | Contracts (-) | Neutral    | Costly
→ EVERY option makes at least one of the two problems worse
→ Đây là định nghĩa của bẫy đình lạm chính sách
```

---

## LENS 3 — PLUMBING: T-Account Tracing Qua Ba Entities

**Entities: CB / Government / Banking Sector**

### State 1 — Early Stage (Quasi-Fiscal Building, Growth Intact)

```
Period T:
┌─────────────────────────────────────────────────────────────────┐
│ CB Balance Sheet                                                 │
│  Assets              │ Liabilities                              │
│  NFA ↑ (inflows)     │ RM ↑ (from FX purchases)                │
│  NCG ~stable         │                                          │
│  OIN ↓ (T-bill abs.) │ [sterilization absorbs part of RM↑]     │
│                      │                                          │
│ Quasi-fiscal loss = r_d × OIN − r_f × NFA [LLM-E]             │
└─────────────────────────────────────────────────────────────────┘

Government:
  Receives seigniorage transfer T (shrinking as QF loss grows)
  Runs fiscal deficit D
  Fills gap: issues domestic debt → banking sector absorbs

Banking sector:
  Holds government bonds ↑
  Available for private credit ↓ (crowding out begins)
  FX loan portfolio growing (borrowers trust FX stability)
```

### State 2 — Mid Stage (Inflation Emerging, Growth Slowing)

```
Period T+n (external shock: commodity prices↑):
┌─────────────────────────────────────────────────────────────────┐
│ CB Balance Sheet                                                 │
│  NFA ↓ (now defending peg against depreciation pressure)        │
│  NCG ↑ (CB accommodating fiscal via secondary market OMO)       │
│  RM ≈ stable (NFA↓ offset by NCG↑)                             │
│                                                                  │
│ CRITICAL SIGNAL: NFA↓ + NCG↑ simultaneously                     │
│ → Dual deterioration (CRISIS PRECURSOR) [RAW-BOOK Lipschitz]   │
└─────────────────────────────────────────────────────────────────┘

Government:
  Fiscal squeeze: seigniorage transfer từ CB đã = 0 hoặc âm
  Revenue pressure: stagnation → tax base không tăng
  Spending: cannot cut politically → deficit widens
  Financing: MODE 4 (bank credit) → crowding out accelerates

Banking sector:
  Government bond portfolio ↑↑ (absorbing fiscal deficit)
  Private credit ↓↓
  FX loan book: UNHEDGED (borrowers assumed peg holds)
  → System is BRITTLE: any FX move → NPL spike
```

### State 3 — Late Stage (Fiscal Dominance, Stagflation Locked In)

```
Period T+2n (fiscal dominance):
┌─────────────────────────────────────────────────────────────────┐
│ CB Balance Sheet                                                 │
│  NFA ↓↓↓ (approaching Greenspan-Guidotti floor: NFA/RM → 1.0) │
│  NCG ↑↑↑ (CB accommodating to prevent rate spike)             │
│  RM ≈ stable BUT backed by NCG not NFA → quality deterioration  │
│                                                                  │
│ "The pattern visible before crisis: NFA declining steadily      │
│  while NDA rising" [RAW-BOOK Lipschitz p.2704]                 │
└─────────────────────────────────────────────────────────────────┘

Government:
  CB independence lost: "no scope for independent monetary policy"
  [RAW-BOOK Lipschitz p.2757]
  Rate held below neutral (political pressure)
  Sterilization halted (CB losses unacceptable)
  → RM starts expanding → inflation accelerates

Banking sector:
  Hold large FX loans + large gov bond portfolio
  Capital constrained: cannot absorb shock
  Credit freeze risk: any confidence event → systemic

INFLATION: RM expanding + FX pass-through + inertial wages = PERSISTENT
STAGNATION: Investment frozen, crowding out maximal, real wages eroded = PERSISTENT
→ STAGFLATION FULLY LOCKED IN
```

---

## LENS 4 — TREASURY DESK: Phân Tích Fiscal Sustainability Dưới FX Target

### True Fiscal Stance (Adjusted for QFOs)

Theo IMF GFS methodology, conventional fiscal deficit UNDERESTIMATES true expansion:

```
True fiscal stance =
  GFS reported deficit
  + CB sterilization net losses            [r_d × stock − r_f × NFA]
  + CB subsidized lending subsidy          [rate differential × volume]
  + Policy bank below-market lending       [unquantified contingent]
  + FX guarantee contingent liabilities    [× probability exercise]
  ± CB recapitalization cost               [PV future interest]
[RAW-BOOK IMF Macro p.2288]
```

**Debt dynamics under FX target:**

```
Standard debt dynamics: Δd = (r−g)d + pd
                        where d = debt/GDP, r = real interest rate, g = real growth
                              pd = primary deficit ratio

Dưới FX target + quasi-fiscal:
  r rises: domestic rate elevated by sterilization absorption + risk premium
  g falls: stagnation từ crowding out + fiscal squeeze
  pd worsens: quasi-fiscal costs reduce revenue, increase spending pressures

→ (r−g) component WIDENS from BOTH sides simultaneously
→ Debt ratio explosion accelerates [LLM-E]
```

### Fiscal Crisis Vector Map (từ IMF Crisis Vector Framework):

```
Giai đoạn 1: MODE 4 (bank credit) dominates
  → Private credit crowded out → growth squeeze → stagnation component

Giai đoạn 2: MODE 2 (reserve drawdown) emerges
  → FX defense consumes reserves → speculative attack window opens

Giai đoạn 3: MODE 1 (monetization) kicks in when reserves near depletion
  → NCG expansion → RM → inflation → full stagflation

Three modes OPERATING SIMULTANEOUSLY = maximum fiscal crisis complexity
[RAW-BOOK IMF Macro p.1943–1945]
```

### Crawling Peg Variant — Disinflation Trap:

Nếu CB dùng active crawl (rate of crawl < inflation differential) để chống lạm phát:

```
Active crawl policy: depreciate LESS than inflation differential
  → Real exchange rate APPRECIATES over time [RAW-BOOK IMF Macro p.3796]
  → Import prices fall (disinflation signal) → temporary
  → BUT: real appreciation → exports less competitive → CA deficit→ reserves↓
  → Growth từ export sector: giảm [STAGNATION component]
  → Imports cheap → domestic import-competing industries bị kill
  → Unemployment in import-competing sectors

Disinflation succeeds (CPI falls) BUT:
  → Growth thuộc export sector/import-competing = ZERO
  → Unemployment rises
  → "Successful disinflation" nhưng growth cost → STAGFLATION LITE [LLM-E]
```

Poland thoát được vì: tight fiscal + incomes policy (popiwek) + credibility = không cần giữ active
crawl quá lâu. Transition ended before real appreciation became growth killer.
[RAW-BOOK IMF Macro p.3798–3804]

---

## LENS 5 — HISTORICAL: Case Studies

### Case A — Bulgaria 1994–1996 (Pathway 3: Fiscal Dominance → Crisis)

```
Setup:   Post-communist transition, soft budget constraint SOEs, banking sector fragile
FX:      Managed peg (crawling)
QF:      NCG expansion financing SOE losses, CB accommodation
Sequence:
  NFA: +12.1 → −234.5 billion lev (2 years)
  NCG: expanding to compensate → RM ≈ stable
  Sterilization: halted when CB capital negative
  Fiscal dominance: CB printed to accommodate
  Outcome: HYPERINFLATION + economic collapse → currency board July 1997
[RAW-BOOK Lipschitz p.2771–2792]
```

**Lesson:** Khi NFA đã âm và NCG đang tăng mạnh, FX defense không còn khả thi →
inflation bùng phát đột ngột chứ không từ từ. Growth collapse trước, then hyperinflation.

### Case B — Poland 1989–1991 (Successful Exit from Near-Stagflation)

```
Setup:   Hyperinflation (55%/month Oct 1989), economic collapse
FX:      Fixed peg to USD (Jan 1990)
QF:      MINIMIZED deliberately — tight fiscal, no CB accommodation
Incomes: Popiwek (excess wage tax) → break wage-price-FX spiral
Sequence:
  Month 1: Inflation SPIKED (pent-up price liberalization)
  Month 2–6: Inflation fell sharply as FX anchor + incomes policy held
  Year 1: Monthly inflation ~5% from 55%
  Growth: V-shaped; contraction then recovery
[RAW-BOOK IMF Macro p.1021, p.3798–3804]
```

**Lesson:** Poland AVOIDED stagflation trap BECAUSE:
1. Tight fiscal → no NCG expansion → no monetization
2. Fixed peg provided nominal anchor (not active crawl → no competitiveness loss)
3. Incomes policy broke inertial inflation FAST → wage-price spiral extinguished
4. Government credibility high → reserves never needed to be used

→ The CONTRAST is instructive: Poland succeeded by NOT relying on FX target alone.

### Case C — Generic EM "Fear of Floating" (Pathway 1: Impossible Trinity)

```
Pattern identified in: Mexico 1994, Asia 1997, Eastern Europe 2008
Setup:   Capital inflows → FX borrowing → no hedge (implicit guarantee)
FX:      Limited flexibility (dirty float or crawl)
QF:      Less relevant; crisis driven by balance sheet mismatch
Sequence:
  Growth phase: credit boom, asset inflation, FX exposure builds
  Trigger: sudden stop (VIX spike, Fed hike, terms-of-trade shock)
  Fear of floating: cannot depreciate → defend reserves
  Reserves bleed → fiscal cost of banking rescue → QF costs suddenly large
  Stagflation: depreciation (when forced) → import inflation spike + growth collapse
[RAW-BOOK Lipschitz p.3693–3814]
```

**Lesson:** Fear of floating creates the CONDITIONS for stagflation; trigger converts it
into actual crisis. The FX exposure buildup during good years IS the inflation time-bomb.

---

## LENS 6 — TIMING: Sequencing và Early Warning Calendar

### Sequencing của Đình Lạm FX-Type

```
PHASE 0 — BUILDUP (không thể thấy từ headline data):
  T-12 months: Sterilization stock growing → QF costs accumulating
  T-8 months:  CB profit transfer to Treasury declining
  T-6 months:  NCG/M2 ratio starting to rise
  T-4 months:  FX loan portfolio in banking sector expanding rapidly
  T-2 months:  NFA starts declining (capital inflow reversal or CA deficit)

PHASE 1 — STAGNATION FIRST (thường xuất hiện trước):
  Growth deceleration: crowding out + fiscal squeeze hits investment first
  Credit slows: domestic lending rate elevated by sterilization
  Export slowdown: (nếu active crawl) real appreciation erodes competitiveness

PHASE 2 — INFLATION PERSISTENCE:
  External shock (commodity) → full pass-through (FX not absorbing)
  Wages: begin indexing to past CPI (inertial embedding starts)
  Core inflation: starts diverging from headline (persistence signal)

PHASE 3 — POLICY PARALYSIS:
  Rate hike attempted → inflows complicate → ineffective
  Rate cut blocked → reserves would bleed
  Fiscal tighten → deepens stagnation
  Sterilize more → QF costs unsustainable
  → Full stagflation trap

PHASE 4 — FISCAL DOMINANCE (if unresolved):
  Reserves approach Greenspan-Guidotti floor (NFA/RM < 1.0)
  Rate held below neutral
  NCG accelerating
  → Binary outcome: IMF program / external shock OR crisis + forced float
```

### Early Warning Indicators (Graded by Lead Time)

| Indicator | Lead Time | Signal Threshold |
|-----------|-----------|-----------------|
| CB profit transfer to Treasury declining | 12–18 months | YoY decline >15% |
| OMO absorption stock growing | 12 months | >15% GDP [LLM-E] |
| NCG/M2 ratio rising | 6–9 months | Uptrend >2 quarters |
| NFA declining + NCG rising simultaneously | 3–6 months | DUAL DETERIORATION |
| Parallel market FX premium >5% | 2–3 months | Speculative attack forming |
| NFA/RM ratio approaching 1.0 | 1–2 months | Greenspan-Guidotti floor |

[LLM-E] thresholds không có sourced benchmark — sử dụng chỉ như order-of-magnitude guidance.
[RAW-BOOK IMF Macro p.3741–3745] — financial vulnerability indicators cho reserve adequacy.

---

## SYNTHESIS: Cái Gì Phân Biệt Stagflation FX-Type Với Classical Stagflation

| Dimension | Classical (1970s supply shock) | FX-Target Type |
|-----------|-------------------------------|----------------|
| **Inflation source** | External supply shock (oil) | Mix: external pass-through + domestic monetization |
| **CB constraint** | Can tighten (painful tradeoff) | Cannot tighten freely (breaks FX target or bleeds reserves) |
| **Growth driver** | Demand shock + higher input costs | Crowding out + fiscal drain + real appreciation |
| **Duration** | Shock-driven → ends when shock passes | Regime-driven → persists until regime changes |
| **Policy exit** | Volcker-style tightening (painful but sufficient) | Requires regime change: FX adjustment + fiscal consolidation + incomes policy |
| **Self-reinforcing?** | Partially (wage spiral) | Fully self-reinforcing (QF costs worsen fiscal → monetization → inflation → more reserve drain) |
| **Historical precedent** | US/EU 1973–1982 | Bulgaria 1994–96, EM crises passim |

---

## POLICY EXIT FRAMEWORK — The Three-Element Heterodox Program

Từ Poland model và IMF literature, exit từ FX-induced stagflation yêu cầu ĐỦ BA yếu tố
đồng thời [RAW-BOOK IMF Macro p.1005]:

```
Element 1 — FX Adjustment:
  Abandon overvalued peg / active crawl
  → Accept one-time inflation spike (import prices)
  → But: restores exchange rate as shock absorber permanently
  → Credibility cost: high, managed with Element 3

Element 2 — Fiscal Consolidation:
  Eliminate deficit financing via NCG
  → Cut quasi-fiscal operations (policy bank subsidies, FX guarantees)
  → IMF program often provides external anchor + BoP financing
  → Painful: real spending cuts during stagnation → J-curve of growth

Element 3 — Incomes Policy (Anti-Inertial):
  Break wage-price spiral via TIP (excess wage tax) or social pact
  "The combination was termed somewhat heterodox: orthodox in demand management,
   heterodox in adding the exchange rate anchor and wage controls" [RAW-BOOK IMF Macro]
  → Temporary only: 12–24 months max before distortions > benefits
  → Critical: must be paired with Element 1+2, not a substitute
```

**Phân tích: Nếu thiếu một element:**

- **Thiếu E1** (giữ peg): FX constraint remains → policy paralysis continues → stagflation persists
- **Thiếu E2** (không fiscal consolidation): NCG expansion restarts → monetization → new inflation round
- **Thiếu E3** (no incomes policy): inertial inflation embeds → disinflation process much slower → higher sacrifice ratio (unemployment + growth cost)

---

## Gaps Triggered — Sources Cần Acquire

1. **IMF WP "Exchange Rate Regimes and Inflation"** (Ghosh, Gulde, Wolf) — systematic cross-country evidence on inflation persistence under different FX regimes
2. **BIS WP on sterilization costs and monetary policy effectiveness in EMEs** — quantify quasi-fiscal carry costs by country
3. **NBER WP on fiscal dominance and stagflation in developing countries** — formal model of the fiscal-monetary-FX nexus
4. **IMF WEO Chapter on stagflation risk in EMs** — current policy discussion

---

## Wiki Promotion Assessment

**Promote-ready components (confidence 4, sourced):**
- The Bulgaria 1994–96 case detail → already in CB_FX_Rate_Target node
- The three-element heterodox program → can be a new wiki node: `Heterodox_Stabilization_Three_Element_Framework`
- The fear-of-floating → stagflation nexus → new node: `Fear_Of_Floating_Stagflation_Amplifier`

**Not ready to promote (confidence 2, LLM-E):**
- Specific threshold numbers (sterilization % GDP, timing leads)
- The "matrix of impossibilities" quantification
- Vietnam SBV estimates

**Contradictions to check:**
- Poland succeeded → suggests FX anchor CAN work. But: Poland avoided QF operations entirely. Contradiction with claim that FX anchor → quasi-fiscal → stagflation? Resolution: Poland had TIGHT fiscal from day 1; the trap only forms when QF costs exist AND fiscal is accommodating. Regimes differ.
