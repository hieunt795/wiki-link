---
finding_id: qt_rs_002
topic: fed_qt_reserve_scarcity
sub_question: sq3
title: Reserve Scarcity Signals — What to Watch and Why
confidence: 3
status: stable
sources:
  - wiki: "[[Reserve_Floor_Payment_System_Demand]]"
  - wiki: "[[Repo_Market_Mechanics_Triparty_Bilateral]]"
  - wiki: "[[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]]"
date: 2026-05-20
---

## Core Finding

Reserve scarcity does not arrive as a cliff — it manifests through a progressive deterioration in repo market functioning. Four observable signals, in order of leading to lagging:

## Signal 1 — Payment Delay Increase (Most Leading)

Banks facing low opening reserve balances shift to "receipt-reactive" payment behavior: they delay sending outgoing Fedwire payments until they receive incoming payments first.

**Observable:** Intraday payment timing data (Fed internal; not publicly real-time)  
**Threshold:** One-std-dev increase in trailing payment delay → ~7bps SOFR-IORB rise [RAW-BOOK Duffie §II]  
**Limitation:** Not publicly observable in real time; retrospective analysis only

## Signal 2 — SOFR-IORB Spread (Core Signal)

SOFR measures the weighted median cost of overnight Treasury repo. IORB is the Fed's floor rate. Under ample reserves, SOFR should trade close to (but slightly below) IORB.

```
Normal:       SOFR ≈ IORB − 5bps to IORB
Elevated:     SOFR > IORB by 10-15bps → elevated but manageable
Stressed:     SOFR > IORB by 25bps+ → reserve scarcity signal
Crisis:       Sep 17, 2019: SOFR = IORB + 315bps (repocalypse)
```

**Watch:** FRED series SOFR and IORB; sustained spread above 15bps = Fed should respond  
**Quarter-end adjustment:** SOFR spikes at quarter-ends are FBO-driven balance window-dressing — not structural scarcity. Distinguish temporary (1-2 day) from persistent (week+) elevation.

## Signal 3 — SOFR-FF Basis (Companion Signal)

SOFR-EFFR spread > 6bps (outside normal range) signals repo market stress rather than structural reserve scarcity. Typically seen during period-end effects.

**Watch:** When SOFR-EFFR and SOFR-IORB both elevate simultaneously → more serious than period-end effect

## Signal 4 — SRF Usage and Discount Window (Lagging)

SRF (Standing Repo Facility) allows primary dealers and depository institutions to borrow reserves overnight against UST/agency collateral at a premium above IORB. Elevated SRF usage = dealers are unable to fund in the market at reasonable rates.

**Caveat:** SRF currently stigmatized — banks reluctant to use even when needed. Usage may understate actual stress. [RAW-BOOK Duffie §I.A]

## Composite Dashboard

| Indicator | Source | Frequency | Scarcity Threshold |
|-----------|--------|-----------|-------------------|
| SOFR-IORB spread | FRED | Daily | >15bps persistent |
| SOFR-EFFR spread | FRED | Daily | >6bps persistent |
| Reserve balances (WALCL components) | Fed H.4.1 | Weekly | Declining trend below $3T |
| ON RRP balance | FRED RRPONTSYD | Daily | <$100B (buffer gone) |
| SRF usage | NY Fed | Daily | Any non-trivial usage |
| Swap spread (10yr) | BBG | Daily | More negative → dealer constraints |

## Sep 2019 Retrospective as Calibration Point

**What happened:** System reserves fell to ~$1.4T; SOFR spiked 315bps above IORB  
**Trigger:** Combination of (a) large Treasury settlement ($54B), (b) corporate tax payments, (c) JPMorgan refusing to lend reserves despite having them  
**Key lesson:** Reserves can appear "ample" in aggregate but be maldistributed — certain large banks hoard rather than lend due to LCR/regulatory constraints. The distribution of reserves matters as much as the level. [RAW-BOOK Reserve Floor node]

**Implication for current cycle:** Even with $3T+ system-wide reserves, scarcity can emerge at specific dealers if they have rotated into USTs (like JPMorgan's $409B → $63B). Aggregate reserve level is a necessary but not sufficient condition.
