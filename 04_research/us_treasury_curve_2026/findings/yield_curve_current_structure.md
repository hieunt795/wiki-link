---
slug: yield_curve_current_structure
topic: us_treasury_curve_2026
sub_question: sq1
date: 2026-05-24
confidence: 2
sources:
  - "[WEB-2026-05-22] US Treasury / FRED confirmed yields"
  - "[RAW-WIKI Treasury_Market_Dealer_Intermediation_Capacity]"
  - "[RAW-WIKI Monetary_Policy_Transmission_Short_Long_Rate_Frictions]"
promote_to_wiki: false
reason_not_promoting: "Time-sensitive snapshot; structural insights partially covered by existing wiki nodes"
---

## Finding: Curve Shape — Positive but Shallow; Bear Steepener at Long End

### Level Summary (May 22, 2026)

The Treasury curve is positively sloped across all maturities. Confirmed anchors:
- 2y: **4.13%** [WEB-2026-05-22]
- 10y: **4.56%** [WEB-2026-05-22]
- 30y: **5.07%** [WEB-2026-05-22]

Key spreads:
- 2s10s = **+43bps** [WEB-2026-05-22]
- 10s30s = **+51bps** [LLM-E]
- 2s30s = **+94bps** [LLM-E]

### Regime Context: End of Inversion

The curve was inverted from approximately November 2022 to August 2024 — driven by Fed hiking to 5.25–5.50% while the long end priced in eventual easing. The inversion ended as the Fed began cutting in September 2024 and the long end failed to rally (or repriced higher on fiscal/inflation concerns).

Current +43bps on 2s10s is shallow by historical standards (pre-GFC normal was +100-200bps), but the direction matters more than the level: the curve is steepening from the long end (bear steepener), not the short end (bull steepener).

**Bear steepener vs. bull steepener distinction:**
- **Bull steepener** (normal easing cycle): short end falls as Fed cuts → 2y falls faster than 10y → curve steepens passively
- **Bear steepener** (current): long end RISES despite or alongside Fed holding → 2y relatively anchored → curve steepens actively from fiscal/premium drivers

The current regime is bear steepener-dominant. The long end is setting the pace.

### Front End: Policy Rate Anchored

The 2y at 4.13% reflects:
1. Fed funds rate: 3.50–3.75% [confirmed from fed_framework_2026 research]
2. Priced cuts: market pricing ~1 cut (25bp) for 2026, ~2-3 more in 2027 [LLM-E]
3. 2y term premium: small but positive (~30-40bps) [LLM-E]

IF the FOMC cuts twice in 2026 (to 3.25–3.50% by year-end), THEN 2y rallies to ~3.80–3.90% [LLM-E].
IF the FOMC holds all year at 3.50–3.75%, THEN 2y remains anchored near 4.10–4.20% [LLM-E].

### Belly: Transition Zone

The 5y [estimated ~4.38%, LLM-E] sits in the transition between Fed anchor and long-end fiscal premium. It is most sensitive to:
- Changes in rate cut path (if Fed signals more cuts → 5y rallies more than 2y on duration)
- Changes in fiscal narrative (if deficit outlook deteriorates → 5y rises on supply premium)

### Long End: Elevated and Structural

30y at 5.07% is near the October 2023 cycle high (~5.18%). This level:
- Incorporates real rate expectations: ~2.5-2.7% [LLM-E, from TIPS 10y real ~2.08% + long-end premium]
- Incorporates inflation expectations: 5y5y forward = 2.29%, 10y breakeven = 2.48% — both above target
- Incorporates term premium: ACM was 0.68% in April; likely 0.75-0.90% by May 22 [LLM-E]
- Incorporates fiscal/liquidity premium for 30y vs 10y maturity extension (~40-50bps) [LLM-E]

### The 20y Cheapness Pattern

The 20-year historically trades cheap relative to the 10/30y butterfly because of:
1. Structural supply: Treasury issues large amounts into 20y since reintroduction in May 2020
2. Dealer intermediation friction: 20y has lower liquidity than benchmark 10y or 30y
3. Convexity: 20y has high duration without the convexity premium embedded in 30y

Estimated 20y at ~4.95% [LLM-E] → trades ~10-15bps cheap to the 10/30 fly. If true, this is a structural richening opportunity when supply concerns ease. [RAW-WIKI Fixed_Income_Relative_Value_Framework]
