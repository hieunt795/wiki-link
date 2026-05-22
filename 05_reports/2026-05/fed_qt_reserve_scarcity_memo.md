---
report_id: rpt_qt_reserve_scarcity_001
topic_slug: fed_qt_reserve_scarcity
title: "Fed QT and Reserve Scarcity: Plumbing, Signals, and Policy Implications"
style: research_memo
date: 2026-05-20
audit_approved: true
audit_log: 04_research/fed_qt_reserve_scarcity/audit_log.json
confidence_floor: 3
---

**TO:** Internal Research  
**FROM:** Wiki-Agentic  
**DATE:** 2026-05-20  
**RE:** Fed QT and Reserve Scarcity — Plumbing, Signals, and Policy Implications

---

## Executive Summary

The Fed's Quantitative Tightening has entered a structurally different phase. The ON RRP buffer — which absorbed ~$2.5T of reserve drain through 2022-2024 — is now effectively exhausted. Each dollar of additional QT now reduces bank reserves more directly, with a structural floor near $3T driven by post-GFC payment system changes. Three actionable conclusions follow: (1) monitor SOFR-IORB spread daily as the primary scarcity signal; (2) distinguish quarter-end noise from structural elevation; (3) the Fed's near-term toolkit is TOMOs + pace reduction, with RMPs as the backstop.

---

## 1. Two Phases of QT: Buffered Then Direct

**Phase 1 — Buffered drain (2022–2024)**

QT began June 2022 at a $60B/month redemption cap. The key dynamic: as Fed assets shrank, the ON RRP facility drained in parallel, releasing pre-existing liquidity into the banking system.

```
ΔReserves = ΔFed_Assets − ΔTGA − ΔON_RRP − ΔCurrency
```

With ON RRP falling ~$2.5T from its $2.6T peak, reserves held broadly stable near $3.3T even as the balance sheet shrank significantly. QT was real in accounting terms; its reserve effect was muted. [RAW-BOOK QT node; RAW-BOOK Reserve Floor node]

**Phase 2 — Direct drain (2025–)**

ON RRP fell below $100B by late 2024. The buffer is gone. From this point, each $100B of QT reduces bank reserves by approximately $80-100B net of TGA and currency effects. [LLM based on reserve supply identity]

The TGA remains a wildcard: debt ceiling mechanics and fiscal spending patterns create reserve volatility independent of QT. But the structural shock absorber has been removed.

---

## 2. The $3T Floor: Why Pre-GFC Experience Is Irrelevant

The pre-GFC federal funds system ran on ~$10B in system reserves. Three structural changes raised the effective minimum to ~$3T: [RAW-BOOK Reserve Floor node — Duffie BPEA 2026]

**Daylight overdraft stigma.** Post-GFC intraday liquidity regulations require GSIBs to self-fund opening reserve balances. Pre-GFC, large banks used $120B/day in Fed daylight overdrafts; post-GFC, under $5B. Each bank must pre-fund its own payment flow.

**IORB removes lending incentive.** When reserves earn the market rate, they become an investment asset rather than a hot potato to lend away. JPMorgan's reserve holdings fell from $409B (end-2023) to ~$63B (Q3-2025) as the bank rotated into higher-yielding Treasuries — a rational portfolio decision that concentrates reserve scarcity risk at settlement time.

**Frictional interbank market.** FDIC insurance fees (up to 55bps combined) make interbank reserve redistribution costly. Reserves no longer flow freely to where they are needed.

Together these create a **ratchet**: periods of abundant reserves allow banks to run lean liquidity operations. When reserves tighten, the system cannot revert to pre-GFC efficiency. The Fed must treat ~$3T as the structural floor, not a historical anomaly. [RAW-BOOK Reserve Floor node — citing Acharya-Rajan 2022]

---

## 3. The Real-Time Monitoring Dashboard

Reserve scarcity does not arrive as a cliff — it manifests progressively:

| Signal | Source | Normal | Approaching Floor | Stressed |
|--------|--------|--------|-------------------|---------|
| SOFR-IORB spread | FRED daily | −5 to 0bps | 10-15bps persistent | >25bps |
| ON RRP balance | FRED RRPONTSYD | — | <$100B (buffer gone) | <$25B |
| SRF usage | NY Fed daily | Zero | Any non-trivial | Large |
| Payment delays | Fed internal | Low | Rising | Record high |

**Critical distinction — noise vs. signal:**  
Quarter-end SOFR spikes are mechanical: foreign banking organizations compress balance sheets for regulatory reporting, draining $200-400B in reserves for 1-2 days before reversing. These are noise. A SOFR-IORB spread sustained above 15bps for a week or more is signal. [RAW-BOOK Reserve Floor node]

**September 2019 calibration:**  
System reserves at ~$1.4T; SOFR spiked IORB + 315bps; interdealer rates briefly 1000bps above IORB; payment delays at 10-year high. Critically: this was not a simple aggregate shortage — it was a *distribution* failure. JPMorgan held reserves but withheld them due to LCR/regulatory constraints. [RAW-BOOK Reserve Floor node]

**Implication:** Monitoring aggregate reserve levels is necessary but not sufficient. Watch *distribution* signals: SOFR-IORB spread reflects what specific dealers face at the margin, not system averages.

---

## 4. SLR: The Hidden Amplifier

Dealer Supplementary Leverage Ratio constraints interact with reserve scarcity non-linearly:

```
Reserves approach floor → Dealers approach SLR limit
    → Cannot expand balance sheet to intermediate repo
    → Refuse to lend reserves even when available
    → SOFR spike appears even with "ample" aggregate reserves
```

[RAW-BOOK SLR LCR node; RAW-BOOK Reserve Floor node]

The 2020-21 temporary SLR exemption for Treasuries materially improved dealer intermediation capacity. Its expiration tightened structural constraints. Basel III Endgame SLR rules represent a continuing headwind — dealer capacity to absorb Treasury supply and intermediate repo is a function of regulatory capital as much as aggregate reserve levels.

---

## 5. Policy Toolkit

**Immediate (days-weeks):**

*Slow or stop QT pace.* The primary lever and first-response tool. Feb 2024 demonstrated the Fed's willingness to reduce pace preemptively — before reaching scarce territory — to avoid a 2019 repeat. [RAW-BOOK QT node]

*TOMOs.* Temporary repo operations inject reserves without permanently expanding the balance sheet. Duffie (BPEA 2026) recommends more systematic TOMO use to smooth period-end volatility, reducing the required permanent reserve buffer. [RAW-BOOK Reserve Floor node]

**Near-term (weeks-months):**

*Reserve Management Purchases (RMPs).* T-bill purchases permanently replenish reserves without targeting long-term yields — no "stealth QE" signal. Precedent: post-2019 repocalypse at ~$60B/month.

**Structural (multi-year):**

*Fedwire LSM.* A liquidity savings mechanism for Fedwire — standard in BOE, ECB, BOC, BOJ systems — would offset outgoing payments against incoming flows before settlement, reducing opening balance requirements. Duffie estimates this could lower the structural reserve floor by hundreds of billions. [RAW-BOOK Reserve Floor node; LLM-E for magnitude]

*Destigmatized SRF.* If the Standing Repo Facility is actively used as a routine liquidity tool (not an emergency backstop), banks would need to hold fewer precautionary reserves. Requires regulatory clarity and cultural shift at GSIBs.

---

## 6. Key Conclusions

1. **The QT buffer phase is over.** ON RRP depletion means direct reserve drain from here. Remaining runway before approaching the floor is limited — estimated $200-400B at current pace. [LLM-E]

2. **$3T is the structural floor, not a relic.** Post-GFC payment system changes are permanent absent structural reform (LSM, SRF destigmatization). The Fed cannot recalibrate toward pre-GFC norms without enabling infrastructure.

3. **Distribution trumps aggregates.** Sep 2019 proved that aggregate reserve levels can appear ample while localized dealer constraints cause market stress. Track SOFR-IORB, not just H.4.1 totals.

4. **SLR amplifies scarcity.** As reserves approach the floor, dealer intermediation capacity becomes a binding constraint independent of aggregate levels. Basel III Endgame SLR rules work against smooth repo intermediation at the margin.

5. **Monitoring threshold:** SOFR-IORB spread sustained above 15bps for 5+ business days = Fed response warranted. Quarter-end spikes are noise.

---

## Limitations

- **No current data.** This analysis is structural — actual SOFR-IORB spread, current reserve level (H.4.1), and ON RRP balance are not included. Verify current levels against FRED before trading or operational decisions.
- **TRUE_GAP — SRF mechanics.** No source in the wiki covers SRF operational mechanics in detail (eligibility, rate structure, stigma quantification). Duffie BPEA 2026 references SRF but does not provide full mechanics.
- **Dealer SLR headroom unquantified.** Current regulatory capital positions of primary dealers are not in the wiki. This analysis treats SLR as a structural constraint without current headroom estimates.

---

## Source Index

| Node | Type | Confidence | Primary Source |
|------|------|-----------|----------------|
| `[[Reserve_Floor_Payment_System_Demand]]` | mechanism | ★★★☆☆ | Duffie BPEA 2026 |
| `[[Quantitative_Tightening_QT_Balance_Sheet_Runoff]]` | mechanism | ★★★☆☆ | Conks — Fed Policies |
| `[[Fed_Overnight_Reverse_Repo_ON_RRP]]` | mechanism | ★★★☆☆ | Conks — Shadow Banking |
| `[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]` | mechanism | ★★★☆☆ | Conks — Liquidity |
| `[[Repo_Market_Mechanics_Triparty_Bilateral]]` | mechanism | ★★★☆☆ | Conks — Repo |
