---
node_id: alm_operating_model_front_middle_office_001
type: framework
title: ALM Operating Model — Front Office vs Middle Office
aliases:
- ALM operating model
- front office Treasury
- middle office ALM
- ALM organizational model
- mô hình hoạt động ALM
- ALM văn phòng giao dịch
- ALM văn phòng giám sát
- xung đột lợi ích ALM
domain:
  primary: alm
  secondary: []
tags:
- ALM-operating-model
- front-office
- middle-office
- ALCO
- conflicts-of-interest
- lines-of-defense
- FTP
confidence: 3
stability: stable
thesis: 'Banks organize ALM/Treasury in two contrasted operating models — front office
  (executes deals, profit center with KPIs on trading operations) vs middle office
  (analytical and strategic, no direct deal execution) — because one department cannot
  set limits on positions AND execute deals for those positions, construct an internal
  yield curve AND make deals with margin to that curve simultaneously without conflict
  of interest.

  '
source_refs:
- path: 02_sources/books/alm/A - Bank Asset Liability Management Best Practice_ Yesterday,
    Today and Tomorrow-De Gruyter (2021).md
  pages: 'Chapters 10–11: ALM Operating Model; ALM Inside a Risk Management Triangle'
parent_node: null
related:
- node: '[[ALM_Enterprise_Risk_Management_Framework]]'
  relation: related_to
- node: '[[Ftp_Transfer_Price_Curve_And_Structural_Contribution]]'
  relation: related_to
- node: '[[Alm_Role_Srep_Pillar2_Capital_Liquidity]]'
  relation: related_to
- node: '[[ALM]]'
  relation: related_to
- node: '[[ALCO]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Thesis

Banks organize ALM/Treasury in two contrasted operating models — front office (executes deals, profit center) vs middle office (analytical and strategic, no direct deal execution) — to prevent conflicts of interest that arise when a single unit sets limits, quotes rates, and executes hedges simultaneously. [LLM] ALM cannot be merged into Risk, the Trading Desk, or Finance because each pairing creates disqualifying conflicts of interest; ALCO is the cross-functional governance mechanism that resolves these tensions.
## Four ALM Task Domains

ALM responsibilities span four interconnected task domains that must be carefully separated to avoid conflicts:
| Domain | Key responsibilities |
|--------|---------------------|
| **ALM risk management** | Interest rate gap, liquidity gap, OCP management, stress testing |
| **Balance sheet structure targeting** | Capital adequacy steering, debt issuance, securitization, funding/capital planning |
| **Price benchmarking** | FTP curve construction, product pricing, business profitability models |
| **Resources allocation** | NII/NIM forecasting, RoE targets, RoRWA, capital allocation |


## Front Office vs Middle Office Operating Model

### Front Office ALM

- ALM desk is a **profit center** — KPIs include income from balance sheet positioning.- Responsible for: all short-term tactical tasks (liquidity buffer management, repo, securities purchases, derivatives execution, FX operations) plus strategic going-concern and gone-concern tasks.- Risk: creates incentive for ALM to use liquidity management limits to achieve proprietary returns rather than pure risk management.
### Middle Office ALM

- ALM desk is primarily **analytical and strategic** — no direct deal execution mandate.- Responsible for: strategic going-concern tasks (IRRBB management, gap modeling, liquidity risk, contingency planning, FTP methodology, behavioral modeling) and gone-concern tasks (ICAAP/ILAAP, stress testing, MREL, resolution/recovery planning).- The Trading Desk executes approved hedges at ALM's request.- Lower profit incentive but cleaner separation of recommendation from execution.
## Conflicts of Interest: Why ALM Cannot Be Merged

### ALM + Risk (disqualified)

Two specific conflicts:1. The unit assessing risk would tend to report improvement after implementing its own measures, regardless of actual dynamics.2. Aware of the cost and difficulty of specific hedging instruments, the unit could systematically underestimate risks to avoid using inconvenient instruments.
Additionally, FTP curve construction — a core ALM function — has no place in Risk.
### ALM + Trading Desk (disqualified)

Three specific conflicts:1. Liquidity management limits could be redirected toward proprietary positions when attractive.2. Awareness of instrument costs could bias risk management recommendations toward instruments convenient for the desk.3. FTP curve could be manipulated by the same unit that benefits from it.
### ALM + Finance (disqualified)

The Finance Department's KPI on budget targets creates incentive to increase risk appetite to improve results, directly conflicting with ALM's mandate to constrain balance sheet risk.
## ALM's Correct Reporting Line

ALM should report to the **CFO or CEO** (when they have KPIs on risk parameters) or to the unit responsible for long-term strategy. [LLM] This ensures:- Independence from risk-taking functions.- Access to full balance sheet and managerial accounting data.- Authority to give approved requests to the Trading Desk for hedging.
## ALM Within Three Lines of Defense

| Line | Role |
|------|------|
| **Business lines** | Generate risk (loans, deposits) — not a line of defense |
| **1st line — ALM/Treasury** | Manages balance sheet (FTP, target structure, hedging, model construction) |
| **2nd line — Risk** | Measures and analyzes ALM risk; controls limits; validates models; reports |
| **3rd line — Internal Audit** | Audits 1st and 2nd lines for compliance with approved policies |
| **4th line — Supervisory authorities** | SREP and on-site inspections (external audit of all three lines) |


## ALCO as Conflict Resolution Mechanism

The Asset and Liability Management Committee (ALCO) ensures cross-functional representation in balance sheet decisions:- Must include representatives from ALM, Risk, and Finance.- Business line representatives may attend for information but should not hold voting rights or constitute the majority.- Sets internal amber zones between risk appetite limits and hard limits, escalating breaches before they become regulatory issues.
**Source:** Chapters 10–11 of Bardaeva, "Bank Asset Liability Management Best Practice" (De Gruyter, 2021). Table 10.1/10.2 (Front/Middle Office task matrices) and Chapter 11 (Risk Management Triangle) are directly from source. [RAW-Bardaeva ch.10-11]
