---
slug: yield_curve_drivers
topic: us_treasury_curve_2026
sub_question: sq3 + sq5 + sq6
date: 2026-05-24
confidence: 2
sources:
  - "[WEB-2026-05-24] TBAC May 2026 minutes: $125B refunding, CBO $1.9T deficit"
  - "[WEB-2026-05-24] Japan Q1 2026 UST selling: $29.6B"
  - "[WEB-2026-05-24] Ferrante Capital: term premium regime analysis"
  - "[RAW-WIKI Treasury_Market_Dealer_Intermediation_Capacity]"
  - "[RAW-WIKI Swap_Spreads_Balance_Sheet_Plumbing_Frictions]"
  - "[RAW-WIKI Fixed_Income_Relative_Value_Framework]"
  - "[RAW-WIKI Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]"
promote_to_wiki: false
reason_not_promoting: "Combines current-event data with structural mechanisms; full promotion requires separating components"
---

## Finding: Four Structural Drivers of Long-End Elevation

### Driver 1 — Fiscal Supply: $1.9T Deficit, Stable Coupon Sizes

**Mechanism:** Treasury issues coupon bonds to finance the deficit. Each new coupon bond transfers duration risk to the private sector. IF private sector balance sheet capacity is fixed in the short run, THEN price-clearing requires higher yield (lower price) to attract new buyers. [WEB-2026-05-24, RAW-WIKI Treasury_Market_Dealer_Intermediation_Capacity]

**Current state:**
- CBO FY2026 deficit: **$1.9 trillion** [WEB-2026-05-24]
- TBAC May quarterly refunding: $125B coupons, $41.7B new cash [WEB-2026-05-24]
- Coupon sizes held steady vs Q1 2026 — no immediate supply increase
- BUT: $1.3T projected funding shortfall FY2027-28 if coupon sizes not increased [WEB-2026-05-24]

**The forward supply premium:** Markets price future supply risk into current long-end yields. Even if Treasury holds coupon sizes today, the credible threat that FY2027-28 requires larger auctions is sufficient to steepen the curve. The 30y at 5.07% contains a supply option premium for the scenario where coupon sizes eventually increase. [LLM-E]

**Key constraint:** Dealer intermediation capacity [RAW-WIKI Treasury_Market_Dealer_Intermediation_Capacity]. Primary dealers must bid at every auction. SLR/LCR constrains how much inventory they can hold. With Treasury at ~$28T outstanding and dealer balance sheets growing much slower, each incremental auction requires a higher clearing yield. The structural intermediation gap (Duffie 2026) is a force multiplier on fiscal supply pressure.

---

### Driver 2 — Fed Duration Withdrawal: Reverse Twist Effect

**Mechanism:** During QE (2008-2014, 2020-2021), the Fed removed duration from the market by buying long-dated UST and MBS → suppressed term premium. During QT (2022-2025), the Fed stopped reinvesting → duration flowed back to private sector → term premium normalized.

**Current state (May 2026):**
- QT2 removed $2.2T ($1.6T UST + $0.6T MBS) from SOMA [from fed_framework_2026 research]
- Fed now buys only T-bills (RMPs) → reinvests principal into short end only
- MBS prepayments → T-bills: shortens SOMA duration, does not replace coupon duration
- Net: SOMA holds ~$4.46T UST + $1.98T MBS. The MBS portfolio naturally ages; as principal returns, it buys T-bills, not new coupons.

**The reverse twist:** QE was a "duration-extracting twist" (buy long, sell nothing). The current operation is a passive "reverse twist" — MBS duration shrinks via prepayments; no new long-duration replacement purchased. Private sector must absorb the duration delta.

IF the Fed restarted coupon purchases (a future QE program), THEN term premium would compress 50-100bps over 6-12 months (2013 taper tantrum analog: ~100bps of term premium moved in 4 months) [WEB-2026-05-24, LLM-E].

---

### Driver 3 — Japan and Foreign Demand Retreat

**Mechanism:** Foreign central banks and sovereign investors historically absorbed a large share of Treasury supply, providing a non-price-sensitive demand buffer. As this buffer shrinks, more supply clears through price-sensitive domestic investors → higher yield required. [WEB-2026-05-24]

**Current state:**
- Japan: $1.24T → $1.19T in March 2026; sold **$29.6B in Q1 2026** — largest quarterly reduction in ~4 years [WEB-2026-05-24]
- JGB 10y yield: **~2.3%** — multi-decade high, near-compete with currency-hedged UST returns [WEB-2026-05-24]
- Total foreign holdings at record $9.49T (Feb) but declining as Japan retreats

**The hedging math:** A Japanese investor buying 10y UST at 4.56% must pay ~250bps/year in USD/JPY currency hedge cost (rough estimate). Net hedged yield = 4.56% - 2.50% = ~2.06% [LLM-E]. Compare to JGB 10y at 2.3% — hedged UST is BELOW JGB yield. Incentive to hold UST is gone unless investor holds unhedged (then carries full FX risk).

**IF JGB yields continue rising (BOJ normalizing from 0.1% to 1.0-1.5%)**, THEN Japanese demand for currency-hedged UST continues declining → marginal buyer shifts from Japanese insurer to domestic US fund → domestic funds demand higher spread → term premium rises [LLM-E].

---

### Driver 4 — Inflation Uncertainty and Credibility Erosion Risk

**Mechanism:** Investors price term premium partly as compensation for inflation uncertainty. IF inflation is unpredictable, THEN locking in nominal yield for 30 years requires additional compensation for the risk that realized inflation erodes returns. [WEB-2026-05-24 Ferrante Capital]

**Current state:**
- 5y5y forward inflation: **2.29%** — above 2% target but not unanchored [WEB-2026-05-18]
- Core PCE: **3.2%** (March 2026) — tariff-driven overshoot [from fed_framework_2026 research]
- FOMC staff baseline: inflation peaks Q2 2026 and falls toward 2% by 2027

**The credibility risk:** If the FOMC staff baseline proves wrong (tariff inflation more persistent than expected), then: (a) 5y5y rises toward 2.5-3.0% → term premium rises another 30-60bps; (b) The Fed faces a dual bind (cannot cut on weak growth, cannot ignore inflation) → policy uncertainty premium builds into 10s/30s.

**What would signal credibility erosion:** 5y5y forward inflation rising above 2.5% for 3+ consecutive weeks, or TIPS 5y breakeven diverging upward from 10y breakeven. Neither has occurred yet — current structure is consistent with "tariff is transitory" baseline. [LLM-E]

---

### RV Implications — sq6

**Key trades implied by the structural analysis:**

**1. Long 2s10s steepener (curve steepener):** IF the Fed eventually cuts (even once) in 2026 AND the long end stays elevated on fiscal/supply premium, THEN 2s10s steepens further toward 70-100bps. Entry at +43bps. Carry is negative (pay 2y at 4.13%, receive 10y at 4.56% — roughly equal carry on DV01-neutral). Risk: no Fed cuts + inflation spike steepens from wrong end. [LLM-E, RAW-WIKI Fixed_Income_Relative_Value_Framework]

**2. 20y butterfly richening opportunity:** 20y cheap to 10s/30s fly by estimated ~10-15bps [LLM-E]. Structural buyers (insurance, pension) have natural appetite for 20y duration. IF issuance pace holds and dealer digestion improves, THEN 20y cheaps unwound → long 20y, short 10y/30y DV01-neutral. [LLM-E]

**3. TIPS breakeven widener at 5y:** IF tariff inflation proves more persistent than FOMC baseline (probability medium), THEN 5y TIPS breakeven rises from ~2.3% toward 2.5-2.7% → 5y nominal yield either stays flat (real yield compresses) or rises further. Long 5y TIPS vs short nominal 5y expresses this view. [LLM-E]

**4. Receiver swaption on 2y (rate path optionality):** 2y at 4.13% is 40-90bps above where it would clear IF the FOMC cuts 2-3 times in H2 2026. IF inflation breaks lower in Q2-Q3 2026 per staff baseline, THEN 2y rallies 40-60bps. Receive fixed on 2y or buy 2y Treasury outright (positive carry at 4.13% if funded above 3.50% = 63bps positive carry on 1yr horizon) [LLM-E].

**TRUE_GAP for RV implementation:** Exact carry/roll-down numbers, swap spread levels, and specific DV01-neutral ratios are not calculable without intraday data and OIS curve details.
