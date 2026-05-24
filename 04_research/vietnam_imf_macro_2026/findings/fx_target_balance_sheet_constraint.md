---
title: "Bảng Cân Đối Ràng Buộc Bởi FX Rate Target — SBV T_MODE_DEEP"
slug: fx_target_balance_sheet_constraint
confidence: 2
mode: T_MODE_DEEP
date: 2026-05-24
wiki_nodes_used:
  - Imf_Monetary_Survey_And_Reserve_Money_Identity_Framework
  - Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis
  - Imf_Flow_Of_Funds_4_Sector_Consistency_Framework
  - Central_Bank_Balance_Sheet_Structure_Liabilities_Assets
  - EM_Central_Bank_Policy_Mix_FIT_Framework
  - Em_Balance_Sheet_Crisis_Anatomy_Fear_Of_Floating
  - CB_Balance_Sheet_Trilemma
data_sources:
  - "FULCRUM: Exchange Rate Stability in Vietnam [WEB-2026-05-24]"
  - "VietnamPlus: SBV bill issuance mechanics [WEB-2026-05-24]"
  - "VietnamNet: SBV T-bill auction data [WEB-2026-05-24]"
  - "IMF Article IV Vietnam 2025 [WEB-2026-05-24]"
  - "NBER WP 13902 — Sterilization framework [WEB-2026-05-24]"
---

## TOP-DOWN ENTRY 🟢 CURRENT (2024-2025)

Khi ngân hàng trung ương cam kết **target tỷ giá** (dù là hard peg, crawling peg, hay managed band), bảng cân đối của CB không còn là biến chính sách tự do — **NFA trở thành biến nội sinh**, được quyết định bởi BOP flows bên ngoài. CB chỉ còn kiểm soát NDA. Đây là ràng buộc cơ bản nhất, phát sinh từ identity `RM = NFA + NDA`.

Với SBV (Việt Nam, 2024-2025), điều này hiện hữu dưới dạng: SBV bán $9.3bn FX trong 2024 để giữ VND trong band ±5%, dự trữ rơi từ ~$90bn xuống ~$83bn, bao phủ nhập khẩu giảm từ 3.3 xuống 2.4 tháng [WEB-2026-05-24] — tiếp tục defending sẽ đẩy gần ngưỡng Greenspan-Guidotti. [LLM-E]

---

## LÝ LUẬN NỀN: TẠI SAO FX TARGET RÀ BUỘC BẢNG CÂN ĐỐI?

### Identity gốc
```
RM  = NFA + NCG + Cb + OIN        [Reserve Money identity]
M2  = NFA + NDA                   [Monetary Survey identity]
NDA = NCG + CPS + OIN(b)
```

Khi CB **không có FX target**: NFA là biến chính sách (CB tự do mua/bán FX theo ý muốn), RM được điều tiết chủ động qua NDA (OMO, lending to banks).

Khi CB **có FX target**: NFA trở thành biến bắt buộc:
```
ΔNFA = BOP_surplus - FX_intervention_sales
     = f(trade flows, FDI, portfolio flows, speculative pressure)
     = NGOẠI SINH với CB
```

→ CB chỉ còn một bậc tự do: **ΔNDA**
→ Nếu muốn giữ RM ổn định: ΔNDA = −ΔNFA (sterilize hoàn toàn)
→ Nếu muốn giữ credit target: ΔNDA ≥ 0 (mở rộng NDA qua credit quota)
→ Hai mục tiêu này mâu thuẫn khi ΔNFA < 0 (đang mất dự trữ) [LLM-E]

---

## CƠ CHẾ 1: DEFENDING DEPRECIATION (Vietnam 2024)

**Điều kiện:** USD mạnh toàn cầu + carry trade outflows + dollarization pressure

```
[Step 1] Market: demand USD ↑ → áp lực depreciation VND
         (trigger: Fed rate cao, tỷ giá USD index tăng, speculative crypto/gold)

[Step 2] SBV can thiệp: bán USD spot → nhận VND về
         → NFA ↓ (mất foreign assets)
         → VND được absorb khỏi hệ thống → RM ↓
         Quy mô 2024: −$9.3bn (−$6.5bn Apr-Jul, −$2.8bn Sep-Dec) [WEB-2026-05-24]

[Step 3] RM ↓ → tác động contractionary:
         Interbank rates ↑ → lending rates ↑ → credit growth chậm lại
         Mâu thuẫn với credit target 15-16%

[Step 4] SBV đối mặt lựa chọn:
         (A) Chấp nhận credit chậm → GDP risk
         (B) Inject VND qua refinancing (Cb ↑) → bù lại RM contraction
             nhưng: thêm VND vào hệ thống → lại có thêm áp lực depreciation
             → vòng lặp tự phủ nhận

[Kết quả 2024] Phương án (A) — SBV để credit tăng nhờ NFA bù bởi CPS tự nhiên
               Credit thực tế đạt 15%, M2 tăng vừa phải dù NFA giảm
               → NDA (đặc biệt CPS) bù đắp phần NFA co lại [WEB-2026-05-24]
```

**T-account SBV khi bán $1bn FX:**
```
SBV ASSETS              SBV LIABILITIES
NFA       −25,000 tỷ    Reserve Money    −25,000 tỷ
                         (banks' VND reserves ↓)
```
**T-account Banking System:**
```
BANK ASSETS             BANK LIABILITIES
Reserves at SBV −25,000 tỷ    (no change in deposits yet)
→ banks giảm excess reserves → liquidity tightening
```

---

## CƠ CHẾ 2: STERILIZATION QUA T-BILL OMO (Vietnam 2023)

**Điều kiện:** RM quá dồi dào từ nới lỏng trước + speculative VND selling do crypto/gold

Khác với Cơ chế 1 (SBV bán FX, hút VND trực tiếp), cơ chế này SBV **không dùng FX reserves** mà dùng **OMO T-bill** để tác động qua kênh lãi suất:

```
[Step 1] SBV phát hành T-bills trên OMO
         Quy mô: ~111 tỷ VND tích lũy đến Oct 2023 [WEB-2026-05-24]
         Tenor: 28 ngày, lãi suất: 1.18-1.4%/năm [WEB-2026-05-24]

[Step 2] Banks mua T-bills → trả VND cho SBV
         → Reserves tại SBV ↓ (VND absorbed)
         → NDA ↓ (OIN giảm hoặc NCG được sterilize)
         → RM ↓

[Step 3] Excess liquidity giảm → interbank overnight rate ↑
         Từ: ~0.1%/năm → 0.55%/năm [WEB-2026-05-24]
         T-bill rate: ~1.18%/năm [WEB-2026-05-24]

[Step 4] VND/USD interest differential thu hẹp:
         Trước: USD deposit rate cao hơn VND ngắn hạn nhiều
         Sau: VND rate tăng → ít hấp dẫn hơn để short VND
         → Speculative demand for USD giảm
         → Exchange rate pressure giảm

[Kết quả] Tỷ giá tự do giảm từ 25,700 → 25,480-25,600 VND/USD [WEB-2026-05-24]
          NFA reserves KHÔNG bị chạm → không mất dự trữ
```

**T-account SBV khi phát hành T-bill:**
```
SBV ASSETS              SBV LIABILITIES
(T-bill outstanding     Reserve Money    −VND absorbed
 = SBV liability)       Banks' reserves ↓
OIN ↓ (net)
```

**Điểm khác biệt then chốt:**

| | Cơ chế 1 (FX intervention) | Cơ chế 2 (T-bill OMO) |
|---|---|---|
| NFA | ↓ (mất dự trữ) | unchanged |
| NDA | unchanged | ↓ (sterilization) |
| RM | ↓ | ↓ |
| Chi phí | Depletion dự trữ | Lãi T-bill phải trả |
| Hiệu quả | Trực tiếp, mạnh | Gián tiếp, qua lãi suất |
| Giới hạn | Dự trữ cạn | Banks mua T-bill đến giới hạn |

---

## CƠ CHẾ 3: CHI PHÍ STERILIZATION — QUASI-FISCAL CONSTRAINT

Sterilization không miễn phí. SBV phải trả lãi T-bill trong khi nhận lãi từ FX reserves:

```
Sterilization Cost = r_domestic × ΔT-bill_outstanding
                   − r_foreign × ΔNFA_sterilized

2023 episode:
  r_domestic (T-bill 28d) = 1.18-1.4%/năm [WEB-2026-05-24]
  r_foreign  (USD T-bill) ≈ 5-5.25%/năm (Fed funds 2023)
  → Cost = 1.4% − 5.2% = −3.8% (negative cost = PROFIT for SBV)
  → Unusual: sterilization was profitable because VN rates << US rates
  → This is the "carry" SBV earned by holding USD reserves vs issuing VND bills

2021-2022 (lower Fed rates):
  r_foreign ≈ 0-0.25%/năm
  r_domestic ≈ 2-3%/năm
  → Cost = 2% − 0% = +2%/năm (normal EM: CB loses money sterilizing)
```

**Hàm ý:** Trong giai đoạn Fed tăng mạnh (2022-2023), SBV có lợi thế bất thường: **lãi suất USD > lãi suất VND** → sterilization profitable → không có quasi-fiscal cost constraint. Đây là lý do SBV có thể duy trì can thiệp tích cực mà không bị áp lực lợi nhuận. Khi Fed cắt giảm lãi suất → lợi thế này biến mất → sterilization trở nên costly hơn → constraint tighter. [LLM-E]

---

## MA TRẬN RÀNG BUỘC ĐỒNG THỜI — SBV 2024-2025

```
              FX BAND    CREDIT     INFLATION   RESERVE
              (±5%)     TARGET      (<4% CPI)  ADEQUACY
              TARGET    (16%)                  (3-4mo)
─────────────────────────────────────────────────────────
FX BAND       —         CONFLICT    NEUTRAL     CONFLICT
              (đây rồi) (tight VND  (no direct  (selling FX
                        vs expand   link)       depletes)
                        credit)

CREDIT TARGET CONFLICT  —           MODERATE    INDIRECT
(16%)         (above)               CONFLICT    CONFLICT
                                    (credit     (credit
                                    drives M2)  drives imports)

INFLATION     NEUTRAL   MODERATE    —           NEUTRAL
(<4%)                   CONFLICT

RESERVE       CONFLICT  INDIRECT    NEUTRAL     —
ADEQUACY      (above)   CONFLICT
```

**Ba ràng buộc đồng thời binding nhất:**

**[CONFLICT 1] FX target vs. Credit quota**
```
Condition: depreciation pressure (2024)
SBV sells FX → NFA ↓ → RM ↓ → banks short on VND
→ Banks raise lending rates to attract deposits
→ Credit growth slows below 16% quota
→ To fix: SBV injects via refinancing (Cb ↑)
→ More VND → more depreciation pressure
→ Back to start
```

**[CONFLICT 2] FX target vs. Reserve adequacy**
```
Condition: sustained depreciation pressure
SBV must sell FX to defend band
→ NFA ↓ → reserves depleted
→ 2024: $83bn = 2.4 months (below IMF 3-4 months target)
→ If continues: approaches Greenspan-Guidotti ratio NFA/RM → 1.0
→ Below 1.0: credibility of peg questioned → self-fulfilling attack risk
Greenspan-Guidotti formula:
  NFA (VND) ≈ 83bn × 25,000 = 2,075,000 tỷ VND
  RM estimate ≈ ~700-900,000 tỷ VND (est.)
  Ratio ≈ 2.3-2.9 → currently OK, but declining [LLM-E]
```

**[CONFLICT 3] Credit quota vs. Fiscal deficit**
```
Condition: fiscal deficit 3.3% GDP 2025
MoF issues govt bonds → banks must absorb
Banks: portfolio = credit_loans + govt_bonds (bound by capital + LDR)
→ If banks absorb more govt bonds → CPS (credit to private) must shrink
→ Credit quota 16% impossible to maintain simultaneously
→ Unless SBV provides additional refinancing → M2 expands → inflation risk
This is classic "crowding out" amplified by credit quota system [LLM-E]
```

---

## DIAGRAM: SBV BALANCE SHEET UNDER FX TARGET

```
        ┌─────────────────────────────────────────────────┐
        │              SBV BALANCE SHEET                  │
        │                                                  │
        │  ASSETS                    LIABILITIES           │
        │  ────────────────────────  ──────────────────   │
        │  NFA ~$83bn                Reserve Money (RM)    │
        │  (ENDOGENOUS under         = Currency circ.      │
        │   FX target)               + Bank reserves       │
        │  ⬆️ buy USD (appreciation)                       │
        │  ⬇️ sell USD (depreciation) Govt deposits        │
        │                                                  │
        │  NCG (small — no           T-bill OMO            │
        │  monetization)             (sterilization tool)  │
        │                                                  │
        │  Cb (refinancing to        Capital + OIN         │
        │  banks — policy tool)                            │
        │                                                  │
        │  IDENTITY: RM = NFA + NCG + Cb + OIN            │
        │  FREEDOM:  Only NDA = f(policy)                  │
        │  CONSTRAINT: NFA = f(BOP + intervention policy)  │
        └─────────────────────────────────────────────────┘

NDA INSTRUMENTS SBV kiểm soát được:
  NCG: mua/bán govt bonds (OMO outright) — limited use
  Cb:  repo/refinancing với banks — primary injection tool
  T-bill issuance: sterilization absorption tool
  OIN: FX forward book, valuation adjustments
```

---

## HỆ QUẢ POLICY — VIETNAM CỤ THỂ

**1. Credit quota system là "second instrument" nhưng tạo perverse dynamics**

Vietnam dùng credit quota (hạn mức tín dụng từng ngân hàng) thay vì lãi suất thị trường để kiểm soát credit. Khi FX target và credit target mâu thuẫn:
- Lãi suất tự do hóa: banks tăng rates → credit chậm → market-clearing
- Credit quota: banks cạnh tranh phân bổ hạn mức → giảm rates để giải ngân → cuối kỳ bùng nổ rồi đóng băng → procyclical

→ Quota làm mờ tín hiệu lãi suất vốn là mechanism truyền tải monetary policy sang FX qua interest rate differential channel [LLM-E]

**2. Quasi-fiscal cost sẽ tăng khi Fed cắt giảm lãi suất**

2023-2024: Fed rate ~5% > VN T-bill rate ~1.4% → SBV earn carry từ reserves → sterilization profitable
2025-2026: nếu Fed cắt về ~3-3.5%, VN tăng rates (chống inflation/FX) → differential thu hẹp → sterilization costly → thêm áp lực lên SBV profit/loss → quasi-fiscal gap mở rộng [LLM-E]

**3. Reserve adequacy là binding constraint thực sự**

SBV muốn tích lũy dự trữ nhưng bị kẹt:
- Buy FX (tích lũy): VND tăng → exports kém cạnh tranh → politically sensitive
- Sell FX (defend): mất dự trữ → adequacy giảm → credibility risk
- Không can thiệp: VND volatile → import inflation → credibility risk khác

→ SBV đang đi dây giữa ba risk: **export competitiveness vs. reserve adequacy vs. import inflation** [LLM-E]

---

## TRUE GAPS — CẦN NGUỒN BỔ SUNG

1. **SBV balance sheet chi tiết theo quý**: NFA/NCG/Cb/OIN time series → không có trên public data hiện tại
2. **Offset coefficient của Vietnam**: bao nhiêu % capital inflows bị offset bởi sterilization? (Typical EM: 0.3-0.6)
3. **Credit quota allocation mechanism**: làm thế nào SBV set quota per bank, và điều này interact với reserve requirement như thế nào?
4. **FX forward book của SBV**: SBV dùng forwards (thấy $4.4bn forward sales Aug 2024) — forward book này không xuất hiện trong spot NFA nhưng tạo future obligation → off-balance-sheet NFA commitment [WEB-2026-05-24]

---

*Confidence: 2 — Framework từ wiki (confidence 4) + Vietnam-specific data từ web (confidence 2-3). Tất cả mechanistic claims [LLM-E]. Verify trước khi promote lên wiki.*
