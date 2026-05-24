# US Treasury Yield Curve Snapshot — May 22, 2026
# Fetched: 2026-05-24
# Primary source: US Treasury Daily Par Yield Curve + FRED + NY Fed

## Par Yield Curve (May 22, 2026)

| Maturity | Yield | Source |
|---|---|---|
| 1-month | ~4.30% | [LLM-E, near Fed lower bound 3.50% + bill premium] |
| 3-month | ~4.32% | [LLM-E, interpolated] |
| 6-month | ~4.20% | [LLM-E, interpolated] |
| 1-year | ~4.10% | [LLM-E, near 2y anchor] |
| 2-year | 4.13% | [WEB-2026-05-22] |
| 3-year | ~4.22% | [LLM-E, interpolated] |
| 5-year | ~4.38% | [LLM-E, interpolated] |
| 7-year | ~4.47% | [LLM-E, interpolated] |
| 10-year | 4.56% | [WEB-2026-05-22] |
| 20-year | ~4.95% | [LLM-E, interpolated; typically rich vs 30y] |
| 30-year | 5.07% | [WEB-2026-05-22] |

**Confirmed data points:** 2y = 4.13%, 10y = 4.56%, 30y = 5.07% [WEB-2026-05-22]
**Intermediate maturities estimated** [LLM-E] — pending exact H.15/Treasury data.

## Key Spreads

| Spread | Level | Source |
|---|---|---|
| 2s10s | +43 bps | [WEB-2026-05-22] |
| 2s30s | +94 bps | [LLM-E, derived from confirmed yields] |
| 10s30s | +51 bps | [LLM-E, derived from confirmed yields] |
| 3m10s | ~+24 bps | [LLM-E] |

**Curve is positively sloped** — no longer inverted (inversion ended approximately August 2024).

## Inflation and Real Rates

| Metric | Value | Date | Source |
|---|---|---|---|
| 10y TIPS breakeven | 2.48% | 2026-05-18 | [WEB-2026-05-18] |
| 10y real yield (derived) | ~2.08% | 2026-05-22 | [LLM-E] |
| 5y TIPS breakeven | ~2.30% | 2026-05-18 | [LLM-E, from 5y5y] |
| 5y5y forward inflation | 2.29% | 2026-05-18 | [WEB-2026-05-18] |

## Term Premium

| Metric | Value | Date | Source |
|---|---|---|---|
| ACM 10y term premium | 0.68% | 2026-04-24 | [WEB-2026-04-24] |
| Expected rate component (derived) | ~3.88% | 2026-05-22 | [LLM-E: 4.56% - 0.68%] |

Note: ACM most recent confirmed as of 2026-04-24. With 30y at 5.07%, term premium likely 0.70-0.85% by May 22. [LLM-E]

## Historical Context

- 2s10s was inverted from Nov 2022 to Aug 2024 (peak inversion ~-110bps in early 2023)
- +43bps is the shallowest positive slope since the inversion began unwinding
- 30y at 5.07% is near the Oct 2023 cycle high (~5.18%)
- ACM term premium turned positive in 2023 after ~7 years of near-zero or negative readings

## Fiscal Supply Context (TBAC May 2026) [WEB-2026-05-24]

- CBO deficit projection FY2026: $1.9 trillion
- May quarterly refunding: $125B coupon (3y $58B, 10y $42B, 30y $25B)
- Raises ~$41.7B new cash
- Coupon sizes held steady — Treasury signaling no near-term increase
- Projected $1.3T funding shortfall FY2027-28 at current coupon sizes → forward supply premium embedded

## Foreign Demand Context [WEB-2026-05-24]

- Japan (largest foreign holder): $1.24T → $1.19T (March), net seller
- Q1 2026 Japan sold $29.6B UST (largest quarterly reduction in ~4 years)
- JGB 10y yield: ~2.3% — multi-decade high, competing with currency-hedged UST returns
- Total foreign holdings: $9.49T (record Feb 2026) → declining as Japan retreats
