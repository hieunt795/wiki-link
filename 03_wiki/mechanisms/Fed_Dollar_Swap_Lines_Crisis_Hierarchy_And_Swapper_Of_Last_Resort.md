---
node_id: fed_dollar_swap_lines_crisis_hierarchy_001
type: mechanism
title: Fed Dollar Swap Lines Crisis Hierarchy and Swapper of Last Resort
aliases:
- Fed swap lines
- FX swap basis indicator
- dollar swap network
- swapper of last resort
- FX swap as currency repo
- cơ chế hoán đổi đô la khẩn cấp
- mạng lưới hoán đổi đô la
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- swap-lines
- fed
- FX-swap
- dollar-shortage
- FIMA
- crisis-mechanism
- lender-of-last-resort
- March-2020
confidence: 3
stability: stable
thesis: 'During dollar funding stress, private FX swap market makers withdraw in a
  predictable sequence (small participants → NY foreign bank branches → US G-SIB dealers)
  before the Fed activates dollar swap lines at OIS+25bps as the public dealer of
  last resort. The FX swap basis spread is the primary real-time indicator of offshore
  dollar scarcity. The Fed, as "swapper of last resort," has expanded its swap line
  network after every crisis (GFC 2008, Repocalypse 2019, COVID 2020, SVB 2023),
  gradually transforming swap lines from backstop to casual dollar supply tool.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's Dollar Swap Network; The Federal Reserve's Gambit
  weight: primary
related:
- node: '[[USD_Swap_Lines_Geopolitical_Dollar_Integration_Tool]]'
  relation: mechanism_behind_geopolitical_tool
- node: '[[Global_Dollar_System_Eurodollar_Architecture]]'
  relation: component_of
- node: '[[Eurodollar_System_Mechanics_And_Post_Reform_Decline]]'
  relation: offshore_dollar_funding_channel
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: analogous_domestic_facility
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## FX Swap as "Currency Repo"

An FX swap (also called "currency repo") is a simultaneous spot purchase and forward sale of a currency pair. Structure:

```
Party A sells USD spot → receives EUR at spot rate
Party A buys USD forward → delivers EUR at preset forward rate

Key property: payments only occur at swap maturity → booked OFF balance sheet
(unlike standard repo = ON balance sheet)
```

The FX swap basis = difference between the cost of borrowing dollars via FX swap vs. the cost in the cash market. **Negative basis = offshore dollars scarcer than onshore** → the primary real-time indicator of global dollar shortage. [RAW-CLIP Conks Fed Policies]

## Dollar Funding Hierarchy During Stress

Private market makers pull back in a predictable sequence during dollar stress:

| Tier | Provider | Role | Behavior Under Stress |
|------|----------|------|----------------------|
| 1st (normal) | FX swap dealers (buy-side, non-bank) | Price-taker arbitrageurs | First to disappear |
| 2nd | NY branches of foreign banks | "Private dealers of first resort"; lax regulation → can step in | Pull back when internal protocols breached |
| 3rd | US G-SIB megabanks (JPMorgan, etc.) | "Private dealers of last resort"; large reserve cushions | Pull back due to Basel III capital/leverage constraints |
| 4th (crisis) | **Fed swap lines** | "Public dealer of last resort" | Activated only when all private tiers fail |

[RAW-CLIP Conks Dollar Swap Network — March 2020 sequence]

## Swap Line Mechanics

**Structure:**
```
Foreign CB (e.g. ECB, BOJ) → draws on swap line with Fed
  → receives USD at spot; promises to return at forward rate
  → cost: OIS (overnight indexed swap rate) + 0.25%

Foreign CB → distributes USD to domestic banks via local repo or lending
  → domestic banks → repay foreign CB → foreign CB repays Fed
```

**March 2020 activation:** Fed + G7 central banks announced swap line resurgence on March 15, 2020. The "unlimited" dollar provision at OIS+25bps caused:
- FX swap basis spreads to collapse from extreme negative to near-zero
- Private dealers returned once volatility fell within internal risk limits
- Total swap line usage peaked at ~$450B at the height of COVID stress

## FIMA Facility (China/Non-Swap-Line Countries)

For countries without formal Fed swap lines (e.g., China), the FIMA repo facility allows foreign CBs to post their Treasury holdings at the NY Fed in exchange for dollar repo. FIMA serves as the "outer ring" of the dollar backstop — less privileged than swap lines (Treasury collateral required), but accessible without formal bilateral agreement. [RAW-CLIP Conks Gambit]

## Trend: Backstop → Casual Dollar Supply Tool

Each crisis has prompted faster, larger swap line activation:
- 2007: First swap lines enacted for rising turmoil
- 2008 (GFC/Lehman): Doubled maximum, activated for all G7 CBs
- 2020 (COVID): "Unlimited" activation within 10 days of stress onset
- 2023 (SVB/Credit Suisse): Swap lines activated preemptively at "first sign of hazard"

Implication: The faster the Fed responds, the more the private market relies on Fed as backstop rather than self-insuring. This creates a structural pull toward expanding the Fed's global dollar authority. [LLM synthesis from RAW-CLIP]

