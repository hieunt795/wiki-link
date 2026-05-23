---
node_id: collateral_framework_haircuts_central_bank_credit_001
type: mechanism
title: Collateral Framework Haircuts Central Bank Credit
aliases:
- collateral framework
- haircuts
- eligible collateral
- collateral scarcity
- khung tai san dam bao
- ty le cat giam
- ELA
domain:
  primary: monetary_policy
tags:
- collateral
- haircuts
- central-bank
- credit-operations
- ela
- safe-assets
confidence: 4
stability: evolving
thesis: 'Central bank collateral frameworks define eligible assets, haircuts, and
  concentration limits for CB credit operations. Haircuts serve as the primary risk
  buffer and function as a secondary monetary policy instrument: tighter haircuts
  raise effective funding costs across the economy. Collateral scarcity — when eligible
  assets are insufficient to meet reserve needs — can cause overnight rates to spike
  above target independently of CB intent.'
source_refs:
- path: 02_sources/books/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md
  pages: Ch9, Bindseil 2014
  weight: primary
related:
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:collateral
- node: '[[Collateral Velocity and Rehypothecation]]'
  relation: shared_tag:collateral
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:collateral
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:collateral
- node: '[[Central Bank Balance Sheet Structure Liabilities Assets]]'
  relation: shared_tag:central-bank
date_created: '2026-05-20'
date_updated: '2026-05-20'
---


Collateral frameworks determine which assets banks can pledge to access CB credit.

**Four dimensions of collateral eligibility (Bindseil Ch9):**
1. Asset eligibility criteria: issuer type, instrument type, minimum credit rating (ECB: BBB-)
2. Valuation: mark-to-market or model price (conservative principle)
3. Haircuts: percentage reduction applied to collateral value to buffer against market risk during liquidation period. Higher haircut = less cash per unit of collateral = binding constraint.
4. Quantitative limits: concentration limits, correlation limits with counterparty credit risk

**Haircut function:** ECB publishes tiered haircut table by (liquidity category x maturity bucket). Example: sovereign bonds 0-1yr = 0.5%; covered bonds 7-10yr = 5.5%; ABS = 10-24% depending on structure.

**Collateral as monetary policy instrument:**
Changing haircuts or eligibility criteria can substitute for rate changes. Tightening haircuts raises effective funding cost for economy: firms borrowing from banks face higher margins because banks have less CB credit headroom. This was modeled by Bindseil as an additional policy dimension.

**Collateral scarcity:**
When eligible assets are scarce (e.g. post-LTRO stigma, or safe asset shortage), the collateral constraint binds before reserve needs are met. Banks in scarcity face involuntary deleveraging. Symptoms: overnight rates spike above policy rate; repo rates spike for specific collateral.

**Segregation of collateral sets:**
CB may accept different collateral pools for different operations (standard vs. emergency). ELA (Emergency Liquidity Assistance) accepts non-standard collateral at national CB risk. Creates two-tier collateral framework during crises.


