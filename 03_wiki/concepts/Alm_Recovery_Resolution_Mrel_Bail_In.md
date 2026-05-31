---
node_id: alm_recovery_resolution_mrel_bail_in_001
type: concept
title: ALM in Recovery and Resolution — MREL, Bail-In, and BRRD
aliases:
- ALM resolution planning
- MREL ALM
- bail-in tool
- BRRD resolution tools
- kế hoạch phục hồi và xử lý ngân hàng
- MREL ALM thanh lý
- công cụ bail-in xử lý ngân hàng
- BRRD kế hoạch xử lý
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- resolution
- MREL
- bail-in
- BRRD
- recovery-planning
- gone-concern
confidence: 3
stability: stable
thesis: 'Local regulatory (resolution) authorities decide on resolution strategy;
  banks receive an MREL target as a result. MREL target = LAA + RCA + MCC (per updated
  2020 SRB logic). ALM is responsible for raising and maintaining MREL-eligible funding,
  MREL forecasting in the funding plan, and gone-concern ICAAP/ILAAP execution. If
  no systemic importance is found, the bank may go under common liquidation with no
  MREL add-on.

  '
source_refs:
- path: 02_sources/books/alm/ALM - Bank Asset Liability Management Best Practice_ Yesterday, Today and Tomorrow-De Gruyter (2021).md
  pages: 'Box 14.1: Recovery and Resolution Planning; Chapter 15: ALM Role in Crisis'
parent_node: null
related:
- node: '[[Alm_Role_Srep_Pillar2_Capital_Liquidity]]'
  relation: related_to
- node: '[[Integrated_Stress_Testing_Capital_Liquidity_Link]]'
  relation: related_to
- node: '[[Optimal_Funding_Tenor_Cost_Risk_Tradeoff]]'
  relation: related_to
- node: '[[Bank_Capital_Structure_And_Capital_Management_Alm]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- node: '[[Basel_III]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

Under the BRRD framework, a bank that exhausts recovery options enters resolution via one of four tools (sale-of-business, bridge institution, asset separation, bail-in). [LLM] The bail-in tool absorbs losses by writing down or converting eligible MREL liabilities into equity; ALM is responsible for MREL forecasting in the funding plan, gone-concern ICAAP/ILAAP execution, and providing the resolution authority with resolvability evidence on capital, liquidity, and operational continuity.
## Four Phases of a Bank Under Stress

Every bank can potentially undergo four sequential phases:
1. **Going concern** — Bank meets minimum regulatory requirements; ICAAP/ILAAP running normally; RAS limits not breached.
2. **Bank-driven recovery** — Recovery triggers are breached; bank implements recovery plan options (capital injection, asset sales, FX repricing, asset transfer) without state support.
3. **Authority-driven recovery and/or resolution** — Authorities determine recovery has failed; resolution plan activated.
4. **Resolution involving external funds** — Last-resort state support, if needed.

## Recovery Plan

A recovery plan defines:- **Recovery triggers**: Metrics (capital, liquidity, profitability) whose breach initiates escalation and option execution.
- **Recovery options**: Capital and liquidity measures available without state support (e.g., asset sales, RWA reduction, deposit repricing, central bank facilities, intragroup support).
- **Escalation process**: Step-by-step communication to supervisors and execution sequence.

Banks must draft recovery plans themselves; resolution plans are drafted by the resolution authority with input from the bank.
## Four BRRD Resolution Tools

When all recovery options are exhausted, authorities select one or a combination of:
| Tool | Description | ALM relevance |
|------|-------------|---------------|
| **Sale-of-business** | Parts of balance sheet sold to a buyer; remainder liquidated | ALM identifies saleable portfolios; estimates capital/liquidity impact |
| **Bridge institution** | Parts of balance sheet transferred to new legal entity; remainder liquidated | ALM provides cashflow mapping for portfolio carve-out |
| **Asset separation** | Assets and liabilities transferred to an asset management vehicle ("bad bank"); core institution continues | ALM defines what constitutes "core" vs "non-core" balance sheet |
| **Bail-in** | Write-down or conversion of eligible liabilities into equity; institution continues | ALM manages MREL stack; ensures eligible instrument stack; prepares bail-in playbook |


## MREL — Minimum Requirement for Eligible Liabilities

MREL instruments must be available to cover **loss absorption and recapitalization** needs in a resolution scenario. [LLM] ALM responsibilities:- **Forecasting**: Include MREL targets in the funding plan at each planning horizon.
- **Instrument management**: Ensure the MREL stack is composed of eligible instruments (subordinated or senior non-preferred debt meeting maturity, contractual terms, and conversion requirements).
- **Playbook**: A working "bail-in playbook" must describe how write-down and conversion would be executed operationally.

MREL requirements are imposed on all banks subject to BRRD resolution strategy (not normal liquidation), i.e., systemically important institutions in Categories 1–3. [LLM] Smaller Category 4 banks default to normal insolvency — no MREL requirement.
## Resolvability Areas

Supervisory authorities require banks to demonstrate resolvability in multiple areas:- **Financial**: Sufficient MREL instruments available; loss absorption and recapitalization capacity modeled.
- **Operational**: Continuity of critical functions (payments, custody, etc.) through resolution.
- **Legal and governance**: No contractual impediments to bail-in; resolution powers recognized in applicable law.
- **IT and data**: Reliable data for valuation and loss attribution in resolution.

## ALM Role in Crisis Liquidity Management

When a bank enters stress, ALM executes a stacking order of liquidity actions:
1. Reprice corporate/retail deposits downward to retain liquidity.2. Negotiate prolongation of interbank funding before counterparty limits close.3. Access central bank facilities (ECB TLTROs, central bank collateralized funding).4. Arrange intragroup liquidity support from parent company.5. Execute loan transfers to parent or third parties (true-sale or silent funded risk participation).6. As ultimate measure: accelerate asset repayment by clients (reputationally costly).
## ALM Role in Crisis Capital Management

Capital action plan under stress:
1. **Quantify capital hits**: FX depreciation (RWA inflation, OCI currency translation), moratoria on repayments (deferred NPL recognition), provisioning, bond portfolio OCI losses.
2. **Estimate post-stress capital levels** vs TSCR and OCR; evaluate available regulatory relief (CCB, P2G, CCyB waivers).
3. **Counterbalancing actions**: RWA optimization (IRB upgrade, collateral enhancement), RWA transfer (true-sale, silent/unfunded risk participations), AT1/T2 injection, CET1 share issuance.
4. **Estimation of residual surplus/shortfall** after all actions.

**Source:** §16.4 ALM Role in Resolution Strategy, and Box 14.1, Chapter 15 of Bardaeva, "Bank Asset Liability Management Best Practice" (De Gruyter, 2021). MREL formula (LAA/RCA/MCC) and eligible liabilities criteria directly from §16.4. [RAW-Bardaeva §16.4]
