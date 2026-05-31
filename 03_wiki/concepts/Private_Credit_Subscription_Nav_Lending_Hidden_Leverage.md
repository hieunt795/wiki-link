---
node_id: private_credit_subscription_nav_lending_hidden_leverage_001
type: concept
title: Private Credit Subscription NAV Lending Hidden Leverage
aliases:
- subscription facilities
- NAV lending
- capital call lines
- tin dung NAV quy tu nhan
- PC hidden leverage
domain:
  primary: basel_risk
tags:
- private_credit
- leverage
- nav_lending
- subscription_facility
- gsib
- liquidity_risk
- systemic
confidence: 1
stability: evolving
thesis: Subscription credit facilities (secured by LP commitments) and NAV loans (secured
  by fund investment values) constitute a hidden leverage layer in private credit
  not visible in standard portfolio metrics; OFR estimates $410-540bn in bank credit
  extended to private credit vehicles, concentrated 60% among 5 GSIBs, creating a
  plausible correlated liquidity transmission route where PC fund stress and bank
  credit tightening reinforce each other.
source_refs:
- path: 02_sources/deep-research/Deep Dive_ Private Credit.md
  pages: ''
  weight: primary
parent_node: null
related:
- node: '[[Basel Driven Credit Migration To Private Markets]]'
  relation: shared_tag:private_credit
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:private_credit
- node: '[[Private Credit Insurer Structural Channel]]'
  relation: shared_tag:private_credit
- node: '[[Private Credit Secondary Market Price Discovery]]'
  relation: shared_tag:private_credit
- node: '[[Bank NBFI Leverage Loop]]'
  relation: shared_tag:leverage
date_created: '2026-05-22'
date_updated: '2026-05-24'
---

## Scope Boundary

[LLM] This node is the canonical instrument taxonomy for subscription facilities and NAV lending inside private credit funds.

[LLM] It should not be used as the canonical explanation of borrower-level PIK stress masking; that belongs to [[PIK_Payment_In_Kind_Credit_Masking]].

[LLM] It should also not carry the full systemic bank feedback-loop argument; that belongs to [[Bank_NBFI_Leverage_Loop]].

## Subscription Facilities
[LLM] Fund-level indebtedness secured by unfunded LP commitments. Key feature: improves IRR optics by delaying LP capital calls, front-running deployment with borrowed money. SEC marketing-rule guidance warns that presenting performance inconsistently (with vs. without subscription facility) misleads investors on true return attribution.

## NAV Lending
[LLM] Borrowing secured by the value and cash flows of existing fund investments. Fitch published a dedicated NAV finance rating methodology (focused on secondaries funds). NAV loans create structural vulnerability: illiquid loan book paired with financing contingent on lender confidence and collateral valuation.

## Hidden Leverage Scale (OFR data)
[LLM] Bank credit extended to private credit vehicles: $410-540bn. LP capital commitments: ~$300bn. Largest US bank credit lines to PC vehicles: ~$95bn as of 2024 Q4 (up ~145% over 5 years). 60% of commitments concentrated in 5 US GSIBs, utilization ~mid-50%.

## Stress Transmission Mechanism
[LLM] If PC funds draw lines defensively during stress while banks simultaneously tighten credit, liquidity becomes correlated across the system rather than idiosyncratic: stress event -> PC funds draw lines (B) -> banks tighten same time (C) -> correlated liquidity crunch.


