---
node_id: fedwire_payment_system_reserve_demand_and_lsm_policy_001
type: concept
title: Fedwire Payment System Reserve Demand And LSM Policy
aliases:
- Fedwire RTGS Reserve Demand
- Payment System Reserve Floor
- Liquidity Savings Mechanism
- LSM Fedwire
- Nhu cầu dự trữ hệ thống thanh toán Fedwire
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
stability: stable
thesis: 'The Federal Reserve''s Fedwire RTGS system generates a structural floor on
  reserve demand because banks must "pre-load" balances to cover gross outgoing payments;
  post-GFC regulatory stigma and intraday liquidity rules have collapsed daylight
  overdraft usage, forcing the Fed to maintain trillions in reserves to prevent payment
  delays and repo rate spikes.

  '
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: Sections I, II, VII
  weight: primary
parent_node: null
related:
- node: '[[Reserve Floor — Payment System Demand and the Minimum Ample Level]]'
  relation: conceptual_extension
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: operational_context
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: liquidity_backstop
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: reserve_volatility_source
date_created: 2026-05-22
date_updated: 2026-05-25
---

## Overview
The Federal Reserve operates **Fedwire Funds**, a Real-Time Gross Settlement (RTGS) system processing ~$4.5 trillion daily. Unlike deferred net settlement systems (e.g., ACH or CHIPS), RTGS requires each outgoing payment to be settled individually and immediately using central bank reserves. This architectural choice makes the payment system the primary driver of the "minimum ample" level of reserves [RAW-BOOK p. 1-5].

## The "Receipt-Reactive" Payment Problem
In an RTGS system without a **Liquidity Savings Mechanism (LSM)**, a bank's ability to make payments depends on its opening reserve balance plus incoming payments already received.
- **Mechanism:** If Bank A must send $10bn to Bank B at 9:00 AM but hasn't received its expected $10bn inflow from Bank C, it must use its own pre-loaded reserves or an intraday credit facility (daylight overdraft).
- **Friction:** If Bank A's reserves are low and it is reluctant to use overdrafts, it "throttles" or delays outgoing payments. This creates a self-fulfilling cycle where other banks also experience delays in their expected inflows, leading to systemic gridlock and spikes in overnight interest rates (e.g., SOFR) as banks scramble for liquidity [RAW-BOOK p. 8-10].

## The Daylight Overdraft Collapse
Pre-GFC, the Fed allowed banks to run massive intraday deficits (daylight overdrafts) with minimal reserves. Post-GFC, this model collapsed due to regulatory and supervisory shifts.

| Metric | Pre-GFC (2007) | Post-GFC (2020+) |
| :--- | :--- | :--- |
| **Total Reserves** | ~$10-15 Billion | ~$3.0+ Trillion |
| **Peak Daylight Overdrafts (Top 10 Banks)** | ~$120 Billion/day | <$5 Billion/day |
| **Reserves per unit of Overdraft** | ~0.1x | ~600x |

**Reason for Shift:** Post-GFC intraday liquidity regulations (e.g., CLAR) and resolution planning ("living wills") require GSIBs to demonstrate they can meet liquidity needs from their own resources. Using Fed daylight overdrafts is now heavily stigmatized, viewed by supervisors as a sign of internal liquidity mismanagement [RAW-BOOK p. 11-12].

## Quarter-End Compression and Window Dressing
Foreign Banking Organizations (FBOs) significantly influence reserve demand through "window dressing" at period ends.
- **Mechanism:** FBOs slash reserve holdings at quarter-end to reduce their leverage ratio footprints (compression of ~$200bn to ~$400bn per quarter-end).
- **Impact:** This sudden drain of reserves forces cash investors into the Fed's **ON RRP** facility. If the remaining reserves at U.S. dealer banks are insufficient to intermediate the payment system, repo rates (SOFR) spike above the IORB [RAW-BOOK p. 6-7].

## Proposed Solution: Liquidity Savings Mechanism (LSM)
An LSM is a structural addition to an RTGS system that allows for "bilateral or multilateral netting" of queued payments.
- **A -> B -> C Loop:** If Bank A owes B $100, B owes C $100, and C owes A $100, an LSM identifies this loop and settles all three payments simultaneously with zero net reserves.
- **Comparison:** The Eurosystem (TARGET2), Bank of England (CHAPS), and Bank of Canada (Lynx) all use LSMs. Fedwire remains a "pure" RTGS system, which is an outlier among major central banks.
- **Potential:** Implementing an LSM for Fedwire could reduce the structural demand for reserves by 30-50% [LLM], allowing the Fed to maintain a significantly smaller balance sheet without risking rate instability [RAW-BOOK p. 25-28].

## T-Account: RTGS Payment (Without LSM)
The following sequence shows how a $5bn payment from Alpha (at Bank A) to Beta (at Bank B) drains Bank A's liquidity until an offsetting inflow occurs.

**Step 1: Outgoing Payment**
| Bank A (Assets) | Bank A (Liabilities) |
| :--- | :--- |
| - $5bn Reserves at Fed | - $5bn Alpha Deposits |

**Step 2: Fed Balance Sheet (Internal Swap)**
| Fed (Assets) | Fed (Liabilities) |
| :--- | :--- |
| (No change) | - $5bn Bank A Reserves |
| | + $5bn Bank B Reserves |

**Step 3: Receipt at Bank B**
| Bank B (Assets) | Bank B (Liabilities) |
| :--- | :--- |
| + $5bn Reserves at Fed | + $5bn Beta Deposits |

[LLM] In this mechanistic chain, Bank A's capacity to send the payment is strictly limited by its starting reserve balance unless it is willing to incur a daylight overdraft (which it is now regulated against) [RAW-BOOK p. 15].
