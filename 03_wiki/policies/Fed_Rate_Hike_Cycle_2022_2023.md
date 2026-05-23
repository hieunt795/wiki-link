---
node_id: policy_fed_hike_cycle_2022_001
type: policy
title: "Fed Rate Hike Cycle 2022–2023"
aliases:
  - Fed tightening cycle 2022
  - FOMC rate hikes 2022-2023
  - post-COVID tightening
  - chu kỳ tăng lãi suất Fed 2022-2023

domain:
  primary: monetary_policy
  secondary:
    - financial_markets
tags:
  - fed
  - rate-hike
  - tightening
  - inflation
  - unconventional-scale

confidence: 3
stability: stable

jurisdiction: US
period: "2022–2023"
policy_type: conventional_monetary
instruments:
  - "Federal funds rate increases (11 hikes: +525bps total, March 2022 – July 2023)"
  - "Quantitative Tightening (QT): balance sheet runoff from June 2022"
  - "Forward guidance: data-dependent, higher-for-longer signaling"
outcome: >
  EFFR raised from 0–0.25% (March 2022) to 5.25–5.50% (July 2023) — fastest tightening
  cycle since the 1980s. Inflation (PCE) declined from 7%+ peak to ~2.5% by end-2024.
  Rate cuts commenced September 2024; by April 2026, EFFR target at 3.50–3.75%.

thesis: >
  The Fed's 2022–2023 tightening cycle — 525bps in 11 meetings — was the fastest since
  Volcker, triggered by post-COVID supply shock inflation amplified by fiscal stimulus.
  The simultaneous QT added a balance sheet tightening channel. The cycle strained
  banking sector duration positions (SVB March 2023) and tested the ample reserves
  framework's resilience to rapid reserve drainage.

source_refs:
  - path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
    weight: primary
  - path: 02_sources/Clipping/Breaking Out of the Central Bank Balance Sheet Trilemma.md
    weight: supporting
  - path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
    weight: supporting

related:
  - node: "[[Fed_QT_2022_Balance_Sheet_Runoff_Policy]]"
    relation: concurrent_with
  - node: "[[Fed_Ample_Reserves_Range_Floor_Framework]]"
    relation: stresses
  - node: "[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]"
    relation: implements
  - node: "[[Irrbb_Eve_Nii_Dual_Metric_Framework]]"
    relation: exposed
  - node: "[[Non_Linear_Inflation_Amplifier_Mechanics]]"
    relation: response_to
  - node: "[[Supply_Shock_Policy_Response_Scenario_Taxonomy]]"
    relation: instance_of
  - node: "[[Federal_Reserve]]"
    relation: executed_by

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The Federal Reserve's 2022–2023 tightening cycle commenced with a 25bps hike in March 2022 and accelerated through four consecutive 75bps hikes (June–November 2022) — an unprecedented pace. The terminal rate of 5.25–5.50% was reached in July 2023 and held until September 2024.

**Hike cadence:**
- March 2022: +25bps (liftoff)
- May 2022: +50bps
- June–November 2022: 4× +75bps
- December 2022: +50bps
- February–May 2023: 3× +25bps
- July 2023: +25bps (terminal)

Total: **+525bps in 16 months.**

## Inflation Context

The cycle was a response to post-COVID inflation driven by: (1) supply chain disruptions, (2) fiscal stimulus demand boost (ARP $1.9tn, infrastructure), (3) commodity price shock (Ukraine war, energy). PCE inflation peaked at 7.0% (June 2022). Core PCE peaked at 5.6% (February 2023).

The Fed's initial "transitory" framing — treating supply shock inflation as self-correcting — delayed liftoff by approximately 6–9 months relative to the inflation signal, contributing to the speed and scale of the eventual catch-up. [LLM]

## Balance Sheet Dimension (QT)

Simultaneous with rate hikes, QT began June 2022: monthly caps of $47.5bn (rising to $95bn) on Treasury + MBS roll-off. QT drained reserves and tested the lower bound of ample reserves. The BoJ's concurrent intervention to defend YCC (selling USTs to fund yen intervention) added external reserve drainage. See [[Fed_QT_2022_Balance_Sheet_Runoff_Policy]].

## Banking Sector Strain (SVB)

The 525bps rate shock exposed duration mismatches in bank held-to-maturity portfolios. Silicon Valley Bank (March 2023) collapse demonstrated that IRRBB frameworks had not adequately priced rate sensitivity in the NII/EVE tradeoff. See [[Irrbb_Eve_Nii_Dual_Metric_Framework]]. The Fed responded with the Bank Term Funding Program (BTFP), temporarily lending against HTM securities at par.

## Post-Cycle: Easing Phase

Rate cuts began September 2024 (-50bps), followed by November and December 2024 (-25bps each). By April 2026, EFFR target is 3.50–3.75% amid supply shock uncertainty from Hormuz closure. [RAW-CLIP CB Commentary April 2026]
