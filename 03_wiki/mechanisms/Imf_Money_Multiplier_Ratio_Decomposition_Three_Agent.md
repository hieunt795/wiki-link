---
node_id: imf_money_multiplier_decomposition_001
type: mechanism
title: Money Multiplier — Ratio Decomposition and Three-Agent Determination
aliases:
- money multiplier
- deposit multiplier
- credit multiplier
- bank money creation
- hệ số nhân tiền
- hệ số nhân tín dụng
- cơ số tiền
- số nhân tiền tệ
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- money_multiplier
- monetary_base
- reserve_requirements
- currency_deposit_ratio
- monetary_survey
- m2
- banking_system
- imf_macro_accounting
confidence: 4
stability: stable
thesis: 'The money multiplier links reserve money (monetary base) to broad money (M2)
  through the behavioral choices of three agents: the monetary authority (reserve
  requirements), commercial banks (excess reserve ratio), and the public (currency
  and time deposit ratios). The simple multiplier mm=(1+c)/(c+r) extends to a full
  decomposition across deposit types and reserve categories: mm=(1+c+b)/ (c+rd+rt·b+re·(1+b)).
  Rising c (currency flight) or re (precautionary excess reserves) compresses the
  multiplier, as do financial innovation (shifts deposits to non-bank instruments)
  and currency substitution (FX deposits exit the multiplier chain).

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: 'lines 4702–4758 (Box concept: fractional reserve basis of multiplier; simple
    mm derivation lines 4708–4726; extended mm with rd/rt/re lines 4728–4754; three-agent
    behavioral determination lines 4756–4758)'
  weight: primary
parent_node: null
related:
- node: '[[Currency_Substitution_Dollarization_Monetary_Control]]'
  relation: compresses_multiplier_via_c_increase
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: multiplier_determines_pass_through_of_reserve_money
- node: '[[Imf_Monetary_Survey_Money_Stock_Definitions]]'
  relation: multiplier_links_base_to_aggregates
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: seigniorage_depends_on_multiplier_stability
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Conceptual Foundation

The money multiplier `mm` relates broad money `M` to reserve money (monetary base, `H`):

```
M = mm × H

Where:
  H = Currency in circulation + Bank reserves (required + excess)
  M = Currency + Deposits (demand + time)
  mm > 1 when banks engage in fractional reserve lending
```

The multiplier is not a mechanical constant — it is the product of behavioral ratios set by three distinct agents. Changes in any agent's behavior shift the multiplier and delink M from RM even when RM is unchanged. [RAW-BOOK IMF p.4702]

---

## Simple Multiplier: One Deposit Type

With only demand deposits (D) and currency (C), two ratios fully determine mm:

```
c = C/D           Currency-to-deposit ratio (public behavior)
r = R/D           Reserve ratio (bank reserves / demand deposits)
                  r = rd + re
                      rd = required reserve ratio (MA policy)
                      re = excess reserve ratio (bank behavior)

H = C + R = c·D + r·D = D(c + r)
M = C + D = c·D + D = D(c + 1)

mm = M/H = (1 + c) / (c + r)
```

**Comparative statics:**
| Change | Effect on mm | Mechanism |
|--------|-------------|-----------|
| ↑ c (public holds more cash) | ↓ mm | Less deposits → smaller lending base |
| ↑ rd (MA raises requirements) | ↓ mm | Banks hold more sterile reserves |
| ↑ re (banks park excess reserves) | ↓ mm | Voluntary reserve hoarding |
| ↓ r (banks lend aggressively) | ↑ mm | Multiplier expansion |

---

## Extended Multiplier: Two Deposit Types

When time deposits (T) are disaggregated from demand deposits (D):

```
c = C/D           Currency-to-demand-deposit ratio (public)
b = T/D           Time-to-demand-deposit ratio (public portfolio choice)
rd = RD/D         Required reserve ratio on demand deposits (MA)
rt = RT/T         Required reserve ratio on time deposits (MA)
re = RE/(D+T)     Excess reserve ratio held by banks

H = C + RD + RT + RE
H = c·D + rd·D + rt·b·D + re·(1 + b)·D
H = D × [c + rd + rt·b + re·(1 + b)]

M2 = C + D + T = (1 + c + b)·D

mm_M2 = (1 + c + b) / [c + rd + rt·b + re·(1 + b)]
```

[RAW-BOOK IMF p.4715–4730]

**Key insight:** The denominator grows with `b` at rate `rt − re`. If `rt > re` (required reserves on time deposits exceed typical excess reserves), expanding time deposits shrinks mm. If `rt < re`, shifting from demand to time deposits expands mm. [LLM — algebraic inference from IMF framework]

---

## Three-Agent Determination

The multiplier is jointly determined by behavioral choices that no single agent fully controls:

```
┌─────────────────────────────────────────────────────────────┐
│ Agent               │ Instruments          │ Multiplier levers │
├─────────────────────────────────────────────────────────────┤
│ Monetary Authority  │ rd (demand deposits) │ ↑ rd → ↓ mm      │
│                     │ rt (time deposits)   │ ↑ rt → ↓ mm      │
│                     │ RP (reserve money)   │ Changes mm base   │
├─────────────────────────────────────────────────────────────┤
│ Commercial Banks    │ re (excess reserves) │ ↑ re → ↓ mm      │
│                     │ Lending decisions    │ Determines D via  │
│                     │                      │ credit supply     │
├─────────────────────────────────────────────────────────────┤
│ Public (Households  │ c (currency/deposit) │ ↑ c → ↓ mm       │
│ + Firms)            │ b (time/demand dep.) │ Changes mm via    │
│                     │                      │ deposit mix       │
└─────────────────────────────────────────────────────────────┘
```

[RAW-BOOK IMF p.4740–4758]

The CB controls `rd` and `rt` directly, and `H` (base money) through OMO. But banks' `re` and the public's `c` and `b` are endogenous to economic conditions — they shift in response to uncertainty, interest rates, and CB credibility.

---

## Multiplier Instability: Why mm Shifts

The multiplier is not stable under:

**1. Financial innovation**
New instruments (money market funds, securitization, sweep accounts) allow the public to shift deposits out of the regulated banking system → `b` changes unpredictably → mm unstable. [RAW-BOOK IMF p.4760]

**2. Banking system stress**
Banks hold precautionary excess reserves → `re` rises → mm falls. Extreme case: GFC (US excess reserves at Fed rose from <$2bn to >$1tr), mm collapsed from ~8x to ~3x. [LLM — contextual example]

**3. Currency substitution / dollarization**
Public converts domestic deposits to FX deposits. FX deposits may lie outside the domestic multiplier chain → effective `c` rises (less domestic deposits) → mm falls. Under full dollarization, the CB has no base money leverage at all. [connects to [[Currency_Substitution_Dollarization_Monetary_Control]]]

**4. Policy rate changes**
Higher rates → ↓ `re` (opportunity cost of holding excess reserves rises) → ↑ mm. But also → ↑ `b` (time deposits more attractive vs demand deposits) → ambiguous net effect.

---

## Monetary Policy Implication: M2 Target vs RM Instrument

If the CB targets M2:

```
M2 = mm × H

To hit M2* given current mm:
  H* = M2* / mm

But if mm is unstable, the required H changes unpredictably.
```

**Stability condition**: M2 targeting is reliable only if `mm` is predictable. Under:
- Stable financial systems → mm predictable → targeting RM achieves M2 target
- Financial innovation / currency substitution → mm unstable → target M2 directly, let H adjust

This is why many CB frameworks shifted from M2 targeting to interest rate targeting (IT): the interest rate `i` directly affects bank lending and deposit rates without depending on mm stability. [RAW-BOOK IMF p.4756]

---

## Seigniorage and the Multiplier

Seigniorage revenue to the CB = `Δ H × (r_domestic)` — the return on non-interest-bearing reserve money issued. But if mm shrinks:

```
ΔM2 = mm × ΔH + ΔH × Δmm   (if mm is falling)
```

A rising monetary base with a falling multiplier produces less M2 expansion — so inflationary pressure per unit of seigniorage is lower, but the CB earns more seigniorage on a larger H. The fiscal value of seigniorage depends on `H`, not directly on `mm`. [LLM — relates to [[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]]
