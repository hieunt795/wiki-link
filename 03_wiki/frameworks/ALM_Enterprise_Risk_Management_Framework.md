---
node_id: alm_enterprise_risk_management_framework_001
type: framework
title: ALM in the Enterprise Risk Management Framework
aliases:
- ALM ERM integration
- ALCO governance framework
- bank risk appetite ALM
- khung quản trị rủi ro tài sản nợ
- ALM trong quản lý rủi ro doanh nghiệp
- ủy ban ALCO
domain:
  primary: alm
  secondary: []
tags:
- risk appetite
- earnings-at-risk
- revaluation-reserve
- governance
confidence: 1
stability: stable
thesis: 'ALM operates within the enterprise risk management (ERM) cycle as the governance
  mechanism that translates board-level risk appetite statements into balance sheet
  constraints on interest rate, liquidity, and capital risk; the five-step ERM cycle
  (identify → select controls → implement → monitor → report) and the ALCO committee
  structure jointly ensure that structural risks are hedged or capitalized within
  approved tolerances. [LLM]

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'Chapter 2: ALM in the Enterprise Risk Management Framework'
parent_node: null
related:
- node: '[[IRRBB_Standardised_Versus_Internal_Model_Approach]]'
  relation: related_to
- node: '[[ILAAP_Supervisory_Liquidity_Framework]]'
  relation: related_to
- node: '[[Bcbs_Irrbb_Standards_2016]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- node: '[[ERM]]'
  relation: related_to
- node: '[[ALCO]]'
  relation: related_to
- node: '[[CET1]]'
  relation: related_to
- node: '[[RWA]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

ALM operates within the enterprise risk management (ERM) cycle as the governance mechanism that translates board-level risk appetite statements into balance sheet constraints on interest rate, liquidity, and capital risk. [LLM]

## Five-Step ERM Cycle

The risk management process follows a five-step cycle applied to all banking-book risks: [LLM]

1. **Identify** — catalogue sources of structural risk (repricing gaps, optionality, basis, credit spread, liquidity mismatch). [LLM]
2. **Select controls** — choose whether to retain, transfer, or hedge each risk source within the board-approved risk appetite. [LLM]
3. **Implement** — execute hedging programs and FTP pricing rules; structural risks are managed by ALCO, transferable risks are passed to treasury via internal transfer pricing. [LLM]
4. **Monitor** — track limit utilization for each risk metric against appetite thresholds; escalate breaches. [LLM]
5. **Report** — produce ALCO packs covering all four structural-risk dimensions (earnings, valuation, capital, commercial). [LLM]

## Risk Appetite Statement — Capital Lens

A well-formed CET1 risk appetite statement takes the form: [LLM]

> "In a 1-in-X years stress scenario, the CET1 ratio must not fall below A%, and must recover to A+B% within the planning horizon using retained earnings alone." [LLM]

This structure forces calibration of both the floor (A%) and the recovery buffer (B%), ensuring resilience and regenerative capacity are addressed simultaneously. [LLM]

## Four Structural-Risk Metrics

ALM governance tracks four complementary metrics to span the ERM risk appetite: [LLM]

| Metric | What it measures | Risk appetite lens |
|--------|------------------|--------------------|
| **Earnings-at-Risk (EaR)** | NII sensitivity to rate shocks over 1–2 year horizon | P&L / dividend stability |
| **Revaluation-reserve-at-risk** | OCI volatility from AFS portfolio mark-to-market | Regulatory capital volatility |
| **RWA-at-risk** | Capital consumption under stress (credit migration, market risk) | CET1 adequacy |
| **Commercial result buffer** | Cushion from customer margin income before structural losses erode capital | Business model sustainability |

[LLM]

## ALCO Governance Structure

The Asset-Liability Committee (ALCO) sits between the Board risk appetite and the treasury execution function: [LLM]

- **Board / Risk Committee** — sets the overall risk appetite (CET1 floor, NII tolerance, liquidity survival horizon). [LLM]
- **ALCO** — translates appetite into limits; approves hedging programs; reviews FTP methodology; monitors EVE, NII, LCR, NSFR versus limits. [LLM]
- **ALM / Treasury desk** — executes approved hedges; manages day-to-day balance sheet positioning within ALCO limits. [LLM]
- **Risk / Finance** — independent measurement, model validation, and reporting back to ALCO. [LLM]

Structural risks (IRRBB, CSRBB, structural FX, structural liquidity) remain on ALCO's mandate. Transferable market risks (trading book, customer derivatives) are transferred to treasury via FTP and managed under separate VaR limits. [LLM]

## Integration with Pillar 2 Capital

Under BCBS IRRBB Principle 9, a material EVE sensitivity must translate into an ICAAP capital allocation. [LLM] The ERM framework links ALCO-monitored EVE positions to the ICAAP capital stack, ensuring that residual IRRBB after hedging is capitalized at the approved internal stress confidence level. [LLM]

---
*Source: Chapter 2 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material and have not been independently verified. Confidence: 1.*
