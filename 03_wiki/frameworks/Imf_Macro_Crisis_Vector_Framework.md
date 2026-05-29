---
node_id: imf_macro_crisis_vector_framework_001
type: framework
title: IMF Macro Crisis Vector Framework — Fiscal, External, And Banking Transmission
aliases:
- crisis vector IMF
- macro crisis transmission IMF
- fiscal crisis vector
- external crisis speculative attack
- banking crisis LOLR
- BOP crisis mechanism
- khủng hoảng kinh tế vĩ mô vector IMF
- cơ chế lây lan khủng hoảng
- tấn công đầu cơ tỷ giá
- dễ bị tổn thương tài chính IMF
- khủng hoảng ngân hàng người cho vay cuối cùng
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- crisis_transmission
- speculative_attack
- fiscal_crisis
- banking_crisis
- financial_vulnerability
- reserve_adequacy
- lolr
- current_account_sustainability
- lawson_doctrine
- imf_macro_accounting
- balance_of_payments
- krugman_model
confidence: 4
stability: stable
thesis: 'The IMF Macro Accounting framework identifies three distinct crisis vectors,
  each with a specific balance-sheet transmission mechanism: (1) Fiscal vector — 4
  modes of deficit financing each generate a distinct macroeconomic imbalance (inflation,
  exchange rate crisis, debt explosion, crowding out); (2) External vector — under
  a fixed peg, unsustainable current account deficits trigger rational speculative
  attacks before reserves are exhausted; reserve adequacy must be assessed against
  financial vulnerability indicators (M2/FX ratio, short-term FX liabilities) rather
  than just the 3-month import rule; (3) Banking vector — the fractional reserve system''s
  maturity mismatch makes banks inherently illiquid; a single bank''s payment difficulty
  can freeze credit across the entire system through a confidence contagion chain,
  requiring LOLR intervention. The 4-sector flow of funds matrix (government, private,
  banking, external) is the accounting tool for tracing which sector''s imbalance
  is generating each crisis vector.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 1941–1945 (4 financing modes → 4 crisis types); lines 3451–3459 (fixed
    peg + unsustainable CAD → speculative attack, Krugman 1979 reference); lines 3486–3498
    (Box 4.6 current account sustainability/solvency; confidence-triggered crisis;
    Lawson doctrine critique); lines 3723–3749 (reserve adequacy: 3-month rule; financial
    vulnerability indicators — M2/FX, short-term FX liabilities; Mexico 1994; Poland
    1991 credibility case); lines 4302 (banking crisis LOLR: illiquid credit system,
    contagion, CB isolation mechanism)'
  weight: primary
parent_node: null
related:
- node: '[[Imf_Gfs_Fiscal_Accounting_Framework_Deficit_Measurement_And_Sustainability]]'
  relation: fiscal_vector_detail_including_debt_dynamics_and_seigniorage
- node: '[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]'
  relation: external_sector_accounting_underlying_crisis_vectors
- node: '[[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]'
  relation: diagnostic_matrix_tracing_crisis_sector_of_origin
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: banking_sector_balance_sheet_underlying_lolr_vector
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: companion_from_lipschitz_schadler_micro_anatomy_of_fx_mismatch_crisis
- node: '[[Currency_Substitution_Dollarization_Monetary_Control]]'
  relation: dollarization_as_crisis_response_and_amplifier
- node: '[[Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design]]'
  relation: exchange_rate_regime_determines_external_crisis_vulnerability
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Overview: The Accounting Approach to Crisis Analysis

The IMF Macro Accounting framework's distinctive contribution to crisis analysis is **sectoral diagnosis**: every macro crisis originates in an imbalance in one of the four sectors of the flow of funds matrix (government, private nonbank, banking, external). The accounting identities make these imbalances visible *before* they trigger a market event.

```
CRISIS VECTOR MAP (IMF Macro Accounting Framework)

┌─────────────────────────────────────────────────────────────┐
│ Sector with             │ Primary          │ Secondary       │
│ primary imbalance       │ crisis type      │ contagion path  │
├─────────────────────────────────────────────────────────────┤
│ Government (fiscal)     │ 4-type vector:   │ → Monetary      │
│                         │ (1) inflation    │ → External BOP  │
│                         │ (2) BOP crisis   │ → Debt rollover │
│                         │ (3) debt crisis  │                 │
│                         │ (4) crowding out │                 │
├─────────────────────────────────────────────────────────────┤
│ External (current       │ Speculative      │ → Reserve       │
│ account deficit)        │ attack on peg    │   depletion     │
│                         │                  │ → Forced float  │
├─────────────────────────────────────────────────────────────┤
│ Banking (maturity       │ Systemic illiq-  │ → Credit freeze │
│ mismatch)               │ uidity / bank    │ → Fiscal (LOLR  │
│                         │ run              │   cost)         │
└─────────────────────────────────────────────────────────────┘
```

---

## Vector 1: Fiscal Crisis Transmission (4 Modes of Deficit Financing)

The macroeconomic impact of a government deficit depends on *how it is financed*. Four financing modes, four distinct crisis outcomes [RAW-BOOK IMF Macro p.1943–1945]:

```
MODE 1: Borrowing from central bank (monetization)
  Balance sheet effect: NCG ↑ → RM ↑ → M2 ↑ (via multiplier)
  Crisis vector:        Excess money creation → INFLATION
  Mechanism:            ΔM > ΔYreal → P rises; at hyperinflation threshold,
                        velocity jumps → seigniorage Laffer curve; base erodes

MODE 2: Running down foreign exchange reserves
  Balance sheet effect: NFA ↓ → RM ↓ (sterilized or not)
  Crisis vector:        EXCHANGE RATE CRISIS
  Mechanism:            Reserve depletion → expectations of devaluation →
                        speculative attack → reserves exhausted → forced float
  
  Example: Mexico 1982 — debt crisis triggered by virtual exhaustion of
  reserves following fiscal imbalance and overvalued exchange rate.
  [RAW-BOOK IMF Macro p.2012]

MODE 3: Domestic nonbank borrowing (domestic debt)
  Balance sheet effect: Government issues bonds; private sector absorbs
  Crisis vector:        HIGH REAL INTEREST RATES + EXPLOSIVE DEBT DYNAMICS
  Mechanism:            IF r > g: Δd = (r−g)d + pd → debt ratio grows without bound
                        → market recognizes unsustainability → credibility cliff
                        → inability to roll over debt → monetization forced or default

MODE 4: Borrowing from domestic banking system (bank credit)
  Balance sheet effect: NCG ↑ (banking system); if CB accommodates → MODE 1
  Crisis vector:        CROWDING OUT OF PRIVATE INVESTMENT
  Mechanism:            IF CB does not accommodate: banks reduce CPS to
                        meet government demand → private credit falls →
                        interest rates rise → investment falls
```

"In a broad sense, each form of financing is associated with a major macroeconomic imbalance: excessive money creation with inflation; excessive foreign borrowing with an external debt problem; depletion of reserves with an exchange rate crisis; and excessive domestic borrowing with high real interest rates — and possibly with explosive growth in public debt from the dynamic interactions between interest payments, deficits, and debt." [RAW-BOOK IMF Macro p.1945]

**Critical complexity:** These are idealized one-to-one mappings. In practice:
- Mode 4 (bank borrowing) + CB accommodation → Mode 1 (monetization)
- Mode 3 (domestic nonbank) + crowding out → higher rates → Mode 2 (foreign borrowing to compensate) → reserve depletion
- Crisis vectors interact and amplify each other through the flow of funds matrix

*For detailed fiscal sustainability arithmetic (Δd = (r−g)d + pd, primary gap, net worth indicators): see [[Imf_Gfs_Fiscal_Accounting_Framework_Deficit_Measurement_And_Sustainability]]*

---

## Vector 2: External Crisis — Speculative Attack Under Fixed Peg

### The Mechanism (Krugman 1979 Model — IMF Reference)

Under a fixed exchange rate with limited capital mobility, current account deficits can be financed only by depleting reserves. The crisis mechanism is **expectations-driven** — it triggers *before* reserves are actually exhausted [RAW-BOOK IMF Macro p.3459]:

```
Phase 1: Unsustainable CAD
  CAD persists → reserves fall at rate ΔRES = −CAB − ΔFinancial Account
  Market observes trajectory → calculates "shadow rate" (what FX rate would be
  if reserves ran out and float were forced)

Phase 2: Shadow rate > pegged rate
  AT THE MOMENT shadow rate exceeds peg:
  → Rational agents attack the peg immediately (not when reserves are zero)
  → Mass conversion of local currency to FX → reserves exhausted instantly
  → Forced float and devaluation

Phase 3: Post-attack
  Devaluation occurs at a rate consistent with the fundamentals
  that would have prevailed anyway — the attack merely *accelerates* the crisis
  (Krugman 1979: "A Model of Balance-of-Payments Crises")

Key insight: The speculative attack is not irrational — it is the rational response to
a predictable policy inconsistency (fixed peg + incompatible fiscal/monetary stance).
[RAW-BOOK IMF Macro Ch.4 footnote 12, p.3471]
```

### Current Account Sustainability Condition (Box 4.6)

A current account position is **sustainable** if its continuation would NOT require a drastic shift in policies or trigger a crisis [RAW-BOOK IMF Macro Box 4.6 p.3488–3494]:

```
SOLVENCY CONDITION:
  PV(future CA surpluses) ≥ current external debt

  A country is insolvent if existing debt cannot be serviced from
  future surpluses — the debt will eventually require:
  → Forced default / restructuring
  → External devaluation + adjustment
  → IMF program with conditionality

SUSTAINABILITY (more restrictive than solvency):
  Current policies, if continued unchanged, would NOT require:
  (a) A drastic shift in policies, OR
  (b) A crisis (exchange rate collapse, external debt default)

  Trigger mechanism: sustainability is an investor perception, not an
  accounting fact — a confidence shift can make a technically solvent
  country face a rollover crisis.
```

### The Lawson Doctrine Critique

The "new view" of the current account (Lawson doctrine): if the CAD reflects purely private sector saving/investment decisions, government need not respond [RAW-BOOK IMF Macro p.3451–3453]:

```
LAWSON DOCTRINE (rejected by IMF):
  Private CAD = private agents' optimal intertemporal choice
  → No government intervention warranted

IMF CRITIQUE (Corden analysis, cited in IMF Macro Ch.4):
  (a) Private borrowing boom may rest on UNSOUND JUDGMENTS
      → Private external debt can end abruptly
  (b) CONTAMINATION SPILLOVER: private foreign borrowing raises
      the risk premium on ALL domestic debt (country risk premium)
      → Sovereign borrowing costs rise even without government borrowing
  (c) REAL EXCHANGE RATE EFFECTS: large CAD → real appreciation →
      competitiveness loss → non-linear reversal risk
  (d) IMF conclusion: "the Lawson doctrine is not valid" as a general rule —
      macroeconomic consequences of unsustainable CAD are too severe for
      hands-off approach [RAW-BOOK IMF Macro p.3453]
```

---

## Vector 2b: Reserve Adequacy Under Financial Vulnerability

### Traditional Rule (Pre-Capital Account Opening)

**3-month import coverage rule:** Gross reserves ≥ 3 months of imports
- Evolved when capital controls were extensive; relevant for *trade* financing risk
- Average for IMF members (excl. difficult positions): 4.5 months in 1994
- Former Soviet transition economies: frequently below 3-month threshold [RAW-BOOK IMF Macro p.3729–3735]

**Limitations of the import rule in open capital markets:**
- Does NOT account for capital account flows (the dominant reserve risk)
- Does NOT account for stock of liquid domestic liabilities that could be converted to FX
- Mexico 1994: "sizable level of reserves can be depleted in the face of a crisis in confidence and the associated sudden capital outflow" [RAW-BOOK IMF Macro p.3739]

### Financial Vulnerability Reserve Adequacy Indicators

When capital accounts are open, reserve adequacy must account for **financial vulnerability** — the stock of obligations that could crystallize as FX demand [RAW-BOOK IMF Macro p.3741]:

```
INDICATOR 1: M2 / FX Reserves (local currency basis)
  Rationale: In a confidence crisis, domestic holders convert money to FX.
  International reserves must be sufficient to back domestic money supply
  (Calvo 1996 — "Tequila Lessons" from Mexico 1994).
  Threshold: No universal rule; the ratio should DECLINE over time
            to signal reserve adequacy improvement.

INDICATOR 2: Short-term FX Liabilities / FX Reserves
  Rationale: Short-maturity FX obligations (sovereign bonds, bank borrowing)
  can be refused rollover in a crisis. Reserves must cover what cannot be rolled.
  (Later formalized as Greenspan-Guidotti: reserves ≥ 1-year external debt)

INDICATOR 3: Capital Account Openness
  More open capital account → faster potential outflow → higher reserve need.
  
INDICATOR 4: FX Reserves / Monetary Base (currency board threshold)
  Rationale: Under a currency board or dollarization-risk scenario,
  reserves must be sufficient to cover every unit of base money.
  If reserves < monetary base, the CB cannot redeem all local currency at peg.
  [RAW-BOOK IMF Macro p.3745]

INDICATOR 5: External Trade / GDP (economy openness)
  More trade-dependent economy → larger exposure to terms-of-trade shocks
  → higher precautionary reserve demand.
```

### Credibility as Reserve Amplifier

Reserve *quantity* is NOT the only determinant of crisis vulnerability — **policy credibility** can substitute for reserve quantity [RAW-BOOK IMF Macro p.3725]:

```
HIGH CREDIBILITY → LOWER reserve threshold needed:
  Poland 1991: Maintained fixed exchange rate despite MODERATE reserve level
  because economic policies commanded HIGH confidence in financial markets.
  $1bn IMF Stabilization Fund boosted credibility — was NEVER used.

LOW CREDIBILITY → reserve quantity is irrelevant:
  "Even with a managed float, a lack of credible economic policies can quickly
  lead to capital flight and may deplete reserves, even if the authorities
  allow the exchange rate to depreciate." [RAW-BOOK IMF Macro p.3725]

Policy implication: Reserve accumulation is an inefficient substitute for
credible policy. The fundamental assessment is always the perceived sustainability
of the macroeconomic program, not the headline reserve level.
```

---

## Vector 3: Banking Crisis and LOLR Mechanism

### Structural Vulnerability: Fractional Reserve and Maturity Mismatch

The banking system is **inherently illiquid** by design [RAW-BOOK IMF Macro p.4302]:

```
MATURITY MISMATCH (structural):
  ASSETS:  Loans to firms/households — long maturity; cannot be called on demand
  LIABILITIES: Deposits — short maturity; withdrawable on demand

  Under fractional reserves:
  → Bank holds only fraction (r) of deposits as liquid reserves
  → (1−r) fraction has been lent out at longer maturities

CONTAGION MECHANISM:
  Step 1: Single bank faces payment difficulty (idiosyncratic shock)
  Step 2: Uncertainty about source of default → "many layers of credit
          and intermediation" → opaque; other banks cannot determine exposure
  Step 3: Systemwide crisis of confidence → "credit freeze"
          → All creditors demand simultaneous redemption
  Step 4: Even solvent banks cannot repay all depositors simultaneously
          → Systemic bank run without fundamental justification

  "If one deposit money bank has payment difficulties, the entire system
  can become illiquid... because of the many layers of credit and intermediation
  in the system, the source of the actual default may not be clear. The result
  of this uncertainty is a systemwide crisis of confidence that leads to a
  credit 'freeze.'" [RAW-BOOK IMF Macro p.4302]
```

### LOLR Mechanism: CB Crisis Response

The central bank's LOLR function is the primary circuit breaker for the banking crisis vector [RAW-BOOK IMF Macro p.4302]:

```
CB LOLR TOOLKIT:
  (1) Isolate problem bank:
      → Prevent contagion by ring-fencing the failing institution
      → Signal to market that other banks are not affected

  (2) Guarantee depositors of problem bank:
      → Eliminate the incentive for depositors to run on other banks
      → Break the contagion transmission chain

  (3) Provide systemwide liquidity (if needed):
      → Discount window access → Cb ↑ → RM ↑
      → Prevents solvent banks from failing for lack of liquidity
      → Keynesian LOLR: lend freely against good collateral at penalty rate

BALANCE SHEET EFFECT OF LOLR:
  Cb (claims on banks) ↑ → RM ↑ → M2 potentially ↑
  → Unless sterilized, LOLR creates monetary expansion
  → If problem bank insolvent (not just illiquid): CB takes credit loss
    → Capital accounts ↓ → OIN ↓ → Potential fiscal cost (recapitalization)

FISCAL-MONETARY NEXUS:
  Systemic banking crisis → LOLR costs → CB capital erosion →
  Government must recapitalize CB → fiscal deficit (quasi-fiscal) → 
  Potential monetization or external borrowing → feeds back into 
  fiscal crisis vector (MODE 1 or MODE 2)
```

---

## Cross-Sector Crisis Amplification: The IMF Flow of Funds View

The flow of funds matrix makes cross-sector crisis amplification explicit. Each column sums to zero, so an imbalance in one sector *must* show up as a counterpart entry in another [from [[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]]:

```
FISCAL → EXTERNAL:
  Fiscal deficit (Sg−Ig < 0) → financed by external borrowing (NFBg ↑) →
  CAB worsens (as per identity: (Sp−Ip) + (Sg−Ig) = CAB) →
  Reserve depletion or real appreciation → speculative attack vulnerability

EXTERNAL → BANKING:
  CAB deficit financed by short-term FX borrowing by banks →
  Banking sector FX liability ↑ → maturity mismatch in FX →
  Sudden stop → bank FX funding dries up → CB provides emergency FX →
  NFA ↓ → reserve depletion

FISCAL → BANKING:
  Government crowds out bank credit to private sector →
  Banks shift portfolio toward government securities →
  If government defaults or restructures → bank capital loss →
  Systemic banking crisis → LOLR → quasi-fiscal cost
```

---

## Diagnostic Framework

```
SIGNAL: Fiscal deficit financed primarily by CB (NCG rising fast)
→ Crisis vector: MONETARY INFLATION
→ Check: ΔRM/RM > ΔY/Y → inflation inevitable
→ Monitor: seigniorage Laffer curve — is seigniorage at or past maximum?

SIGNAL: Fiscal deficit financed by reserve drawdown + fixed peg maintained
→ Crisis vector: EXCHANGE RATE CRISIS (speculative attack imminent)
→ Calculate: shadow exchange rate trajectory → attack timing window
→ Check: M2/FX reserves ratio rising → financial vulnerability increasing

SIGNAL: Fiscal deficit financed by domestic nonbank borrowing; r > g
→ Crisis vector: EXPLOSIVE DEBT DYNAMICS → debt rollover crisis
→ Calculate: Δd = (r−g)d + pd → is d path explosive?
→ Monitor: market confidence indicators (CDS spread, bid-ask on government bonds)

SIGNAL: Reserves falling despite no large fiscal deficit; CAD rising
→ Likely: private sector CAD (investment boom or consumption boom)
→ Apply Lawson doctrine TEST:
  Is private borrowing FDI-quality (financing productive investment)?
  → If yes: may be sustainable (Lawson partially valid)
  → If no (consumption boom, property speculation):
    Apply contamination spillover test → country risk premium rising?
    → If yes: systemic risk building → policy response required

SIGNAL: Banking system showing signs of stress (interbank rate spike, bank runs)
→ Crisis vector: BANKING (illiquidity or insolvency)
→ Diagnose: Is problem idiosyncratic (single bank) or systemic?
  → Idiosyncratic: LOLR intervention + ring-fencing effective
  → Systemic: Solvency problem — LOLR cannot solve → fiscal recapitalization
→ Check: LOLR expansion → RM increase → watch for monetary inflation vector
```
