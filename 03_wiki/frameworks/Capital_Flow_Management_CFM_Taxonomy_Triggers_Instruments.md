---
node_id: capital_flow_management_cfm_taxonomy_001
type: framework
title: Capital Flow Management — Taxonomy, Triggers, and Instruments
aliases:
- CFM instruments
- capital controls taxonomy
- foreign capital flow management
- unremunerated reserve requirement URR
- capital flow management triggers
- quản lý dòng vốn ngoại
- công cụ CFM
- biện pháp kiểm soát vốn
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- cfm
- capital_controls
- capital_flows
- em_policy
- macroprudential
- fx_intervention
- impossible_trinity
- perry_warjiyo
confidence: 3
stability: stable
thesis: 'Capital Flow Management (CFM) is a third policy instrument used by EME central
  banks to manage the impossible trinity when interest rates and FX intervention alone
  are insufficient. CFM tools range from administrative (taxes, URR, restrictions)
  to prudential (NOP, LDR, FX loan caps), with IMF 2012 guidance identifying three
  trigger conditions for deployment. CFM reduces the offset coefficient by directly
  restricting the volume of inflows that generate sterilization pressure and quasi-fiscal
  costs. [LLM]

  '
source_refs:
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-6.md
  pages: 'lines 287–355 (CFM principles, targets, instruments, country cases: Brazil,
    Colombia, Korea, Croatia)'
  weight: primary
parent_node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
related:
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: component_of
- node: '[[Sterilization_Offset_Coefficient_EME_Monetary_Autonomy]]'
  relation: reduces_offset_coefficient
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: complements
- node: '[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]'
  relation: reduces_sterilization_pressure
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: preventive_tool
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Why CFM Exists: Gap in the Standard Policy Toolkit

Under post-GFC conditions, "interest rates alone, as the main policy instrument, cannot respond to
the volatility and magnitude of foreign capital flows to EMEs, even when complemented with foreign
exchange intervention as a secondary instrument." [RAW-BOOK Perry p.293]

The problem is circular:
1. Capital inflows → CB intervenes (buys FX) → RM expands
2. CB sterilizes → r_domestic rises → more inflows (offset effect)
3. FX reserves accumulate → sterilization cost builds (quasi-fiscal)
4. Each rate adjustment draws more flows than it sterilizes

CFM breaks this cycle by **reducing inflow volume** — cutting the problem at source rather than managing its monetary consequences after arrival.

---

## IMF (2012) Three Trigger Conditions for CFM

CFM is appropriate when [RAW-BOOK Perry p.295]:

**Trigger 1 — Macro policy space exhausted**
Monetary and fiscal policy have already tightened (or cannot tighten further), but inflows remain excessive. Signs: economic overheating, asset price bubbles, accumulating external debt, exchange rate overvaluation, excessive and costly reserve accumulation.

**Trigger 2 — Policy transmission lag**
Macroeconomic policy adjustment is delayed by institutional process (fiscal requires parliamentary approval; monetary transmission has lags through expectations and demand channels). CFM can provide immediate flow restriction while policy catches up.

**Trigger 3 — Financial stability risk**
Inflows are generating systemic risk through credit booms, excessive leverage, or banking sector FX exposure — risks that macroprudential policy alone cannot fully address without targeting the source flows.

---

## CFM Design Principles (IMF 2013)

Effective CFM must be [RAW-BOOK Perry p.301]:

| Principle | Definition |
|-----------|-----------|
| **Transparent** | Clear communication of targets and instruments to avoid market distortion |
| **Targeted** | Applied to the specific flow type posing the highest risk (typically PI and short-term debt) |
| **Temporary** | Tightened when inflows increase; loosened as flows ebb or reverse |
| **Non-discriminatory** | Apply equally to residents and non-residents where possible; capital controls (non-resident-specific) are acceptable when non-discriminatory measures fail |

---

## Instrument Taxonomy

### Administrative / Quantitative Instruments
Directly restrict specific flow types regardless of financial channel.

| Instrument | Description | Example |
|-----------|-------------|---------|
| **Tobin tax / financial transaction tax** | Tax on specific capital inflows (PI stocks, bonds, external loans) | Brazil: 2% IOF tax on PI bonds (Oct 2009) [RAW-BOOK Perry p.335] |
| **Unremunerated Reserve Requirement (URR)** | Non-interest-bearing deposit required against foreign inflows; imposes carry cost on inflows | Colombia: 40% URR at 6 months on external borrowing + PI (2007), raised to 50% (May 2008) [RAW-BOOK Perry p.335] |
| **Minimum holding period** | Non-residents must hold investment for minimum period before selling | Chile (1990s): minimum holding before exit; Ukraine: minimum holding before transfer of proceeds [RAW-BOOK Perry p.325] |
| **Transfer tax** | Tax on conversion/transfer of proceeds from investment sale | Malaysia: tax on transfer of sale proceeds [RAW-BOOK Perry p.325] |
| **Quantity restrictions / bans** | Direct limits or prohibitions on specific capital flows | Iceland: restrictions on resident investment in offshore instruments [RAW-BOOK Perry p.325] |

### Prudential Instruments
Applied to domestic financial institutions; target currency or maturity risk rather than residency.

| Instrument | Description | Country |
|-----------|-------------|---------|
| **Net Open Position (NOP) limits** | Cap on bank FX net exposure relative to capital | Korea: 50% of capital limit on FX derivatives position [RAW-BOOK Perry p.347] |
| **Foreign loan restrictions** | Limits on bank borrowing from foreign sources (debt-to-capital, maturity restrictions) | Korea: ceiling on FX forward positions to restrict non-resident bond funding [RAW-BOOK Perry p.347] |
| **FX reserve requirements** | Differentiated reserve requirements by currency (not by residency) | BI: FX reserve requirements on banking obligations |
| **LTV / debt-to-equity caps on FX borrowers** | Restrict corporate FX borrowing by requiring hedging or imposing D/E limits | Corporate sector prudential CFM |
| **Risk weights on FX loans** | Higher capital requirements on bank FX lending to unhedged borrowers | Standard macroprudential + CFM overlap |

---

## CFM vs Macroprudential: The Boundary

A frequent confusion — CFM and macroprudential have **different targets** [RAW-BOOK Perry p.313]:

```
CFM target:        Restrict capital flow VOLUME and COMPOSITION
Macroprudential:   Mitigate systemic RISK in domestic financial system

Example — Reserve requirement on FX bank liabilities:
  → If applied to restrict external debt inflows: CFM
  → If applied to reduce bank leverage and FX mismatch: macroprudential
  → In practice: usually both simultaneously
```

The two become complementary when capital flows GENERATE systemic risk (credit booms, FX mismatch, asset bubbles from PI inflows). Under these conditions, CFM + macroprudential in tandem is more effective than either alone. [RAW-BOOK Perry p.315]

---

## Country Cases

### Brazil and Colombia (2007–2010)

Both applied CFM to mitigate BRL/COP appreciation from hot money:

- **Colombia**: 40% URR at 6 months on external borrowing + PI; expanded to include FDI staying < 2 years (May 2008). Exempted ADR issuances but then closed that loophole.
- **Brazil**: 1.5% IOF on PI stocks/bonds (March 2008); removed at GFC; reintroduced at 2% (Oct 2009); differential treatment for ADR conversions.

Both initially targeted external loans, then expanded scope to cover portfolio flows as investors arbitraged narrow restrictions via bond markets. [RAW-BOOK Perry p.335]

**Key lesson**: CFM must be dynamic — regulatory loopholes are exploited quickly. "The authorities must be ready to refine the regulations as necessary." [RAW-BOOK Perry p.333]

### Korea

Applied prudential regulations on banking sector FX derivatives position (cap at 50% of capital for domestic banks, 250% for foreign bank branches) to restrict NDF-driven capital inflows:

Non-resident bond investors hedged NDF short-KRW positions by buying domestic government bonds → capital inflows through bond market persisted even after bank FX loan restrictions. [RAW-BOOK Perry p.347]

**Key lesson**: Prudential CFM on banks may divert flows to non-bank channels (direct foreign borrowing, NDF offshore). Comprehensive coverage across all channels is required.

### Croatia

CNB as Eurosystem member had limited monetary tools; fiscal policy constrained by structural deficit. CNB relied on prudential regulations on banking sector FX exposure to manage capital inflows:

- Tightened restrictions → credit growth slowed but loans shifted to **direct foreign borrowing** by corporates (outside prudential perimeter)
- Result: capital flows persisted through a different vehicle; bank-intermediated credit fell but total external debt did not

**Key lesson**: "The disintermediation escape valve" — prudential CFM only works if the alternative channels (non-bank, direct offshore) are also regulated or limited by structural features. [RAW-BOOK Perry p.353]

---

## The Sequencing Logic (Perry Defense Line Framework)

Optimal response sequence when facing capital flow surge [RAW-BOOK Perry p.289]:

```
LINE 1: Prudent macroeconomic policy (fiscal + monetary adjustment)
LINE 2: FX reserves accumulation + bilateral/multilateral swap arrangements
LINE 3: Financial sector deepening + institutional capacity strengthening
LINE 4: CFM (targeted, temporary, transparent, non-discriminatory)
         → Administrative: taxes, URR, holding periods
         → Prudential: NOP, FX loan limits, reserve requirements
```

CFM is not the first line of defense — it supplements macroeconomic policy when those tools reach their limits. Deploying CFM without first exhausting Lines 1–3 risks masking underlying macro imbalances. [LLM]

---

## Exit Conditions

CFM should be unwound when [RAW-BOOK Perry p.317]:
- Capital flows have ebbed and volatility subsided
- CFM is becoming an undesirable economic drag or evasion-prone
- Underlying macro imbalances (inflation, current account) are corrected

Certain **macroprudential** measures should be maintained even after CFM is removed — systemic risks from past flow episodes (FX mismatches, credit overhangs) persist after flows stop.

For permanent/structural capital flow changes: CFM is insufficient — requires financial sector deepening, productivity improvement, and institutional reform to change the structural pull factors. [RAW-BOOK Perry p.317]
