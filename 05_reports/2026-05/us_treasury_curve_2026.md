---
TO: Internal
FROM: Wiki-Agentic Research
DATE: 2026-05-24
RE: US Treasury Yield Curve 2026 — Bear Steepener, Term Premium Regime, and RV Implications
CLASSIFICATION: Internal
AUDIT: approved (us_treasury_curve_2026, 2026-05-24)
---

## Executive Summary

The US Treasury curve is positively sloped for the first time since the 2022–2024 inversion: 2y=4.13%, 10y=4.56%, 30y=5.07% as of May 22, 2026 [WEB-2026-05-22]. The slope is shallow (+43bps in 2s10s) but the direction matters more than the level — the steepening is driven from the long end (bear steepener), not from a rally in short rates. Four structural forces are holding the long end elevated: fiscal supply from a $1.9T deficit, Fed duration withdrawal (no coupon reinvestment), Japan selling ($29.6B Q1 2026), and inflation uncertainty from tariff pass-through. The ACM 10y term premium reached 0.68% in April [WEB-2026-04-24] — a structural regime shift from near-zero readings in 2016–2022. The dominant constraint for a long-end rally is fiscal: until the deficit outlook materially improves or the Fed restarts coupon purchases, the long end will remain anchored at elevated levels.

---

## I. Yield Curve Structure — Bear Steepener Regime

The curve uninverted approximately August 2024, as the Fed began cutting (September 2024 first cut) and the short end fell faster than the long end. Since then, the steepening has continued — but not in the bull mode typical of easing cycles.

| Maturity | Yield (May 22, 2026) | Source |
|---|---|---|
| 2-year | 4.13% | [WEB-2026-05-22] |
| 5-year | ~4.38% | [LLM-E] |
| 10-year | 4.56% | [WEB-2026-05-22] |
| 20-year | ~4.95% | [LLM-E] |
| 30-year | 5.07% | [WEB-2026-05-22] |

Key spreads: 2s10s = **+43bps** [WEB-2026-05-22]; 10s30s = **+51bps** [LLM-E]; 2s30s = **+94bps** [LLM-E].

A **bull steepener** — the normal easing-cycle signature — occurs when short yields fall faster than long yields as the Fed cuts. A **bear steepener** occurs when long yields rise faster than short yields on fiscal, supply, or inflation-driven premium. The current regime is bear steepener-dominant. The 2y at 4.13% is anchored by the FOMC hold at 3.50–3.75% plus approximately one 25bp cut priced into 2026 [LLM-E]. The 10y and 30y are rising on fiscal and structural demand forces, not on rate expectations.

Two forward scenarios:

IF the FOMC cuts twice in 2026 AND the long end holds, THEN 2s10s widens to 80–100bps as the short end falls — a standard bull-steepen continuation [LLM-E].

IF the FOMC holds all year AND the fiscal supply premium builds, THEN 2s10s widens from the long end only, reaching 70–80bps as 30y approaches its 2023 cycle high near 5.18% [LLM-E].

## II. Yield Decomposition — Term Premium and Inflation Expectations

### Nominal 10y Decomposition (May 22, 2026)

| Component | Estimate | Source |
|---|---|---|
| 10y nominal yield | 4.56% | [WEB-2026-05-22] |
| 10y TIPS breakeven (inflation compensation) | 2.48% | [WEB-2026-05-18] |
| 10y real yield | ~2.08% | [LLM-E: 4.56% − 2.48%] |
| ACM term premium (10y) | 0.68% | [WEB-2026-04-24] |
| Expected average rate component | ~3.88% | [LLM-E: 4.56% − 0.68%] |

The ~3.88% expected rate component is consistent with the FOMC cutting gradually from 3.625% toward ~2.75–3.25% over 2026–2030 [LLM-E]. The 0.68% term premium is a structural regime shift: during the QE era (2016–2022), the Fed suppressed term premium to near-zero by absorbing duration. QT2 ($2.2T runoff) and the transition to T-bill-only reinvestment have removed that suppression. Term premium is not returning to zero while the deficit is $1.9T and the Fed is not buying coupons.

### Breakeven Structure: Tariff Inflation Encoded, Not Unanchored

| Metric | Level | Fed 2% Target Gap | Source |
|---|---|---|---|
| 10y TIPS breakeven | 2.48% | +48bps | [WEB-2026-05-18] |
| 5y5y forward inflation | 2.29% | +29bps | [WEB-2026-05-18] |

The 5y5y forward at 2.29% is the key signal. It reflects market expectations for average inflation from 2031 to 2036 — well beyond any credible tariff pass-through window. At 29bps above target, this is an **inflation uncertainty premium**, not an embedded structural inflation view. Ferrante Capital (2026) notes: "The term premium story is not being driven by runaway inflation expectations" [WEB-2026-05-24]. The breakdown signal to watch is if 5y5y diverges above 2.5% sustained — that would indicate tariff effects are being priced as permanent, which would keep long-end term premium elevated regardless of the rate path.

The real 10y yield at ~2.08% is elevated relative to the 2010–2019 average (~0.5–1.5%). This reflects a mix of: genuinely higher r* (fiscal expansion, AI investment demand) and supply-clearing premium above fundamentals. IF a credible deficit-reduction path emerges, THEN real yields compress toward 1.5% without any change in monetary policy [LLM-E].

## III. Four Structural Drivers of Long-End Elevation

### III.1 Fiscal Supply — $1.9T Deficit, Forward Premium

Treasury issued $125B in coupon bonds in the May 2026 quarterly refunding — $58B in 3y notes, $42B in 10y notes, $25B in 30y bonds — raising $41.7B in new cash [WEB-2026-05-24]. The CBO projects a FY2026 deficit of **$1.9 trillion** [WEB-2026-05-24]. More significantly, Treasury's own projections point to a **$1.3 trillion funding shortfall in FY2027–2028** if current coupon auction sizes are maintained [WEB-2026-05-24]. Markets are pricing the future supply risk today.

The mechanism: primary dealers are obligated to bid at every auction; SLR and LCR constraints limit the inventory they can warehouse [RAW-WIKI Treasury_Market_Dealer_Intermediation_Capacity]; as Treasury outstanding approaches $28T and dealer balance sheet capacity grows more slowly, each marginal auction clears at a higher yield premium. The structural intermediation gap (Duffie 2026) is a force multiplier on fiscal supply pressure.

### III.2 Fed Duration Withdrawal — Passive Reverse Twist

QT2 ran June 2022 to November 2025, removing $2.2T from SOMA. The Fed now reinvests all principal into T-bills only (Reserve Management Purchases). The $1.98T MBS portfolio continues declining via prepayments, with proceeds directed to T-bills rather than new coupons. At ~$25–30B/month prepayment speed, SOMA releases approximately $300B of MBS duration to the private market annually — duration the Fed previously absorbed and suppressed [LLM-E].

The key distinction: this is not term premium increasing; it is the removal of artificial suppression. IF the Fed were reinvesting MBS into coupons (as pre-QT), term premium would be approximately 30–50bps lower [LLM-E]. Current operations are yield-curve neutral to mildly bearish for the long end — they do not cap term premium normalization.

### III.3 Japan Demand Retreat

Japan, the largest foreign holder of US Treasuries at $1.24T (February 2026), reduced its holdings to $1.19T by March — selling **$29.6B in Q1 2026**, the largest quarterly reduction in approximately four years [WEB-2026-05-24]. The driver is mechanical: the Bank of Japan's rate normalization has pushed JGB 10y yields to ~2.3%, a multi-decade high [WEB-2026-05-24]. With USD/JPY currency hedging costs at approximately 250bps annually, a Japanese investor receives only ~2.06% net on a hedged 10y UST position [LLM-E] — below the unhedged JGB yield. The incentive to buy US Treasuries at current levels is structurally negative for hedged Japanese buyers.

Each $100B decline in non-price-sensitive foreign demand transfers that absorptive capacity to domestic price-sensitive investors, who require a higher clearing yield — estimated 15–25bps at the margin per $100B shift [LLM-E; no authoritative empirical estimate available, TRUE_GAP].

The forward path is a tailwind: IF the BOJ normalizes to 1.0–1.5% by 2028, THEN the USD/JPY interest rate differential narrows, hedging costs fall, and hedged UST returns become competitive again. This is not a current tailwind, but it is a secular reversal mechanism.

### III.4 Inflation Uncertainty

The tariff shock embedded in 2026 core PCE (3.2% in March) creates genuine uncertainty about the Fed's ability to return inflation to 2.0% without sacrificing growth. Long-dated bond investors price uncertainty about conditions over the bond's life — not just expected inflation. The 29bps gap between 5y5y (2.29%) and the 2.0% target is the market's current estimate of that uncertainty premium [WEB-2026-05-18]. It is moderate, not extreme, consistent with the Fed's credibility remaining intact while the tariff question resolves.

## IV. Connection to the Fed Framework

From the preceding fed_framework_2026 analysis: the FOMC holds rates at 3.50–3.75% until core PCE trends durably below 2.5%. The Treasury curve and the Fed's rate decisions interact through three channels:

**Fiscal feedback:** Higher long-end yields increase federal interest expense (~$70B annually per 25bp rise on $28T outstanding [LLM-E]), widening the deficit, requiring more coupon issuance, and reinforcing the supply premium. This is a self-reinforcing loop that only breaks with a credible fiscal consolidation.

**Private credit tightening:** The 10y at 4.56% benchmarks the 30y mortgage rate at approximately 7.0–7.3% [LLM-E]. Housing affordability remains constrained — a tightening impulse operating entirely independently of the FFR. The FOMC does not need to raise rates to maintain restrictive financial conditions; the curve does it.

**Curve slope and rate cuts:** IF the Fed cuts in H2 2026, THEN the 2y rallies and 2s10s steepens further (bull steepener adds on top of the existing bear steepener). The long end does not automatically rally alongside; it may even sell off if a cut is read as premature on inflation. A clean long-end rally requires both a rate cut AND a credible signal that inflation is durably below 3.0%.

## V. Risks and RV Implications

**Tail risk — term premium spike to 1.5%:** A 2013 taper-tantrum-style episode would move ACM term premium by ~100bps in four months [WEB-2026-05-24]. IF fiscal path deteriorates materially OR Japan accelerates selling, THEN 10y reaches ~5.35–5.50% with no change in rate expectations [LLM-E].

**Base case — gradual normalization:** Term premium drifts from 0.68% toward 0.90–1.0% over 2026–2027 as supply absorbs steadily; 10y trades 4.5–5.0% range; 30y tests 5.18% (2023 high) before stabilizing.

**Bull case — fiscal catalyst:** IF Congress passes a multi-year deficit reduction package reducing the FY2027+ borrowing path by $500B+, THEN supply premium compresses 20–30bps and 10y rallies toward 4.2–4.3% [LLM-E].

**RV implications:**

- **2s10s steepener** — long 10y / short 2y (DV01-neutral): approximately zero carry at current levels; directional view is a further 30–50bps of steepening as the cut cycle begins. Entry at +43bps [LLM-E, RAW-WIKI Fixed_Income_Relative_Value_Framework].
- **20y butterfly** — 20y estimated ~10–15bps cheap to the 10s/30s fly [LLM-E]. Structural cheapness from supply overhang since 2020 reintroduction; insurance/pension demand provides floor. Duration-neutral, limited carry cost.
- **5y TIPS breakeven widener** — long 5y TIPS vs short nominal 5y: expresses medium-probability tariff persistence scenario; breakeven target 2.5–2.7% [LLM-E].
- **Long 2y outright** — +63bps carry above overnight rate; IF inflation breaks below 2.5%, 40–60bp rally potential [LLM-E].
- **False trade — long 30y for duration return:** Value trap if FY2027–28 supply forces larger coupon auctions. 10y offers better risk-adjusted duration exposure with less tail supply risk.

---

## Sources

**Fresh data (fetched 2026-05-24):**
- US Treasury Daily Yield Curve, May 22, 2026: [home.treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)
- FRED 10y TIPS Breakeven (T10YIE), May 18, 2026: [fred.stlouisfed.org/series/T10YIE](https://fred.stlouisfed.org/series/T10YIE)
- FRED 5y5y Forward Inflation (T5YIFR), May 18, 2026: [fred.stlouisfed.org/series/T5YIFR](https://fred.stlouisfed.org/series/T5YIFR)
- NY Fed ACM Term Premia, April 24, 2026: [newyorkfed.org/research/data_indicators/term-premia-tabs](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs)
- TBAC May 2026 Quarterly Refunding Minutes: [home.treasury.gov/news/press-releases/sb0491](https://home.treasury.gov/news/press-releases/sb0491)
- Wolf Street — Japan / Largest Foreign UST Holders, April 2026: [wolfstreet.com](https://wolfstreet.com/2026/04/15/the-largest-foreign-holders-of-us-treasury-securities-and-the-basis-trade-april-2026-update/)
- Ferrante Capital — Term Premium Is Back, 2026: [ferrantecapitaladvisers.com](https://ferrantecapitaladvisers.com/insights/treasury-term-premium-regime-2026/)

**Wiki nodes (structural/mechanistic):**
- [[Treasury_Market_Dealer_Intermediation_Capacity]] — SLR/LCR dealer capacity and structural intermediation gap
- [[Monetary_Policy_Transmission_Short_Long_Rate_Frictions]] — short vs. long rate decoupling, Greenspan conundrum analog
- [[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]] — negative swap spreads, SLR driver
- [[Fixed_Income_Relative_Value_Framework]] — carry, roll-down, butterfly trade construction
- [[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]] — regulatory capital constraints on dealer intermediation
- [[Treasury_QE_Duration_Swap_RRP_Drain_Mechanisms]] — duration swap mechanics
- [[Treasury_Tbill_Supply_RRP_Drain_MMF_Cash_Routing]] — T-bill supply and money market plumbing

**Connected research:**
- `04_research/fed_framework_2026/` — FOMC rate path (3.50–3.75% hold), QT halt, RMPs ($10B/month), reserve adequacy
- `05_reports/2026-05/fed_operating_framework_2026.md` — published report, balance sheet and reserve framework
