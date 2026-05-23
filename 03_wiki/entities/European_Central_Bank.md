---
node_id: entity_ecb_001
type: entity
title: "European Central Bank (ECB)"
aliases:
  - ECB
  - Eurosystem
  - Ngân hàng Trung ương châu Âu

domain:
  primary: monetary_policy
  secondary:
    - financial_markets
tags:
  - central-bank
  - eurozone
  - monetary-policy
  - balance-sheet
  - operational-framework

confidence: 3
stability: stable

entity_type: central_bank
jurisdiction: EU
established: 1998
mandate: "Price stability (inflation below but close to 2% over medium term; revised to symmetric 2% target in 2021)"

thesis: >
  The ECB sets monetary policy for the 20-member eurozone via the Governing Council,
  operating through the Eurosystem of national central banks (NCBs). Its 2024
  operational framework shift — from excess liquidity via TLTRO to structural repo
  operations — marks the transition from an asset-purchase-driven floor system back
  toward a demand-driven corridor.

source_refs:
  - path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
    weight: primary
  - path: 02_sources/books/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md
    weight: supporting

related:
  - node: "[[ECB_New_Operational_Framework_2024]]"
    relation: implements
  - node: "[[Interest_Rate_Corridor_Floor_System_Standing_Facilities]]"
    relation: instance_of
  - node: "[[Central_Bank_Balance_Sheet_Structure_Liabilities_Assets]]"
    relation: instance_of
  - node: "[[Inflation_Targeting_Framework_Central_Bank]]"
    relation: implements

date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The European Central Bank, established in 1998 under the Maastricht Treaty, is the monetary authority for the eurozone. Monetary policy is set by the **Governing Council** (six ECB Executive Board members plus 20 NCB governors) by consensus or majority vote. Implementation is decentralized through the Eurosystem — the ECB plus NCBs — which collectively execute open market operations and manage collateral frameworks.

The ECB's primary mandate is price stability, defined as 2% inflation over the medium term (symmetric since the 2021 strategy review). A secondary mandate to support the EU's general economic policies applies only insofar as it does not prejudice price stability.

## Operational Framework

The ECB historically operated a **corridor system** with the main refinancing operation (MRO) rate as the center and deposit facility (DF) / marginal lending facility (MLF) as floor and ceiling. Post-GFC quantitative easing and TLTROs flooded the system with excess liquidity, collapsing rates to the deposit facility floor. [RAW-CLIP ECB AND FED POLICY OPERATIONAL FRAMEWORKS]

The **2024 operational framework reform** announced a structural shift: as TLTROs mature and excess liquidity drains, the ECB will conduct regular structural longer-term repo operations to provide a durable liquidity base, keeping the system in a demand-driven mode with the MRO as anchor. The spread between MRO and DF was narrowed to 15bps to limit incentive for excess reserve accumulation. See [[ECB_New_Operational_Framework_2024]].

## Transmission Mechanism Specifics

Unlike the Fed, the ECB lends against a broad collateral pool managed by NCBs under the Eurosystem Credit Assessment Framework (ECAF). Collateral haircuts vary by asset class and credit quality, creating a collateral channel in transmission. [LLM] Fragmentation risk — where peripheral sovereign spreads widen during stress — required tools like the Outright Monetary Transactions (OMT) and Transmission Protection Instrument (TPI) to maintain a single monetary policy across the currency union.

## Related Concepts

The 2024 framework reform details are in [[ECB_New_Operational_Framework_2024]]. The generic corridor vs floor system comparison is in [[Interest_Rate_Corridor_Floor_System_Standing_Facilities]].
