---
node_id: indicator_sofr_001
type: indicator
title: SOFR — Secured Overnight Financing Rate
aliases:
- SOFR
- secured overnight rate
- repo benchmark rate
- LIBOR replacement
- lãi suất repo qua đêm có bảo đảm
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
tags:
- interest-rate
- overnight
- secured
- repo
- benchmark
- libor-replacement
confidence: 3
stability: stable
indicator_type: market
frequency: daily
data_source: Federal Reserve Bank of New York (FRBNY) — published each morning for
  prior business day; based on tri-party repo, bilateral repo, and GCF Repo transactions
interpretation: 'SOFR measures the cost of borrowing cash overnight collateralised
  by US Treasury securities. Spikes above the SRF rate signal repo market stress.
  Persistent SOFR near the ON RRP floor indicates excess liquidity; drift toward IORB
  and above indicates tightening conditions. SOFR-EFFR basis compression/expansion
  signals shifts in secured vs unsecured market balance.

  '
thesis: 'SOFR is the ARRC-endorsed replacement for USD LIBOR, capturing the broad
  US Treasury repo market across tri-party, bilateral, and GCF segments (~$1 trillion
  daily volume). Unlike EFFR (unsecured), SOFR is secured by Treasuries, making it
  sensitive to collateral availability and repo market stress. SOFR is the underlying
  rate for the vast majority of new USD floating-rate contracts and OIS derivatives
  post-2023.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  weight: primary
- path: 02_sources/books/conks/Conk - Repo.md
  weight: supporting
- path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
  weight: supporting
parent_node: '[[SOFR_EFFR_Basis_Spread]]'
related:
- node: '[[EFFR_Effective_Federal_Funds_Rate]]'
  relation: compared_with
- node: '[[SOFR_EFFR_Basis_Spread]]'
  relation: component_of
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: measures
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: floored_by
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: capped_by
- node: '[[Interest_Rate_Swaps_OIS_Fixed_Floating]]'
  relation: underlies
date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The **Secured Overnight Financing Rate (SOFR)**, published daily by the FRBNY since April 2018, measures the volume-weighted median rate on overnight cash borrowing collateralised by US Treasury securities. It replaced USD LIBOR across financial contracts on 30 June 2023.

SOFR covers three segments of the Treasury repo market:
1. **Tri-party repo** (Bank of New York Mellon as custodian/clearing agent)
2. **GCF Repo** (DTCC's interdealer general collateral repo)
3. **Bilateral repo** (directly negotiated between counterparties, cleared at FICC)

Combined daily volume: approximately $1–1.5 trillion. This breadth makes SOFR significantly more robust to manipulation than the panel-based LIBOR.

## Behaviour and Volatility

SOFR's key feature vs LIBOR: it is a backward-looking overnight rate (not a term rate), making it volatile at month-end, quarter-end, and tax dates. At these dates, dealers need to shrink their balance sheets (reducing repo lending capacity), pushing SOFR up sharply. The Conks framework notes: "SOFR can thus trade much higher and more comfortably near the Fed's upper boundary before central bank intervention" — because the SRF provides a ceiling via intraday repo. [RAW-CLIP Conks Money Market Update]

## SOFR vs EFFR Structure

In normal conditions: ON RRP rate < SOFR ≈ EFFR. SOFR is typically slightly below EFFR because secured borrowing is inherently less risky than unsecured. When repo demand surges (month-end, tax dates), SOFR can temporarily spike above EFFR, widening the [[SOFR_EFFR_Basis_Spread]] in the positive direction.

## Term SOFR

CME Group publishes **Term SOFR** — forward-looking rates at 1, 3, 6, and 12 months — derived from SOFR futures. Term SOFR provides a LIBOR-equivalent for contracts requiring rate certainty in advance of the interest period, but the ARRC recommends it only for legacy LIBOR-based exposures, not new originations.

## Related Concepts

Repo market mechanics underlying SOFR computation are in [[Repo_Market_Mechanics_Triparty_Bilateral]]. The SRF ceiling on SOFR spikes is in [[Standing_Repo_Facility_SRF_Fed_Backstop]]. SOFR-EFFR dynamics are in [[SOFR_EFFR_Basis_Spread]].
