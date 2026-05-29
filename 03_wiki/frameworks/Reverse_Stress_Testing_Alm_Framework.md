---
node_id: reverse_stress_testing_alm_framework_001
type: framework
title: 'Reverse Stress Testing: Process-Oriented Framework for ALM'
aliases:
- RST framework
- Reverse stress test
- Business model failure scenarios
- Stress test ngược
- Kiểm tra khả năng chịu đựng ngược
domain:
  primary: alm
tags:
- reverse_stress_testing
- rst
- liquidity_risk
- capital_risk
- business_model_viability
- scenario_design
- alm
confidence: 1
stability: evolving
thesis: '[LLM] Reverse stress testing (RST) differs from conventional stress testing
  by starting from an outcome — business model failure — and reverse-engineering the
  scenarios that could produce it; this methodology is especially powerful for ALM
  because it forces explicit identification of capital-induced liquidity failures
  (where solvency deterioration triggers funding withdrawal) and liquidity-induced
  capital failures (where funding constraints prevent necessary hedges). [LLM] The
  practical value lies not in the scenarios themselves but in the process of cross-functional
  thinking about vulnerabilities, failure sequences, and management actions before
  a crisis materialises.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Ch 20 — Reverse Stress Testing: Linking Risks, Earnings, Capital and Liquidity
    (Harz University; University of Basel)'
  weight: primary
parent_node: null
related:
- node: '[[Integrated_Stress_Testing_Capital_Liquidity_Link]]'
  relation: related_to
- node: '[[Bank_Capital_Structure_And_Capital_Management_Alm]]'
  relation: related_to
- node: '[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Core Distinction: RST vs Conventional Stress Testing

**Conventional stress test:**
1. Define an adverse macro or market scenario
2. Estimate impact on earnings, capital, and liquidity
3. Check if the bank survives

**Reverse stress test:**
1. Define the outcome: business model becomes unviable
2. Identify scenarios that, if they unfold, would produce this outcome
3. Assess plausibility and derive management actions

[LLM] RST explores deeper into the tail of the distribution than VaR, economic capital, or conventional stress tests — scenarios are, by design, severe enough to break the bank. The primary challenge is not imagination but the process of aggregating knowledge across silos in a structured, consistent way.

## The 6-Step RST Process

**Step 1: Identify Failure Points**

Three dimensions of failure:
- **Earnings failure:** Sustained negative pre-tax income (PTI) making the business model commercially unviable; can precede capital or liquidity exhaustion (reputational damage alone can "break" a bank)
- **Capital failure:** Insolvency (equity = 0), or earlier triggers: breach of internal risk appetite, mandatory AT1 conversion, resolution triggers
- **Liquidity failure:** HQLA buffer drops below predefined threshold; survival horizon breached; contingent funding plan exhausted

[LLM] A fourth dimension is important: **capital-induced liquidity failure** — deteriorating capital causes creditors to withdraw funding before the bank is technically insolvent. This is the mechanism by which solvency stress converts into a liquidity crisis.

**Step 2: Vulnerability Analysis — Risk Inventory**

Conducted top-down (risk-type aggregation) or bottom-up (business unit interviews). Output: a comprehensive heat map classifying identified vulnerabilities by:
- Time horizon to failure ("sudden fatal punch" — days to months vs "slow bleeding out" — multi-year)
- Failure dimension (earnings / capital / liquidity / capital-induced liquidity failure)

[LLM] Interview-based approaches for private banks (the worked example in the source) consistently identified: (a) reputational/conduct risk chains as distinct from direct operational risk, (b) liquidity risk appearing as a downstream consequence of other risk types rather than an independent primary driver.

**Step 3: Generic Storyboards**

[LLM] Rather than jumping directly to specific parameterised scenarios, the framework recommends 8 generic storyboard groups (one per cell of the time × failure dimension matrix). Generic storyboards show the qualitative sequence of events (e.g., "adverse macro → capital amber zone → operational risk incident → capital-induced liquidity drain → liquidity failure") without requiring specific numerical calibration yet.

This prevents "scenario creep" — the tendency for stress testing to become bounded by historical precedent.

**Step 4: Scenario Parameterisation**

Specific calibration of each storyboard, using:
- Historical episodes (for realism check)
- Regulatory guidance (BCBS, PRA, Swiss FINMA, Fed)
- Expert judgement
- Quantitative methods (principal component analysis, maximum likelihood)

**Step 5: Plausibility Checks and Management Actions**

Feasibility checks: Can hedging strategies actually be executed in the RST scenario (e.g., can ALM unwind interest rate positions if the market is stressed)? Does the scenario calibration pass sanity checks vs historical events?

Management action categories:
- **Risk avoidance/hedging:** Review netting agreements, enhance operational risk controls
- **Effect mitigation:** Adjust capital planning, liquidity contingency plan, living will triggers
- **Real options:** Delay decisions pending uncertainty resolution; create management options rather than committing

**Step 6: Monitoring and Reporting**

[LLM] RST scenarios should be monitored continuously, with dashboards tracking proximity of real-world conditions to each identified RST scenario. Annual RST reports should go to the appropriate governing body. If likelihood of a scenario crosses a predefined threshold, mandatory escalation and formal management action follow.

## ALM Applications

ALM experts are natural contributors to bank-wide RST for two reasons:
1. Their macro view across business lines enables assessment of scenario plausibility and cross-risk sequencing
2. They are best placed to assess structural balance-sheet vulnerabilities (IRRBB positions, funding mismatch, HQLA adequacy) under extreme scenarios

[LLM] Specific ALM RST questions addressable with this framework:
- What macro scenario would cause the bank's fixed-rate mortgage book to generate sufficient prepayment to strand long-term funding?
- What interest rate path combined with deposit outflow would simultaneously breach IRRBB limits and LCR?
- What sequence of events (credit deterioration → rating downgrade → covered bond overcollateralisation calls → HQLA depletion) could drive capital-induced liquidity failure?
- Under what conditions does delta hedging of IRRBB positions become impossible (counterparty failure, market illiquidity)?

## Practical Tips

- Start with earnings failure scenarios (easier to reach failure threshold) rather than full capital insolvency scenarios — still useful for risk management dialogue even if the primary RST purpose is the more severe scenarios
- Combine moderate adverse events in sequence rather than requiring a single catastrophic shock — accumulation scenarios are both more plausible and more practically illuminating
- Narrow scope to specific products, business lines, or time horizons when a full bank-wide RST is too complex
