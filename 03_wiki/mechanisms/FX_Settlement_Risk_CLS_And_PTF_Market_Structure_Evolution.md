---
node_id: fx_settlement_risk_cls_ptf_001
type: mechanism
title: FX Settlement Risk, CLS, and PTF Market Structure Evolution
aliases:
- FX settlement risk
- Herstatt risk
- Continuous Linked Settlement
- CLS bank
- principal trading firms FX
- PTF market makers
- FX market structure
- rủi ro thanh toán FX
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
tags:
- fx-market
- settlement-risk
- CLS
- Herstatt
- PTF
- market-structure
- dealer-banks
- HFT
confidence: 3
stability: stable
thesis: 'FX settlement risk — the risk one party delivers currency but the counterparty
  fails to deliver (Herstatt risk, 1974) — was structurally mitigated by CLS Group
  (2002) via payment-vs-payment (PvP) settlement. Simultaneously, the FX dealer oligopoly
  eroded: from voice brokers → EBS/Reuters (1992) → single-bank platforms (2001)
  → multi-dealer ECNs → algo trading (2004) → principal trading firms (PTFs) like
  Jump Trading and XTX Markets entering the interdealer market post-GFC, displacing
  bank proprietary desks constrained by regulation.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Global Dollar and Eurodollar Systems.md
  pages: The Foreign Exchange Evolution
  weight: primary
related:
- node: '[[Global_Dollar_System_Eurodollar_Architecture]]'
  relation: component_of
- node: '[[Eurodollar_System_Mechanics_And_Post_Reform_Decline]]'
  relation: shares_fx_structure
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: parallel_settlement_structure
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## Herstatt Risk — Why FX Settlement Is Dangerous

In 1974, German bank Bankhaus Herstatt was shut by regulators mid-business-day. Counterparties had already delivered DEM to Herstatt but never received USD legs — because New York had not yet opened. Global FX payments halted; credit contracted. This "Herstatt risk" (settlement leg failure due to time-zone mismatch between currency payment windows) became the defining FX systemic risk problem of the 20th century.

**Magnitude:** In a $7.5T/day FX market, settlement failure of even a single large counterparty creates a self-reinforcing freeze — banks stop sending payments until the other leg is confirmed, causing cascading liquidity withdrawal. [RAW-CLIP]

## Continuous Linked Settlement (CLS) — 2002 Solution

CLS Group, implemented by the major FX players and regulators in 2002, provides **payment-vs-payment (PvP)** settlement: payment leg A is released only if payment leg B is confirmed simultaneously. The mechanism:

```
Bank A → sends EUR → CLS → holds until
Bank B → sends USD → CLS → releases both simultaneously
```

CLS survived the 2008 GFC intact, validating its design. [RAW-CLIP Conks FX Evolution]

**Coverage:** Majority of interbank FX volume now settles via CLS; non-CLS settlement retains Herstatt exposure (bilateral settlement with credit risk).

## FX Market Structure Evolution (1980s → present)

| Era | Structure | Dominant Mechanism |
|-----|-----------|-------------------|
| 1980s | Voice brokers + interdealer | Manual phone, EBS/Reuters not yet |
| 1992 | Reuters electronic brokerage → EBS | Electronic price discovery begins |
| 2001+ | Single-bank platforms (SDPs) | UBS, Barclays, Goldman Sachs internal ECNs |
| 2004 | Algo trading on EBS/Reuters | 60% volume algorithmic by ~2007 |
| Post-GFC | PTFs enter interdealer market | Non-banks match/exceed bank dealers |

**Key dynamic:** EBS/Reuters EUR-USD and USD-JPY quotes became the de facto global FX price → then bank proprietary desks shrank (Basel/Volcker) → PTFs (Jump Trading, XTX Markets) filled the market-making gap.

## Principal Trading Firms (PTFs) and the Algo Revolution

PTFs are non-bank, HFT-style market makers who:
- Do not rely on client flow for profitability → compete on latency and model quality
- Originally in arbitrage only → now substantial interdealer liquidity providers
- XTX Markets, Jump Trading now in top-10 FX liquidity providers

**Implication for systemic risk:** PTF liquidity is more fragile than bank dealer liquidity — PTFs can step back during stress (no regulatory obligation, no client relationship), creating sudden liquidity air pockets not present when bank dealers dominated. [LLM synthesis from RAW-CLIP]

## Asian Dollar Market (Singapore / ACU Banks)

Parallel to the European Eurodollar: Bank of America negotiated with Singapore MAS in the late 1960s to create Asian Currency Units (ACUs) — independent branches booked offshore, engaging in dollar maturity transformation via SIBOR (Singapore Interbank Offered Rate). 

Key points:
- Singapore chosen over Tokyo (exchange rate controls) and Hong Kong (15% interest tax)
- ACUs issued CDs, time deposits, dollar bonds; lent at SIBOR + spread
- Singapore grew to ~10% of global FX turnover; Tokyo ~4.5%; Hong Kong ~7%
- ACU structure abolished post-GFC as Asian and European dollar markets converged
- Post-reform: Singapore operates as an integrated dollar center, not a separate "Asian dollar" system [RAW-CLIP]

