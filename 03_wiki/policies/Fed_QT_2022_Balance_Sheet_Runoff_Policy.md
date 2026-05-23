---
node_id: policy_fed_qt_2022_001
type: policy
title: "Fed Quantitative Tightening 2022 — Balance Sheet Runoff Policy"
aliases:
  - Fed QT 2022
  - QT 2022
  - balance sheet runoff 2022
  - thắt chặt định lượng Fed 2022

domain:
  primary: monetary_policy
  secondary:
    - financial_markets
tags:
  - fed
  - qt
  - balance-sheet
  - reserve-drain
  - qe-reversal

confidence: 3
stability: evolving

jurisdiction: US
period: "2022–present"
policy_type: unconventional_monetary
instruments:
  - "Passive roll-off: Treasuries capped at $30bn/month (rising to $60bn); MBS capped at $17.5bn/month (rising to $35bn)"
  - "No active sales (QT1 style) — purely passive maturity non-replacement"
outcome: >
  Fed balance sheet shrank from ~$9tn peak (April 2022) toward ~$7tn by mid-2024,
  draining approximately $1.5–2tn in reserves. ON RRP facility declined from ~$2.4tn
  peak (December 2022) toward zero by late 2024, buffering direct reserve impact.
  QT pace slowed (tapered) in June 2024 from $95bn to $60bn/month to avoid repo stress.

thesis: >
  The Fed's 2022 QT reduced the balance sheet passively via maturity non-replacement,
  draining reserves first from the ON RRP buffer (money funds withdrew from RRP as
  T-bill rates rose above ON RRP rate) and then from bank reserves. The existence of
  the $2.4tn ON RRP buffer created a significant cushion before reserves became scarce,
  fundamentally changing QT dynamics vs the 2017–2019 episode.

source_refs:
  - path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
    weight: primary
  - path: 02_sources/books/conks/Conks - Plumping note (Money market.md
    weight: supporting
  - path: 02_sources/Clipping/Breaking Out of the Central Bank Balance Sheet Trilemma.md
    weight: supporting

related:
  - node: "[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]"
    relation: instance_of
  - node: "[[Qt_Reserve_Drain_Effectiveness_And_Deposit_Funding_Condition]]"
    relation: produces
  - node: "[[Fed_Overnight_Reverse_Repo_On_Rrp]]"
    relation: drained_through
  - node: "[[Ample_Reserves_Buffer_Sizing_Tga_Volatility]]"
    relation: tests
  - node: "[[Fed_Rate_Hike_Cycle_2022_2023]]"
    relation: concurrent_with
  - node: "[[Federal_Reserve]]"
    relation: executed_by
  - node: "[[CB_Balance_Sheet_Trilemma]]"
    relation: constrained_by

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The Fed's second Quantitative Tightening episode began June 2022, operating through **passive runoff**: as Treasury securities and MBS mature, the Fed reinvests only the excess above monthly caps. No active outright sales (unlike the ECB's APP partial active unwind discussion).

**Monthly caps (announced May 2022):**
- Phase 1 (June–August 2022): Treasuries $30bn/month, MBS $17.5bn/month
- Phase 2 (September 2022+): Treasuries $60bn/month, MBS $35bn/month
- Taper (June 2024): Treasuries reduced to $25bn/month; MBS cap maintained

## ON RRP Buffer Dynamic

The critical insight distinguishing QT2 from QT1 (2017–2019): the **ON RRP facility** peaked at $2.4tn in December 2022. This buffer meant initial reserve drainage hit money market funds' ON RRP balances first, not bank reserves directly. As T-bill rates rose above the ON RRP rate through 2023, money funds shifted from ON RRP to T-bills — funds moved from Fed ON RRP → Treasury → market → bank reserves. This sequencing delayed reserve scarcity by 12–18 months relative to naive balance sheet accounting. [RAW-CLIP Napkin Math for an Ample Reserves Buffer]

## 2024 QT Taper

In June 2024 the FOMC slowed the Treasury runoff cap from $60bn to $25bn/month, responding to signs of tightening repo conditions and the Conks-type indicators showing SOFR-FF basis widening. The MBS cap was maintained. The taper was framed as "technical" (not a policy easing signal) — distinguishing balance sheet normalisation from rate policy.

## Remaining Reserve Buffer Question

The core unresolved question: when does QT drain reserves to the "lowest comfortable level of reserves" (LCLoR)? The Napkin Math framework estimates LCLoR at 10–13% of nominal GDP (~$2.8–3.6tn), implying QT had meaningful remaining room as of mid-2024. But TGA volatility and intraday payment system demands create episodic stress well above that level. [RAW-CLIP Napkin Math for an Ample Reserves Buffer]

## Distinction from QT1 (2017–2019)

The 2017–2019 episode had no ON RRP buffer; reserve drain hit banks directly and faster. September 2019 repo market stress (repo rates spiked >10%) forced emergency Fed intervention and early QT1 end. QT2 is designed to avoid this: gradual taper, SRF backstop, and ON RRP buffer provide cushion. See [[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]] for the general mechanism.
