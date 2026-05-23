---
node_id: basel_iii_endgame_001
type: framework
title: Basel III Endgame — Capital, Liquidity, and Credit Migration
aliases:
- Basel III Endgame
- Basel III.1
- output floor
- RWA mechanics
- sàn đầu ra Basel
- Basel vốn và thanh khoản
- credit migration to private credit
- originate-to-distribute
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
  - macro_outlook
tags:
- Basel
- capital-regulation
- RWA
- output-floor
- LCR
- NSFR
- leverage-ratio
- private-credit
- credit-migration
- originate-to-distribute
confidence: 2
stability: evolving
thesis: 'Basel III and its Endgame extensions create a structured causal chain: RWA
  requirements + output floor + leverage ratio + LCR/NSFR raise the cost of holding
  specialized and long-duration corporate credit → banks are driven from originate-to-hold
  to originate-to-distribute → private credit funds fill the financing gap, reaching
  $2.1T globally. Critically, risk is not eliminated but redistributed: bank solvency
  risk converts to network liquidity risk in the bank-NBFI interconnected system.

  '
source_refs:
- path: 02_sources/deep-research/Basel, Ngân hàng, Tín dụng Tư nhân.md
  pages: §I-VIII (Core Framework through Ultimate Insight)
  weight: primary
related:
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: shares_regulatory_drivers
- node: '[[Shadow_Banking_Market_Based_Finance]]'
  relation: private_credit_is_instance_of
- node: '[[Private_Credit_SRT_NAV_Loans_Bank_Partnerships]]'
  relation: mechanism_within
- node: '[[Collateral_Velocity_Rehypothecation]]'
  relation: related_shadow_banking
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: bank_nbfi_interconnect
- node: '[[Basel Driven Credit Migration To Private Markets]]'
  relation: shared_tag:Basel
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:Basel
- node: '[[US Shadow Banking Post-GFC Market Based Finance Structure]]'
  relation: shared_tag:Basel
- node: '[[IRRBB EVE NII Dual Metric Framework]]'
  relation: shared_tag:Basel
- node: '[[Basel Output Floor Specialized Lending Impact]]'
  relation: shared_tag:RWA
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Core Causal Chain [LLM]

```
Basel III Mechanics
  (RWA + Output Floor + Leverage Ratio + LCR + NSFR)
          ↓
  Cost of holding specialized corporate credit rises sharply
          ↓
  Bank response: originate-to-distribute; SRT; partnerships with PC funds
          ↓
  Credit migrates to Private Credit ($2.1T global AUM)
          ↓
  Hybrid system: banks provide leverage (NAV loans, sub-lines) to PC funds
          ↓
  Systemic risk transformation:
    Bank Solvency Risk → Network Liquidity Risk (correlated drawdowns)
```

[RAW-BOOK Basel, Ngân hàng §I — Core Framework]

---

## Basel Mechanics — The Four Regulatory Axes

### 1. RWA and Capital Cost

**Core equation:**
```
CET1 Ratio = CET1 Capital / Risk-Weighted Assets ≥ [10%-13%]
            (floor + conservation buffer + G-SIB surcharge)

RWA = Σ(Asset × Risk Weight) across credit, market, and operational risk
```

**Risk weight assignment:**
- Standardised Approach (SA): uses external credit ratings or prescribed weights
- Internal Ratings-Based (IRB): uses bank-estimated PD × LGD × EAD

**Impact on corporate lending:** Leveraged loans and unrated middle-market loans receive high risk weights under SA. Since most middle-market borrowers lack external ratings, they default to high RWA categories — making these assets capital-intensive. [LLM synthesis from RAW-BOOK Basel §II.1]

**ROE mechanism:**
```
ROE = Net Income / Equity
Basel forces ↑ Equity (denominator) for same loan portfolio → ROE↓
→ Bank response: cut high-RWA assets to restore ROE
```

### 2. Output Floor — Direct Strike on Specialized Lending

The output floor (Basel III Endgame §d424) prevents IRB-computed RWA from falling below 72.5% of SA-computed RWA. Implementation schedule:

| Date | Output Floor |
|------|-------------|
| 1 Jan 2022 | 50.0% |
| 1 Jan 2023 | 55.0% |
| 1 Jan 2024 | 60.0% |
| 1 Jan 2025 | 65.0% |
| 1 Jan 2026 | 70.0% |
| 1 Jan 2027 | 72.5% (full) |

[RAW-BOOK Basel §II.2 — cites BIS d424]

**Mechanism:** Banks previously used IRB to optimize RWA for specialized lending (project finance, commercial real estate, infrastructure). These assets often have low empirical default rates but lack external ratings → SA assigns high arbitrary risk weights. Output floor compresses the IRB advantage → specialized lending becomes uneconomical on a capital basis.

**European impact:** ~80% of Group 1 European banks will be constrained by the output floor; MRC (minimum required capital) rises 21.3% for the EU — accounting for 41.4% of total Basel III impact. [LLM citing ECB WP 2824]

### 3. Leverage Ratio — Absolute Balance Sheet Cap

```
Leverage Ratio = Tier 1 Capital / Exposure Measure ≥ 3%
(G-SIBs: higher, with additional G-SIB buffer)

Exposure Measure = on-balance-sheet assets + derivatives + repo
```

**Key property:** Risk-insensitive — a AAA-rated corporate loan consumes the same leverage ratio as a junk bond of the same notional. Even if RWA approaches zero, the leverage ratio binds. This creates a hard cap on balance sheet size, forcing banks to prioritize highest-return-per-unit-of-balance-sheet assets. [RAW-BOOK Basel §II.3 — cites BIS d457]

Note: The SLR (Supplementary Leverage Ratio) is the US implementation of the leverage ratio; G-SIB requirement ~5.64% for US G-SIBs. See `[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]` for Treasury market implications.

### 4. Liquidity Rules — Structural Funding Constraints

**LCR (Liquidity Coverage Ratio):**
```
LCR = HQLA / Net Cash Outflows (30-day stress scenario) ≥ 100%
```
Banks must hold unencumbered HQLA (Treasuries, CB reserves) equal to 30-day stressed outflows. Committed credit lines to corporates and PE funds incur high assumed drawdown rates (up to 100%), forcing banks to hold expensive low-yield HQLA as offset. Cost = HQLA yield gap vs. alternative deployment. [RAW-BOOK Basel §II.4 — cites BIS 238]

**NSFR (Net Stable Funding Ratio):**
```
NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF) ≥ 100%
```

RSF factors for key assets:
- Long-term corporate loans (≥1 year): RSF = 85%
- Short-term corporate loans (<1 year): RSF = 50%
- HQLA (Treasuries, reserves): RSF = 0-5%

**Implication:** Each $100 of long-duration corporate credit requires $85 of stable funding (expensive term deposits or long bonds). Long-term corporate lending is structurally disadvantaged versus short-term or liquid assets. [RAW-BOOK Basel §II.4 — cites BIS d295]

---

## Regional Implementation — Diverging Bank Behavior

| Region | Key Feature | Basel Impact | Private Credit Dynamic |
|--------|-------------|--------------|----------------------|
| **US** | "Gold-plating" — extends rules to banks >$100B assets | G-SIBs: +21% capital requirement; regional banks: +10% | Largest PC market: $1.34T of $2.1T global; deep syndicated loan/CLO markets absorb bank outflows [LLM-E] |
| **Europe** | Bank-centric system; securitization market shallow | Output floor = dominant shock; 80% Group 1 banks constrained; +21.3% MRC from floor alone | Financing gap emerging for specialized lending (infra, CRE, project finance); PC growing from low base [LLM-E] |
| **APAC** | Flexible implementation; state influence on credit direction | Banks continue to hold credit on balance sheet; regulatory arbitrage less severe | Small but fast-growing: ~$59B → projected $92B by 2027 (+46%) [LLM citing ADM Capital 2025] |
| **Vietnam** | Credit quota system → transitioning to Basel CAR | Thông tư 14/2025: CAR 8.625% → 10.5% by 2030; corporate bond market frozen post-2022 crisis | PC enters via special situations, M&A finance; FX regulation forces preference share / offshore SPV structures [LLM-E] |

---

## Banking System Response — Three Structural Shifts

### Shift 1: Originate-to-Distribute (OTD) Model

Traditional model: originate → hold → earn spread → bear credit risk.
OTD model: originate → package → distribute to non-banks → earn fees → transfer risk.

**Mechanism:** Banks use relationship/origination capability; credit risk sold to CLOs, insurance companies, pension funds. Fee income replaces spread income as the primary revenue source. Capital efficiency improves dramatically since risk-bearing assets leave the balance sheet. [LLM from RAW-BOOK Basel §IV.2]

### Shift 2: Significant Risk Transfer (SRT)

SRT allows banks to transfer credit risk from existing balance-sheet portfolios to third-party investors (PC funds, pension funds, development banks) via credit derivatives or securitization structures.

**Structure:**
```
Bank holds: loan portfolio (e.g., $1B auto loans)
SRT: bank buys protection on first-loss tranche (0%-12.5% of portfolio)
  → pays coupon to PC fund investor: ~8-12%
  → receives: regulatory capital relief on senior tranches
     (senior tranches retain low risk weight after first-loss transfer)

Example economics:
  Cost of protection: $5.5M
  Capital saved: $15.5M equivalent
  Net benefit: $10M capital freed → ROE lifts from 9% to 13% on that portfolio
```

[RAW-BOOK Basel §IV.3 — cites BIS qt2409b]

**Key insight:** SRT does not eliminate credit risk — it transfers first-loss to PC investors. The bank retains senior tranches (low risk weight) and receives fee income. Risk migrates from bank balance sheet to private credit fund balance sheet.

### Shift 3: Private Credit Partnerships

Major bank-PC partnerships restructure the intermediation chain:

| Model | Bank Role | PC Fund Role | Scale |
|-------|-----------|--------------|-------|
| Originate-to-Share (Citigroup + Apollo) | Originate, arrange, earn fees; off-balance-sheet | Bear credit risk; manage positions | $25B target |
| Integrated Balance Sheet (JPMorgan) | Retain capital-efficient senior tranches; 50B from own BS | Bear mezzanine/first-loss | $65B platform ($50B JPM + $15B co-investors) |

[RAW-BOOK Basel §IV.4]

---

## Credit Migration — The Capital Flow Reroute

```
Traditional flow:
  LP capital (pensions, insurance) → bank deposits → corporate loans

Post-Basel flow:
  LP capital → Private Credit Funds (via commitment: illiquidity premium)
             → PC Funds → direct corporate loans (bilateral, illiquid, flexible covenants)
             → Corporates → payments → bank deposits (liquidity services)

PC Funds also borrow from banks:
  → Subscription lines (backed by LP capital call rights; boosts IRR)
  → NAV loans (backed by portfolio NAV; provides portfolio-level leverage)
```

[RAW-BOOK Basel §V — cites Fed FEDS Note 2025-05-23]

**Subscription lines:** Short-term revolving facilities secured against LP capital call rights (not portfolio assets). Allow immediate deployment without LP cash calls → delays LP investment date → artificially inflates IRR. [LLM from RAW-BOOK Basel §V]

**NAV loans:** Portfolio-level leverage; PC fund SPV pledges portfolio cash flows and equity interests as collateral. Bank applies LTV covenants; breach triggers cash sweeps or asset seizure. Banks become "lender to the lender" — indirect exposure to corporate credit risk. [LLM from RAW-BOOK Basel §V]

---

## System Outcome — Risk Transformation

### Structural Shift

```
Pre-Basel III:          Post-Basel III Endgame:
Bank-centric system     Hybrid system
  ↓                       ↓
Banks hold all          Banks: payment infrastructure + leverage to NBFIs
credit risk on          PC funds: credit origination + risk bearing
balance sheet           LP investors: ultimate credit loss absorbers
```

### Risk Transformation: Solvency → Network Liquidity Risk

**Old systemic risk:** Bank solvency risk — corporate defaults → bank equity wiped → bank run → payment system failure.

**New systemic risk:** Network liquidity risk (correlated drawdowns):
1. Market stress → PC fund NAV declines
2. Bank triggers margin calls / cash sweeps on NAV loans
3. PC funds simultaneously draw on subscription lines / revolvers at banks
4. Correlated drawdown: if all PC vehicles draw 100% of unused lines → +44% utilization rate = $36B immediate outflow [Fed stress test estimate, LLM citing Fed FEDS Note 2025]
5. For US G-SIBs: manageable (-2bps CET1; -1pp LCR) but opacity prevents accurate assessment

**Key opacity problem:** Private credit lacks public reporting → regulators cannot assess contagion path from PC stress → mutual funds → repo → pension funds. [LLM citing FSB NBFI Monitoring Report 2023]

### The Ultimate Insight [LLM — synthesized from RAW-BOOK Basel §VIII]

Basel III does not eliminate systemic risk — it redistributes risk into the shadow of regulation:
- Solvency risk exits banks through the front door (capital + HQLA buffers)
- Credit risk re-enters through the back door (NAV loans, sub-lines, SRT, OTD partnerships)
- Risk "changes address" from regulated bank balance sheets to unregulated private credit vehicles
- The next crisis trigger: not bank insolvency (2008 model) but correlated network liquidity seizure across the PC ecosystem

---

## Private Credit Market Size

| Geography | AUM 2024 | Projection |
|-----------|----------|------------|
| Global | ~$2.1T | — |
| North America | ~$1.34T | Dominant share |
| APAC | ~$59B | ~$92B by 2027 (+46%) |
| Europe | Growing from low base | Financing gap from output floor |

[LLM citing IMF GFSR April 2024; ADM Capital APAC Outlook 2025]

---

## Confidence Note

This node is confidence=2 (LLM synthesis). Source is a Gemini deep-research document that accurately cites BIS framework documents (d424 output floor, d457 leverage ratio, bcbs238 LCR, d295 NSFR), IMF GFSR April 2024, and Fed FEDS Note May 2025. Mechanical facts (output floor schedule, RSF factors, leverage ratio minimums) are authoritative. Interpretive claims (risk transformation thesis, regional impact quantification) are marked [LLM]. Upgrade to confidence=3 after cross-referencing with BCBS source documents directly.

