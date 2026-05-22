---
finding_id: qt_rs_001
topic: fed_qt_reserve_scarcity
sub_question: sq1, sq2
title: QT Reserve Supply Dynamics — RRP Buffer, TGA, and Drain Sequencing
confidence: 3
status: stable
sources:
  - wiki: "[[Quantitative_Tightening_QT_Balance_Sheet_Runoff]]"
  - wiki: "[[Fed_Overnight_Reverse_Repo_ON_RRP]]"
  - wiki: "[[Treasury_General_Account_TGA_Reserve_Swap]]"
date: 2026-05-20
---

## Core Finding

QT does not drain reserves 1-for-1. The actual path from QT to reserve scarcity runs through two buffers that absorb the shock first: **ON RRP** and **TGA drawdowns**. Understanding the drain sequencing is critical for estimating how far QT can run before reserves become scarce.

## Reserve Supply Identity

```
Bank Reserves = Fed Assets − Currency − TGA − ON RRP − Other Liabilities

ΔReserves = ΔFed_Assets − ΔTGA − ΔON_RRP − ΔCurrency
```

QT reduces Fed Assets. But reserves only fall if TGA and ON RRP do NOT fall simultaneously to offset.

## Phase 1 (2022-2023): RRP as Buffer

- QT started June 2022 at $60B/month cap (Treasuries + MBS)
- ON RRP peaked at ~$2.6T (Dec 2022) — excess MMF cash with nowhere to go (T-bill yields below RRP rate after liftoff lag)
- As QT ran, RRP drained: cash returned from ON RRP → bank deposits → reserves
- Net reserve effect of QT was muted during Phase 1 because RRP drain released pre-existing liquidity

**Mechanism:**
```
QT: Fed assets ↓ → reserves ↓
RRP drain: MMFs withdraw from ON RRP → bank deposits ↑ → reserves ↑
Net: roughly offsetting → reserves stable ~$3.3T through 2022-2023
```

## Phase 2 (2024-2025): RRP Depleted, Reserves Exposed

- ON RRP fell below $100B by late 2024 — buffer essentially exhausted
- From this point, QT directly reduces reserves with no RRP offset
- Reserves fell from ~$3.3T (peak) toward ~$3.0T range
- JPMorgan example: reserves fell $409B → $63B as bank rotated into higher-yielding USTs

## TGA as Wildcard

TGA (Treasury's checking account at Fed) creates reserve volatility independent of QT:
- TGA increase → reserves fall (Treasury "withdrawing" from banking system)
- TGA decrease (spending) → reserves rise
- Debt ceiling standoffs force TGA drawdown → temporary reserve surge → then sharp reversal when ceiling resolved

Post-debt ceiling resolution: Treasury rebuilds TGA via T-bill issuance → cash from MMFs (ON RRP drops) or from bank deposits (reserves drop). If rebuilding comes from bank deposits → reserve drain.

## Implications

With RRP buffer exhausted, the Fed is in a structurally different phase of QT:
- Each $100B of additional QT now reduces reserves by ~$80-100B (net of TGA/other)
- The remaining distance to the reserve floor is now a direct function of QT pace
- Market signal to watch: SOFR-IORB spread — when it begins rising persistently above 10-15bps, the floor is approaching
