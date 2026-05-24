---
TO: Internal
FROM: Wiki-Agentic Research
DATE: 2026-05-24
RE: Fed Operating Framework 2026 — Rate Path, QT Halt, Balance Sheet, and Reserve Adequacy
CLASSIFICATION: Internal
AUDIT: approved (fed_framework_2026, 2026-05-24)
---

## Executive Summary

The Fed is holding rates at 3.50–3.75% in a restrictive stance anchored by above-target inflation driven by tariff effects. Quantitative tightening ended December 1, 2025 after draining $2.2 trillion from the balance sheet. Reserve Management Purchases (RMPs) — T-bill purchases at $10 billion/month as of mid-May — now replace QT as the active balance sheet tool, maintaining reserves at $3.13 trillion. Reserves are ample but near the lower bound of the comfortable range; the margin is thinner than in 2022–2024. The headline SOFR-IORB spread (~0bps) suggests no stress, but FHLB segmentation and FBO quarter-end dynamics mean the spread understates tail risk. The single dominant policy constraint is inflation: until core PCE trends durably below 3.0%, the FOMC will not cut, regardless of balance sheet conditions.

---

## I. Rate Framework — Restrictive Hold with Easing Bias Removed

The FOMC held the federal funds rate at **3.50–3.75%** at the April 28–29, 2026 meeting [WEB-2026-05-24]. One member dissented in favor of a 25bp cut. The Committee removed its prior easing bias from the statement language — a deliberate signal that near-term cuts are not the path of least resistance.

The March 2026 dot plot set the median year-end 2026 projection at **3.4%**, implying one 25bp cut for the full year [WEB-2026-05-24]. But the distribution is evenly split: seven of nineteen participants projected no cut in 2026 (3.625%), seven projected one cut (3.375%), and five projected two or more cuts. This near-50/50 divide reflects a genuine disagreement about whether the current inflation overshoot is structural or transitory.

Core PCE reached an estimated **3.2%** in March 2026, up from 3.0% in February. Total PCE hit approximately 3.5%, pushed by energy prices and tariff pass-through [WEB-2026-05-24]. The FOMC's staff baseline calls for inflation to peak in Q2 2026 as tariff effects dissipate, then fall toward 2.0% by end-2027. The cut threshold is clear: core PCE must trend durably below 2.5% over two or more consecutive months before the Committee will move.

The floor system operates normally. IORB sits at approximately 3.65% (upper bound minus 10bps) and the ON RRP rate at 3.50% (lower bound). SOFR ranged 3.50–3.64% in May, averaging approximately 3.58% — a SOFR-IORB spread of roughly -7 to 0bps, consistent with ample reserve conditions [WEB-2026-05-24].

## II. Balance Sheet — QT Ended; RMPs Now the Active Instrument

QT2 ran from June 2022 to November 2025, reducing the Fed's securities portfolio by **$2.2 trillion** — $1.6 trillion in Treasuries and $600 billion in agency MBS [WEB-2026-05-24]. The FOMC announced the halt on October 29, 2025, effective December 1. All principal payments from Treasury and agency holdings are now reinvested in T-bills.

As of May 20, 2026, the balance sheet stands at **$6.71 trillion** [WEB-2026-05-24]:

| Item | Amount |
|---|---|
| U.S. Treasuries | $4.46T |
| Agency MBS | $1.98T |
| Reserve balances | $3.13T |
| ON RRP | $0.32T |
| Treasury General Account | $0.78T |

**Reserve Management Purchases** began mid-December 2025 at $40 billion/month, front-loaded ahead of the April tax-season TGA surge. The pace tapered to $25 billion in mid-April and to **$10 billion** for mid-May through mid-June [WEB-2026-05-24]. RMPs purchase only T-bills and are explicitly not QE: they carry no rate-policy signal and do not target long-term yields. The tapering pace itself is the forward guidance — declining RMPs indicate the Fed judges reserves are approaching a sustainably ample level.

The MBS portfolio will continue declining slowly as prepayments are reinvested into T-bills. This structural shift shortens SOMA duration and aligns with the Warsh-Bessent Accord's intent of removing the Fed from credit allocation [RAW-WIKI Fed_Treasury_Accord_2026_Proposal], though the operational rationale is reserve management, not political accommodation.

## III. Reserve Plumbing — Ample but Near the Floor

The structural reserve floor rose from approximately $10 billion pre-GFC to roughly $3 trillion post-GFC, driven by three durable changes: RTGS Fedwire pre-funding requirements ($7.3 trillion settled daily), IORB remuneration removing the incentive to lend idle reserves, and LCR/SLR regulations stigmatizing daylight overdrafts [RAW-BOOK Duffie §I, RAW-WIKI Reserve_Floor_Payment_System_Demand]. This ratchet cannot be reversed without structural reforms — Fedwire LSM adoption, SRF destigmatization, or IORB tiering — none of which are scheduled for 2026.

At $3.13 trillion, reserves sit near the lower bound of the comfortable range. The Duffie (2026) estimate of the Lowest Comfortable Level of Reserves (LCLoR) is 10–13% of GDP, approximately **$2.8–3.6 trillion** at current size [RAW-BOOK Duffie Abstract]. This is why the Fed halted QT and launched RMPs: further passive drain would have consumed the remaining buffer within months.

**The SOFR-IORB spread is a necessary but not sufficient indicator of adequacy.** Three structural factors cause it to understate stress:

*FHLB arbitrage suppression.* FHLBs, ineligible for IORB, lend reserves into the federal funds market at EFFR slightly below IORB. Banks borrow at EFFR and deposit at IORB for the spread. This arbitrage pins EFFR below IORB and dampens SOFR even when specific dealer banks are short. EFFR does not rise until FHLB supply dries up — at which point scarcity is already binding. [RAW-WIKI Fhlb_Effr_Iorb_Arbitrage_Floor_Mechanism]

*FBO quarter-end compression.* Foreign banking organizations shed $200–400 billion in reserves at each quarter-end monitoring date, causing temporary SOFR spikes. In a tight reserve environment, a quarter-end event can be sufficient to push SOFR above IORB and trigger SRF activation or payment delay cascades. [RAW-BOOK Duffie §I.B]

*SOFR median obscures tail distribution.* SOFR is a volume-weighted median of overnight Treasury repo. With reserve distribution skewed toward non-dealer banks, the median can look benign while TGCR (tri-party repo, reflecting dealer bank conditions directly) is already elevated. Logan and Schulhofer-Wohl (2025) propose TGCR as the superior monitoring target for precisely this reason [RAW-WIKI Reserve_Floor_Payment_System_Demand].

**The ON RRP at $324 billion** is a seasonal artifact, not a stress signal [WEB-2026-05-24]. Tax-season TGA accumulation forced MMFs out of T-bills and into ON RRP temporarily. Once TGA normalizes in May–June, ON RRP should retrace toward $100–150 billion.

## IV. Interactions and Policy Tensions

**Rate policy and balance sheet policy are operationally independent.** The FOMC does not treat QT halts or RMP tapers as monetary easing; this framing has been explicit since the June 2024 QT taper. The two instruments pursue compatible goals on separate tracks: rates address inflation, balance sheet operations maintain the reserve floor.

**The tariff shock creates a dual bind.** Import price pass-through raises CPI/PCE — keeping the Fed on hold. But higher input costs compress corporate margins and slow capex, creating a growth headwind. If both persist simultaneously, the FOMC faces a constraint it cannot resolve with a single instrument: holding rates high suppresses demand but cannot reverse supply-driven price increases. The staff baseline assumes the tariff effect is transitory; if wrong, the 2026 dot plot median of 3.4% will not be reached.

**The Warsh-Bessent Accord** proposal — returning debt maturity control to the Treasury, exiting MBS, and narrowing the Fed's mandate — points directionally toward a smaller balance sheet [RAW-WIKI Fed_Treasury_Accord_2026_Proposal]. The Fed's MBS-to-T-bills reinvestment is a step consistent with this direction. However, reducing the balance sheet below $6 trillion without enabling infrastructure (Fedwire LSM, destigmatized SRF) risks a reserve floor breach. The operational constraint, not political will, is the binding limit on balance sheet reduction in 2026.

## V. Risks

**Inflation persistence (high probability).** Seven of nineteen FOMC participants already project no 2026 cut. If core PCE does not fall below 3.0% in Q2–Q3, the September dot plot will shift upward and market pricing for 2026 cuts will collapse entirely. Rate premium on duration assets widens.

**TGA surge triggering repo stress (medium probability).** An unexpected TGA increase of $200–300 billion within 2–4 weeks — possible if debt ceiling negotiations delay Treasury spending — could push reserves temporarily below $2.8 trillion. SOFR-IORB would widen above +10bps; Fed would need to increase RMPs or activate TOMOs. A quarter-end FBO event coinciding with an elevated TGA poses the highest-probability acute stress scenario.

**Premature RMP halt under political pressure (low-medium probability).** If the Warsh-Bessent Accord creates pressure to demonstrate balance sheet restraint, the Fed could stop RMPs before ON RRP is sufficiently depleted. Without the organic buffer, reserve drain accelerates and the LCLoR is breached faster. The operational case for continuing RMPs is strong; the political case for pausing them is asymmetric and visible.

**FX swap line activation (low probability).** A geopolitical shock triggering large-scale USD demand would expand the balance sheet involuntarily through swap lines. This lies outside the FOMC's domestic framework and cannot be pre-managed through QT or RMP calibration.

---

## Sources

**Fresh data (fetched 2026-05-24):**
- Federal Reserve H.4.1, May 21, 2026: [federalreserve.gov/releases/h41/current/](https://www.federalreserve.gov/releases/h41/current/)
- FOMC Summary of Economic Projections, March 18, 2026: [federalreserve.gov/monetarypolicy/fomcprojtabl20260318.htm](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260318.htm)
- FOMC Minutes, April 28–29, 2026: [federalreserve.gov/monetarypolicy/fomcminutes20260429.htm](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm)
- NY Fed Teller Window — Implementation of Reserve Management Purchases, March 31, 2026: [tellerwindow.newyorkfed.org](https://tellerwindow.newyorkfed.org/2026/03/31/the-implementation-of-reserve-management-purchases-to-maintain-ample-reserves/)
- SOFR historical rates, May 2026: [global-rates.com](https://www.global-rates.com/en/interest-rates/sofr/historical/2026/)

**Wiki nodes (structural/mechanistic):**
- [[Fed_Ample_Reserves_Range_Floor_Framework]] — dual-floor system mechanics
- [[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]] — QT transmission mechanism
- [[Fed_QT_2022_Balance_Sheet_Runoff_Policy]] — QT2 timeline and ON RRP buffer dynamic
- [[Fed_Overnight_Reverse_Repo_On_Rrp]] — ON RRP shock absorber role
- [[Reserve_Floor_Payment_System_Demand]] — Duffie (2026) RTGS reserve floor, LCLoR, TGCR
- [[Fhlb_Effr_Iorb_Arbitrage_Floor_Mechanism]] — FHLB arbitrage and SOFR-IORB signal limitation
- [[Fed_Treasury_Accord_2026_Proposal]] — Warsh-Bessent framework
- [[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]] — coupon issuance and reserve impact

**Raw sources:**
- Duffie, D. (2026). *Payments Liquidity and the Federal Reserve Balance Sheet*. BPEA. `02_sources/books/duffie_bpea_payments_2026/`
- Conks — Fed's Policies and Facilities. `02_sources/books/conks/`
