# ILAAP — Internal Liquidity Adequacy Assessment Process

**Date:** 2026-05-27
**Sources:**
- Elkenbracht-Huizing Handbook ALM (Ch.13, lines 3853–3902) — Patrick de Neef (DNB/ECB SREP author)
- Choudhry Principles of Banking (Ch.20, lines 11799–11981)
- bcbs144 (BCBS 17 Principles, 2008) — ILAAP's conceptual foundation
- EBA/GL/2016/10 — Guidelines on ICAAP and ILAAP information for SREP
- ECB Guide to ILAAP (November 2018)

---

## Định nghĩa và vị trí

ILAAP = **bộ quy trình nội bộ toàn diện** để một ngân hàng tự đánh giá mức độ đủ thanh khoản của mình.

```
LCR / NSFR          Regulatory minimums (fixed, public)
    ↓ necessary but not sufficient
ILAAP               Internal, adaptive, comprehensive process (private, bank-specific)
    ↓ results submitted to supervisor
SREP / L-SREP       Supervisor challenges ILAAP → issues Individual Liquidity Guidance
```

**Nguồn gốc:**
- Term "ILAAP" không xuất hiện trong các văn bản BCBS — đây là construct của EBA/DNB (2012)
- Được xây dựng trực tiếp từ BCBS 17 Principles (bcbs144), đặc biệt Principles 10–12
- ECB chuẩn hóa qua SSM từ 2014, hướng dẫn chính thức 11/2018
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3855]

---

## Tại sao ILAAP quan trọng hơn chỉ LCR + NSFR?

Hai lý do cốt lõi từ góc nhìn giám sát (DNB):

**1. LCR/NSFR không thích ứng được:**
- Phải mất ~10 năm để đưa vào làm minimum requirement
- Không thể recalibrate nhanh khi balance sheet ngân hàng thay đổi
- Cùng một metric không thể phù hợp tất cả ngân hàng ở mọi quốc gia

**2. Giám sát viên không thể tự đưa ra assumptions:**
- Bank hiểu business model, client behaviour, market của mình tốt hơn supervisor
- ILAAP buộc bank phải chọn, calibrate, và justify các assumptions nội bộ
- Supervisor chỉ challenge — không tự quyết định

**3. ILAAP là quy trình đầy đủ, không chỉ metric:**
```
ILAAP bao gồm:
  ① LCR, NSFR (regulatory metrics — foundation)
  ② Internal stress tests → survival periods, time-to-central-bank
  ③ Risk appetite limits + escalation procedures
  ④ Funding strategy + CFP
  ⑤ Contingency liquidity buffer (CB-eligible, không phải HQLA)
  ⑥ Liquidity adequacy statement (board-approved conclusion)
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3869]
```

---

## Cấu trúc quy trình ILAAP (best practice từ Elkenbracht-Huizing)

```
BƯỚC 1: NHẬN DIỆN RỦI RO
  Input: business model, client types, markets, regions, products
  Output: danh sách risk drivers → chọn metrics phù hợp

BƯỚC 2: ĐO LƯỜNG
  → Calibrate tools: LCR, NSFR, survival period, time-to-CB...
  → Quality assurance: validate models + assumptions + audits

BƯỚC 3: SET RISK APPETITE
  → Limits cho từng metric, từng scenario
  → Lưu ý: appetite ≠ nhau cho từng scenario type:
    (breach LCR do market disruption = xấu hơn breach do combined shock)

BƯỚC 4: REPORTING & ESCALATION
  → Internal reporting đủ granular: entity, currency, actual vs limit
  → Escalation procedures khi limits bị đe dọa

BƯỚC 5: BOARD DECISION
  → Board ra Liquidity Adequacy Statement
  → Board quyết định action nếu liquidity position không đạt mức mong muốn

BƯỚC 6: CFP / RECOVERY LINK
  → Liquidity contingency plan (CFP) phải consistent với recovery measures
  → Policies phải clarify: actions nào đã được thực hiện TRƯỚC KHI recovery triggers
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3902]
```

---

## Stress Test trong ILAAP: 3 Scenarios bắt buộc

| Scenario | Mô tả | Retail impact | Wholesale |
|---|---|---|---|
| **Market disruption** | Systemic — không phải idiosyncratic với bank | Không hoặc nhỏ | Không renew |
| **Idiosyncratic** | Chỉ bank bị ảnh hưởng (downgrade, reputational) | Significant withdrawal | Không renew |
| **Combined** | Cả hai đồng thời | Half idiosyncratic rate | Không renew |

[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3880–3882; Choudhry_Principles_of_Banking p.11886–11888]

**3 Metrics cốt lõi từ stress test:**

```
① Time-to-LCR-breach:
   Đo thời gian trước khi LCR < 100% khi đang trong stress
   Kết hợp: khoảng cách tuyệt đối + maturity profile ngắn hạn của balance sheet
   Risk appetite phải set dựa trên: data lag + escalation speed + investor sensitivity

② Time-to-central-bank:
   Đo thời gian sống sót chỉ dựa trên market-liquid assets (không dùng CB)
   Minimum: 30 ngày; internal target thường cao hơn đáng kể
   Note: LCR ≥ 100% KHÔNG đảm bảo sống sót 30 ngày (intra-period mismatches)

③ Combined survival period:
   Đo thời gian sống sót dùng cả HQLA + contingent liquidity buffer (CB-eligible non-HQLA)
   Metric toàn diện nhất — phản ánh thực tế management actions cần thực hiện
   Choice: "run-down" (assume contractual inflows) vs "going concern" (assume some rollover)
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3886–3890]
```

---

## Contingent Liquidity Buffer — Tầng ngoài HQLA

```
Cấu trúc thanh khoản:
  Layer 1: LCR HQLA        (market liquid, tính vào LCR)
  Layer 2: CB-eligible assets không đủ điều kiện HQLA
           → repo với central bank trong stress
           → không tính LCR nhưng có thể truy cập CB repo/ELA
  Layer 3: Central bank extraordinary facilities (LOLR, ELA)
           → discretionary, không đảm bảo
           → risk appetite: tăng theo thời gian kéo dài của disruption

"Banks should not just count on extraordinary measures being available overnight.
 While such measures are at CB discretion, likelihood increases the longer disruptions persevere."
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3892]
```

---

## Cấu trúc tài liệu ILAAP (Choudhry khuyến nghị)

```
1   Executive Summary
2   Business model, governance, strategy
3   Risk management framework
4   Forecast balance sheet
5   Funding profile and plan
6   Liquidity risk definition and ownership
7   Liquidity risk management framework
8   Liquidity risk appetite
9   ILAAP coverage
10  Stress scenarios
11  Stress testing results (all material liquidity and funding risks)
12  Pillar 2 Liquidity
13  Liquidity risk assessment
14  Liquidity risk mitigants + management actions
15  HQLA policy and portfolio
16  Other funding sources / mitigants
17  Reverse Stress Test
18  ILAAP challenge and internal approval process
19  Use of ILAAP in the firm

Appendices:
  A1: Reference to LCP (Liquidity Contingency Plan)
  A2: Stress testing assumptions
  A3: FTP Policy
  A4: Deposit pricing policy and model
[RAW-BOOK Choudhry_Principles_of_Banking Ch.20 p.11951–11974]
```

---

## L-SREP: Supervisor review của ILAAP

Sau khi ngân hàng submit ILAAP, supervisor thực hiện **Liquidity SREP (L-SREP)**:

```
L-SREP đánh giá:
  ① Framework: IT system để identify liquidity risk đủ chưa?
  ② Governance: framework quanh liquidity risk management đủ chặt chưa?
  ③ FTP: có transfer pricing mechanism cho liquidity phù hợp không?
  ④ LAB: controls trên liquid asset buffer đủ không?
  ⑤ Strategy: bank có define và communicate liquidity risk tolerance rõ không?
  ⑥ Limits: internal limit + control framework đủ toàn diện không?

Output: Individual Liquidity Guidance (ILG):
  → Quantity + quality của liquid assets: đủ chưa?
  → Funding profile: phù hợp không?
  → Qualitative arrangements cần cải thiện thêm
  → Guidance extends BEYOND LCR — cover risks LCR không capture
[RAW-BOOK Choudhry_Principles_of_Banking Ch.20 p.11940–11981]
```

---

## ILAAP vs ICAAP — Song song nhau

```
ICAAP (Internal Capital Adequacy Assessment Process)
  → Đánh giá mức độ đủ VỐN
  → Pillar 2 capital add-ons

ILAAP (Internal Liquidity Adequacy Assessment Process)
  → Đánh giá mức độ đủ THANH KHOẢN
  → Individual Liquidity Guidance

Cả hai phải:
  → Board-approved annually (hoặc khi business model thay đổi)
  → Proportionate to nature, scale, complexity
  → Linked to same Risk Appetite Framework
  → Not just compliance exercise — phải inform real decision-making
[RAW-BOOK De Gruyter ALM Best Practice p.469]
```

---

## Tiêu chuẩn thông tin lên Board (Best practice test)

Board phải có khả năng tự trả lời 7 câu hỏi này từ ILAAP information pack:

```
1. Liquidity risk đến từ đâu trong mô hình kinh doanh của bank này?
2. Risk được đo lường như thế nào? Assumptions quan trọng nào?
3. Information có đầy đủ không? (entities, countries, currencies)
4. Information có đủ granular không? (entity level, actual vs limit)
5. Information có thể tin cậy được không? (QA, validation, audit)
6. Information có link position với risk appetite (limits) không?
7. Information có đưa ra kết luận rõ ràng theo metrics xác định không?

→ Nếu Board không tự trả lời được → ILAAP governance FAIL
[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM Panel 13.3, p.3857–3868]
```

---

## Common Failures

```
ILAAP design failures:
  ✗ Created for supervisor, not for internal use → loses practical value
  ✗ Metrics không adapted theo business model → miss material risks
  ✗ Scenarios quá mild → không test real stress
  ✗ CFP không linked với stress test results
  ✗ LCR sensitivity analysis vắng mặt → Board không biết buffer volatile đến đâu
  ✗ Internal stress đặt LCR thấp để peer comparison tốt → underestimates risk

GOVERNANCE failures:
  ✗ Board approves ILAAP nhưng không challenge assumptions
  ✗ ILAAP process không tích hợp với ALM, treasury, recovery planning
  ✗ Quá nhiều documents không có internal logic → documentation overload

[RAW-BOOK Elkenbracht-Huizing_Handbook_ALM p.3898–3902; Choudhry_Principles_of_Banking p.11938]
```

---

## Link với các quy trình khác

```
ILAAP ↔ Stress testing (Principle 10): stress results là input cho ILAAP
ILAAP ↔ CFP (Principle 11): CFP là output/action plan từ ILAAP
ILAAP ↔ HQLA cushion (Principle 12): buffer sizing từ ILAAP scenarios
ILAAP ↔ Recovery Planning: CFP phải consistent với recovery triggers
ILAAP ↔ FTP: internal pricing phải reflect liquidity cost assumptions từ ILAAP
ILAAP ↔ ALCO: ILAAP là foundation cho ALCO reporting + decision-making
```

---

*Related wiki nodes:*
- `[[Bcbs_Liquidity_Stress_Testing_Principle_10]]`
- `[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]`
- `[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]`
- `[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]`
