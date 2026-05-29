---
node_id: bond_accrual_price_effect_interaction_001
type: mechanism
title: Bond Accrual Price Effect Interaction
aliases:
- Accrual vs Price Effect
- Coupon Reinvestment Offset
- Tương tác tích lũy lãi suất và giá trái phiếu
domain:
  primary: financial_markets
tags:
- fixed_income
- duration
- coupon_reinvestment
- bond_return_decomposition
confidence: 3
stability: evolving
thesis: Over a multi-period horizon, a bond portfolio's coupon accruals (reinvestment
  income) accumulate roughly as the square of the horizon while price effects are
  linear — meaning accruals dominate price effects at long horizons, and this asymmetry
  is the engine behind DT convergence.
source_refs:
- path: 02_sources/books/homer_leibowitz_yield_book/Homer_Leibowitz_Inside_the_Yield_Book.md
  pages: Chapter 1-2
  weight: primary
parent_node: null
related:
- node: '[[Duration Targeting Bond Portfolio Framework]]'
  relation: shared_tag:fixed_income
- node: '[[Asset Swap Mechanics And Spread]]'
  relation: shared_tag:fixed_income
- node: '[[Duration Targeting Convergence And Yield Trap]]'
  relation: shared_tag:fixed_income
- node: '[[Swap Carry And Roll Down Analysis]]'
  relation: shared_tag:fixed_income
- node: '[[DV01, Duration, and Convexity — Fixed Income Risk Measures]]'
  relation: shared_tag:duration
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Return Decomposition
Total bond return over horizon H decomposes into three components [RAW-CLIP]:

1. **Coupon income:** Deterministic, accrues at rate ≈ Y₀ per period
2. **Reinvestment income:** Earned on re-invested coupons; grows as ≈ Y_avg × (H²/2) — proportional to H²
3. **Price effect:** Capital gain/loss from duration exposure = –D × ΔY; proportional to H (linear)

## Asymmetric Accumulation
The key asymmetry:

| Component | Scales with |
|-----------|-------------|
| Reinvestment income | H² (quadratic) |
| Price effect | H (linear) |

At short horizons (H << D), price effects dominate — this is why short-horizon bond returns are volatile [RAW-CLIP].

At long horizons (H >> D), reinvestment income dominates — the portfolio's return converges to Y₀ regardless of path. This is the mechanism behind DT convergence and statistical immunization [RAW-CLIP].

## Crossover Point
The crossover — where accrual effects first balance price effects — occurs approximately at H ≈ 2D (the effective maturity). Beyond this point, the accumulated reinvestment gains exceed any price loss from adverse yield moves [RAW-CLIP].

## Practical Implication: Risk Horizon Scaling
For risk management, this mechanism means:
- **Short-horizon (H < D):** Duration risk dominates → use modified duration / DV01 for risk
- **Medium-horizon (H ≈ D):** Mixed regime → both components material
- **Long-horizon (H > 2D):** Reinvestment risk (rate path uncertainty) dominates → DV01 understates total risk [LLM]

Portfolio managers with long liabilities (pension funds, insurers) must model the reinvestment component explicitly — using only DV01 as a risk measure structurally underestimates long-horizon interest rate risk [LLM].


