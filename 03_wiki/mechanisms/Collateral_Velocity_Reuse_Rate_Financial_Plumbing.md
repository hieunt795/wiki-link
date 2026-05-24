---
node_id: collateral_velocity_reuse_rate_plumbing_001
type: mechanism
title: Collateral Velocity Reuse Rate And Financial Plumbing
aliases:
- collateral velocity
- collateral reuse rate
- pledged collateral market
- rehypothecation chains
- tốc độ tài sản thế chấp
- tái sử dụng tài sản thế chấp
domain:
  primary: financial_markets
  secondary: monetary_policy
tags:
- collateral
- repo
- shadow_banking
- rehypothecation
- financial_plumbing
- velocity
- dealer_banks
- financial_stability
confidence: 4
stability: stable
thesis: "Collateral velocity (reuse rate) = total pledged collateral received by large dealer banks / primary collateral sources (hedge funds + custodians); the ratio measures the length of collateral chains and acts as an analog to the velocity of money — higher velocity means greater financial lubrication; velocity fell from ~3.0x (end-2007, $10T total) to ~1.8x (end-2015, $5.6T), driven by counterparty risk and QE draining good collateral from the market; 10-15 global dealer banks are the sole intermediaries capable of moving collateral across borders in bulk, and deleveraging has two components: balance-sheet shrinking AND shortening of collateral chains (reduced interconnectedness), the latter being underappreciated."
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: lines 595-920 (Chapters 1-2; collateral definition, velocity methodology, deleveraging)
  weight: primary
related:
- node: '[[QE Collateral Velocity Monetary Policy Transmission]]'
  relation: extends
- node: '[[Uncleared Bilateral Repo UBR Hedge Fund Leverage Systemic Risk]]'
  relation: related_mechanism
- node: '[[Fed Balance Sheet Floor Payment System Reserve Demand]]'
  relation: related_mechanism
- node: '[[Nbfi Sovereign Market Supervisory Gap]]'
  relation: related_concept
date_created: '2026-05-23'
date_updated: '2026-05-24'
---

## Scope Boundary

[LLM] This node is canonical for Singh-style collateral velocity, pledged-collateral measurement, and dealer-bank chain length.

[LLM] [[Collateral_Velocity_Rehypothecation]] is an older overview and should not be expanded with the full measurement framework.

[LLM] QE's effect on collateral velocity belongs to [[QE_Collateral_Velocity_Monetary_Policy_Transmission]], while collateral upgrade/rental chains belong to [[Collateral_Transformation_Chain]].

## What Is Pledged Collateral?

Financial collateral = liquid securities (debt or equity) that are liquid, mark-to-market, and part of a legal cross-border master agreement — used as "cash equivalent" to settle accounts in cross-border markets. Collateral does not have to be AAA-rated; liquidity and legal enforceability are the requirements. [RAW-CLIP]

**Title transfer vs. pledge**: Title transfer (used in repo, securities lending, OTC derivatives under ISDA English-law CSAs) gives full ownership to the collateral taker → free to reuse in any way; must return *equivalent* collateral (same type/value, not the exact same security). Pledge: collateral taker holds security interest only; rehypothecation requires express contractual grant. [RAW-CLIP]

**Rehypothecation vs. reuse**: Rehypothecation = onward pledging as security for collateral taker's own obligations. Reuse = any use including sale or lending. Title-transfer arrangements make reuse inherent; pledge arrangements require explicit grant. [RAW-CLIP]

**US vs. non-US**: In the US, SEC Rule 15c3-3 limits broker-dealer rehypothecation to 140% of the customer's debit balance. Outside the US (UK, continental Europe), title transfer is standard → more collateral freed for reuse, longer chains, higher velocity. [RAW-CLIP]

## The Scale of the Pledged Collateral Market

Pre-Lehman (end-2007): ~$10 trillion total pledged collateral intermediated by 10-15 large dealer banks — larger than US M2. [RAW-CLIP]

Post-crisis: Market contracted to ~$5 trillion (end-2009), partially recovered to ~$5.6 trillion (end-2015) — still ~45% below pre-Lehman peak. [RAW-CLIP]

Off-balance-sheet character: Pledged collateral appears only in footnotes to financial statements under "fair value of securities received as collateral that may be repledged." Example: Lehman's last balance sheet (Nov 2007) was $691B; pledged collateral received with reuse rights was $798B — larger than the balance sheet itself. [RAW-CLIP]

## Collateral Velocity: Definition and Measurement

**Velocity formula**:
> Velocity = Total collateral received by large dealer banks / Primary collateral sources

Primary collateral sources (two buckets):
1. **Hedge funds**: via prime broker agreements and repo strategies; estimated ~$1.7T (2007), ~$2.0T (2015)
2. **Security lending (custodians)**: pension funds, insurers, official sector accounts via RMA data; ~$1.7T (2007), ~$1.1T (2015)

**Velocity data (Singh 2011, updated)**:

| Year | Primary Sources ($T) | Total Pledged ($T) | Velocity |
|------|---------------------|-------------------|----------|
| 2007 | 3.4 | 10.0 | 3.0 |
| 2010 | 2.4 | 5.8 | 2.4 |
| 2012 | 2.8 | 6.0 | 2.2 |
| 2013 | 2.85 | 5.8 | 2.0 |
| 2015 | 3.1 | 5.6 | 1.8 |

[RAW-CLIP]

Velocity decline drivers: (1) heightened counterparty risk post-Lehman → more collateral siloed idle in segregated accounts; (2) QE draining good collateral from market (taking it onto central bank balance sheets); (3) regulatory constraints limiting dealer balance-sheet space. [RAW-CLIP]

## Two Channels of Deleveraging (Shin 2009 Framework)

Deleveraging has two mathematically separable components:

1. **Balance-sheet shrinking**: Haircut/price increases → on-balance-sheet assets contract → debt contracts. Extensively studied in academic literature. [RAW-CLIP]

2. **Reduced interconnectedness (shorter collateral chains)**: Counterparty risk aversion → banks ring-fence themselves → collateral sits idle → chains shorten even without price changes. Loss of $4-5T in collateral flow since end-2007 attributable to shorter chains, not just price declines. This component received minimal attention at the time of writing. [RAW-CLIP]

**Key insight**: The financial system can implode (shorter chains, higher credit costs) even while balance sheets appear stable, because the interconnectedness (the Π matrix in Shin's notation) contracts independently of asset prices. [RAW-CLIP]

## The 10-15 Bank Core

Only 10-15 large global dealer banks (Goldman Sachs, Morgan Stanley, JPMorgan, Citi, BofA/ML in the US; Deutsche, UBS, Barclays, CS, SocGen, BNP, HSBC, Nomura, RBS in Europe) can move collateral across borders in bulk. [RAW-CLIP]

Entry into this market requires: global footprint, global clients, ability to price and move liquid securities in seconds. Legal perfection (title transfer, ISDA master agreements, prime-brokerage agreements) is essential for cross-border collateral movement. [RAW-CLIP]

**Bilateral vs. triparty**: Bilateral repo (the "market for collateral") is the core of financial plumbing — fully mark-to-market, reuse possible. Triparty repo ($1.6T US, down from $2.8T) is a "market for funding" — cash for dealer banks collateralized by securities, cleared via JPMorgan or BoNY. Bilateral market is the primary source of collateral velocity; triparty is downstream. [RAW-CLIP]

## Monetary Policy Implications

A shortage of acceptable collateral cascades similarly to a reduction in the monetary base:
- First-round impact: Primary collateral pools (hedge funds, pensions, insurers) become risk-averse → collateral stays idle → fewer completed transactions
- Second-round impact: Shorter chains → higher cost of capital for the real economy → transmitted via banks passing on higher funding costs [RAW-CLIP]

Collateral velocity is therefore a financial conditions indicator alongside money supply — it captures the non-M2 funding that asset managers provide to banks, which is not captured in traditional monetary aggregates. [RAW-CLIP]
