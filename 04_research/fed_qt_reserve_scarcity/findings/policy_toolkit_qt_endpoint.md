---
finding_id: qt_rs_003
topic: fed_qt_reserve_scarcity
sub_question: sq4, sq5
title: Fed Policy Toolkit for Reserve Management and QT End-Point
confidence: 3
status: stable
sources:
  - wiki: "[[Reserve_Floor_Payment_System_Demand]]"
  - wiki: "[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]"
  - wiki: "[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
date: 2026-05-20
---

## Core Finding

The Fed has four tools to manage reserve scarcity during QT wind-down. The choice between them carries different implications for balance sheet size, rate volatility tolerance, and structural reform. SLR constraints on dealer banks create a separate but interacting friction.

## Tool 1 — Slowing/Stopping QT (Primary Lever)

The most direct response to reserve scarcity signals is reducing the redemption cap or pausing QT entirely.

**Decision trigger:** Fed has signaled it will slow QT when SOFR-IORB spread rises persistently — even before reaching "scarce" territory, to avoid a repeat of Sep 2019.

**Feb 2024 precedent:** FOMC slowed QT pace from $60B/month to $25B/month as reserves fell below comfort zone — not scarce, but approaching the lower bound of ample.

## Tool 2 — TOMOs (Temporary Open Market Operations)

TOMOs are short-term repo operations where the Fed lends reserves to primary dealers against collateral, temporarily boosting reserve supply without permanently expanding the balance sheet.

**Use case:** Period-end reserve compression (FBO window-dressing), TGA volatility shocks, unexpected reserve demand spikes.

**Duffie recommendation:** More active use of TOMOs to smooth intra-quarter reserve volatility, reducing the required "buffer stock" of reserves the system must permanently maintain. [RAW-BOOK Duffie Abstract]

**Status:** Fed currently uses TOMOs ad hoc; Duffie argues for systematic use to lower the structural reserve floor.

## Tool 3 — Reserve Management Purchases (RMPs)

If QT has gone too far and reserves need permanent replenishment, the Fed conducts RMPs: purchases of short-term T-bills that permanently add reserves without expanding duration holdings.

**Key distinction from QE:** RMPs target reserve supply, not long-term yields. T-bill purchases have minimal effect on 10yr Treasury yields → no "stealth QE" signaling.

**Recent use:** Fed conducted RMPs in late 2019 after the repocalypse, purchasing ~$60B/month of T-bills to stabilize reserves.

## Tool 4 — LSM for Fedwire (Structural Reform)

A Liquidity Savings Mechanism (LSM) allows Fedwire to queue outgoing payments and offset against incoming payments before final settlement — reducing the opening balance requirements for each day.

**Impact:** Could reduce structural reserve demand by hundreds of billions — meaning QT could run further before hitting the floor.

**Status:** Fedwire does not yet have an LSM (unlike CHIPS, BOE RTGS, ECB TARGET2, BOC LVTS). Duffie explicitly recommends implementation. [RAW-BOOK Duffie §III]

**Timeline:** Multi-year infrastructure project; not a near-term option.

## SLR Interaction — The Hidden Constraint

Even when system-wide reserves are "ample," dealer SLR constraints can create localized scarcity:

```
Dealer bank approaches SLR limit
    ↓
Cannot expand balance sheet to intermediate repo
    ↓
Refuses to lend reserves to counterparties needing cash
    ↓
Localized reserve maldistribution → SOFR spike
    ↓
Looks like scarcity even with aggregate reserves "ample"
```

This is the same mechanism as Sep 2019: JPMorgan had reserves but wouldn't lend them due to regulatory/operational considerations.

**Policy implication:** Aggregate reserve level is insufficient — dealer intermediation capacity (SLR headroom) must also remain adequate. SLR exemption for Treasuries (temporary in 2020-21) materially improved intermediation capacity when active.

## QT End-Point Estimate

Given current structural dynamics:
- Pre-GFC floor: ~$10B
- Post-GFC structural floor: ~$3T (payment system + IORB + FDIC)
- Current reserve level: ~$3.0-3.3T [LLM-E, based on Reserve Floor node and QT node]
- Remaining QT runway (without LSM or SRF destigmatization): limited — $200-400B at most before floor approached

**Fed's two-step response pattern:**
1. Slow QT when SOFR-IORB spread rises → signals approaching floor
2. Begin RMPs (T-bill purchases) to stabilize permanently

**Enabling reforms that would extend QT runway:**
- Fedwire LSM: could lower floor by $200-500B [LLM-E]
- Destigmatized SRF: removes precautionary hoarding, lowers individual bank reserve demand
- Revised LCR/daylight overdraft rules: reduces GSIB self-insurance motive
