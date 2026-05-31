---
node_id: bcbs_liquidity_internal_pricing_ftp_p4_001
type: regulation
title: BCBS Liquidity Internal Pricing (FTP) — Principle 4 (2008)
aliases:
- BCBS liquidity FTP Principle 4
- liquidity transfer pricing Basel
- internal liquidity cost allocation
- liquidity cost benefit risk attribution
- định giá thanh khoản nội bộ FTP
- phân bổ chi phí lợi ích rủi ro thanh khoản
domain:
  primary: banking_regulation
  secondary: banking_operations
tags:
- ftp
- funds_transfer_pricing
- liquidity_risk
- internal_pricing
- incentive_alignment
- business_line
- bcbs
- bcbs144
confidence: 4
stability: stable
thesis: 'BCBS Principle 4 (2008) requires banks to incorporate liquidity costs, benefits
  and risks in internal pricing (FTP), performance measurement and new product approval
  for all significant on- and off-balance sheet activities. The purpose is incentive
  alignment: business lines that create liquidity risk must bear the cost of that
  risk, so that line management incentives reinforce rather than undermine the bank-wide
  liquidity risk tolerance. A liquidity charge is assigned to positions, portfolios
  or transactions based on anticipated holding periods, market liquidity characteristics
  and the benefit of stable funding sources. This principle directly addresses the
  pre-2008 misalignment where business lines profited from activities that created
  liquidity risk without bearing the cost.

  '
source_refs:
- path: 02_sources/regulator/bcbs/bcbs144 - Principles for Sound Liquidity Risk Management and Supervision.md
  pages: 'para 19–21 (Principle 4 full text: attribution, transparency, product approval),
    para 3 (pre-2008 failure: incentives misaligned with risk tolerance)'
  weight: primary
parent_node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
related:
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: parent_framework
- node: '[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]'
  relation: nmd_ftp_connection
- node: '[[Funds_Transfer_Pricing_Rate_Decomposition_Base_Liquidity_Credit_Optionality_Components]]'
  relation: ftp_rate_decomposition
- node: '[[Ftp_As_Unified_Balance_Sheet_Control_Mechanism_Transmission_To_Risk_Factors]]'
  relation: implementation_mechanism
- node: '[[Ftp_Curve_Construction_By_Tenor_Short_Medium_Long_Term_Spread_Framework]]'
  relation: curve_construction
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## The Pre-2008 Problem Principle 4 Solves

"Many banks had not considered the amount of liquidity they might need to satisfy
contingent obligations, either contractual or non-contractual, as they viewed
funding of these obligations to be highly unlikely."

"Incentives at the business level were misaligned with the overall risk tolerance
of the bank." [RAW-BOOK bcbs144 para 3]

Before Principle 4, a business line could generate revenue from activities (ABCP
conduits, committed credit lines, complex derivatives) while the liquidity risk
was borne by the central treasury — creating a cross-subsidy from prudent
balance sheet activities to risky off-balance sheet exposures.

---

## The Requirement

```
"A bank should incorporate liquidity costs, benefits and risks in the internal
pricing, performance measurement and new product approval process for all
significant business activities (both on- and off-balance sheet), thereby
aligning the risk-taking incentives of individual business lines with the
liquidity risk exposures their activities create for the bank as a whole."
[RAW-BOOK bcbs144 Principle 4]

SCOPE:
  → All significant business activities (not just funded balance sheet)
  → On-balance sheet: loans, securities, deposits
  → Off-balance sheet: undrawn commitments, letters of credit, guarantees,
    ABCP conduit backup lines, derivative collateral obligations
  → Contingent exposures "which may not immediately have a direct balance sheet impact"
  [RAW-BOOK bcbs144 para 19]
```

---

## FTP Charge Design

```
FACTORS TO INCORPORATE IN LIQUIDITY CHARGE:
  ① Anticipated holding period of asset or liability
     → Short-term assets: lower charge; long-term assets: higher charge
     → Demand deposits: benefit from implied stable funding → FTP credit
  ② Market liquidity risk characteristics
     → Illiquid assets: higher charge (harder to liquidate in stress)
     → Liquid assets (HQLA): lower charge
  ③ Stressed liquidity availability
     → How would this position behave under P10 stress scenarios?
  ④ Stable funding benefit
     → Retail deposits, long-term wholesale: FTP credit (benefit allocation)
     → Volatile wholesale funding: FTP debit (cost allocation)
  [RAW-BOOK bcbs144 para 19]

STRESS DIMENSION:
  "The quantification and attribution of these risks should... include consideration
  of how liquidity would be affected under stressed conditions."
  [RAW-BOOK bcbs144 para 20]
  → FTP is not a normal-conditions-only price; stress scenarios must be reflected
```

---

## Attribution: Explicit and Transparent

```
"The quantification and attribution of these risks should be explicit and
transparent at the line management level"
[RAW-BOOK bcbs144 para 20]

IMPLEMENTATION REQUIREMENTS:
  ① Charge must be visible to line managers, not buried in overhead allocation
  ② Attribution to specific positions, portfolios or transactions — not just aggregated
  ③ Analytical framework reviewed as business and market conditions change
  ④ Must be addressed in new product approval process
     → New products generate liquidity risk that FTP must capture before launch
  [RAW-BOOK bcbs144 para 19–21]
```

---

## FTP Credit for Stable Funding: The Benefit Side

Principle 4 is not just about charging for liquidity costs — it also allocates
liquidity benefits:

```
ACTIVITIES RECEIVING FTP CREDIT (benefit):
  → Business lines that attract retail deposits (sticky funding)
  → Long-term wholesale funding (NSFR-like benefit)
  → Collateralised activities (self-funding via pledging)

ECONOMIC EFFECT:
  → Lines with stable funding receive lower net funding cost
  → Lines with volatile wholesale funding receive higher net funding cost
  → Creates market-like pricing for the internal liquidity pool
[LLM — derived from para 19 "benefits from having access to relatively stable
sources of funding, such as some types of retail deposits"]
```

---

## Linkage to Non-Maturity Deposit (NMD) Replication

The principle directly connects to NMD modelling:

```
Retail deposits receive FTP credit proportional to their behavioural stability.
But stability requires modelling:
  → What is the "core" stable portion of demand deposits?
  → What maturity to assign for FTP purposes?

This becomes the NMD replication portfolio problem:
  → P4 requires the BENEFIT be priced; NMD modelling determines what that benefit is
  → If core deposits modelled with 2-year replication → FTP credit based on 2-year rate
  → If demand deposits treated as overnight → FTP credit = overnight rate (much smaller)

P4 creates the incentive; NMD modelling sets the magnitude.
[LLM — policy logic from para 19 + NMD methodology connection]
```
