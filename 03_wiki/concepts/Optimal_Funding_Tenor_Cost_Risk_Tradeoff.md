---
node_id: optimal_funding_tenor_cost_risk_tradeoff_001
type: concept
title: 'Optimal Funding Tenors: Cost-Risk Tradeoff for Uncollateralised Derivatives
  and ALM'
aliases:
- Funding tenor optimisation
- Short-term vs long-term funding tradeoff
- FVA funding tenor
- Tối ưu kỳ hạn tài trợ vốn
- Chi phí tài trợ và rủi ro thanh khoản
domain:
  primary: alm
tags:
- funding_tenor
- fva
- liquidity_risk
- cost_of_funds
- regulatory_liquidity_cost
- wholesale_funding
- alm
confidence: 1
stability: stable
thesis: '[LLM] The choice of wholesale funding tenor involves a fundamental tradeoff:
  short-term funding benefits from the normally upward-sloping funding spread curve
  (lower cost of funds) but creates rollover and repricing risk; long-term funding
  eliminates liquidity risk but introduces overborrowing inefficiencies (high bid-offer
  costs) and pays a larger term premium. [LLM] Regulatory requirements (LCR''s short-term
  liquidity charge, NSFR''s stable funding cost) create additional non-linear tenor
  costs that shift the optimal tenor toward longer funding than pure carry optimisation
  would suggest.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Ch 22 — Optimal Funding Tenors (Barclays)
  weight: primary
parent_node: null
related:
- node: '[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]'
  relation: related_to
- node: '[[Secured_Funding_Instruments_Repo_Covered_Bond_Abs]]'
  relation: related_to
- node: '[[Bank_Capital_Structure_And_Capital_Management_Alm]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## The Core Problem

[LLM] For a bank holding an uncollateralised derivative with positive MTM, the full MTM must be funded at all times at the unsecured funding rate. On each business day, the bank decides: how long to raise that funding for? This decision is the "funding tenor" choice, and it has persistent economic consequences across the life of the trade.

The funding cost has four components:
1. **Libor/reference rate charge:** The base cost of borrowing at the reference rate (OIS or Libor). This largely offsets the MTM evolution of the trade on an expected basis; it is the "riskless" borrowing cost.
2. **Cost of funds:** The spread of the bank's unsecured funding rate over the reference rate. The key tenor-sensitive component.
3. **Bid-offer charge:** Friction cost (~10bp spread) incurred when both borrowing and lending money. Overborrowing (raising more than the net MTM, then lending excess back) amplifies this cost.
4. **Regulatory liquidity cost:** An additional tenor-based spread reflecting the cost of regulatory requirements (LCR short-term buffer charges, NSFR stable funding charges). Shape: typically higher for short tenors (LCR) and lower for long tenors (NSFR if already satisfied).

## Short-Term Strategy vs Long-Term Strategy

The chapter presents a direct comparison on a £10M receiver swap (10-year maturity, positive MTM initially) funded semi-annually using the same simulation framework for 10 years.

**Assumed spreads:**
- 6M funding spread: 50bp over reference rate
- 5Y funding spread: 250bp over reference rate
- Bid-offer: 10bp flat
- 6M regulatory spread: 30bp; 5Y regulatory spread: 10bp

| Cost Component | Short-Term Strategy | Long-Term Strategy |
|----------------|--------------------|--------------------|
| Cost of funds (expected, 10Y) | ~£25,000 (50bp × £0.5M avg × 10Y) | ~£220,000 (higher spread + correlation effect) |
| Bid-offer (expected, 10Y) | ~£5,000 (10bp × £0.5M × 10Y) | ~£32,000 (overborrowing → bidoffer on both sides) |
| Regulatory liquidity (expected, 10Y) | ~£15,000 (30bp × £0.5M × 10Y) | ~£5,000 (long-term funding exempted) |
| Liquidity risk | High (rollover risk at 6M intervals) | Low (no rollover needed for 10 years) |

[LLM] Key insight: short-term strategy is cheaper in expected total cost but exposes the bank to funding spread volatility and rollover risk. Long-term strategy eliminates liquidity risk but creates overborrowing (the 5-year funding instrument persists while MTM changes, so new funding is added on top of existing — creating gross borrowing well above the net MTM). This overborrowing drives up bid-offer costs substantially.

## Advanced Strategies

**Matched funding (fund to expected cashflows):** Appropriate for sticky payoffs (fixed bonds). Fund each expected cashflow bucket separately. Eliminates liquidity risk for static cashflows but still has rollover risk for dynamic portfolios.

**Term strategy (constant weighted average life):** [LLM] An interpolation between short and long. Specify a percentage-tenor pair (e.g., 50% to 1Y + 50% to 2Y). At each stopping date, only expired instruments are replaced. This keeps the WAL constant. Note: in the example of 50%-1Y + 50%-2Y with annual rebalancing, the realised WAL is only 1.5 years (not 2 years), because 2Y instruments age to 1Y before replacement.

**Forward volatility cone strategy:** [LLM] Fund not to the expected MTM but to a lower percentile (e.g., the 16th percentile — approximately 1 standard deviation below the mean). This shortens average funding tenor compared to matched funding, reducing cost-of-funds, while accepting slightly higher overfunding in tail scenarios (16% of cases vs 50% for matched funding). Reduces overborrowing and hence bid-offer cost.

**Limit strategy:** Sets hard limits on the mismatch between funding profile and expected cashflow profile. Allows tenor shortening (cost reduction) subject to a maximum tolerated funding gap.

**Buffer strategy:** Overborrow a fixed amount long-term (the "buffer") to capture small MTM fluctuations without short-term borrowing; lend the excess short-term. Reduces regulatory liquidity charges while avoiding large bid-offer costs from frequent overborrowing.

## Efficient Frontier

[LLM] By running multiple funding strategies across the spectrum from short to long, a bank can construct an efficient frontier of expected cost vs liquidity risk (measured as standard deviation of funding cost, or the 95th percentile). The optimal strategy is the point on this frontier matching the bank's cost-risk appetite.

Key parameters driving the frontier shape:
- The slope of the funding spread curve (steeper → stronger incentive to fund short)
- Correlation between funding spreads and derivative MTM (negative correlation → funding costs rise precisely when MTM is high, amplifying long-tenor cost)
- The regulatory spread curve shape (high short-term regulatory spreads → penalise very short funding)

## Theoretical Foundation (FVA)

[LLM] Under risk-neutral assumptions with deterministic funding spreads (Piterbarg 2010; Burgard-Kjaer 2011), the funding adjustment (FVA) is independent of the funding tenor chosen — because forward funding rates are realised by assumption. The practical value of tenor optimisation arises precisely because real-world funding rates do not always realise their forwards (rollover risk is real risk), and regulatory costs are non-linear in tenor.

The chapter adopts OIS as the reference rate (the risk-free benchmark post-2008) rather than Libor (which includes a bank credit premium). Choosing Libor vs OIS changes the decomposition of the funding adjustment but not the total funding-adjusted MTM.
