---
node_id: fedwire_payment_system_reserve_demand_and_lsm_policy_001
type: mechanism
title: Fedwire Payment System Reserve Demand And LSM Policy
aliases:
- Fedwire RTGS Reserve Demand
- Payment System Reserve Floor
- Liquidity Savings Mechanism
- LSM Fedwire
- Daylight Overdraft Collapse
domain:
  primary: monetary_policy
tags:
- fedwire
- rtgs
- reserves
- payment_system
- lsm
- daylight_overdraft
- fed
- balance_sheet
confidence: 4
stability: evolving
thesis: The Fed's Fedwire RTGS payment system generates structural demand for reserve
  balances because banks must pre-load reserves for outgoing payments before receiving
  inflows; post-GFC intraday liquidity regulations caused daylight overdrafts to collapse
  from $120B/day to under $5B/day, dramatically raising the minimum reserve floor;
  adding a Liquidity Savings Mechanism (LSM) to Fedwire could substantially reduce
  reserve demand without sacrificing payment speed.
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: Full document
  weight: primary
related:
- node: '[[Reserve Floor — Payment System Demand and the Minimum Ample Level]]'
  relation: shared_tag:fedwire
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:reserves
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:reserves
- node: '[[Central Bank Balance Sheet Structure Liabilities Assets]]'
  relation: shared_tag:reserves
- node: '[[Ample Reserves Buffer Sizing TGA Volatility]]'
  relation: shared_tag:reserves
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
The Federal Reserve operates **Fedwire Funds** (real-time gross settlement, ~$4.5T/day) and **Fedwire Securities** (~$2.6T/day, early morning settlement). RTGS systems require each bank to pre-load enough reserve balances to cover gross outgoing payments — unlike deferred net settlement (ACH), no netting occurs [RAW-CLIP].

## Why RTGS Creates Large Reserve Demand
In RTGS, Bank A must have $X in reserves to send $X to Bank B, *before* Bank A receives any incoming payments. This is the "receipt-reactive" payment problem: banks that receive payments early in the day can fund their outgoing payments from inflows, but banks that lag are exposed.

Key evidence (Duffie 2026):
- Pre-GFC (2007): Banks used daylight overdrafts freely; total overdrafts at 10 largest banks ~$120B/day; total reserves only $10-15B
- Post-GFC (2020+): Total daylight overdrafts by all banks <$5B; yet total reserves needed = $3 trillion
- The 12,000× increase in reserves needed per unit of overdraft capacity used reflects regulatory aversion to Fed liquidity dependence [RAW-CLIP]

## The Regulatory Shift
Post-GFC intraday liquidity rules require banks to demonstrate self-reliance — using daylight overdrafts at the Fed is seen as evidence the bank cannot meet its own liquidity needs. Result: banks stopped using the Fed's free intraday credit and instead "pre-loaded" billions in reserve balances at day open [RAW-CLIP].

## Quarter-End Compression
Foreign banking organizations (FBOs) "window dress" their balance sheets at each quarter-end by slashing reserve holdings:
- Last 15 quarter-ends: ≥$200B compression on 15 occasions; ≥$300B on 7; ≥$400B on 2
- Cash investors flee to Fed ON RRP ($50-100B jumps on quarter-end dates)
- Dealer banks reluctant to fill gap via SRF due to capital/stigma costs [RAW-CLIP]

## Policy Options to Reduce Reserve Floor
Duffie (2026) proposes four approaches:

| Policy | Mechanism | Effect |
|--------|-----------|--------|
| **TOMOs** | Temporary OMOs to offset TGA shocks | Smooth supply fluctuations |
| **LSM for Fedwire** | Queue payments and net against incoming flows (like CHIPS, Eurosystem) | Reduce opening balance need by ~30-50% [LLM] |
| **Tiered IORB** | Pay lower rate on "excess" reserves above payment needs | Incentivize banks to lend reserves, revive interbank market |
| **Liquidity reg reform** | Reduce stigma of using SRF/discount window | Allow demand-driven approach (BoE model) |

## LSM Comparison
Other major central banks operate RTGS with LSMs:
- **Bank of England (CHAPS):** Throughput rules + queue matching; reserve demand significantly reduced
- **Eurosystem (TARGET2/T2):** Queue optimization mechanism
- **Bank of Canada (Lynx):** Throughput targets with monitoring
- **US CHIPS (private, ~$2T/day):** 95% international, uses bilateral netting + LSM; highly efficient [RAW-CLIP]

The Fed's Fedwire lacks LSM — a structural anomaly compared to all other major RTGS systems.


