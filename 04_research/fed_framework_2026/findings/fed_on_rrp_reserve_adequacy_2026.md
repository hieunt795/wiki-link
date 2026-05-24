---
title: "Fed ON RRP Drain and Reserve Adequacy 2026"
topic: fed_framework_2026
sub_question: sq3, sq4, sq6
status: stable
confidence: 2
date_created: 2026-05-24
sources:
  - type: web_fresh
    url: "https://www.federalreserve.gov/releases/h41/current/"
    fetched: 2026-05-24
  - type: web_fresh
    url: "https://tellerwindow.newyorkfed.org/2026/03/31/the-implementation-of-reserve-management-purchases-to-maintain-ample-reserves/"
    fetched: 2026-05-24
  - type: wiki
    node: "[[Fed_Overnight_Reverse_Repo_On_Rrp]]"
  - type: wiki
    node: "[[Reserve_Floor_Payment_System_Demand]]"
  - type: wiki
    node: "[[Ample_Reserves_Buffer_Sizing_Tga_Volatility]]"
---

## ON RRP: From $2.4T to $324B

**Current ON RRP balance (week ending May 20, 2026):** $323,745M (~**$324B**) [WEB-2026-05-24]

**Historical trajectory:**
- Peak: ~$2.4T (December 2022)
- Jan 2024: ~$600B
- Jan 2025: ~$100-150B (estimated)
- May 2026: ~$324B (elevated slightly by tax-season TGA dynamics)

**Why is ON RRP still $324B (not zero)?**
- Tax-season TGA peak (April) forces Treasury to accumulate large TGA balance → drains bank reserves → MMFs face fewer T-bill yields; shift back to ON RRP temporarily
- Once TGA normalizes (May-June), ON RRP expected to decline again
- This is the seasonal cycle: tax months → ON RRP bumps; TGA release months → ON RRP drains

**Structural floor for ON RRP:** ~$50-100B expected minimum, driven by operational settlement needs of MMFs and GSEs that cannot use IORB. [LLM-E]

## Reserve Adequacy Assessment

**Current reserves:** $3,129,562M ($3.13T) as of May 20, 2026 [WEB-2026-05-24]

**SOFR signal (May 2026):**
- SOFR range: 3.50–3.64%; average ~3.58% [WEB-2026-05-24]
- IORB (estimated): ~3.65%
- **SOFR-IORB spread: approximately -7 to 0 bps** → reserves AMPLE [LLM-E inference from rate structure]

**Diagnostic framework (from [[Reserve_Floor_Payment_System_Demand]]):**

| Signal | Current State | Assessment |
|---|---|---|
| SOFR-IORB spread | ~-7 to 0 bps | Normal — ample |
| ON RRP balance | $324B | Healthy buffer remains |
| Reserve level | $3.13T | Above estimated LCLoR floor |
| TGA | $781B (elevated) | Tax-season peak; will normalize |
| RMP pace | $10B/month | Still ongoing = Fed sees adequate but not excessive |
| Payment delays | Not elevated (no reports) | No stress signal |

**Conclusion:** Reserves are **ample**, not scarce. The RMP program was launched precisely to prevent the transition from ample → scarce. The taper of RMPs from $40B → $10B/month suggests the Fed sees the current $3.13T reserve level as appropriate.

## TGA / Treasury Interaction (sq6)

**Current TGA:** $781B (May 20, 2026) — **elevated**, consistent with post-tax-season peak [WEB-2026-05-24]

**TGA mechanics:**
- Tax payments (April) → TGA surges → bank reserves fall → ON RRP rises as buffer
- Treasury spending / debt issuance (ongoing) → TGA normalizes → reserves recover

**Bill-vs-coupon issuance mix:**
- Treasury's decision to issue more bills vs coupons affects where the cash lands
- Bills → absorbed primarily by MMFs → ON RRP may fluctuate
- Coupons → bought by duration-investors from bank deposits → reserves drain more directly

**Debt ceiling risk:** No active debt ceiling constraint visible in current data. TGA at $781B suggests normal operating conditions.

**RMPs and TGA:** The Fed calibrated the $40B/month RMP pace to pre-position reserves ahead of the April TGA peak. The taper to $10B signals the TGA peak has passed.

## Ample Reserve Floor — How Low Can Reserves Go?

Based on [[Reserve_Floor_Payment_System_Demand]] (Duffie BPEA 2026):

**LCLoR estimate:** ~10-13% of nominal GDP ≈ **$2.8–3.6T** at current GDP

At $3.13T, reserves are near the **lower end** of the ample range. This explains:
1. Why Fed halted QT (December 2025)
2. Why Fed launched RMPs (prevent further decline)
3. Why RMP pace is still $10B/month despite reserves seeming sufficient

**Risk scenario:** If TGA were to drain rapidly (e.g., debt ceiling suspension → Treasury spending surge), reserves could spike temporarily above $3.5T then fall back — no immediate scarcity risk, but the margin above LCLoR is thinner than 2022-2024.
