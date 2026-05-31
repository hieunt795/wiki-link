---
node_id: collateral_velocity_001
type: concept
title: Collateral Velocity and Rehypothecation
aliases:
- collateral reuse
- rehypothecation
- pledged collateral velocity
- tái sử dụng tài sản thế chấp
- tốc độ lưu thông tài sản thế chấp
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
  - shadow_banking
tags:
- collateral
- rehypothecation
- repo
- shadow-banking
- financial-plumbing
- leverage
confidence: 3
stability: stable
thesis: 'Collateral velocity measures how many times a given piece of collateral is
  reused (pledged and re-pledged) within the financial system. Pre-Lehman, the pledged-collateral
  market reached ~$10 trillion — comparable to M2 — and collapsed to ~$5 trillion
  in 2008-9 as reuse chains broke. High velocity amplifies credit creation; restricted
  velocity (via QE or regulation) impairs financial intermediation analogously to
  a drying-up of interbank markets.

  '
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: Ch.1-2, pp.1-30
  weight: primary
parent_node: '[[Shadow_Banking_Market_Based_Finance]]'
related:
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: mechanism_of
- node: '[[Shadow_Banking_Market_Based_Finance]]'
  relation: component_of
- node: '[[Collateral_Framework_Haircuts_Central_Bank_Credit]]'
  relation: contrasts_with
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:collateral
- node: '[[Collateral Framework Haircuts Central Bank Credit]]'
  relation: shared_tag:collateral
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:collateral
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:collateral
- node: '[[Triparty Repo Market Structure And Daily Cycle]]'
  relation: shared_tag:repo
date_created: 2026-05-20
date_updated: 2026-05-24
---


## Scope Boundary

[LLM] This node is an older overview of collateral velocity and rehypothecation.

[LLM] The canonical detailed treatment of the pledged-collateral reuse-rate methodology is [[Collateral_Velocity_Reuse_Rate_Financial_Plumbing]].

[LLM] The QE-specific monetary-policy transmission channel belongs to [[QE_Collateral_Velocity_Monetary_Policy_Transmission]].

[LLM] The transaction-chain service that converts lower-quality collateral into HQLA belongs to [[Collateral_Transformation_Chain]].

## Core Mechanism

Financial collateral — any liquid security (not necessarily AAA) that is mark-to-market and covered by a legal cross-border master agreement — functions as a **cash equivalent** for settling interbank obligations. The key feature enabling this is the right to reuse: under title-transfer arrangements (repo, securities lending, OTC derivatives), the collateral taker acquires full legal ownership and can re-pledge the security to a third party.

**Velocity** = total pledged-collateral in system / underlying primary collateral pool

Pre-Lehman velocity was approximately 2.5–3×: each unit of primary collateral (e.g., UST) was reused 2–3 times before reaching its final resting place. This multiplied financial lubrication beyond what money metrics captured.

## Rehypothecation vs. Reuse

| Term | Definition | Jurisdiction |
|------|-----------|-------------|
| Rehypothecation | Collateral taker uses received collateral as security for its own obligations to a third party (onward pledging) | US: SEC Rule 15c3-3 caps at 140% of client debt |
| Reuse (broader) | Any use compatible with ownership — sell, lend, pledge | EU: legally supported under Financial Collateral Directive; UK: contractual limits |
| Title transfer | Ownership changes; collateral taker free to use without restriction | Europe: repo treated as sale + forward repurchase |

## Collateral Market Size and Crisis Dynamics

| Period | Pledged-collateral volume | Notes |
|--------|--------------------------|-------|
| End-2007 (peak) | ~$10 trillion | Lehman balance sheet $691B but pledged collateral footnote $798B |
| 2008-9 (crisis) | ~$5 trillion | 50% collapse; financial lubrication halved |
| Post-crisis trend | $5-7 trillion | Regulatory restrictions (LCR, leverage ratio, CCP mandates) constrain reuse |

The collapse in collateral velocity during 2008-9 is economically equivalent to a collapse in interbank lending. Both are forms of financial deleveraging.

## QE's Collateral Effect

Central bank QE removes high-quality collateral (USTs, Bunds) from circulation and replaces it with reserves. Reserves cannot be rehypothecated — they sit at the central bank. This **suppresses collateral velocity**, which may partially offset the stimulative intent of QE by impairing secured funding markets. [LLM] Singh argues this monetary-policy/collateral tension deserves more attention from policymakers.

## Policy Implications

1. **Velocity as monetary indicator**: collateral reuse rate functions alongside M2/M3 as a measure of financial liquidity; policymakers who ignore it miss a key channel
2. **QE exit complexity**: unwinding QE re-releases collateral into markets → velocity rises → secured funding conditions ease beyond what reserve draining alone suggests
3. **SLR/LCR drag**: Basel III constraints that limit dealer balance sheet simultaneously cap collateral intermediation capacity — see [[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]

