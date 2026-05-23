---
node_id: collateral_velocity_and_pledged_collateral_market_mechanics_001
type: mechanism
title: Collateral Velocity And Pledged Collateral Market Mechanics
aliases:
- Collateral Velocity
- Pledged Collateral Market
- Rehypothecation Mechanics
- Vận tốc tài sản đảm bảo
- Thị trường tài sản đảm bảo
domain:
  primary: financial_markets
tags:
- collateral
- rehypothecation
- repo
- velocity
- qe
- shadow_banking
- plumbing
confidence: 4
stability: evolving
thesis: Pledged collateral functions as a parallel money supply in financial markets
  — it can be reused (rehypothecated) multiple times, creating a 'velocity of collateral'
  analogous to money velocity; QE reduces this velocity by hoovering up high-quality
  collateral from the market, with the bilateral pledged-collateral market (not triparty)
  being the core of global financial plumbing.
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: Ch. 1-2
  weight: primary
related:
- node: '[[Collateral Framework Haircuts Central Bank Credit]]'
  relation: shared_tag:collateral
- node: '[[Collateral Velocity and Rehypothecation]]'
  relation: shared_tag:collateral
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:collateral
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:collateral
- node: '[[Triparty Repo Market Structure And Daily Cycle]]'
  relation: shared_tag:repo
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Overview
Financial markets require two things for settlement: **money** (central bank reserves) and **collateral** (high-quality securities). Collateral functions as "cash equivalent" when it can be reused — and the number of times a piece of collateral is reused is its **velocity**, a concept analogous to the money velocity in monetary macroeconomics [RAW-CLIP].

## The Pledged Collateral Market
Before Lehman (2007): ~$10 trillion in pledged collateral circulating globally in bilateral repo, securities lending, OTC derivatives, and prime brokerage.
After Lehman (2009): ~$5 trillion — a 50% collapse [RAW-CLIP].

Key insight: Lehman's own balance sheet was $691B, but pledged collateral it received (and could reuse) was $798B — the shadow balance sheet was larger than the official one.

## Two Tiers of the Repo Market
| Tier | Mechanism | Collateral Treatment |
|------|-----------|---------------------|
| **Bilateral repo** | Dealer-to-dealer or dealer-to-hedge fund directly | Full reuse (title transfer); dealers pick the best securities first |
| **Triparty repo** | Via BNYM custodian; MMFs as cash providers | Restricted reuse; settlement through custodian |

Analogy: Bilateral repo is like a clothing jobber popping open bales — dealers extract the best collateral for bilateral use; residual goes to triparty [RAW-CLIP].

## Rehypothecation Rules
| Jurisdiction | Legal Basis | Limit |
|-------------|------------|-------|
| **US** | SEC Rule 15c3-3 | Max 140% of client debit balance |
| **UK/EU** | Financial Collateral Directive (title transfer) | Contractually agreed (often unlimited) |
| **Key insight** | Higher rehypothecation in London = hedge funds historically preferred London prime brokers for leverage efficiency [RAW-CLIP] |

## Collateral Velocity and QE
QE mechanism on collateral:
1. Fed buys Treasuries (good collateral) from non-banks → pays with reserves
2. Good collateral exits the bilateral pledged market → collateral velocity falls
3. Non-banks hold reserves (or MMF shares) instead of Treasuries → less collateral available for securities lending / repo chains

QE thus creates a **dual effect**: (1) expands monetary reserves; (2) **compresses collateral velocity**, reducing private-sector credit creation capacity. When QE is unwound (QT), collateral returns to market, velocity rises — but banks' balance sheet capacity may be constrained by SLR/LCR [RAW-CLIP].

## Policy Implication
Central banks' expanded balance sheets make them part of the financial plumbing — and potentially impair monetary policy transmission:
- If the Fed holds Treasuries, those Treasuries are not available for repo chains → market rates (repo/SOFR) may not respond normally to FFR changes
- "The larger the balance sheet, the more the central bank is part of the plumbing, and the more monetary policy transmission is weakened" [RAW-CLIP]


