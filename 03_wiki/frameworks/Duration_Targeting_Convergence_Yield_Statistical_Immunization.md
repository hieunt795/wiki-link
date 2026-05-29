---
node_id: duration_targeting_convergence_yield_001
type: framework
title: Duration Targeting Convergence To Yield And Statistical Immunization
aliases:
- duration targeting
- DT convergence
- yield convergence
- statistical immunization
- yield trap
- effective maturity
- trendline model duration
- hội tụ lãi suất danh mục
domain:
  primary: financial_markets
  secondary: null
tags:
- duration
- fixed_income
- bond_portfolio
- yield
- convergence
- immunization
- risk_management
confidence: 4
stability: stable
thesis: 'Duration-targeted (DT) bond portfolios — which maintain a stable duration
  through periodic rebalancing — exhibit a gravitational pull toward the initial yield
  over multi-year horizons, regardless of whether yields rise or fall; the key insight
  (Homer-Leibowitz 2013 edition): over a horizon equal to approximately 2×duration−1
  years (''effective maturity''), cumulative accruals precisely offset cumulative
  price gains/losses, making annualized return converge to the initial yield for virtually
  any yield path; this creates ''statistical immunization'' and simultaneously a ''yield
  trap'' — you cannot escape the initial yield without changing the duration target.'
source_refs:
- path: 02_sources/books/homer_leibowitz_yield_book/Homer_Leibowitz_Inside_the_Yield_Book.md
  pages: 'lines 104-520 (Part I: Duration Targeting — Introduction, Chapter 1 Trendline
    Model)'
  weight: primary
parent_node: null
related:
- node: '[[Fixed Income Relative Value Framework]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Three Types of Bond Portfolio Strategies

| Type | Duration behavior | Return objective |
|------|------------------|-----------------|
| Buy and hold | Decreases over time | Lock in initial yield (absolute return) |
| Immunization | Decreases to match liability duration | Match liability cash flows |
| Duration targeted (DT) | Maintained stable through rebalancing | Benchmark-relative or absolute with stable risk |

DT is the most common institutional approach: both active management (benchmark-relative) and passive indexing (index-matching) implicitly maintain a stable duration target through periodic rebalancing. [RAW-CLIP]

## The Convergence Mechanism

DT rebalancing: each period, sell aged bonds (shortened duration) → buy new bonds at current yield → portfolio duration returns to target D.

Two opposing forces operate:
1. **Price effect**: When yields rise, rebalancing sells into a loss (price ↓); when yields fall, rebalancing captures price gains. Price effect ≈ −Duration × yield change. [RAW-CLIP]
2. **Accrual effect**: After rebalancing at higher yields, the new accrual (coupon/yield) is higher than before. Accruals accumulate at an accelerating rate proportional to the square of the horizon. [RAW-CLIP]

Over short horizons, price effects dominate accruals. Over longer horizons, accruals increasingly dominate the constant annual price effect. [RAW-CLIP]

## The Trendline (TL) Model and Accrual Factor

For trendline paths (yield moves by equal increments each period), the **accrual factor** = (excess average accrual) / (total yield change) = (1 − 1/N) / 2, where N = horizon in years.

**Effective maturity (N*)**: The horizon at which cumulative accruals exactly offset cumulative price gains/losses → annualized return = initial yield, regardless of terminal yield. N* ≈ 2×D − 1 years (one year less than twice the duration target). [RAW-CLIP]

Example: D = 5 years → N* ≈ 9 years. Historical validation: 5-year duration DT portfolios using Barclays index (1977–2011) show annualized 6-year returns converge to starting yields. [RAW-CLIP]

## Mirror-Image Property: TL Represents Average Across All Paths

For any non-trendline path, a mirror-image path exists (same terminal yield, deviations from TL have same magnitude but opposite sign). Key result:
- Price effect (depends only on beginning/ending yield): same for all paths to a given terminal yield
- Average accrual factor: always equals the TL accrual factor for any mirror pair
- Therefore: TL return = average return across all paths to a given terminal yield [RAW-CLIP]

This gives the TL model broad generality — investors need only forecast terminal yields, not precise yield paths, to use the convergence framework. [RAW-CLIP]

## Statistical Immunization

Within the "stability window" (horizon ≈ effective maturity, approximately 2×D−1 years), DT portfolios exhibit:
1. **Low volatility**: Total multi-year volatility compresses significantly below single-period duration-based estimates. Example: 5-year DT with 100bps annual yield volatility → total volatility stabilizes at ~90bps over 6-9 year window. [RAW-CLIP]
2. **Return convergence**: Expected annualized return converges to starting yield ± tracking error
3. Consequence: Duration-based risk estimates from single-period models **overstate** multi-year bond fund risk relative to equities in asset allocation

Within this window, starting yield ± tracking error is an ex ante estimate of realized multi-year return — akin to immunization but achieved statistically rather than through cash-flow matching. [RAW-CLIP]

## The Yield Trap

The convergence property creates a "yield trap": if an investor is dissatisfied with the current yield level (believes yields will rise/fall), DT rebalancing means the initial yield strongly anchors multi-year returns regardless. [RAW-CLIP]

**Implication for rate views**: An investor who expects yields to rise cannot count on higher subsequent yields to meaningfully improve multi-year annualized returns under DT — accruals and price effects offset each other. [RAW-CLIP]

**Only escape**: Depart from the DT target — materially shorten or lengthen the duration. This changes the effective maturity and recalibrates the convergence anchor to the new yield level at the time of the duration change. [RAW-CLIP]

## Practical Implications

- **Asset allocation models** that use instantaneous duration × yield vol as multi-year bond risk significantly overstate risk → bias against bond allocations that should be corrected using multi-year convergence estimates [RAW-CLIP]
- **Rate view implementation**: Changing the rate view requires changing the DT target, not relying on yield path effects within a constant DT mandate
- **Benchmark risk**: Active bond managers benchmarked to a duration-stable index are implicitly in a DT framework → excess returns vs. benchmark will be far smaller than single-period duration differences suggest over multi-year horizons [LLM]
