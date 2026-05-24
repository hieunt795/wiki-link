---
slug: term_premium_decomposition
topic: us_treasury_curve_2026
sub_question: sq2 + sq4
date: 2026-05-24
confidence: 2
sources:
  - "[WEB-2026-04-24] NY Fed ACM term premium: 0.68%"
  - "[WEB-2026-05-18] FRED T10YIE: 2.48%; T5YIFR: 2.29%"
  - "[WEB-2026-05-22] Treasury confirmed yields: 2y=4.13%, 10y=4.56%, 30y=5.07%"
  - "[WEB-2026-05-24] Ferrante Capital term premium regime analysis"
promote_to_wiki: false
reason_not_promoting: "Specific to May 2026 snapshot; term premium estimates are time-sensitive"
---

## Finding: 10y Yield Decomposition and Inflation Expectations Structure

### Nominal 10y Yield Decomposition (May 22, 2026)

10y nominal yield = expected average short rate + real term premium + inflation compensation

Using confirmed data + ACM model:

| Component | Level | Source |
|---|---|---|
| 10y nominal yield | 4.56% | [WEB-2026-05-22] |
| 10y TIPS breakeven | 2.48% | [WEB-2026-05-18] |
| 10y real yield | ~2.08% | [LLM-E: 4.56% - 2.48%] |
| ACM term premium (10y) | 0.68% | [WEB-2026-04-24] |
| Expected rate component (10y avg) | ~3.88% | [LLM-E: 4.56% - 0.68%] |

**Interpretation:**
- The ~3.88% expected rate component is consistent with: FOMC starting at 3.625% (midpoint) and cutting to ~3.0-3.25% over 2026-2030 at a gradual pace [LLM-E]
- The 0.68% term premium is structurally positive — a regime break from 2016-2022 when ACM was 0 or negative
- At ~2.08%, the real 10y yield is high by historical standards (1990-2020 average was ~1.0-1.5%), reflecting either elevated r* or excess supply premium embedded in the real rate

### ACM Term Premium: Regime Analysis

The ACM model isolates investor compensation for duration risk beyond expected rates. As of April 2026 at 0.68%, the term premium is:
- **Positive territory** since ~early 2023 (after years of near-zero/negative from QE suppression)
- **Elevated but not extreme**: 2000s average was ~1.5-2.0%; 1980s-90s average was higher
- **Likely higher now**: Given 30y at 5.07% and the spike in May (UST sold off), the ACM estimate for May 22 is likely 0.75-0.90% [LLM-E]

**Structural forces keeping term premium positive (not returning to zero):**
1. Fed is NOT buying duration (no QE) — no artificial suppression
2. Private sector must absorb $1.9T deficit supply at auction [WEB-2026-05-24]
3. Forward fiscal uncertainty: $1.3T projected shortfall FY2027-28 [WEB-2026-05-24]
4. Foreign demand structurally retreating (Japan selling) [WEB-2026-05-24]
5. Inflation uncertainty: 5y5y at 2.29% is above target, creating uncertainty premium [WEB-2026-05-18]

IF any of these forces reverses (Fed resumes QE, deficit narrows, foreign buying returns), THEN term premium compresses and long end rallies [LLM-E].

### Breakeven Structure: Tariff Inflation Persistence

| Metric | Level | Interpretation |
|---|---|---|
| 10y TIPS breakeven | 2.48% | Average inflation 2026–2036 implied by market [WEB-2026-05-18] |
| 5y5y forward inflation | 2.29% | Average inflation 2031–2036 implied by market [WEB-2026-05-18] |

**Key insight:** The 5y5y at 2.29% is ABOVE the Fed's 2.0% target, despite being a long-dated expectation five years forward. This is unusual — historically, 5y5y anchored near 2.0-2.5% when the Fed's credibility was high.

Two interpretations:

**Interpretation A (tariff is transitory):** 5y5y at 2.29% reflects modest above-target expectations, consistent with the Fed eventually cutting and inflation normalizing. The 27bp gap above 2% is "inflation uncertainty premium" rather than a view that inflation stays structurally above 2%.

**Interpretation B (tariff is structural):** 5y5y at 2.29% means the market expects the tariff regime to permanently embed a 20-30bp inflation premium. IF tariffs remain in place for 5+ years AND pass-through proves durable, THEN the Fed's long-run inflation credibility erodes → 5y5y drifts toward 2.5-3.0% [LLM-E].

**Current evidence favors A over B:** The FOMC staff baseline calls for inflation to peak in Q2 2026 and fall toward 2.0% by 2027. But 5y5y's failure to anchor firmly at 2.0% is a warning signal for long-end buyers.

### Real Rate Level: r* or Supply Premium?

Real 10y yield at ~2.08% can be read two ways:

**Reading 1 (r* elevated):** Post-pandemic fiscal expansion, AI investment boom, and structural demand shifts raised the neutral real rate from ~0.5% (2010-2019) toward ~1.5-2.0%. The Fed's own r* estimate (Holston-Laubach-Williams) moved up to ~1.5% in 2025 [LLM-E]. Real 10y at 2.08% = r* + small real term premium → not overvalued.

**Reading 2 (supply premium):** Real yield is mechanically elevated because Treasury supply exceeds private sector's capacity to absorb it at neutral levels. The "extra" real yield is a supply-clearing mechanism rather than a genuine r* signal. IF Congress passes a deficit reduction package, THEN real yields compress toward 1.5% regardless of monetary policy path [LLM-E].

Both forces likely operating simultaneously — magnitude of each is a TRUE_GAP without granular r* decomposition tools.
