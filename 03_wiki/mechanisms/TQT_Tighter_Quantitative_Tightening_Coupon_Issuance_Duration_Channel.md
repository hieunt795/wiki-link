---
node_id: tqt_coupon_duration_tightening_001
type: mechanism
title: TQT Tighter Quantitative Tightening Coupon Issuance Duration Channel
aliases:
- TQT Tighter Quantitative Tightening
- coupon issuance tightening
- Treasury duration tightening
- Janet Yellen TQT
- thắt chặt định lượng mạnh hơn
domain:
  primary: fiscal_policy
  secondary: monetary_policy
tags:
- tqt
- qe
- coupon_issuance
- duration
- treasury
- tightening
- risk_assets
confidence: 1
stability: stable
thesis: "TQT (Tighter Quantitative Tightening) — when the U.S. Treasury shifts issuance from short-term bills toward longer-duration coupon bonds (notes and bonds) — is more effective at tightening financial conditions than standard QT, because duration risk forces investors to reassess risk tolerance and sell riskier assets to offset the new duration exposure; the Treasury (not the Fed) controls this dimension of financial tightening."
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: batches 39-41 (chars ~225000-248000)
  weight: primary
related:
- node: '[[Treasury QE Duration Swap RRP Drain Mechanisms]]'
  relation: inverse_of
- node: '[[Fed Balance Sheet Size And Policy Rate Independence]]'
  relation: context
- node: '[[Treasury Buybacks Sovereign Debt Liquidity Intervention]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Why the Treasury Controls QT's Tightening Power

Standard Fed QT (rolling off $95B/month from balance sheet) removes reserves and deposits, but:
- Treasury can offset this by issuing only short-term bills → absorbed easily with no risk repricing
- Markets don't need to sell riskier assets to fund T-bill purchases (0 additional duration risk)
- Result: QT drains reserves but doesn't tighten financial conditions meaningfully [RAW-CLIP]

**Key insight**: The U.S. Treasury — not the Fed — dictates how much tightening QT delivers, by choosing the maturity composition of its new issuance. [RAW-CLIP]

## TQT Mechanism (Coupon Bond Issuance → Duration → Asset Sales)

When Treasury shifts toward coupon bonds (notes 2-10yr, bonds 30yr):

1. **Investors buy coupon bonds** → must accept meaningful duration risk (interest rate sensitivity)
2. **Risk management response** → investors sell riskier assets (equities, credit, etc.) to offset the added interest rate exposure
3. **Asset price pressure** → lower risk appetite, higher credit spreads, equity P/E compression
4. **Markets front-run** → once Treasury *announces* increased coupon issuance, markets pre-emptively sell risk assets [RAW-CLIP]

## Historical Instance (2023)

Treasury Secretary Yellen announced large increases in coupon issuance (Q3 2023: +$185B duration, Q4 2023: +$339B) → triggered a fast front-running selloff in risk assets even before bonds were issued. [RAW-CLIP]

## TQT vs QT vs QE Summary

| Tool | Who Controls | Mechanism | Effect |
|------|-------------|-----------|--------|
| QE | Fed | Buy bonds, issue reserves | Easing |
| QT | Fed | Roll off bonds, drain reserves | Mild tightening |
| **TQT** | **Treasury** | **Issue coupon bonds (duration)** | **Stronger tightening** |
| Treasury QE | Treasury | Buy back bonds, inject reserves/RRP drain | Easing |
| Not-QE (BTFP etc.) | Fed | Repo/liquidity facilities | Stealth easing |
