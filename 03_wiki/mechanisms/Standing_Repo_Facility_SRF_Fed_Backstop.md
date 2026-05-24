---
node_id: standing_repo_facility_srf_mec_001
type: mechanism
title: Standing Repo Facility (SRF) Fed Backstop
aliases:
  - SRF
  - Standing Repo
  - Fed Repo Backstop
  - Dealer of Last Resort
  - Trần lãi suất Repo (SRF)
domain:
  primary: monetary_policy
tags:
  - fed
  - repo
  - srf
  - liquidity
  - backstop
  - sofr
  - primary_dealer

confidence: 4
stability: stable

thesis: >
  The Standing Repo Facility (SRF) is the Federal Reserve's "upper jaw" in its interest rate corridor, designed to cap secured overnight rates (SOFR) and serve as a "dealer of last resort" for primary dealers and banks during liquidity stress.

source_refs:
  - path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
    pages: "169-175, 481-489"
    weight: primary
  - path: 02_sources/books/conks/Conk - Repo.md
    pages: "227-243, 324, 1073-1252"
    weight: primary
  - path: 02_sources/books/conks/Conks - Plumping note (Money market.md
    pages: "902-940"
    weight: supporting

related:
  - node: "[[Fed Ample Reserves Rate Control Framework]]"
    relation: operational_framework
  - node: "[[Fed Overnight Reverse Repo ON RRP]]"
    relation: floor_counterpart
  - node: "[[SOFR — Secured Overnight Financing Rate]]"
    relation: target_benchmark
  - node: "[[BTFP SVB Crisis and Fed Emergency Lending Evolution]]"
    relation: emergency_lending_context

date_created: 2026-05-22
date_updated: 2026-05-24
---

## Overview
The Standing Repo Facility (SRF), established as a permanent tool in July 2021, allows the Federal Reserve to provide unlimited overnight cash loans to primary dealers and eligible depository institutions. By accepting high-quality collateral (UST, Agency Debt, Agency MBS), the Fed enforces a "ceiling" on the Secured Overnight Financing Rate (SOFR), preventing the "repocalypses" seen in September 2019 [RAW-CLIP].

## Mechanism of Action
The SRF functions as a standing offer to lend reserves against securities at a fixed rate (SRFR), typically set at the top of the FOMC's target range.

1. **The Bid:** Counterparties submit "propositions" to the Open Market Trading Desk ("The Desk") via FedTrade [RAW-CLIP].
2. **The Swap:**
   - **Participant Pledges:** U.S. Treasuries, Agency Debt, or Agency MBS.
   - **Fed Provides:** Reserves (cash) credited to the participant's Master Account.
3. **Settlement:** Operations are conducted as triparty repos on the BNY Mellon platform. Securities are moved to a segregated pledge account, and cash is settled by mid-afternoon (~3:30 PM) [RAW-CLIP].

## Structural Evolution: Morning vs. Afternoon
Originally, the SRF operated only in the afternoon (1:30 PM - 1:45 PM). This created a "timing defect" because the bulk of repo trading (~70%) occurs between 7:00 AM and 9:00 AM.
- **Problem:** Dealers lending in the morning faced interest rate risk and negative carry if they had to wait until 1:30 PM to borrow from the Fed at a lower rate [RAW-CLIP].
- **Fortification:** In late 2024, the Fed added "Morning Fed Repos" (8:00 AM - 8:30 AM settlement by 9:00 AM) to better align the facility with peak market activity and reduce intraday rate volatility [RAW-CLIP].

## Frictions and the "Soft" Ceiling
The SRF is often described as a "soft" ceiling rather than a hard cap for two primary reasons:

### 1. The Stigma Problem
Similar to the Discount Window, banks fear that using the SRF signals financial distress to supervisors or the market. This "psychological plumbing" defect causes dealers to borrow at private market rates well above the SRFR before "breaking the seal" to tap the Fed [RAW-CLIP].

### 2. Balance Sheet Costs
Using the SRF consumes a dealer's balance sheet (RWA and Leverage Ratio).
- **Mechanism:** Unlike private repo which can sometimes be "netted" if centrally cleared, SRF trades are bilateral with the Fed and currently un-nettable.
- **Cost:** Dealers often require a ~25bp spread over the SRFR to justify the capital cost of intermediating Fed liquidity to the broader market (e.g., hedge funds). Consequently, market SOFR can trade significantly above the SRFR without triggering massive facility usage [RAW-CLIP].

## T-Account: SRF Usage (Dealer Perspective)
When a Primary Dealer (PD) taps the SRF to fund a position:

**Step 1: SRF Repo Execution**
| Primary Dealer (Assets) | Primary Dealer (Liabilities) |
| :--- | :--- |
| + $1bn Reserves (Cash) | + $1bn Repo Payable to Fed |
| - $1.02bn UST (Pledged as Collateral) | |

**Step 2: Fed Balance Sheet**
| Fed (Assets) | Fed (Liabilities) |
| :--- | :--- |
| + $1bn Repo Receivable (PD) | + $1bn Reserves (PD Master Acct) |

[LLM] This expansion of the Fed's balance sheet injects fresh reserves into the system, neutralizing the liquidity drain caused by Treasury settlements or corporate tax flows [RAW-CLIP].
