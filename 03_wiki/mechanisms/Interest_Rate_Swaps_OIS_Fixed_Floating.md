---
node_id: irs_ois_fixed_floating_001
type: mechanism
title: Interest Rate Swaps — OIS, Fixed-for-Floating, Clearing, and Basis
aliases:
  - IRS
  - interest rate swap
  - OIS
  - overnight index swap
  - fixed-for-floating swap
  - basis swap
  - SOFR swap
  - hoán đổi lãi suất
  - hợp đồng hoán đổi lãi suất

domain:
  primary: financial_markets
  secondary: [monetary_policy, shadow_banking]
tags: [interest-rate-swaps, OIS, SOFR, derivatives, clearing, CCP, DV01, basis-swap, counterparty-risk]

confidence: 4
stability: stable

thesis: >
  Interest rate swaps exchange fixed for floating interest payments on a notional amount.
  OIS (overnight index swaps, e.g., SOFR swaps) are near-riskless; fixed-for-floating swaps
  (e.g., Euribor) carry a basis vs. the risk-free rate. Market notionals ($210T) vastly overstate
  risk — ENNs (entity-netted notionals) of $16T are comparable to other fixed income markets.
  Swaps DV01 is entirely on the fixed leg; clearing via CCPs concentrates but does not eliminate
  counterparty risk; the default waterfall (IM → default fund → CCP skin → member assessments →
  VM haircutting) is the last line of defense.

source_refs:
  - path: 02_sources/books/tuckman_serrat_fixed_income/Tuckman_Serrat_Fixed_Income_2022.md
    pages: "Ch.13 (pp.4993-5283), Ch.14 (asset swap spreads)"
    weight: primary

related:
  - node: "[[DV01_Duration_Convexity_Fixed_Income]]"
    relation: uses
  - node: "[[Repo_Market_Mechanics_Triparty_Bilateral]]"
    relation: funded_via
  - node: "[[Collateral_Framework_Haircuts_Central_Bank_Credit]]"
    relation: margin_analogy
  - node: "[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
    relation: constrained_by

date_created: 2026-05-20
date_updated: 2026-05-20
---

## Taxonomy of Interest Rate Swaps

| Type | Floating Index | Settlement | Primary Users |
|------|---------------|------------|---------------|
| OIS (SOFR swap) | Daily-compounded SOFR | Annual; no payment delay | Dealers, hedge funds, sovereigns |
| Fixed-for-floating | Term rate (Euribor 3m/6m) | Semiannual/quarterly | Banks, corporates |
| Forward-starting swap | SOFR or term | Deferred start | Debt issuers hedging future issuance |
| Basis swap | Two floating rates | Periodic | Banks hedging funding basis |
| Cross-currency basis swap | Short-term rate in 2 currencies | Periodic | Multi-currency funding desks |

**Key taxonomy point:** Dodd-Frank defines FRAs, caps, floors, and swaptions as "swaps" — market conventions differ, causing notional inflation in headline statistics. [RAW-BOOK Tuckman Ch.13]

---

## Market Size — Notional vs. ENNs

US reporting entities as of September 2020: [RAW-BOOK Tuckman Table 13.1]

| Metric | Amount |
|--------|--------|
| Total notional (long+short) | $210.7T |
| Total 5-year equivalents | $137.1T |
| Entity-netted notionals (ENNs) | $16.1T |

**ENNs** = net long/short 5-year equivalents between each counterparty pair → removes offsets. At $16.1T, comparable to other US fixed income markets. Swap dealers compress $100T long/short into $9.3T ENNs via offsetting positions.

**Sector net direction (ENNs):**
- Banks: net short (hedging fixed-rate mortgage/bond assets)
- Pensions/Insurance: net long (hedging long-duration liabilities)
- Non-financial corporates: net short paying fixed (hedging floating bank loans)

---

## Cash Flow Mechanics

### OIS (SOFR Swap)
- Fixed leg: periodic interest at agreed rate, actual/360 convention
- Floating leg: daily-compounded SOFR over the period; payment delayed by 1 day (SOFR not published until morning after)
- Floating leg valuation trick: add fictional notional at maturity → floating leg = par on every reset date; between resets = accrued value at realized SOFR

### Fixed-for-Floating (e.g., Euribor)
- Floating rate set at beginning of period (2 business days before), known in advance — no payment delay
- Floating leg valuation: par on reset dates; between resets = PV of (notional + interest determined at last reset date)
- **Basis vs. risk-free:** Euribor includes bank credit risk → floating leg ≠ par when discounted at risk-free (€STR) rates; must use two-curve pricing

### DV01 of a Swap
```
Receive Fixed (SOFR swap):
  Fixed leg DV01 ≈ that of a same-maturity coupon bond  (e.g., 10yr → ~0.09)
  Floating leg DV01 ≈ 0  (accrues at fair rate regardless of rate shift)
  Net DV01 of receive-fixed ≈ 0.09

Receive Fixed (Euribor swap):
  Fixed leg DV01 ≈ 0.09  (10yr)
  Floating leg DV01 ≈ DV01 of ZCB to next reset  (e.g., 6m → ~0.005)
  Net DV01 ≈ 0.085 — hedge fixed and floating legs separately
```
[RAW-BOOK Tuckman §13.2]

### NPV and Unwinding
At initiation: NPV = 0 (par swap rate equates fixed/floating PV). Over time, NPV ≠ 0 as rates move. Three unwind options:
1. **Cancel with original counterparty** — NPV payment + tear-up; limited by counterparty reluctance
2. **Offset same rate** — pay same fixed to third party; two swaps remain live
3. **DV01-neutral offset** — most common: trade most liquid swap, adjust notional; some curve risk remains

Industry practice: offsetting not unwinding → notional proliferation → periodic **compression** programs cancel offsetting positions across the system.

---

## Key Use Cases

### Pension Liability Hedging
Pension: $1B liabilities with DV01 = $2M; corporate bond portfolio DV01 = $500K. Gap = $1.5M DV01. Solution: receive fixed in long-term IRS with DV01 = $1.5M → no upfront cash (only margin). Swap lets fund choose assets on credit merit; adjusts duration separately. [RAW-BOOK Tuckman §13.3]

### Forward-Starting Swap (Debt Issuance Hedge)
Corporation plans to sell bonds in 1 year. Lock in borrowing cost by paying fixed on forward-starting swap. Regardless of rate moves:
```
Net cost = forward swap rate + credit spread (over swap rate)
         = locked in at time of forward swap initiation
```
Alternative: spot-starting swap with DV01-matched notional; introduces curve risk.

### Bank Loans — Floating-Rate Transformation
Bank prefers floating-rate loans (match deposit funding); customer wants fixed.
Resolution: Bank makes floating-rate loan → receives fixed from customer → pays fixed to dealer (back-to-back swap). Net: bank has floating-rate loan; customer has fixed-rate cost.

### Synthetic Floating-Rate Debt (Banks)
Bank issues long-term fixed-rate bonds → receives fixed + pays floating in IRS → net = long-term floating-rate debt (harder to withdraw than deposits, but still floating).

### Sovereign Hedging (Greece case study, 2018)
€50B+ floating Euribor+spread debt; 10yr swap rates ~1.60%. Greece paid fixed on 10yr Euribor swaps to lock funding cost. Complication: Greece below IG, no collateral posting → dealers bore credit exposure. Resolution: novation of positive-NPV swaps from reluctant to willing dealers (Dealer X → Dealer Y for NPV payment). [RAW-BOOK Tuckman §13.3]

---

## Counterparty Credit Risk and Margin

### Safe Harbor
Swap contracts exempt from bankruptcy stay: upon default, surviving counterparty may (1) terminate all contracts in master agreement, (2) net payables/receivables, (3) liquidate posted collateral. Exposure = total NPV across all contracts with defaulting counterparty.

### Variation Margin (VM)
| Type | Mechanics |
|------|-----------|
| VM Collateralized-to-Market (CTM) | Counterparty with negative NPV posts collateral daily; returned when NPV flips |
| VM Settled-to-Market (STM) | Daily P&L settled in cash (irrevocable); used for cleared trades; 1-day capital treatment |

### Initial Margin (IM)
Covers NPV changes **between** VM calls. Sized via statistical analysis: e.g., 99% VaR of NPV move + replacement costs = IM. Key parameter: **Margin Period of Risk (MPOR)** = assumed time to hedge/replace defaulted swap. Longer MPOR → higher IM.

IM model for non-cleared: ISDA SIMM (Standard Initial Margin Model)

### Credit Valuation Adjustment (CVA)
Dealers charge a fee = insurance premium against counterparty default. Expressed as a rate adjustment: lower received fixed or higher paid fixed. Suitable for creditworthy clients without margin infrastructure (e.g., non-financial end users).

---

## Clearing and CCPs

### Bilateral vs. Cleared
```
Bilateral:   A ←→ B   (each bears other's default risk)
Cleared:     A → CCP → B  (CCP interposes; each faces CCP)
Client:      Client → Clearing Member → CCP  (member backstops client default)
```

Clearing concentrates IRS risk: ~LCH dominates USD IRS; CME distant second; Eurex growing for €STR swaps. [RAW-BOOK Tuckman §13.5]

### CCP Default Waterfall (in order)

| Step | Source | Notes |
|------|--------|-------|
| 1 | Defaulter's IM | First line — sized for normal moves |
| 2 | Defaulter's default fund contribution | Members pre-fund in proportion to position size |
| 3 | CCP capital (skin-in-the-game) | Typically small; contested topic |
| 4 | Surviving members' default fund | Mutualized loss; "too big to fail" concern |
| 5 | Unfunded member assessments | Legally binding but operationally uncertain in crisis |
| 6 | VM haircutting | Fraction of owed VM not paid to participants |
| 7 | Voluntary member contributions | Last resort before CCP ceases |

**Margin procyclicality:** CCPs raise IM requirements in stress → members face simultaneous margin calls + operational obligations → amplifies stress. Known tradeoff: reducing counterparty risk increases liquidity risk.

---

## Basis Swaps

A basis swap exchanges one floating rate for another:
```
€STR vs. 3m Euribor (Feb 2022): bank receives €STR + 13.8bps, pays Euribor
```
**Why the spread exists:** Euribor > €STR (bank credit risk premium) → fair compensation requires paying a spread over the risk-free €STR to receive Euribor. [RAW-BOOK Tuckman §13.6]

**Two-curve pricing:** When floating index ≠ risk-free, value floating leg as:
```
PV(floating leg) = par + PV(basis spread payments)
  where discounting uses risk-free (€STR/SOFR) discount factors
```

Common basis types:
- OIS vs. term IBOR (active during LIBOR transition)
- Cross-currency basis (SOFR vs. €STR) — accounts for relative demand for USD vs. EUR funding
- Tenor basis (3m SOFR vs. 6m SOFR) — liquidity and credit risk of term vs. overnight

---

## Asset Swap Spreads (related: Ch.14)

Asset swap converts fixed-rate bond into floating-rate exposure:

**Par asset swap:** Buy bond at market price P, borrow 100 from repo, pay fixed coupon to swap desk → receive LIBOR/SOFR + s_par. Net: no cash at initiation; earns floating + credit spread so long as no default.

**Market value asset swap:** Borrow P from repo (not 100); swap pays P-100 at maturity. Same return, different collateral timing.

Relationship: s_par × 100 = s_mkt × P → choice between par and market value asset swap = collateral preference, not economics.

**Financing risk:** Long-dated bond + short-term repo → risk that repo rate rises faster than spread earned, or lender refuses to roll.
