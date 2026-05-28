# Contingency Funding Plan (CFP) — Research Finding

**Date:** 2026-05-27
**Sources:** bcbs144 (Principle 11), Choudhry Principles of Banking (Ch.11), Basel Framework

---

## Định nghĩa gốc (BCBS)

> "A contingency funding plan (CFP) is the compilation of policies, procedures and
> action plans for responding to severe disruptions to a bank's ability to fund
> some or all of its activities in a timely manner and at a reasonable cost."
> [RAW-BOOK bcbs144 para 110]

CFP ≠ funding plan thông thường. Nó là **kế hoạch khủng hoảng** — chỉ được kích hoạt khi funding bình thường bị đứt gãy.

---

## Vị trí CFP trong khung quản lý thanh khoản

```
Stress Test (Principle 10)
       ↓ kết quả stress test là INPUT cho CFP
Contingency Funding Plan (Principle 11)
       ↓ CFP dựa vào
HQLA Cushion (Principle 12)  +  Central Bank Facilities
```

CFP không được thiết kế độc lập — phải **tích hợp trực tiếp với kết quả stress test**.
CFPs pre-2008 thất bại vì không có liên kết này. [RAW-BOOK bcbs144 para 3, 112]

---

## Cấu trúc bắt buộc của một CFP (Principle 11, para 110–122)

### 1 — Danh mục nguồn dự phòng

```
Yêu cầu cho mỗi nguồn:
  ① Tên nguồn + ước lượng số tiền có thể huy động
  ② Lead time để kích hoạt (giờ? ngày? tuần?)
  ③ Điều kiện tiên quyết (collateral? limit? đàm phán trước?)
  ④ Hạn chế pháp lý hoặc hoạt động

Format: "diversified menu of options" — không phải 1 nguồn, phải nhiều lớp
[RAW-BOOK bcbs144 para 111]
```

**Danh sách nguồn thực tế (Choudhry Ch.11):**
- Central bank funding (lender of last resort)
- CD và CP/ECP issuance programmes
- Internet-based deposits (qua broker)
- Sovereign wealth funds
- Foreign central bank reserves
- Repo/securitisation (nếu thị trường còn hoạt động)

### 2 — Kịch bản & phân loại mức độ khủng hoảng

```
CFP phải cover ít nhất 3 loại:
  A. Firm-specific stress  (chỉ ngân hàng bị ảnh hưởng)
  B. Market-wide stress    (toàn hệ thống bị ảnh hưởng)
  C. Combination          (cả hai đồng thời)

Phải bao gồm cả intraday — không chỉ overnight/term
[RAW-BOOK bcbs144 para 112–113]
```

### 3 — Roles, Responsibilities & Escalation

```
Bắt buộc ghi rõ:
  ① Ai có thẩm quyền INVOKE CFP (kích hoạt kế hoạch)
  ② Crisis team: tên + số điện thoại + địa điểm + người thay thế (alternates)
  ③ Tại ngưỡng nào thì escalate lên cấp cao hơn
  ④ Quyết định cụ thể: what actions, by whom, at what time

"Establishment of a formal crisis team may facilitate internal coordination"
[RAW-BOOK bcbs144 para 114–115]
```

### 4 — Communication Plan

```
Internal:  các business lines, chi nhánh, địa điểm
External:
  → Supervisors (SBV / regulators)
  → Central banks
  → Payment system operators
  → Correspondents, custodians, counterparties, customers

Lý do: "the actions of these parties could significantly affect the bank's
liquidity position and may vary with the underlying source of the problem"
[RAW-BOOK bcbs144 para 116]
```

### 5 — Thiết kế kỹ thuật CFP

**5a. Asset sale / repo constraints:**
```
CFP phải tính đến:
  → Impaired ability to sell/securitise assets khi thị trường stress
  → Link giữa asset market liquidity và funding liquidity closure
  → Second-round effects: bán TPCP nhiều → giá TPCP giảm → collateral value giảm
  → Reputational effects: drawdown CB facility → thị trường biết → outflow tăng
[RAW-BOOK bcbs144 para 117]
```

**5b. Central Bank lending:**
```
Phải ghi rõ trong CFP:
  → Loại facility nào available (OMO? repo? SBV tái cấp vốn? ELA?)
  → Collateral được chấp nhận là gì
  → Operational procedures để truy cập
  → Đánh giá reputational risk khi dùng CB facilities
[RAW-BOOK bcbs144 para 118]
```

**5c. Intraday coverage:**
```
CFP phải có:
  → Cơ chế prioritise critical payments khi intraday liquidity thiếu
  → Khả năng identify và mobilise additional intraday collateral
  → Xử lý settlement obligations của cả khách hàng + hệ thống payment
[RAW-BOOK bcbs144 para 119]
```

**5d. Cross-border / intragroup transfer constraints:**
```
CRITICAL: Assets dùng làm collateral trong CFP
  → PHẢI ở đúng legal entity và location NGAY BÂY GIỜ
  → Không được assume "sẽ chuyển khi cần" — transfer cross-border mất thời gian
  → Realistic timelines cho transfer phải được đưa vào liquidity model
[RAW-BOOK bcbs144 para 120]
```

---

## Testing, Update & Maintenance

```
Tần suất: "regular" — không chỉ annual
Nội dung test:
  ① Roles/responsibilities: đúng không? mọi người có hiểu không?
  ② Contact info: còn cập nhật không?
  ③ Cash/collateral transferability: đặc biệt cross-border — thực sự làm được không?
  ④ Legal/operational documentation: sẵn sàng execute ngay không?
  ⑤ Ability to sell/repo assets: TEST THỰC TẾ (not just document)
  ⑥ Credit line drawdown: TEST THỰC TẾ (periodically draw down)

Annual review: senior management review → submit cho board approve
BCP integration: CFP phải hoạt động được ngay cả khi BCP được kích hoạt
Off-site access: CFP phải accessible khi văn phòng chính không vào được
[RAW-BOOK bcbs144 para 121–122]
```

**Key failure**: CFP thất bại nếu chỉ là "paper exercise" — yêu cầu test thực tế định kỳ.

---

## Survival Horizon & Early Warning Indicators

**Theo Choudhry (Ch.11–12):**

```
ALCO cần biết từ liquidity MI pack:
  ① Self-sufficiency: bank có tự tài trợ được không?
  ② Forward liquidity requirement: 12 tháng tới, normal + stress
  ③ Early Warning Indicators (EWIs): cảnh báo sớm stress points
  ④ Survival horizon ("survival days"): bao nhiêu ngày sống được
     nếu funding markets đóng hoàn toàn, chỉ dùng HQLA + secured repo
  ⑤ Funding concentration: phụ thuộc quá mức vào 1–2 nguồn?
  ⑥ Daily funding requirement: nhu cầu cash hàng ngày
[RAW-BOOK Choudhry_Principles_of_Banking Ch.11]
```

**EWI phân loại:**
- **Internal EWIs**: có thể ảnh hưởng được — LDR, funding concentration, HQLA ratio
- **External EWIs**: không kiểm soát được nhưng phải monitor — CB rate, market spreads, credit ratings của ngân hàng

---

## 3 Scenarios Chuẩn cho CFP

| Scenario | Mô tả | Nguồn trám chính | Timeframe |
|---|---|---|---|
| **Idiosyncratic** | Chỉ ngân hàng bị ảnh hưởng (tin đồn, downgrade) | CB OMO + HQLA | Days–weeks |
| **Market-wide** | Toàn hệ thống (crisis 2008-style) | CB last resort + asset sales | Weeks–months |
| **Combined** | Cả hai (SVB 2023: rising rates + firm-specific run) | ELA + HQLA fire sale | Hours–days |

**Combined scenario** là nguy hiểm nhất và thường bị underestimate trong CFP design.

---

## Vị trí CFP trong ALCO Reporting

Theo Choudhry, ALCO deck chuẩn phải include:
- Stress test results
- NII/NIM sensitivity + basis risk
- Funding composition + refinancing risk stress points
- **Contingency Funding Plan (CFP) — cập nhật thường xuyên**
- HQLA buffer status

CFP là **standing agenda item** của ALCO, không phải tài liệu one-off.

---

## Common Failures

```
Pre-2008 [RAW-BOOK bcbs144 para 3]:
  ✗ CFP không linked với stress test results
  ✗ Assume funding markets remain open (single scenario)
  ✗ Chỉ là paper exercise, không test thực tế

SVB 2023 [RAW-BOOK Tata_Bank_ALM_2025 §4.3]:
  ✗ Behavioral assumptions sai: deposit base (VC/PE funds) không stable như assumed
  ✗ CFP không test intraday scenario — run xảy ra trong vài giờ
  ✗ Asset side (long-duration MBS) không liquidate được without massive fire sale loss

Vietnam-specific [LLM]:
  ✗ Assume SBV OMO luôn mở — nhưng nếu bank bị stigma, counterparty cắt repo
  ✗ TPCP collateral tính trên account nhưng chưa pre-pledged với SBV
  ✗ CFP không phân biệt firm-specific vs systemic — xử lý như nhau
```

---

## Link với NIM Sensitivity

```
NIM Sensitivity (funding gap → cost of funds → NIM impact)
  ↑
CFP cung cấp framework:
  → Nguồn trám nào có sẵn (pre-arranged vs ad-hoc)
  → Lead time bao lâu (ảnh hưởng urgency premium)
  → Volume tối đa từ mỗi nguồn (ảnh hưởng volume effect trên spread)

CFP tốt → liquidity premium thấp khi crisis xảy ra
CFP tệ (paper exercise) → phải vay gấp → spread cao → NIM bị ăn nhiều hơn
```

---

*Related wiki nodes:*
- `[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]`
- `[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]`
- `[[Bcbs_Liquidity_Stress_Testing_Principle_10]]`
- `[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]`
- `[[Bcbs_Intraday_Liquidity_Management_Principle_8]]`
