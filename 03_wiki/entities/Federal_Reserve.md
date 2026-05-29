---
node_id: entity_federal_reserve_001
type: entity
title: Federal Reserve (Fed)
aliases:
- Fed
- Federal Reserve System
- FOMC
- US central bank
- Cục Dự trữ Liên bang
- Ngân hàng Trung ương Mỹ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
  - fiscal_policy
tags:
- central-bank
- united-states
- monetary-policy
- balance-sheet
- lender-of-last-resort
confidence: 3
stability: stable
entity_type: central_bank
jurisdiction: US
established: 1913
mandate: Maximum employment, stable prices (2% inflation target), moderate long-term
  interest rates
thesis: 'The Federal Reserve is the central bank of the United States, operating as
  a decentralized system of 12 Reserve Banks under a Board of Governors, with monetary
  policy set by the FOMC. It controls the federal funds rate target, manages the Fed''s
  balance sheet (assets: Treasuries + MBS; liabilities: reserves + currency + TGA),
  and serves as fiscal agent for the US Treasury.

  '
source_refs:
- path: 02_sources/Clipping/Breaking Out of the Central Bank Balance Sheet Trilemma.md
  weight: primary
- path: 02_sources/Clipping/Napkin Math for an Ample Reserves Buffer.md
  weight: supporting
- path: 02_sources/Clipping/The Checking Account of the U.S. Federal Government....md
  weight: supporting
- path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
  weight: supporting
- path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
  weight: supporting
parent_node: null
related:
- node: '[[Fed_Ample_Reserves_Range_Floor_Framework]]'
  relation: implements
- node: '[[Fed_Fiscal_Agent_Treasury_Relationship]]'
  relation: participates_in
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: operates
- node: '[[Central_Bank_Balance_Sheet_Structure_Liabilities_Assets]]'
  relation: instance_of
- node: '[[EFFR_Effective_Federal_Funds_Rate]]'
  relation: controls
- node: '[[IORB_Interest_on_Reserve_Balances]]'
  relation: sets
- node: '[[US_Treasury_Department]]'
  relation: fiscal_agent_for
date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The Federal Reserve System, established by the Federal Reserve Act of 1913, comprises 12 regional Reserve Banks and a Board of Governors in Washington, DC. The **Federal Open Market Committee (FOMC)** — seven Board members plus five rotating Reserve Bank presidents — sets the federal funds rate target and determines the pace of balance sheet expansion or contraction.

The Fed's balance sheet is the operational core of US monetary policy. Assets consist primarily of US Treasury securities and mortgage-backed securities (MBS). Liabilities are reserves held by depository institutions, Federal Reserve Notes (physical currency), the Treasury General Account (TGA), and the ON RRP facility. [RAW-CLIP Breaking Out of the Central Bank Balance Sheet Trilemma]

## Key Operational Tools

The Fed operates a **floor system** under ample reserves: IORB sets the floor under the federal funds rate; the ON RRP sets a sub-floor for money market funds; the Standing Repo Facility (SRF) caps repo rates at the ceiling. The EFFR is expected to trade within this corridor. [RAW-CLIP Napkin Math for an Ample Reserves Buffer]

As fiscal agent for the US Treasury, the Fed maintains the Treasury General Account (TGA) — the government's checking account. TGA drawdowns inject reserves into the banking system; TGA buildups drain them. [RAW-CLIP The Checking Account of the US Federal Government]

## Governance and Current Status

FOMC votes require a majority. In April 2026, the FOMC held rates at 3.50–3.75% on an 8-4 vote — the most divided vote since 1992. Powell announced his intention to remain on the Board as Governor after his Chair term (expires 15 May 2026), with Kevin Warsh nominated as Chair. [RAW-CLIP CB Commentary April 2026]

## Related Concepts

The Fed's framework evolution — from corridor to floor system, from scarce to ample reserves — is documented in [[Fed_Ample_Reserves_Range_Floor_Framework]]. Its fiscal agent role and TGA mechanics are in [[Fed_Fiscal_Agent_Treasury_Relationship]]. The CB Balance Sheet Trilemma constraining policy choices is in [[CB_Balance_Sheet_Trilemma]].
