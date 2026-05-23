---
node_id: indicator_effr_001
type: indicator
title: "EFFR — Effective Federal Funds Rate"
aliases:
  - EFFR
  - federal funds rate
  - o/n FF
  - interbank rate
  - FF rate
  - lãi suất quỹ liên bang hiệu dụng

domain:
  primary: monetary_policy
  secondary:
    - financial_markets
tags:
  - interest-rate
  - overnight
  - unsecured
  - fed-target
  - money-market

confidence: 3
stability: stable

indicator_type: monetary
frequency: daily
data_source: "Federal Reserve Bank of New York (FRBNY) — published each morning for prior day"
interpretation: >
  EFFR is the Fed's primary policy rate target. When EFFR trades within the FOMC's
  target range, the floor system is functioning normally. EFFR trading toward the
  upper bound signals tightening reserve conditions; sustained printing at the ceiling
  signals reserve scarcity requiring Fed intervention.

thesis: >
  The EFFR is the volume-weighted median rate of overnight federal funds transactions —
  uncollateralised lending of reserve balances between depository institutions. It is
  the Fed's operational target: the FOMC sets a target range (currently 25bps wide) and
  uses IORB and ON RRP to keep EFFR within that range. EFFR diverging from IORB toward
  the upper bound of the range is an early signal of emerging reserve scarcity.

source_refs:
  - path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
    weight: primary
  - path: 02_sources/books/conks/Conks - Plumping note (Money market.md
    weight: supporting
  - path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
    weight: supporting

related:
  - node: "[[IORB_Interest_on_Reserve_Balances]]"
    relation: bounded_by
  - node: "[[SOFR_EFFR_Basis_Spread]]"
    relation: component_of
  - node: "[[Fed_Ample_Reserves_Range_Floor_Framework]]"
    relation: target_of
  - node: "[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]"
    relation: measured_by
  - node: "[[Federal_Reserve]]"
    relation: controlled_by
  - node: "[[Reserve_Floor_Payment_System_Demand]]"
    relation: signal_for

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The **Effective Federal Funds Rate (EFFR)** is computed daily by the FRBNY as the volume-weighted median of transactions in the federal funds market — overnight, uncollateralised interbank loans of reserve balances held at the Fed. It is the benchmark for US monetary policy stance.

Under the current **ample reserves floor system**, EFFR is expected to trade close to IORB (the floor) and well inside the FOMC's target range. The 2024 target range was 5.25–5.50%; as of April 2026 it stands at 3.50–3.75%.

## Structure of the Federal Funds Market

Counterparties in the fed funds market are primarily depository institutions lending excess reserves to institutions with reserve needs, and FHLBs — which are not eligible for IORB — lending to banks above IORB to earn a spread. This FHLB arbitrage is the key reason EFFR trades slightly below IORB rather than exactly at it. See [[Fhlb_Effr_Iorb_Arbitrage_Floor_Mechanism]].

## EFFR as Reserve Scarcity Signal

In the pre-2008 corridor system, EFFR oscillated daily. Under the post-2008 floor system, EFFR prints in a near-straight line. A break in that line — EFFR drifting toward the upper bound of the target range — is the primary early warning of reserve scarcity. [RAW-CLIP Napkin Math for an Ample Reserves Buffer]

The Conks money market framework treats EFFR vs IORB spread as a live monitor: "for the first time in years, the Fed Funds rate… no longer printing in a straight line" signals the end of ample reserves. [RAW-CLIP Conks Money Market Update]

## Relationship to SOFR

EFFR is unsecured; SOFR is secured (Treasury repo). In normal conditions SOFR < EFFR because secured borrowing is less risky. At month/quarter-end, SOFR can spike above EFFR due to repo market demand exceeding supply. This SOFR-EFFR relationship is tracked via the [[SOFR_EFFR_Basis_Spread]].
