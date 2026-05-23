---
node_id: reserve_floor_payment_001
type: mechanism
title: Reserve Floor — Payment System Demand and the Minimum Ample Level
aliases:
- reserve floor
- payment system reserve demand
- Fedwire RTGS reserve demand
- minimum ample reserves
- sàn dự trữ ngân hàng
- yêu cầu dự trữ hệ thống thanh toán
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
  - shadow_banking
tags:
- reserves
- Fedwire
- RTGS
- payment-system
- reserve-floor
- IORB
- SRF
- QT
- bank-liquidity
confidence: 3
stability: stable
thesis: 'The minimum level of reserve balances ("reserve floor") that the Fed must
  supply is driven primarily by the demand of the payment system, not by monetary
  policy alone. RTGS (real-time gross settlement) requires banks to pre-fund large
  opening-of-day reserve balances; post-GFC liquidity regulations stigmatize intraday
  overdrafts; and IORB remuneration removes incentives to lend excess reserves. These
  three structural changes raised the minimum from ~$10B pre-GFC to ~$3T, creating
  a ratchet effect. When reserves fall below the ample floor, payment delays beget
  repo rate spikes (September 2019 being the canonical example). Policy options to
  lower the floor include liquidity savings mechanisms (LSMs), tiered IORB, revised
  LCR/daylight overdraft rules, and TOMOs.

  '
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: Sections I, II, III — Abstract, p.1-40
  weight: primary
related:
- node: '[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]'
  relation: mechanism_of
- node: '[[Treasury_General_Account_TGA_Reserve_Swap]]'
  relation: interacts_with
- node: '[[Quantitative_Tightening_QT_Balance_Sheet_Runoff]]'
  relation: triggered_by
- node: '[[Fed_Overnight_Reverse_Repo_ON_RRP]]'
  relation: related_facility
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: regulatory_driver
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:reserves
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:reserves
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:reserves
- node: '[[Central Bank Balance Sheet Structure Liabilities Assets]]'
  relation: shared_tag:reserves
- node: '[[Ample Reserves Buffer Sizing TGA Volatility]]'
  relation: shared_tag:reserves
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Why the Reserve Floor Exists: The RTGS Mechanism

The Federal Reserve's payment system (Fedwire Funds Service) uses **Real-Time Gross Settlement (RTGS)**:
- Each payment settled immediately and individually in full, in central bank money
- No netting of inflows/outflows until after the fact
- Result: banks must "pre-load" large reserve balances at the opening of each day to process payment obligations

Contrast with **Deferred Net Settlement (DNS)** (ACH, CHIPS):
- Payments batched and netted; only the net position settles
- CHIPS handles ~$2T/day at 95% international; achieves high efficiency via netting + LSM
- DNS reduces opening balance requirements but adds settlement delay risk

**Daily scale:** Fedwire + Fedwire Securities process ~$7.3T/day. [RAW-BOOK Duffie §II]

### The Payment Throttling Feedback Loop

```
Low opening reserve balances (dealer banks)
         ↓
Banks throttle outgoing payments (receipt-reactive)
         ↓
Other banks receive payments later than normal
         ↓
Those banks also throttle → potential gridlock
         ↓
Elevated repo rates (SOFR-IORB spread widens)
         ↓
If persistent → repo market stress → SRF usage or Fed intervention
```

Empirical evidence: One-standard-deviation increase in trailing payment delay → ~7bps increase in SOFR-IORB spread. [RAW-BOOK Duffie §II, citing Copeland-Duffie-Yang 2025b]

**Canonical case:** September 17, 2019 — system reserve balances at sample record low → SOFR jumped to 315bps above IORB (the "repocalypse"); interdealer rates briefly ~1000bps above IORB. Payment timing delays were simultaneously at their 10-year record high. [RAW-BOOK Duffie §II]

---

## Structural Drivers: Why the Floor Jumped from $10B to $3T

Pre-GFC (2007), total reserve balances were ~$10B. Post-GFC structural changes raised the effective floor dramatically:

| Driver | Pre-GFC | Post-GFC |
|--------|---------|---------|
| Daylight overdrafts | $120B/day (top 10 banks) | <$5B/day (all banks) |
| IORB remuneration | 0% (no interest on reserves) | ~EFFR (market rate) |
| Interbank lending incentive | High (opportunity cost of idle reserves) | Low (IORB ≈ market return) |
| FDIC fees on wholesale liabilities | Lower | Up to 42bps + 13bps SVB surcharge |
| LCR/intraday liquidity regs | None | Banks self-insure; stigma on Fed facilities |

### 1. Daylight Overdraft Stigma (GSIB Self-Reliance)
Post-GFC intraday liquidity regulations require GSIBs to demonstrate that their liquidity needs can be met from their own resources. Using daylight overdrafts (even if secured, interest-free) signals dependence on Fed, triggering LCR implications and reputational risk. Pre-GFC, large banks collectively used ~$120B/day in daylight overdrafts; post-GFC this collapsed to under $5B. [RAW-BOOK Duffie §I.D]

### 2. IORB Remuneration Removes Lending Incentive
Pre-GFC: excess reserves earn 0% → strong incentive to lend overnight in federal funds market or repo → efficient reserve redistribution.
Post-GFC: reserves earn IORB ≈ market rate → no incremental return from lending; reserves become an "investment portfolio" asset. [RAW-BOOK Duffie §I.D]

Example: JPMorgan's reserve balance fell from $409B (end-2023) to ~$63B (Q3-2025) — treated as investment rotation, not operational necessity. When term yields rose above IORB, excess reserves migrated to USTs.

### 3. Frictional Cost of Interbank Lending
FDIC insurance fees (up to 42bps + 13bps SVB surcharge) make wholesale borrowed reserves expensive to the receiving bank. Higher capital requirements (leverage ratio) add cost. Result: interbank reserve redistribution is costly, not frictionless.

**Net result:** Reserve demand ratchet — each period of abundant reserves reduces bank investment in efficient liquidity management systems, raising the structural floor for the next cycle. [RAW-BOOK Duffie §I.C, citing Acharya-Rajan 2022]

---

## TGCR as Policy Target (over EFFR)

**Federal funds market is now tiny:**
- Daily volume: ~$100B, of which <$3B is true interbank lending
- Most EFFR activity: FHLB lending to foreign banks (FHLBs earn no IORB; foreign banks avoid FDIC fees)

**SOFR/TGCR = the relevant benchmark:**
- Treasury repo market: ~$8.8T outstanding, ~$6T overnight
- SOFR = volume-weighted median of overnight Treasury repo
- TGCR = tri-party subset of SOFR; directly reflects dealer bank reserve conditions

Logan and Schulhofer-Wohl (2025) propose TGCR as superior FOMC target. EFFR "demand elasticity to reserve supply" remains near zero even during repo stress, whereas SOFR/TGCR respond sensitively. [RAW-BOOK Duffie §I.B]

---

## Supply-Driven vs. Demand-Driven Framework

| Approach | Mechanics | Tolerance for Rate Volatility | Examples |
|----------|-----------|------------------------------|---------|
| Supply-driven (abundant) | Maintain conservatively ample reserves; banks don't need Fed facilities | Near-zero SOFR-IORB spread | Fed 2020-2025 (ON RRP era) |
| Demand-driven (ample, not abundant) | Smaller standing supply; banks use SRF/liquidity facilities regularly; some rate volatility acceptable | Some SOFR-IORB spikes tolerated | Bank of England (Short Term Repo), ECB plan |

**Key distinction:** In demand-driven framework, Fed's liquidity facilities are **tools for day-to-day liquidity management**, not emergency backstops. Requires stigma removal around SRF/Discount Window use. [RAW-BOOK Duffie §I.A]

**Fed's SOMA Manager (Perli):** "Some repo rate volatility is not problematic and is arguably beneficial for allowing markets to send signals on market conditions. However, if repo funding costs become too volatile and unpredictable, the likelihood of forced liquidations of repo-financed Treasury positions increases." [RAW-BOOK Duffie §I.A]

---

## Quarter-End Reserve Compression

Foreign banking organizations (FBOs) reduce reserve balances at quarter ends to improve capital ratios (monitored dates). This can compress system-wide reserves by $200-400B on quarter ends, triggering temporary SOFR spikes and ON RRP usage by MMFs.

Process:
```
Quarter-end → FBOs slash repo funding and reserves
            → System-wide reserve supply drops temporarily
            → Cash investors move to ON RRP
            → SOFR spikes vs. IORB
            → Next day: balances rebound; ON RRP reverts
```

[RAW-BOOK Duffie §I.B — citing Crandall/Wrightson analysis]

---

## Policy Options to Reduce the Reserve Floor

| Policy | Mechanism | Status |
|--------|-----------|--------|
| **Temporary OMOs (TOMOs)** | Offset period-end and TGA-driven reserve shocks; smoother reserve path | Available; Duffie recommends more active use |
| **Liquidity Savings Mechanism (LSM) for Fedwire** | Queue outgoing payments; offset against incoming payments; reduce opening balance needs | Not yet implemented in US; BOE, ECB, BOJ, BOC all use LSMs |
| **Tiering of IORB** | Pay below-market rate on "excess" reserves; restore incentive to lend reserves | Proposed; would reduce reserve hoarding |
| **Revised intraday LCR/overdraft rules** | Clarify that daylight overdrafts ≠ LCR failure; remove stigma on Fed facilities | Partially addressed post-SVB |

**CHIPS as model:** Private system using netting + LSM handles $2T/day with much smaller pre-funded balances. Fedwire (RTGS, no LSM) requires far more pre-funding for the same volume.

---

## Implications for QT End-Point

The reserve floor is higher than the Fed's pre-GFC experience would suggest. Indicators of approaching the floor:
- SOFR-IORB spread persistently above SRF ceiling
- Payment delays to dealer banks rising (receipt-reactive throttling increasing)
- Reserve demand elasticity to EFFR rising (from near-zero toward positive)
- Banks increasing SRF/Discount Window usage regularly

The Fed's two-step response: (1) slow/stop QT when SOFR-IORB spread rises; (2) begin Reserve Management Purchases (RMPs) of T-bills to restore ample level. [RAW-BOOK Duffie Abstract, §I.A]

**Balance sheet cost-benefit:** Larger balance sheet → smooth rates, no payment risk; Smaller balance sheet → lower political/fiscal cost, requires active liquidity management + LSM infrastructure + stigma removal. [LLM] The optimal point depends on whether enabling infrastructure (LSMs, destigmatized SRF) is in place.

