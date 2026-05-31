---
node_id: dv01_duration_001
type: indicator
indicator_type: sensitivity
title: DV01, Duration, and Convexity — Fixed Income Risk Measures
aliases:
- DV01
- dollar value of a basis point
- duration
- modified duration
- Macaulay duration
- convexity
- độ nhạy lãi suất
- thời lượng trái phiếu
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
tags:
- fixed-income
- duration
- DV01
- convexity
- interest-rate-risk
- bond-math
confidence: 5
stability: stable
thesis: 'DV01 (dollar value of a basis point) measures the price change of a fixed
  income instrument for a 1bp parallel shift in yields. Duration (modified) is the
  percentage price sensitivity; convexity captures the curvature — the fact that price-yield
  relationship is non-linear. Together they form the fundamental risk language for
  all fixed income positions: hedging, relative value, and P&L attribution.

  '
source_refs:
- path: 02_sources/books/tuckman_serrat_fixed_income/Tuckman_Serrat_Fixed_Income_2022.md
  pages: Ch.4, Ch.5
  weight: primary
parent_node: null
related:
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: applied_in
- node: '[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]'
  relation: measured_by
- node: '[[Duration Targeting Bond Portfolio Framework]]'
  relation: shared_tag:duration
- node: '[[Bond Accrual Price Effect Interaction]]'
  relation: shared_tag:duration
- node: '[[Duration Targeting Convergence And Yield Trap]]'
  relation: shared_tag:duration
- node: '[[Financial Repression Distributional Welfare Effects]]'
  relation: shared_tag:duration
- node: '[[QE Duration Extraction from Private Sector]]'
  relation: shared_tag:duration
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Core Definitions

### DV01 (Dollar Value of a Basis Point)

```
DV01 = -ΔPrice / Δy  where Δy = 0.0001 (1 basis point)

Approximation: DV01 ≈ Price × Modified_Duration / 10,000
```

DV01 is the absolute sensitivity in dollar terms. For a $1M face 10-year UST trading near par with duration ~9, DV01 ≈ $900.

### Modified Duration

```
Modified Duration = Macaulay Duration / (1 + y/m)
  where y = yield, m = compounding periods per year

% Price Change ≈ -Modified Duration × Δy
```

Macaulay Duration = weighted average time to cash flows (weights = PV of cash flow / total PV).

### Convexity

```
Price Change = -Duration × Δy × Price + ½ × Convexity × (Δy)² × Price

Convexity > 0: price rises more than duration predicts for rate ↓;
               price falls less than duration predicts for rate ↑
```

**Positive convexity** (plain bonds): always benefits the holder — larger gains, smaller losses, vs. duration-only approximation.  
**Negative convexity** (callable bonds, MBS): price is capped when rates fall because the issuer calls/prepays.

## Key Orders of Magnitude

| Instrument | Approx Duration | DV01 per $1M face |
|-----------|----------------|------------------|
| 3-month T-bill | 0.25 | $25 |
| 2-year UST | ~1.9 | $190 |
| 5-year UST | ~4.5 | $450 |
| 10-year UST | ~8.5-9.0 | $850-900 |
| 30-year UST | ~18-20 | $1,800-2,000 |
| 10-year interest rate swap | ~8-9 (DV01 on PV) | ~$800-900 |

## Multi-Factor Extensions

**Key-rate DV01s** (partial DV01s): sensitivity to individual par-rate tenors rather than a parallel shift. Essential for yield-curve trades — a 2s10s steepener has zero parallel DV01 but large key-rate DV01 at 2y and 10y.

**Forward-bucket DV01s**: sensitivity to forward rates across tenor buckets; used in mortgage/convexity hedging.

## P&L Attribution

Daily bond P&L attribution:
```
P&L ≈ Carry (daily accrual)
     + Roll-down (slide down the curve)
     + Duration effect (-Duration × Δy_parallel × Price)
     + Twist effect (key-rate DV01 × Δy_curve)
     + Convexity effect (½ × Convexity × (Δy)² × Price)
     + Residual
```

## Hedging Applications

1. **Duration-neutral hedge**: match DV01 of long position with short DV01 of hedge instrument
2. **Curve hedge**: match key-rate DV01s to isolate specific curve segment
3. **Futures hedge**: Tuckman notes that futures have a "tail effect" — carry on the variation margin position modifies the effective DV01 of a futures hedge vs. an equivalent cash position
4. **Swap overlay**: interest rate swaps can be sized by DV01 to hedge bond portfolio rate risk without selling bonds (avoids transaction costs, preserves credit exposure)

