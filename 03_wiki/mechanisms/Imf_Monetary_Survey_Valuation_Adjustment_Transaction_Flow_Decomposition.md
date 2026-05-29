---
node_id: imf_monetary_survey_valuation_adjustment_001
type: mechanism
title: IMF Monetary Survey — Valuation Adjustment and Transaction Flow Decomposition
aliases:
- valuation adjustment monetary survey
- VAj exchange rate revaluation
- transaction flow vs stock change
- NFA revaluation adjustment
- ΔNFA vs ΔRES reconciliation
- điều chỉnh định giá khảo sát tiền tệ
- phân tách giao dịch và định giá lại tỷ giá
- VAj tỷ giá
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- valuation_adjustment
- monetary_survey
- nfa
- exchange_rate
- transaction_flow
- financial_programming
- imf_macro_accounting
- balance_of_payments
- reconciliation
confidence: 4
stability: stable
thesis: 'Changes in monetary survey stock items (especially NFA) between two periods
  reflect both actual transaction flows AND valuation effects from exchange rate changes.
  Box 5.8 of the IMF Macro Accounting framework provides a formal decomposition: the
  transaction component is converted at the period-average exchange rate, while the
  valuation adjustment (VAj) captures the revaluation of the opening stock due to
  exchange rate movement. Failing to separate these components causes ΔNFA in the
  monetary survey (local currency) to diverge from ΔRES in the BOP (foreign currency),
  invalidating monetary programming targets.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 4609–4653 (Box 5.8 Valuation Adjustments: decomposition of stock changes
    into transaction flows and exchange rate revaluations; average period exchange
    rate for transaction conversion; VAj formula; OIN(net) treatment)'
  weight: primary
parent_node: '[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]'
related:
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: valuation_adjustment_required_for_accurate_NFA_change_measurement
- node: '[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]'
  relation: ΔRES_in_BOP_must_match_transaction_component_of_ΔNFA
- node: '[[Imf_Financial_Programming_NDA_Ceiling_And_BOP_Monetary_Approach]]'
  relation: NDA_ceiling_requires_clean_ΔNFA_transaction_figure
- node: '[[Imf_Monetary_Analysis_Quantity_Theory_Velocity_And_Exchange_Rate_Regimes]]'
  relation: exchange_rate_regime_determines_magnitude_of_valuation_adjustments
- node: '[[Cb_Fx_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: FX_intervention_generates_ΔNFA_that_includes_valuation_component
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## The Core Problem: Stock Changes ≠ Transaction Flows

In monetary survey analysis, analysts routinely compute period-to-period changes in balance sheet stocks (NFA, NCG, CPS, M2) and treat these changes as "flows" — i.e., the actual transactions that occurred in the period. This is **not always accurate**.

"In analyzing the balance sheet of the banking system, changes in stocks are often equated with transaction flows. This is not always accurate. In particular, changes between two periods in stocks reflect not only transaction flows, but also revaluation and other factors." [RAW-BOOK IMF Macro Box 5.8 p.4613]

**Sources of stock-change ≠ transaction-flow divergence:**
```
1. Exchange rate revaluation (most important)
   → FX-denominated assets/liabilities re-priced when exchange rate changes
   → Same dollar amount becomes different local-currency amount

2. Price changes on financial assets (mark-to-market)
   → Bond portfolio value changes with interest rate movements

3. Other changes
   → SDR allocations or cancellations by the IMF
   → Debt write-offs by creditors
```

"Revaluations result from changes in the prices of financial assets and liabilities due to fluctuations in market prices or exchange rates, and other changes, including allocation or cancellation of SDRs and writing off of debts by creditors." [RAW-BOOK IMF Macro Box 5.8 p.4613]

---

## Why Exchange Rate Revaluation Matters Most

For most developing and transition economies, the largest monetary survey items denominated in foreign currency are:

```
ASSETS:
  Net Foreign Assets (NFA)
    → Gold reserves (priced in USD)
    → FX reserves (typically USD/EUR/etc.)
    → SDR holdings
    → IMF reserve position

LIABILITIES:
  Foreign-currency deposits of residents (quasi-money)
  External borrowing by government or banks
```

When the exchange rate changes (local currency depreciates or appreciates), all these items change in **local-currency terms even if nothing was bought or sold**. A CB that held $1 billion throughout a year sees its NFA rise from 10 trillion zloty to 12 trillion zloty if the exchange rate moved from 10 to 12 — with zero transactions.

"Equating changes in stocks over time to transaction flows is particularly misleading when exchange rate changes are significant over the period of analysis." [RAW-BOOK IMF Macro Box 5.8 p.4613]

---

## Formal Decomposition: The VAj Formula

**Notation used in Box 5.8** [RAW-BOOK IMF Macro Box 5.8 p.4617–4621]:

```
A_L   = balance sheet stock item denominated in local currency
A_$   = balance sheet stock item denominated in dollars (foreign currency)
E_t   = exchange rate (local currency units per dollar), end of period t
Ē     = exchange rate (local currency units per dollar), period average
```

Since A_L = E × A_$, the change in local-currency stock between periods t-1 and t is:

```
ΔA_L = A_L_t − A_L_(t-1)
     = E_t × A_$_t − E_(t-1) × A_$_(t-1)
```

This total change has two components [LLM-E — algebraic decomposition consistent with Box 5.8]:

```
TRANSACTION COMPONENT (actual flows during the period):
  = Ē × ΔA_$               ← dollar flows converted at AVERAGE rate
  = Ē × (A_$_t − A_$_(t-1))

VALUATION ADJUSTMENT (VAj):
  VAj = ΔA_L − Ē × ΔA_$
      ≈ A_$_(t-1) × ΔE     ← opening stock × exchange rate change
```

**Why average rate for transactions?**
"The average period exchange rate is used to convert dollar-denominated transactions into local currency. This reflects the fact that these transactions are presumed to have taken place throughout the period." [RAW-BOOK IMF Macro Box 5.8 p.4653]

**Simplified intuition when ΔA_$ is small:**
```
If little was actually transacted (ΔA_$ ≈ 0):
  VAj ≈ A_$_(t-1) × ΔE
       = Opening dollar stock × change in exchange rate

Example:
  NFA at end-1992: $8.1 bn = 128 trillion zloty (E = 15,767 zloty/$)
  Exchange rate moves to E = 21,344 by end-1993 → ΔE = +5,577 zloty/$
  
  Valuation gain ≈ 8.1 × 5,577 = 45.2 trillion zloty
  → Appears as NFA increase in local currency WITHOUT any FX purchase
```

---

## Treatment in the Balance Sheet

When FX-denominated assets and liabilities are adjusted to isolate transaction flows, the valuation adjustment must go somewhere to keep the balance sheet in balance:

"If foreign currency-denominated assets and liabilities in the monetary survey are adjusted for the effects of exchange rate changes, valuation adjustments should, in this case, be reflected in 'other items (net)' to ensure that the balance sheet remains in balance." [RAW-BOOK IMF Macro Box 5.8 p.4651]

```
BEFORE valuation adjustment:
  NFA (local) = transactions + VAj
  OIN(net) unchanged
  → Balance sheet still balanced

AFTER isolating transaction flows:
  NFA (local, transaction component only) = Ē × ΔA_$
  OIN(net) absorbs the VAj
  → Balance sheet still balanced
```

This is why OIN (Other Items Net) in the monetary survey often shows large and volatile movements when exchange rates are changing — it is absorbing the accounting residuals from valuation adjustments.

---

## The BOP Reconciliation Problem

The Balance of Payments records **ΔRES** (change in reserves) in **foreign currency** (dollars), while the Monetary Survey records **ΔNFA** in **local currency**. These must ultimately be consistent, but the conversion is non-trivial.

```
From footnote 16 of Chapter 5 [RAW-BOOK IMF Macro p.4597]:
  "ΔRES = -ΔNFA"   (with sign conventions: BOP decline in reserves = 
                     monetary survey NFA decrease)

BUT: This equality holds only for TRANSACTION FLOWS, not total stock changes.

Correct reconciliation:
  ΔRES (BOP, in USD) × E_conversion = ΔNFA_transactions (monetary survey)

Where:
  ΔNFA (total, local currency) = ΔNFA_transactions + VAj
  ΔNFA_transactions = total ΔNFA − VAj

Failure to adjust:
  → ΔNFA from monetary survey appears LARGER than ΔRES × E
    (when currency depreciates: same dollar reserves = more local-currency NFA)
  → Analysts incorrectly conclude reserves are "increasing" when actually
    the local currency is just depreciating
```

"The link between the monetary accounts and the balance of payments is often complicated by exchange rate changes and valuation adjustments." [RAW-BOOK IMF Macro Ch.5 p.4601]

---

## Application: IMF Financial Programming

The NDA ceiling — the core monetary programming target in IMF programs — depends on clean ΔNFA figures:

```
Monetary Survey Identity (flow form):
  ΔM2 = ΔNFA + ΔNDA

NDA ceiling derivation:
  ΔNDA ≤ ΔMd − ΔNFA_target

WHERE: ΔNFA_target must be the TRANSACTION component, not total stock change

IF valuation adjustments are included in ΔNFA:
  → ΔNDA ceiling is artificially tight or loose depending on exchange rate direction
  → Depreciation → VAj inflates ΔNFA → NDA ceiling appears to have more room
                                       (incorrect: reserves haven't actually increased)
  → Appreciation → VAj deflates ΔNFA → NDA ceiling is artificially tighter
                                        (incorrect: reserves haven't actually fallen)
```

**Policy implication:** In countries with significant exchange rate movements, all NDA ceiling calculations in IMF programs must use valuation-adjusted ΔNFA figures. Standard practice: express NFA in **US dollar terms** for programming purposes, converting to local currency only for balance sheet presentation.

---

## Diagnostic

```
OBSERVED: ΔNFA (local currency, monetary survey) differs significantly from
          ΔRES (BOP) × average exchange rate
→ Magnitude of difference = valuation adjustment
→ Decompose: how much is transactions vs. how much is exchange rate revaluation?

OBSERVED: OIN(net) shows large unexplained movements
→ Likely: absorbing valuation adjustments from FX items
→ Check: if exchange rate moved significantly during period, consistent

OBSERVED: NDA ceiling in IMF program appears to be breached
→ Before concluding policy violation: check valuation adjustment
→ If local currency depreciated, ΔNFA includes positive VAj
→ True transaction-based ΔNFA is lower → NDA may actually be within ceiling

OBSERVED: M2 growing faster than ΔNDA + ΔNFA would predict
→ Check: are FX deposits included in M2?
→ If yes: depreciation raises local-currency value of FX deposits
→ This appears as M2 growth but is NOT monetary expansion — it's revaluation
```
