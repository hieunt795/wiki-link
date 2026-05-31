---
node_id: cb_quasi_fiscal_sterilization_seigniorage_001
type: mechanism
title: CB Quasi-Fiscal Mechanism — Sterilization Costs, Seigniorage, and the Fiscal-Monetary
  Nexus
aliases:
- quasi-fiscal CB operations
- sterilization quasi-fiscal cost
- seigniorage transfer channel
- fiscal dominance mechanism
- CB profit transfer to government
- cơ chế bán tài chính ngân hàng trung ương
- chi phí bán tài chính sterilization
- kênh seigniorage chuyển lợi nhuận cho chính phủ
- thống trị tài khóa
- tương tác chính sách tiền tệ và tài khóa
domain:
  primary: monetary_policy
  secondary: fiscal_policy
tags:
- quasi_fiscal
- seigniorage
- sterilization
- fiscal_dominance
- cb_independence
- ncg
- monetization
- cb_capital
- fiscal_monetary_nexus
- em_policy
- fx_intervention
confidence: 4
stability: stable
thesis: 'The FX rate target creates a quasi-fiscal channel that runs in both directions:
  (1) the normal seigniorage channel transfers CB profits to government as nontax
  revenue when CB issues non-interest-bearing liabilities and earns on backing assets;
  (2) sterilization of inflows inverts this channel — CB earns low-yield FX assets
  while paying high-yield domestic assets, converting seigniorage transfers into calls
  on the government budget; (3) NCG expansion to accommodate fiscal deficits looks
  neutral in the monetary survey but functions as de facto deficit monetization, masking
  fiscal imbalances until NFA depletion forces adjustment; (4) fiscal dominance —
  where government pressure prevents policy correction — is the endpoint of sustained
  NCG accommodation combined with FX target defense. The IMF GFS framework classifies
  CB sterilization losses, subsidized lending, and FX guarantees as quasi-fiscal operations
  that must be added to the conventional fiscal deficit to measure the true policy
  stance.

  '
source_refs:
- path: 02_sources/books/lipschitz_schadler_macro/Lipschitz_Schadler_Macroeconomics.md
  pages: lines 2209–2239 (Box 4.1 seigniorage), lines 2641–2663 (Box 4.6 helicopter
    money and CB P&L), lines 2720–2728 (sterilization costs), lines 2730–2763 (fiscal
    accommodation and fiscal dominance), lines 2948, 2963–2969 (profit transfers as
    nontax revenue)
  weight: primary
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: lines 2280–2292 (Box 3.7 Quasi-Fiscal Operations), lines 1846 (CB profits
    in GFS), lines 2467 (sterilization cost exercise)
  weight: primary
- path: 02_sources/books/central_policy_Perry/Perry Warjiyo and Solikin M. Juhro -
    Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-5.md
  pages: lines 863–882 (fiscal-monetary coordination, CB independence under crisis,
    government backstop of CB solvency)
  weight: secondary
parent_node: null
related:
- node: '[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]'
  relation: upstream_mechanism
- node: '[[CB_Seigniorage_Income_Capital_Loss_Policy_Independence]]'
  relation: companion_concept
- node: '[[Imf_Gfs_Fiscal_Accounting_Framework_Deficit_Measurement_And_Sustainability]]'
  relation: accounting_foundation
- node: '[[Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework]]'
  relation: identity_foundation
- node: '[[Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating]]'
  relation: crisis_endpoint
- node: '[[EM_Central_Bank_Policy_Mix_FIT_Framework]]'
  relation: policy_response_framework
date_created: '2026-05-24'
date_updated: '2026-05-24'
steps:
- 'Step 1: the normal seigniorage channel transfers CB profits to government as nontax revenue when CB issues non-interest-bearing liabilities and earns on backing assets'
- 'Step 2: sterilization of inflows inverts this channel — CB earns low-yield FX assets while paying high-yield domestic assets, converting seigniorage transfers into calls on the government budget'
- 'Step 3: NCG expansion to accommodate fiscal deficits looks neutral in the monetary survey but functions as de facto deficit monetization, masking fiscal imbalances until NFA depletion forces adjustment'
- 'Step 4: fiscal dominance — where government pressure prevents policy correction — is the endpoint of sustained NCG accommodation combined with FX target defense. The IMF GFS framework classifies CB sterilization losses, subsidized lending, and FX guarantees as quasi-fiscal operations that must be added to the conventional fiscal deficit to measure the true policy stance'

---

## The Fundamental Channel Architecture

Under the monetary base identity `RM = NFA + NCG + Cb + OIN`, two balance sheet positions determine the fiscal-monetary linkage:

**NFA** — Net foreign assets: the FX intervention channel. Changes here are driven by BOP flows under an FX target.

**NCG** — Net claims on government: the fiscal channel. Changes here reflect CB lending to government or CB purchases of government securities.

The quasi-fiscal nexus operates through **both** channels simultaneously. FX targeting endogenizes NFA; the government financing decision shapes NCG. When both move adversely — NFA falling from depreciation defense, NCG rising from fiscal accommodation — the CB balance sheet deteriorates along two axes at once. [RAW-BOOK Lipschitz p.2753]

---

## Channel 1: The Normal Seigniorage Transfer (Baseline Case)

In normal operation, the CB is a profitable institution that transfers income to the government:

```
CB Balance Sheet (baseline):
  Assets                         Liabilities
  Interest-bearing bonds (+r_a)  Banknotes (cost ≈ 0)
  FX reserves (+r_foreign)       Bank reserves (cost ≈ 0 or low)

Seigniorage = r_a × assets − cost of liabilities
            ≈ r_a × RM  (when liabilities are unremunerated)
```

"When the central bank increases the outstanding stock of non-interest-bearing base money, it transfers real resources to (increases the purchasing power of) the government... So the profits of the central bank rise, and much of this is transferred to the government." [RAW-BOOK Lipschitz p.2211]

**Fiscal accounting treatment:** "For most countries profit transfers from the central bank are a significant nontax revenue. [RAW-BOOK Lipschitz p.2948]" Under GFS methodology: "Seigniorage — i.e., revenue from the printing of money by the central bank — may also be treated as part of government financing. It is more usually included above the line in nontax revenues as profit transfers from the central bank." [RAW-BOOK Lipschitz p.2963]

The IMF GFS manual requires: "The profits of the central bank that are actually transferred to the government are treated as revenue. However, it should be noted both that these profits should not include unrealized profits stemming from the revaluation of holdings of foreign exchange or gold reserves and that they should cover the entire operations of the central bank, and not just its selected operations." [RAW-BOOK IMF Macro p.1846]

**Key implication:** Seigniorage transfers are not only a monetary phenomenon — they are a **fiscal revenue item**. Their size depends on: (a) the stock of unremunerated CB liabilities, (b) the yield earned on backing assets, and (c) the cost of any sterilization operations layered on top.

---

## Channel 2: Sterilization of Capital Inflows → Seigniorage Destruction

When a CB with an FX target sterilizes appreciation pressure (buying FX, issuing domestic securities to absorb RM), the income arithmetic inverts:

```
Sterilization operation:
  CB buys FX reserves          → earns r_foreign (e.g. USD T-bill yield ~4-5%)
  CB issues domestic T-bills   → pays r_domestic (e.g. EM rate ~6-10%)

Net carry = r_foreign × NFA_accumulated − r_domestic × sterilization_stock
          = NEGATIVE (for typical EM with r_domestic > r_foreign)
```

"Such sterilization can be costly. It entails, in effect, buying low-yield foreign exchange assets (usually US Treasury bills) and selling relatively high-yield domestic assets... thus the sterilization operation reduces the profits (or increases the losses) of the central bank, and reduces (increases) its transfers to (calls on) the government budget. Governments are usually loath to allow such policies to continue indefinitely." [RAW-BOOK Lipschitz p.2720]

**The fiscal consequence:** The seigniorage transfer does not merely shrink — it reverses. Instead of the CB transferring profits to the Treasury, the government must **recapitalize the CB** or accept that the CB carries negative equity on its books. Either:
- Government provides capital injection (explicit fiscal cost)
- CB books losses, carries negative equity (implicit fiscal cost — deferred)
- Government pressures CB to stop sterilizing (independence erosion)

"Sustained sterilization to offset the monetary effects of this type of intervention is typically costly to a central bank, weakening its capital position, and reducing seigniorage transfers to the government." [RAW-BOOK Lipschitz p.2728]

**Condition for this channel to bind:** r_domestic > r_foreign AND sustained capital inflows requiring large-scale sterilization. Most EM central banks that have maintained undervalued currencies face this over multi-year periods (China 2003–2013, Korea, Brazil, Vietnam SBV OMO T-bill operations post-COVID). [LLM]

---

## Channel 3: NCG Expansion — The Hidden Monetization Path

The most dangerous quasi-fiscal path: government deficit expands → banks buy government bonds → CB provides offsetting OMO to prevent monetary tightening → NCG rises → M2 expands. This is **de facto monetization** even when no direct CB-to-government lending occurs.

The three-step Lipschitz & Schadler mechanism [RAW-BOOK Lipschitz p.2745–2753]:

```
Step 1 — Government offers bonds to market (direct CB lending restricted by law):
  Banks absorb bonds → NCG↑ in banking survey → CO↓ (crowding out private credit)

Step 2 — CB accommodates (prevents monetary tightening):
  CB buys equivalent bonds from banks → RM↑ → CO reverses back up
  Net balance sheet: NCG↑, M2↑ (same outcome as direct CB lending)

Step 3 — External adjustment:
  Higher spending → CA deficit pressure → CB defends FX → NFA↓
  End state: NCG↑↑, NFA↓, M2 ≈ unchanged but backed by worse-quality assets
```

"In effect, the higher government deficit is being financed by a drawdown in central bank reserves to finance a resource transfer from abroad." [RAW-BOOK Lipschitz p.2753]

The critical monitoring signal: **NCG rising while NFA falling** within the same monetary survey period. These two movements cancel in M2 but signal structural deterioration — the CB is simultaneously financing the government (NCG↑) and defending the FX rate (NFA↓), and neither is sustainable separately.

---

## Channel 4: CB Recapitalization — The Fiscal Backstop

At the far end of the deterioration sequence, CB losses exhaust capital. The government must act:

**Recapitalization mechanics:**
- Government issues bonds → injects equity into CB
- CB balance sheet: Equity↑, losses absorbed
- Government balance sheet: Debt↑ (explicit), revenue from CB profit transfer → zero for years

**Under GFS methodology:** "Governments may inject capital into the banks and in some cases take over their debts... only the interest payments on the assumed debt affect the size of the fiscal balance." [RAW-BOOK IMF Macro p.1841]

This creates a perverse accounting result: a large CB recapitalization appears only as future interest expense flows in the conventional fiscal deficit, not as a stock event. The **true fiscal cost** (the PV of future interest on the recapitalization bonds) is not captured in headline deficit data.

Perry Warjiyo: "under serious crisis conditions that threaten the solvency of the central bank's balance sheet, with potentially massive financial losses expected, the government is expected to stand firm in its backing of the central bank." [RAW-BOOK Perry p.875]

The backstop creates **moral hazard**: CBs that expect government rescue have weaker incentives to resist political pressure to extend sterilization or NCG accommodation beyond the optimal point.

---

## IMF Quasi-Fiscal Taxonomy (Box 3.7)

The IMF GFS framework identifies three main quasi-fiscal operation types for CBs:

| QFO Type | Mechanism | Fiscal Impact |
|----------|-----------|---------------|
| **FX subsidies through exchange system** | Multiple exchange rates; CB sells FX at below-market rate to favored importers | Subsidy cost = (market rate − administered rate) × volume |
| **Subsidized lending** to government, public enterprises, or private entities | CB lends at below-market rate (directed credit) | Subsidy cost = (market rate − lending rate) × loan stock |
| **Unfunded contingent liabilities** — FX rate guarantees, deposit insurance | CB guarantees FX rate for borrowers; guarantee is exercised → CB absorbs loss | Contingent cost materializes when FX depreciates + borrowers cannot service FX debt |

"Where these quasi-fiscal operations are significant, their costs need to be included in any comprehensive measure of the public sector deficit, for several reasons. In many countries, central and public sector bank losses are so large that they contribute to financial instability. Their existence also means that the conventional measures of government's fiscal balance are misleading indicators of the role of fiscal operations in the economy." [RAW-BOOK IMF Macro p.2288]

**Reform objective:** "quasi-fiscal activities should be transformed into normal budgetary operations — that is, quasi-fiscal taxes and subsidies should be replaced with explicit taxes and subsidies. The long-term objective should be to address the root causes of quasi-fiscal operations." [RAW-BOOK IMF Macro p.2290]

---

## Fiscal Dominance: The Endpoint State

Fiscal dominance is reached when the government's financing requirements so constrain the CB that independent monetary policy becomes impossible:

**Formal definition:** "in situations like this (known as 'fiscal dominance') there is no scope for independent monetary policy." [RAW-BOOK Lipschitz p.2757]

**The causal sequence:**

```
Fiscal expansion → deficit > domestic financing capacity
→ CB accommodates (buys bonds, holds NCG steady, keeps rates from rising)
→ RM expands → inflation pressure → CB defends FX → NFA↓
→ Repeat each period: NCG↑↑, NFA↓↓
→ Reserves approach critical minimum
→ Risk premia rise → outflows accelerate → self-reinforcing crisis
→ CB abandons IT/FX target → "vicious circle of self-perpetuating depreciation,
   increasing inflation, and rising inflation expectations" [RAW-BOOK Lipschitz p.2757]
```

**Preconditions that accelerate fiscal dominance:**
1. CB legally prohibited from direct government lending but accommodation occurs via secondary market purchases (same monetary effect)
2. Government unwilling or politically unable to reduce deficit
3. CB independence weak — insufficient institutional insulation to resist accommodation pressure
4. FX reserves low — CB has little buffer to absorb both NFA defense and NCG expansion simultaneously

**Note on CB independence as the structural firewall:** "Under normal conditions, there is a clear separation between the domains of central bank monetary policy and government fiscal policy. Nevertheless, the opposite can occur under crisis conditions." [RAW-BOOK Perry p.865] Perry identifies fiscal-monetary coordination during crisis as *necessary* but stresses the CB must "prudently extricate itself from the policy compromise with the government and gradually rebuild its independence" once the crisis passes. [RAW-BOOK Perry p.877]

---

## Measuring the True Fiscal Stance: Adjusting for QFOs

The conventional fiscal deficit underestimates the true fiscal-monetary expansion when QFOs are significant. Full measurement requires:

```
True fiscal stance =
  GFS fiscal deficit
  + CB sterilization net losses (r_domestic × stock − r_foreign × NFA)
  + CB subsidized lending subsidy element (rate differential × volume)
  + FX guarantee contingent liabilities × probability of exercise
  + Policy bank (development bank) below-market lending subsidy
  ± CB recapitalization cost (PV of future interest on recap bonds)
```

**Vietnam SBV example (2024, estimated) [LLM — data from research, not source books]:**

| QFO | Estimated Scale |
|-----|-----------------|
| VBSP subsidized lending (VND 398.1tr outstanding, rate differential ~3-4%) | ~0.2-0.3% GDP/year |
| SBV OMO T-bill sterilization (Oct 2023: VND 111tr, rate 1.18%) | ~0.1-0.2% GDP |
| VDB off-budget contingent liabilities | Unquantified |
| SBV FX intervention losses (sell-high/buy-low cycle) | Variable |
| **Reported GFS deficit 2024** | **-1.5% GDP** |
| **True stance (estimated)** | **-2.0% to -2.5% GDP** |

---

## Policy Interaction Matrix

| CB Policy Stance | Fiscal Stance | Balance Sheet Outcome | Sustainability |
|-----------------|---------------|----------------------|----------------|
| Sterilize inflows | Surplus or balanced | NFA↑, NDA↓, RM stable — but CB carries negative carry on FX assets | Medium-term: unsustainable if r spread large |
| Sterilize inflows | Deficit | NFA↑, NCG↑, RM expands despite sterilization — M2 overshoot | Low: double expansionary pressure |
| Defend FX rate | Surplus | NFA↓ (intervention drain) offset by NCG↓ (fiscal tightening draws reserves back) | Sustainable if transitory shock |
| Defend FX rate | Deficit + accommodation | NFA↓↓, NCG↑↑ — the Bulgaria 1994-1996 path | Unsustainable: trajectory to crisis |
| Pure IT (no FX target) | Any | NDA is free instrument — CB adjusts policy rate | No FX constraint; fiscal position shows in NCG/crowding out |

---

## Diagnostic Summary

```
SIGNAL 1 — STERILIZATION COST BUILDING:
  NFA rising while OIN/NCG rising simultaneously
  → CB accumulating FX but paying out domestic yield
  → Quasi-fiscal cost = interest differential × stock
  → Watch: CB profit transfer to Treasury declining year-over-year

SIGNAL 2 — COVERT MONETIZATION:
  NCG rising quarter-over-quarter despite "no direct CB lending"
  → CB accommodating government via secondary market OMO
  → Fiscal deficit being monetized indirectly
  → Watch: NCG/M2 ratio rising

SIGNAL 3 — DUAL DETERIORATION (CRISIS PRECURSOR):
  NFA declining AND NCG rising simultaneously
  → CB defending FX AND accommodating fiscal
  → Both drains on policy space at once
  → Watch: NFA/RM ratio approaching Greenspan-Guidotti floor (1.0)

SIGNAL 4 — FISCAL DOMINANCE ENDPOINT:
  CB rate held below neutral despite inflation
  Sterilization halted despite inflows
  NCG expanding without CB resistance
  → Political pressure overriding CB mandate
  → "No scope for independent monetary policy" [RAW-BOOK Lipschitz p.2757]
```
