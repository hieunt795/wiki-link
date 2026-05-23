---
node_id: indicator_sofr_effr_basis_001
type: indicator
title: "SOFR–EFFR Basis Spread"
aliases:
  - SOFR-FF basis
  - SOFR-EFFR spread
  - repo-to-interbank spread
  - secured-unsecured spread
  - SOFR-FF basis spread

domain:
  primary: financial_markets
  secondary:
    - monetary_policy
tags:
  - money-market
  - repo
  - basis-spread
  - reserve-scarcity
  - plumbing

confidence: 3
stability: evolving

indicator_type: market
frequency: daily
data_source: "Derived: SOFR (FRBNY) minus EFFR (FRBNY). Also tracked via OIS basis swaps (SOFR OIS vs FF OIS)."
interpretation: >
  Normal condition: SOFR slightly below EFFR (negative basis, ~0 to -5bps) because
  secured borrowing is cheaper than unsecured. A positive basis spike (SOFR > EFFR)
  signals repo market stress — excess demand for Treasury collateral or repo dealer
  balance sheet constraints at month/quarter end. Conks targets 6bps SOFR-FF basis
  as a normal-to-elevated threshold; sustained positive basis above ~10bps warrants
  concern about plumbing conditions.

thesis: >
  The SOFR–EFFR basis measures the spread between the overnight secured repo rate and
  the overnight unsecured interbank rate. In the ample reserves floor system, this
  basis should be small and slightly negative. Persistent or spiking positive basis
  indicates dealer balance sheet stress, collateral shortage, or funding market
  dislocations — the key plumbing friction indicator in Conks' money market framework.

source_refs:
  - path: 02_sources/books/conks/Conks - Plumping note (Money market.md
    weight: primary
  - path: 02_sources/books/conks/Conk - Repo.md
    weight: supporting

related:
  - node: "[[SOFR_Secured_Overnight_Financing_Rate]]"
    relation: component_of
  - node: "[[EFFR_Effective_Federal_Funds_Rate]]"
    relation: component_of
  - node: "[[Repo_Market_Mechanics_Triparty_Bilateral]]"
    relation: measures
  - node: "[[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]]"
    relation: related_to
  - node: "[[Standing_Repo_Facility_SRF_Fed_Backstop]]"
    relation: bounded_by
  - node: "[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
    relation: driven_by

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The **SOFR–EFFR basis** (also called the SOFR-FF basis in Conks terminology) is the daily spread between the Secured Overnight Financing Rate (Treasury repo) and the Effective Federal Funds Rate (unsecured interbank). It captures the price difference between secured and unsecured overnight dollar funding.

In well-functioning markets: SOFR < EFFR because secured borrowers face lower counterparty risk — the lender holds Treasury collateral as backstop. The normal basis runs approximately -3 to -5bps.

## When the Basis Inverts or Spikes

The basis can temporarily go positive (SOFR > EFFR) at:
- **Month-end / quarter-end**: dealers constrained by leverage ratio reporting shrink repo books, reducing supply of secured lending → SOFR spikes
- **Tax dates**: large Treasury settlements create settlement demand → repo rates spike above EFFR
- **Year-end**: global balance sheet compression amplifies the mechanism

Conks' observation in the September money market update: "we've seen an anticipated widening in the SOFR-FF basis… beyond Conks' target of 6bps for October." The framework treats 6bps as the normal upper bound; widening beyond implies funding stress that "has peaked and is priced in for the month." [RAW-CLIP Conks Money Market Update]

## SRF Interaction

The Standing Repo Facility (SRF) provides a ceiling on SOFR spikes: the Fed offers overnight repo to primary dealers and depository institutions at the SRF rate, putting a cap on how high SOFR can go before dealers substitute SRF borrowing for market repo. Conks notes: "SOFR can thus trade much higher and more comfortably near the Fed's upper boundary before central bank intervention" compared to pre-2019. [RAW-CLIP Conks Money Market Update]

## OIS Basis Swap Market

The SOFR-EFFR basis is also traded in the derivatives market as an **OIS basis swap**: receive SOFR / pay EFFR (or vice versa). These swaps allow market participants to express views on or hedge exposure to funding market structure shifts — particularly around LIBOR-to-SOFR transition and future reserve regime changes.

## Relationship to Swap Spreads

The SOFR-EFFR basis is a subset of the broader money market plumbing friction set. Conks treats **swap spreads** as the primary plumbing friction indicator and SOFR-FF basis as the money market sub-component. See [[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]].
