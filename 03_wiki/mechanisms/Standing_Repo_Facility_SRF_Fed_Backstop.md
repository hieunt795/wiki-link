---
node_id: standing_repo_facility_srf_mec_001
type: mechanism
title: Standing Repo Facility SRF Fed Backstop
aliases:
- SRF
- Công cụ Repo thường trực (SRF) của Fed
- Fed Repo Ceiling
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- fed
- repo
- sofr
- srf
- liquidity
- backstop
confidence: 3
stability: stable
thesis: 'The Standing Repo Facility (SRF) acts as a ceiling for the SOFR and a liquidity
  safety valve for the US Treasury market, designed to cap secured rates and mitigate
  dealer balance sheet stress by providing a destigmatized backstop.

  '
source_refs:
- path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
  pages: Introduction & Section 3.2
  weight: primary
related:
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: backstop_for
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: mitigates
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Overview
Introduced by the Federal Reserve in July 2021, the **Standing Repo Facility (SRF)** serves as a backstop in the overnight repo market. It allows primary dealers and eligible banks to borrow reserves from the Fed by providing high-quality collateral (Treasuries, Agency debt, MBS) [RAW-CLIP].

## Purpose and Mechanism

### 1. Capping Secured Rates (SOFR)
The primary role of the SRF is to contain spikes in the **Secured Overnight Financing Rate (SOFR)**. When demand for liquidity in the repo market exceeds supply, pushing rates upward, participants can turn to the SRF at its pre-set administered rate, which effectively acts as a ceiling for the market repo rate [RAW-CLIP].

### 2. De-stigmatization
Unlike the **Discount Window**, which has historically suffered from "stigma" (where banks avoid using it to prevent being seen as weak), the SRF is designed to be a "normal" part of market operations [RAW-CLIP]. 
- **Example:** In late 2025, concerns about stigma were discussed in a Fed meeting with primary dealers. Subsequent usage (e.g., **$24 billion** in a single week) indicated that the facility was becoming a functioning tool for containing rate pressure [RAW-CLIP].

### 3. Treasury Market Stability
The SRF is crucial for the stability of the US Treasury market. By providing a guaranteed way for dealers to fund their inventories of Treasuries via repos, it prevents forced selling of securities during liquidity stress [RAW-CLIP].
- **Basis Trades:** High repo rates can trigger the unwinding of basis trades executed by hedge funds (which involve $2 trillion in Treasuries). The SRF helps avoid this by capping repo rates and ensuring funding is available [RAW-CLIP].

## Key Features
- **Counterparties:** Primary dealers and eligible banks.
- **Collateral:** Treasury securities, Agency debt, and Agency MBS.
- **Rate:** Set by the Fed, typically at the top of the target range for the FFR.
- **Operation:** Daily, fixed-rate, full allotment (up to a large limit).

## Comparison with ON RRP
While the **ON RRP** allows participants to lend cash to the Fed (extracting liquidity), the **SRF** allows them to borrow cash from the Fed (injecting liquidity). Together, they provide a set of administered rates that bracket both the unsecured (FFR) and secured (SOFR) money markets [LLM].

