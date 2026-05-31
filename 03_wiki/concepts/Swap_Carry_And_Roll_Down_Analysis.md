---
node_id: swap_carry_and_roll_down_analysis_001
type: concept
title: Swap Carry And Roll Down Analysis
aliases:
- Carry Roll-Down
- Fixed Income Carry
- Phân tích carry và roll-down swap
domain:
  primary: financial_markets
tags:
- swaps
- carry
- roll_down
- fixed_income
- relative_value
- rates_trading
confidence: 4
stability: evolving
thesis: For any interest rate swap held over a horizon period, the total P&L from
  inaction decomposes into (1) carry — net interest earned while holding the trade
  — and (2) roll-down — the mark-to-market gain from the swap aging on an unchanged
  curve; together these define the break-even rate move required to lose money on
  the position.
source_refs:
- path: 02_sources/books/howard_corb_swaps/Howard_Corb_Interest_Rate_Swaps.md
  pages: Chapter 8
  weight: primary
parent_node: null
related:
- node: '[[Asset Swap Mechanics And Spread]]'
  relation: shared_tag:swaps
- node: '[[Duration Targeting Bond Portfolio Framework]]'
  relation: shared_tag:fixed_income
- node: '[[Bond Accrual Price Effect Interaction]]'
  relation: shared_tag:fixed_income
- node: '[[Duration Targeting Convergence And Yield Trap]]'
  relation: shared_tag:fixed_income
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Core Identity
For any NPV=0 swap entered at inception:

> **Spot Price = PV(Carry) + Forward Price of Residual Swap**

Since a par swap has Spot Price = 0:

> **PV(Carry) = –Forward Price of Residual Swap**

Carry and the forward price of the residual swap are exactly equal and opposite — a direct consequence of no-arbitrage [RAW-CLIP].

## Carry
**Definition:** Net interest earned from holding the position over the investment horizon. For a receive-fixed swap:

> Carry (per period) = Fixed Rate – Floating Rate Paid

Example: receive 5.47% in a 4-year swap vs. 1Y LIBOR at 5.00% → carry = 47bps for the year [RAW-CLIP].

**Sign intuition (upward-sloping curve, receive-fixed):**
- Carry is **positive** when fixed rate > short-term LIBOR (normal curve)
- Carry is **negative** when fixed rate < short-term LIBOR (inverted curve or pay-fixed trade on upward curve) [LLM]

## Roll-Down
**Definition:** The change in the swap's mark-to-market value purely from the passage of time, assuming the **swap curve is unchanged** at the horizon date [RAW-CLIP].

Mechanism: A 4-year swap held for 1 year becomes a 3-year swap. If the 3-year rate is below the original 4-year rate (upward slope), the swap is now above-market → positive mark-to-market [RAW-CLIP].

Example: Receive-fixed 5.47% 4-year → becomes 3-year. Market 3-year rate = 5.30%. Roll-down ≈ 46.13bps upfront ≈ 17bps running [RAW-CLIP].

## Total Carry + Roll-Down
For the stylized example above:
- Carry: ~47bps (≈17.4bps running over residual)
- Roll-down: ~46.13bps (≈17.0bps running)
- **Total ≈ 93bps** for a 1-year horizon [RAW-CLIP]

## Break-Even Analysis
If rates rise by **exactly** the total carry + roll-down (expressed in bps), the position breaks even. This is the break-even rate move:

> Break-Even = Total Carry + Roll-Down (in rate space, per PV01)

Positions with high carry + roll-down are more resilient to adverse rate moves — a key metric in relative value selection [RAW-CLIP].

## Relationship to Forward Rate
Carry + roll-down is also equivalent to the **difference between the forward rate and the spot rate**:
- Forward rate = break-even rate (no-arbitrage)
- If realized rate < forward rate → position makes money beyond carry
- The forward rate is not a prediction; it is the market's "no-profit" level [LLM]

## Key Trade Intuition
On an upward-sloping curve:
- **Receive-fixed trades** have **positive carry + roll-down** — you get paid to hold.
- **Pay-fixed trades** have **negative carry + roll-down** — the curve works against you while you hold.
- This is why curve flatteners (receive long-end, pay short-end) often have negative carry on the short leg even if the view is directionally correct [LLM].


