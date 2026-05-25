---
node_id: transition_economy_monetary_issues_001
type: concept
title: Transition Economy Monetary Special Issues
aliases:
  - transition economy monetary policy
  - post-communist monetary reform
  - velocity jumps transition
  - monobank legacy
  - interenterprise arrears
  - kinh tế chuyển đổi tiền tệ
  - chính sách tiền tệ kinh tế chuyển đổi
  - nợ liên doanh nghiệp
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
  - transition_economy
  - monetary_policy
  - velocity
  - dollarization
  - banking_system
  - fiscal_dominance
  - hyperinflation
  - imf_macro_accounting
  - monobank
confidence: 3
stability: stable
thesis: >
  Monetary analysis in transition economies (post-communist reform) faces five
  structural distortions absent from standard frameworks: (1) rapid, discrete
  velocity jumps (up to 3-fold in one quarter, Armenia/Georgia 1993); (2) banking
  systems that do not behave as profit maximizers (monobank legacy); (3)
  interenterprise arrears that substitute for bank credit when credit is tightened;
  (4) interest rates that may perversely amplify inflation via enterprise borrowing to
  service debt; (5) very wide lending-deposit spreads due to NPL burden, preferential
  credit legacy, and non-interest reserve requirements. Hyperinflation episodes
  (Cagan: ≥50% monthly) show real money demand can collapse to 1/30th of pre-
  inflation levels, with recovery taking years even after stabilization. [LLM]
source_refs:
  - path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md
    pages: "lines 4870–4919 (transition economy special issues, velocity jumps, monobank legacy, interenterprise arrears, interest rate problems, spreads, Box 5.10 Hyperinflation)"
    weight: primary
related:
  - node: "[[Currency_Substitution_Dollarization_Monetary_Control]]"
    relation: dollarization_is_dominant_transition_economy_symptom
  - node: "[[Imf_Money_Multiplier_Ratio_Decomposition_Three_Agent]]"
    relation: multiplier_breaks_down_under_transition_conditions
  - node: "[[Hyperinflation_Dynamics_Cagan_Real_Money_Collapse]]"
    relation: describes_endpoint_of_transition_monetary_failure
  - node: "[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]"
    relation: transition_government_financing_generates_seigniorage_pressure
date_created: "2026-05-25"
date_updated: "2026-05-25"
---

## Context: The Monobank Legacy

In centrally planned economies, a single "monobank" performed both CB and commercial banking functions:
- Served as the central bank (monetary authority)
- Had a monopoly on all commercial banking (deposits, loans)
- Credit allocation was administrative (plan-based), not price-based

At transition, the monobank was split into a CB + commercial banks. But the legacy persisted in:
- Banks initially fully state-owned → no profit-maximizing behavior
- Large stocks of preferential credits (subsidized rates to SOEs)
- Surplus of credits over deposits transferred from the monobank era
- No interbank markets to recycle funds
- Banks continued to depend on CB refinancing (CB became permanent lender, not lender of last resort)

[RAW-BOOK IMF p.4876]

---

## Five Structural Distortions

### 1. Rapid, Discrete Velocity Jumps

**Standard assumption**: Money velocity (V = PY/M) changes slowly and predictably.

**Transition reality**: Velocity rises in large, discrete jumps during high-inflation episodes.

```
Normal velocity change: 5-15% per year (gradual trend)
Transition velocity jump: 3-fold in ONE QUARTER (Armenia, Georgia, late 1993)

Mechanism:
  High inflation → money loses store-of-value function
  → Public cuts real money balances to minimum transactions level
  → M falls faster than PY → V jumps
  → Jump is non-reversible in the short run:
    Even after inflation falls, V stays high for years
    (real balances remain subdued until trust rebuilds)
```

[RAW-BOOK IMF p.4874]

**Policy implication**: M2 targets set using stable-velocity assumptions are unreliable. Money demand is structurally unstable in transition → velocity jumps make RM control insufficient for price stability. Countries must use positive real interest rates to restore domestic currency attractiveness. [RAW-BOOK IMF p.4874]

---

### 2. Banking Systems Without Profit-Maximizing Behavior

**Standard assumption**: Banks maximize profit → respond to interest rate signals from CB.

**Transition reality**: State-owned banks do not behave as profit maximizers.

```
Implication for monetary control:
  Indirect monetary instruments (OMO, policy rate) work through:
    CB rate change → bank profitability changes → bank adjusts lending
  
  If banks are not profit-driven:
    → Bank lending does not respond to rate signals
    → OMO has limited effect on credit conditions
    → CB must fall back on direct (non-price) controls:
        - Credit ceilings
        - Directed credit allocation
        - Reserve auctions with quantity limits
```

[RAW-BOOK IMF p.4876]

The shift to indirect monetary instruments (IT, OMO, standing facilities) requires banking sector competition as a prerequisite. Without it, the transmission mechanism is broken. [LLM]

---

### 3. Interenterprise Arrears (Disintermediation via Payments Arrears)

When credit is tightened but enterprises cannot adjust, a shadow credit system emerges:

```
CB tightens credit (reduces bank loans to SOEs)
→ SOEs cannot service bills from suppliers
→ Instead of defaulting, they simply delay payment
→ Supplier extends implicit "trade credit" (arrears)
→ Arrears substitute for bank credit

Arrears = unsecured, unregulated, non-performing credit
         flowing through enterprise-to-enterprise channels
         outside the banking system
```

[RAW-BOOK IMF p.4880]

**Why clearing arrears doesn't solve the problem**:
Romania's experience: providing bank credit to clear arrear balances was not a lasting solution. Unless enterprises face hard budget constraints (threat of bankruptcy, managerial accountability), new arrears accumulate immediately after clearing. [RAW-BOOK IMF p.4880]

**Required conditions to prevent arrears**:
- Positive real interest rates (making arrears costly)
- Improved payments systems (clearing infrastructure)
- Managerial accountability + bankruptcy legislation
- Enterprise restructuring / privatization

---

### 4. Perverse Interest Rate Effect (Inflation Amplification)

**Standard assumption**: Higher CB rate → tighter money → lower inflation.

**Transition pathology**: Higher rates → enterprises borrow MORE to pay interest → inflation increases.

```
Mechanism:
  CB raises lending rate
  → SOEs facing existing loan stock must pay higher interest
  → SOEs lack profits to service debt (budget constraint soft)
  → SOEs borrow from banks to pay interest obligations
  → Bank credit expands → money supply grows
  → Inflation increases

Result: Rate hike has PERVERSE effect on inflation
```

[RAW-BOOK IMF p.4884]

This pathology is structurally linked to soft budget constraints (governments guarantee SOE survival → no credible bankruptcy threat → SOEs can always borrow to roll over debt). [LLM]

---

### 5. Wide Lending-Deposit Spreads

Transition banking systems maintained abnormally wide spreads due to four structural factors [RAW-BOOK IMF p.4886]:

```
Factor 1: Non-performing loans (NPL)
  → High NPL burden → banks charge spread to provision for losses
  → Non-performing SOE loans dominate balance sheets

Factor 2: Preferential/subsidized credit legacy
  → Below-market rate loans → cross-subsidized by higher rates on market borrowers
  → Wide average spread to cover below-market portfolio

Factor 3: Non-interest reserve requirements
  → CB relied on non-remunerated reserve requirements
  → Banks lose income on reserve assets → compensate via wider spread

Factor 4: High administrative costs / absent competition
  → "Cost-plus" pricing without competitive pressure
  → No incentive to improve efficiency
```

Result: Financial intermediation is expensive → credit allocation is inefficient → investment is suppressed → real sector recovery is delayed. [RAW-BOOK IMF p.4898]

---

## Box 5.10 — Hyperinflation Dynamics

**Cagan definition**: Hyperinflation = sustained monthly price increase ≥ 50%, maintained for several months. [RAW-BOOK IMF Box 5.10 p.4892]

Historical episodes: Germany (post-WWI and post-WWII), Austria (interwar), Hungary, Bolivia, and Latin American cases.

**Three common features across all hyperinflation episodes:**

**Feature 1 — Real money demand collapses**
```
At the end of Germany's 1920s hyperinflation:
Real money demand = 1/30th of its level two years earlier

Mechanism: Expected inflation becomes the opportunity cost of holding money
  (nominal interest rates become meaningless — lending disappears)
  → Public minimizes money holdings → real balances → transaction minimum
```

[RAW-BOOK IMF Box 5.10 p.4894]

**Feature 2 — Relative price instability**
```
Germany: Real wages changed (up or down) by ~1/3 every month
→ Massive uncertainty → impossible to make investment/employment decisions
→ Social instability from arbitrary wealth redistribution
   (debtors gain, creditors lose in real terms)
```

**Feature 3 — Highly variable inflation rate**
```
Germany 1921-1923: Monthly inflation ranged from 0% to 500%
→ Nominal interest rates useless as anchor (lending virtually disappears)
→ Only metric: expected inflation rate as cost of holding money
→ Cagan (1956) money demand: m = exp(-α × π^e)
   Higher expected inflation → exponentially lower real money demand
```

**Post-stabilization persistence**: Even after inflation sharply falls, real money balances remain subdued for years. Trust rebuilds slowly. Countries that restored positive real returns on domestic money recovered confidence fastest. [RAW-BOOK IMF Box 5.10 p.4894]

---

## Fiscal Dominance in Transition Economies

Transition governments face the classic monetary-fiscal tension in extreme form [RAW-BOOK IMF p.4900]:

```
State:
  High budget deficits (collapsed tax base, spending rigidity)
  Limited access to domestic bond markets (no OMO infrastructure)
  Limited external financing (new/untested creditworthiness)

Result:
  CB must accommodate government financing needs
  → NCG (net credit to government) expands
  → Reserve money expands
  → Inflation accelerates

If monetary policy is not divorced from political process:
  → CB cannot refuse to finance government
  → Fiscal dominance is complete
  → CB loses all monetary independence
```

The critical reform: institutional separation of CB from government financing + development of domestic bond market as an alternative financing channel. [LLM — standard transition economics prescription]

---

## Connection to Standard Monetary Framework

These five distortions map directly to the standard IMF monetary framework disruptions:

| Standard assumption | Transition violation | Effect on money/inflation |
|--------------------|--------------------|--------------------------|
| Stable velocity | Velocity jumps 3x | M targets fail; price instability unpredictable |
| Banks maximize profit | State banks don't respond to rates | Indirect instruments ineffective |
| Credit tightening → less lending | Arrears substitute for loans | Monetary control illusory |
| Higher rates → less inflation | Perverse SOE borrowing | Rate hikes may amplify inflation |
| Competitive spreads | Cost-plus monopoly pricing | Suppressed financial intermediation |
