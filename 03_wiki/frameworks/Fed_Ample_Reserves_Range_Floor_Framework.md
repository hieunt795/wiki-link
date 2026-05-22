---
node_id: fed_ample_reserves_range_floor_frm_001
type: framework
title: Fed Ample Reserves Range Floor Framework
aliases:
  - Fed Range Floor System
  - Khuôn khổ sàn dự trữ dư dật (Range Floor) của Fed
  - Fed Dual Floor System

domain:
  primary: monetary_policy
  secondary: [financial_markets]
tags: [fed, operational_framework, floor_system, iorb, on_rrp, ffr]

confidence: 3
stability: stable

thesis: >
  The Fed maintains a "range floor" for the Federal Funds Rate (FFR) using two administered rates — IORB for banks and ON RRP for non-banks — to manage market segmentation and ensure rate control within an ample reserves regime.

source_refs:
  - path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
    pages: "Section 3.2"
    weight: primary

related:
  - node: "[[Reserve_Floor_Payment_System_Demand]]"
    relation: driven_by
  - node: "[[Fed_Overnight_Reverse_Repo_ON_RRP]]"
    relation: component_of

date_created: 2026-05-20
date_updated: 2026-05-20
---

## Overview
The Federal Reserve operates an "ample reserves" regime, which is a version of a floor system. Unlike a pure floor system with a single rate, the Fed uses a "range floor" to account for the fact that not all participants in the money market have access to the same facilities [RAW-CLIP].

## The Dual-Floor Mechanism

### 1. The Upper Floor: IORB
- **Instrument:** **Interest on Reserve Balances (IORB)**.
- **Participants:** Depository institutions (banks).
- **Function:** Banks will generally not lend in the interbank market (FFR) at rates significantly below the IORB because they can earn the IORB risk-free by keeping reserves at the Fed [RAW-CLIP].

### 2. The Lower Floor: ON RRP
- **Instrument:** **Overnight Reverse Repo Facility (ON RRP)**.
- **Participants:** Non-bank institutions including Money Market Funds (MMFs), Government-Sponsored Enterprises (GSEs like FHLB), and Primary Dealers [RAW-CLIP].
- **Function:** Since GSEs and MMFs cannot earn interest on reserves at the Fed, they would otherwise lend at very low rates. The ON RRP provides them with a "hard floor" by allowing them to lend to the Fed (collateralized by Treasuries) at a fixed rate [RAW-CLIP].

## Market Segmentation and the FFR Range
The **Federal Funds Rate (FFR)** typically hovers between the ON RRP rate and the IORB rate [RAW-CLIP].
- **Spread:** The spread between IORB and ON RRP is typically **10 basis points** [RAW-CLIP].
- **Market Dynamics:** The FFR is often pushed below the IORB because non-banks (like FHLBs) offer liquidity in the unsecured market but cannot access the IORB, while banks engage in arbitrage (borrowing at FFR and depositing at IORB) [LLM].

## Evolution of the Framework
- **Pre-2008:** The Fed used open market operations to adjust scarce liquidity to hit a target rate.
- **2008 Transition:** Authorization to pay interest on reserves (IOR) allowed the Fed to credit bank accounts during QE without losing control of interest rates, establishing the first floor [RAW-CLIP].
- **2013/2015:** The ON RRP was introduced to address the "leakage" of the floor caused by non-bank participants, creating the "range floor" system [RAW-CLIP].

## Operational Goals
The Fed's objective is to ensure that "active management of the supply of reserves is not required" to control the FFR, relying instead on its administered rates (IORB and ON RRP) to steer market rates [RAW-CLIP].
