# Liquidity Stress Testing — Quy trình & Thiết kế trong ILAAP

**Date:** 2026-05-27
**Sources:**
- Choudhry Principles of Banking (Ch.20, p.11799–11921)
- Elkenbracht-Huizing Handbook ALM (Ch.13, p.3876–3892)
- bcbs144 Principle 10 (existing wiki node)

---

## Stress Test là gì trong ILAAP context

Stress test ≠ tính LCR. Đây là quá trình:

```
INVENTORY (balance sheet, maturity profile, off-BS)
    ↓ apply
STRESS SCENARIOS (idiosyncratic / market / combined)
    ↓ với
BEHAVIOURAL ASSUMPTIONS (tỷ lệ rút tiền, rollover, draw-down)
    ↓ ra
OUTPUT: Cash-flow survival period + liquidity position theo từng time bucket
    ↓ review bởi
ALCO + BOARD → action nếu survival period < risk appetite
```

[RAW-BOOK Choudhry_Principles_of_Banking p.11803–11848]

---

## 3 Scenario Types (ILAAP standard)

### A. Market Disruption (Systemic)
- Markets severely disrupted nhưng bank không bị stigma riêng
- Retail: không stress, hoặc có thể có thêm inflow khi bank được thấy là ổn
- Wholesale: precautionary — không renew maturities
- Mortgage redemptions/remortgage: giảm (economic activity giảm)
- Nguồn trám: HQLA; bank tương đối an toàn nếu không có idiosyncratic element

### B. Idiosyncratic Stress (Firm-specific)
- Bank bị ảnh hưởng trực tiếp: prudential/reputational issue
- Retail withdrawal: weeks 1–2: ~2.8%/ngày (high-risk accounts), ~0.75%/ngày (relationship)
  Sau đó ổn định vì deposit guarantee scheme được hiểu rõ
- Wholesale: 100% không renew on maturity
- Cash management term deposits: 100% rút khi đáo hạn
- Branch-based retail term: 25% rút khi đáo hạn
- Nguồn trám: CB facilities (Discount Window, OMO) + HQLA

### C. Combined (Worst Case)
- Market disruption + idiosyncratic cùng lúc
- Retail withdrawal: ~half of idiosyncratic rate
- Wholesale: không renew
- Remortgage activity: giảm
- Nguồn trám: cả HQLA + CB + management actions phối hợp

[RAW-BOOK Choudhry_Principles_of_Banking p.11886–11888; Elkenbracht_Huizing_Handbook_ALM p.3880]

---

## Behavioural Assumptions — Các rủi ro phải model

Choudhry liệt kê 14 assumption categories:

```
FUNDING SIDE:
  ① Retail funding risk (tỷ lệ rút theo cohort, account type)
  ② Wholesale secured + unsecured funding risk (rollover rate)
  ③ Correlation + concentration of funding (diversification fails under stress)
  ④ Additional contingent off-balance sheet exposures (committed lines drawn)
  ⑤ Funding tenors (shortening under stress)

INTRADAY:
  ⑥ Intraday liquidity risk (timing của payments)

CREDIT QUALITY:
  ⑦ Deterioration in firm's credit rating (collateral calls, triggers)

FX + CROSS-BORDER:
  ⑧ FX convertibility + access to FX markets
  ⑨ Ability to transfer liquidity across entities, sectors, countries

BALANCE SHEET DYNAMICS:
  ⑩ Future balance sheet growth
  ⑪ Impact on reputation and franchise value

ASSET SIDE:
  ⑫ Marketable and non-marketable asset risk (haircuts, liquidity)
  ⑬ Internalisation risk (customer short-position close-out → outflows)

MACRO:
  ⑭ Impact on economic activity (mortgage redemption rates change)
[RAW-BOOK Choudhry_Principles_of_Banking p.11821–11834]
```

---

## Output: Cash-Flow Survival Period

Metric chính của stress test output:

```
"How many days can the bank's liquidity sources
 (liquid assets + cash inflows + contingent facilities)
 offset assumed outflows under the stress scenario?"
```

**Ví dụ thực tế (UK regional bank, Choudhry):**

| Resource | O/N | 1W | 1M | 2M | 3M | 6M | 1Y |
|---|---|---|---|---|---|---|---|
| BoE Reserve | 215.9 | 177.8 | 112.3 | 81.1 | 0.1 | 150.8 | 259.1 |
| L1 HQLA securities | 121 | 121 | 121 | 0 | 0 | 50 | 50 |
| Pre-action total | 375.7 | 299.1 | 233.3 | 81.1 | 0.1 | 200.8 | 309.1 |
| Post-action total | 375.7 | 299.1 | 233.3 | 175.4 | 180.2 | 200.9 | -124 |

Management Actions trong ví dụ:
- Action A: Retail term deposit issuance £3m/tháng từ tháng 3–6
- Action B: BoE Discount Window £10m tháng 1–2 (sau 92 ngày OLAR đạt được)
- Ngừng cho vay mới → giảm advances từ tháng 3 onward

[RAW-BOOK Choudhry_Principles_of_Banking p.11858–11919]

---

## Survival Horizon vs OLAR (UK PRA framework)

```
OLAR = Overall Liquidity Adequacy Rule
"Bank must maintain sufficient liquidity reserves to withstand a stress event
 in line with its own stated appetite for liquidity risk."

Bank trong ví dụ: target survival ≥ 92 ngày
→ Là user-specified (không phải regulatory minimum cố định)
→ Reflect risk appetite + escalation speed + recovery action feasibility

Nếu stress test kết quả < risk appetite:
  → Corrective action required:
    ① Reduce exposures to certain products/markets
    ② Reduce limits on contractual outflows
    ③ Review CFP strategies
[RAW-BOOK Choudhry_Principles_of_Banking p.11842–11852]
```

---

## Thiết kế Survival Period — 2 Approaches

```
"Run-down of bank" view:
  → Assume contractual inflows ARE received (loans repaid as scheduled)
  → Bank closed to new business
  → Result: HIGHER inflows, longer survival period
  → Use case: measure floor (worst case exit scenario)

"Going concern" view:
  → Assume SOME loan rollover (bank still making new loans)
  → Result: LOWER inflows, shorter survival period
  → Use case: realistic ongoing operations scenario

Best practice: analyse BOTH and set risk appetite accordingly
Higher uncertainty in client behaviour → set HIGHER target survival period
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3889–3890]
```

---

## 3 Internal Metrics từ Stress Test (Elkenbracht-Huizing)

| Metric | Đo lường | Risk appetite set bởi |
|---|---|---|
| **Time-to-LCR-breach** | Thời gian đến khi LCR < 100% | Data lag + escalation speed + investor sensitivity |
| **Time-to-central-bank** | Thời gian sống bằng market-liquid assets (chưa dùng CB) | ≥ 30 ngày minimum; internal target cao hơn |
| **Combined survival period** | Thời gian dùng HQLA + CB-eligible buffer | Uncertainty of assumptions + management action speed |

**Lưu ý quan trọng:**
- LCR ≥ 100% KHÔNG đảm bảo survive 30 ngày (có intra-period mismatches)
- Calibration áp lực peer comparison → bias về inaccurate thay vì conservative

---

## ILAAP Stress Test vs LCR Stress Test — Khác biệt then chốt

| Dimension | LCR Stress | ILAAP Internal Stress |
|---|---|---|
| Scenarios | Cố định, regulatory-defined | Bank-generated, focus on own vulnerabilities |
| Horizon | 30 ngày | 30 ngày → 1 năm+ |
| Assets | Chỉ tính HQLA | HQLA + contingent CB-eligible buffer |
| Assumptions | Standardized run-off rates | Bank-specific behavioral data |
| Public | Yes (Pillar 3) | No — enables more severe scenarios |
| Adaptation | Cố định | Adapts to business model changes |
| Review | Quarterly | Continuous + annual formal |

---

## Link với CFP

```
Stress test output → DRIVES CFP design:

Câu hỏi stress test trả lời → CFP phải có sẵn:
  Q: Tại bucket 3M, outflow vượt HQLA bao nhiêu?
  A: CFP phải có sources trám khoản đó với lead time < 3M

  Q: Nếu combined scenario xảy ra, bao nhiêu ngày có để act?
  A: CFP phải có escalation procedures nhanh hơn số ngày đó

"The stress test results form the basis for the CFP — if projected funding
deficits exceed risk tolerance, management MUST either adjust the liquidity
position OR bolster the CFP." [RAW-BOOK bcbs144 para 109]
```

---

*Related nodes:*
- `[[Ilaap_Internal_Liquidity_Adequacy_Assessment_Framework]]`
- `[[Bcbs_Liquidity_Stress_Testing_Principle_10]]`
- `[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]`
