---
node_id: alm_balance_sheet_optimization_framework_001
type: framework
title: ALM Balance Sheet Optimization Framework
aliases:
- ALM Optimization
- Balance Sheet Optimization
- Strategic ALM
- Target Balance Sheet Profile
- tối ưu hóa bảng cân đối ALM
- quản lý bảng cân đối chiến lược
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- alm
- optimization
- balance_sheet
- nii
- eve
- liquidity
- irrbb
- funding
confidence: 1
stability: stable
thesis: '[LLM] ALM balance sheet optimization is a formal process that defines the
  target composition of assets and liabilities by simultaneously maximizing asset
  profitability and minimizing funding costs, subject to constraints on interest rate
  risk (NII volatility, EVE), liquidity ratios (LCR, NSFR, structural gaps), capital
  absorption, and funding concentration — replacing reactive balance sheet management
  with a proactive, mathematically grounded approach. [LLM] The optimization output
  is a target profile for the banking book that maximizes profitability within regulatory
  and internal risk limits, integrating IRR and liquidity risk under a single framework
  rather than managing them in silos.

  '
source_refs:
- path: 02_sources/books/alm/A - Asset liability optimization.md
  pages: Introduction, Ch 1, Ch 4
  weight: primary
parent_node: '[[ALM_Banking_Book_Risk_Management]]'
related:
- node: '[[ALM_Banking_Book_Risk_Management]]'
  relation: component_of
- node: '[[Income_Gap_vs_Economic_Value_Gap]]'
  relation: related_to
- node: '[[ALM_Structural_Liquidity_Gap]]'
  relation: component_of
- node: '[[FTP_Methodology]]'
  relation: implements
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Core Concept

[LLM] The ALM balance sheet optimization framework transforms ALM from a reactive function (accepting the balance sheet structure that emerges from commercial activity) into a proactive function that shapes the balance sheet structure to achieve a defined target profile. [LLM] Lubinska defines this target profile as "the definition of a composition of assets and liabilities so that the profitability of the banking book reaches its maximum, taking into account a number of regulatory and internal risk constraints."

## The Optimization Problem Structure

[LLM] The optimization is formalized as a mathematical programming problem with two objective functions and a set of constraint functions:

**Asset side objective:** Maximize asset income (return on the asset portfolio)  
**Liability side objective:** Minimize cost of funding  

**Constraint functions include:**
- Interest rate risk: NII volatility limits (Δ NII within ±200 bps shock) and EVE limits
- Short-term liquidity: LCR ≥ 100%, gap ratio limits by time bucket
- Structural liquidity: NSFR ≥ 100%, structural gap ratios beyond 1Y, 3Y, 5Y horizons
- Capital absorption: capital adequacy ratio constraints
- Funding concentration: avoidance of excessive reliance on any single funding source
- Behavioral assumptions: rollover rates for time deposits, balance volatility of CASA

[LLM] The constraint functions establish the "feasible region" within which the optimization operates, ensuring regulatory compliance is maintained at the optimum. The Lagrange multipliers method is used for equality constraints; Kuhn-Tucker theorem for inequality constraints (which are the more common form in banking, since most limits are expressed as inequalities, e.g., NII volatility must be below a threshold).

## The ALM Triangle: Liquidity-Capital-Profitability

[LLM] A central insight of the framework is the existence of three-way trade-offs that cannot all be simultaneously maximized:

1. **Profitability vs. liquidity:** Building larger HQLA buffers and extending funding maturity reduce NIM (opportunity cost of carry on liquid assets; higher cost of longer-term funding).
2. **Profitability vs. capital:** Higher-yielding assets (e.g., corporate loans) consume more capital via risk weights.
3. **Liquidity vs. IRR:** Extending asset duration to ride the yield curve improves NIM in low-rate environments but increases EVE sensitivity.

[LLM] The optimization process makes these trade-offs explicit and quantifiable, allowing the treasurer and ALCO to make informed decisions about which constraints are binding and where to relax them.

## Integration of IRR and Liquidity Risk

[LLM] The key methodological contribution is the rejection of a silo-based approach. Lubinska shows through a simple example (fixed-rate loan funded by a 3-month floating liability) that:
- The interest rate gap and the liquidity gap occur at different points in time
- Managing only one dimension (e.g., closing IRR via IRS) leaves the other open (liquidity risk remains if funding maturity is shorter than asset maturity)
- The ALM margin has two components: locked-in margin (already crystallized) and margin at risk (uncertain, exposed to rate moves or liquidity spread changes)

[LLM] The total NIM of the banking book therefore depends on both the interest rate positioning and the funding spread positioning, and optimizing one without the other leads to suboptimal outcomes.

## Mathematical Framework

[LLM] The optimization is solved using:
- **Lagrange multipliers** for equality-constrained problems
- **Kuhn-Tucker theorem** for inequality-constrained problems (the typical banking case)
- **Interior-point methods** (e.g., MATLAB `fmincon`) for non-linear constraint cases

[LLM] The model is dynamic — it can be run at predefined intervals and under multiple scenarios (base case, +200bps, -200bps, steepener, flattener), providing the treasurer with a benchmark for the optimal balance sheet composition under each scenario.

## Practical Output

[LLM] The optimization output serves as a benchmark for:
- The funding plan (optimal mix of retail deposits, wholesale funding, bond issuance)
- Asset allocation decisions (target proportions of fixed vs. floating, short vs. long duration)
- Hedging strategy design (which residual mismatches to hedge with derivatives)
- ALCO reporting: quantified economic benefit of achieving vs. not achieving the target profile

[LLM] Case studies in Lubinska (2020) demonstrate that applying the optimization model delivers measurable P&L improvement relative to the unoptimized baseline, both in NII and in funding cost reduction.
