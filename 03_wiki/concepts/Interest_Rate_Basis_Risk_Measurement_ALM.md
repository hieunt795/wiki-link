---
node_id: interest_rate_basis_risk_measurement_alm_001
type: concept
title: Interest Rate Basis Risk Measurement in ALM
aliases:
- basis risk ALM
- multi-curve ALM framework
- EURIBOR OIS basis spread
- tenor basis swap ALM
- rủi ro cơ sở lãi suất ALM
- đa đường cong chiết khấu ALM
- chênh lệch EURIBOR OIS
domain:
  primary: alm
  secondary: []
tags:
- basis-risk
- multi-curve
- tenor-basis
- gap-analysis
- key-rate-duration
confidence: 3
stability: stable
thesis: 'Interest rate basis risk derives from imperfect correlation between rates
  to which different instruments are indexed; the global financial crisis dramatically
  increased the volatility of quoted basis spreads, which were previously essentially
  stable. Gap analysis measures NII sensitivity over 1–2 year horizons; the economic
  value approach captures long-term effects of rate changes via present value of all
  cashflows. BCBS IRRBB 2016 requires both earnings and economic value perspectives.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 4: Basis Risk and Key Rate Durations in ALM'
parent_node: null
related:
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[NMD_Decay_Model_Volume_Segmentation]]'
  relation: related_to
- node: '[[Hedge_Accounting_IFRS9_ALM]]'
  relation: related_to
- node: '[[IRRBB]]'
  relation: related_to
- node: '[[EURIBOR]]'
  relation: related_to
- node: '[[OIS]]'
  relation: related_to
- node: '[[NII]]'
  relation: related_to
- node: '[[PV01]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Two Perspectives on Interest Rate Risk

Two possible perspectives for measuring and managing interest rate risk: [RAW-Elkenbracht-Huizing ch.4 p.1]

**Earnings perspective (NII):** concentrates on the effects of interest rate movements on NII over short time horizons (1–2 years). Simple to implement via gap analysis; directly targets the income statement. Weakness: may fail to indicate long-term impacts — mismatches can be hidden beyond the analysis horizon.

**Economic value perspective (EVE):** based on the present value of all cashflows; addresses long-term effects of rate changes. Can serve as a lead indicator for prospective earnings impact. Weakness: does not focus on time distribution of cashflows — effects are condensed into a single present-valued figure.

Many banks (especially smaller) prioritize earnings over economic value. Optimal management combines both perspectives. [RAW-Elkenbracht-Huizing ch.4 p.1]

## Regulatory Treatment (BCBS IRRBB 2016)

Banking book positions are subject to IRRBB under Pillar 2 (not Pillar 1 minimum capital). BCBS IRRBB 2016 requires: [RAW-Elkenbracht-Huizing ch.4 p.2]

- Risk systems must address IRRBB for **all assets, liabilities, and off-balance-sheet positions**.
- Measurement using **both earnings and economic value** approaches under wide and appropriate range of interest rate shocks and stress scenarios.
- IRRBB included in ICAAP — banks self-assess capital sufficiency.
- **Outlier test:** theoretical decline of EVE by more than **15% of Tier 1 capital** under 6 regulator-prescribed interest rate shocks triggers supervisory review; additional capital and mitigation can be required.

## Basis Risk — Definition and Sources

Basis risk derives from **imperfect correlation between the rates to which different instruments are indexed**, even if their coupon structure is similar or identical. If rates do not move in sync, a mismatch arises. [RAW-Elkenbracht-Huizing ch.4 p.2]

Sources of basis risk: [RAW-Elkenbracht-Huizing ch.4 p.2]

1. **Different rate types:** e.g., a loan priced on the prime rate funded by a EURIBOR/LIBOR liability. The prime rate adjusts only by discrete amounts (e.g., 50bp) and its differential with money market rates can drift substantially.
2. **Adjustable rate loans indexed to average cost of funding:** the funding cost index cannot be recalculated daily, creating a lag versus market rates.
3. **Retail deposit rates:** typically lower than market rates; FTP systems represent these as portfolios of market rates that replicate actual exposures based on historical correlations — the true repricing characteristics should not be hidden by the measurement system.
4. **Spreads between floating rates with different repricing schedules or currencies:** e.g., 3M vs 6M EURIBOR tenor basis, or cross-currency basis swaps.

The **global financial crisis dramatically increased the volatility of quoted basis spreads** which were previously essentially stable. Since mid-2007, basis spreads became a fundamental variable and a top priority for banking book risk management. [RAW-Elkenbracht-Huizing ch.4 p.2]

## Gap Analysis

Gap analysis measures the effect of a yield curve shift on NII over a short-term horizon. Despite a move towards simulation techniques, it is still widely used — especially in small to medium-sized banks. [RAW-Elkenbracht-Huizing ch.4 p.3]

A **gap** = the difference in one time bucket between interest rate sensitive assets, liabilities, and off-balance-sheet items. An item is "interest rate sensitive" if it matures, amortises, or its coupon can change during the bucket.

- **Positive gap** (asset-sensitive): more assets than liabilities reprice at higher rates → NII benefits from rate increases.
- **Negative gap** (liability-sensitive): opposite effect.

Standard time bucketing: O/N, O/N–1M, 1M–3M, 3M–6M, 6M–12M, above 1Y. [RAW-Elkenbracht-Huizing ch.4 p.3]

## Economic Value of Equity (EVE) and Duration

The chapter covers EVE sensitivity and duration, key rate duration, convexity, option-adjusted value and duration, and term structure of interest rates (single-curve and multi-curve approaches) including the yield curve construction evolution post-crisis (OIS discounting and tenor basis). [RAW-Elkenbracht-Huizing ch.4 p.1]
