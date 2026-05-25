---
finding_id: stagflation_fx_qf_001
title: "Stagflation Under FX Rate Target + Quasi-Fiscal Operations — Three Transmission Pathways"
topic_slug: stagflation_fx_quasi_fiscal
type: mechanism_synthesis
confidence: 2
status: draft
created: 2026-05-25
sources_used:
  - "[[CB_FX_Rate_Target_Balance_Sheet_Constraint_Sterilization]]"
  - "[[CB_Quasi_Fiscal_Sterilization_Seigniorage_Fiscal_Monetary_Nexus]]"
  - "[[Stagflation_Regime_Diagnostic_Framework]]"
  - "[[Stagflation_Policy_Response_Tradeoff_Framework]]"
  - "[[Enhanced_Taylor_Rule_EME_FX_Augmented]]"
  - "[[Cost_Push_Inflation_Persistence_Mechanism]]"
  - "[[Imf_Inflation_Analysis_Cpi_Gdp_Deflator_Four_Types_Core]]"
gaps_triggered:
  - "stagflation under FX rate targeting quasi-fiscal costs"
  - "fiscal dominance stagflation EME"
template_insights: []
---

## Central Thesis [LLM]

Stagflation "kiểu FX rate target + quasi-fiscal" là một bẫy chính sách đặc thù của EME: lạm phát
dai dẳng và tăng trưởng đình trệ xảy ra đồng thời, không phải do cú sốc cung thuần túy như mô hình
1970s, mà do cấu trúc chính sách tự khóa—FX target vô hiệu hóa công cụ lãi suất, trong khi quasi-fiscal
costs bào mòn không gian tài khóa. Kết quả: cả monetary lẫn fiscal đều không thoải mái sử dụng đúng
hướng cùng lúc.

---

## Ba Pathway Dẫn Đến Đình Lạm

### Pathway 1 — FX Target Blocking Monetary Transmission (Impossible Trinity Trap)

**Cơ chế:**

```
Shock: depreciation pressure hoặc external cost-push (import prices↑)
    ↓
CB phải defend FX target → bán reserves → NFA↓, RM↓
    ↓
Monetary conditions tighten → interest rates↑ → credit↓ → growth↓   [STAGNATION channel]
    ↓
NHƯNG: import prices vẫn cao (CB chỉ defend nominal rate, không giải quyết real shock)
Wage indexation / contract embedding → cost-push persists             [INFLATION channel]
    ↓
CB không thể cắt lãi suất (sẽ break FX target → reserves bleed faster)
→ Kẹt: lãi suất cao + lạm phát dai dẳng = STAGFLATION
```

**Điều kiện kích hoạt:**
- FX target regime (peg cứng hoặc managed band)
- Capital account open (impossible trinity binding)
- Shock là persistent (không phải transitory) → sterilization không giải được

**Source foundation:** [RAW-BOOK Lipschitz p.2704–2706] "NFA would reach a critical minimum, intervention would no longer be possible... risk premia would rise. Financial outflows would then add to exchange market pressure." Kết hợp với IMF inflation taxonomy: cost-push shock → inertial inflation khi không có policy tightening hiệu quả. [RAW-BOOK IMF p.878–927]

---

### Pathway 2 — Quasi-Fiscal Drain → Fiscal Crowding Out → Stagnation

**Cơ chế:**

```
FX target + capital inflows → CB mua FX → NFA↑, RM↑ (appreciation pressure)
    ↓
CB sterilize: phát hành domestic T-bills, OMO absorption → NDA↓
    ↓
Quasi-fiscal cost = r_domestic × sterilization_stock − r_foreign × NFA
                  = NEGATIVE carry (EM r_domestic > r_foreign)          [LLM]
    ↓
CB losses → seigniorage transfer to Treasury↓ → fiscal revenue↓
    ↓
Government: (a) cắt giảm chi tiêu → AD↓ → growth↓                   [STAGNATION via fiscal]
         OR (b) không cắt → deficit↑ → NCG expansion → monetization
    ↓
Route (b): NCG↑ → M2↑ → lạm phát (ẩn) → thực chất accommodation     [INFLATION channel]
Route (a): Real squeeze: fiscal tightening → output gap âm           [STAGNATION channel]

Cả hai route đều dẫn đến: growth stagnation + inflation persistence = STAGFLATION
```

**Mechanism quantification [LLM-E]:**

```
Cho EME typical:
  r_domestic = 7%, r_foreign (USD T-bill) = 4.5%
  Sterilization stock = 20% GDP
  Annual quasi-fiscal cost = (7% − 4.5%) × 20% GDP = 0.5% GDP/year

  → Tương đương với một khoản "thuế ẩn" 0.5% GDP/năm rút khỏi
    fiscal space, buộc government phải chọn giữa cắt chi (stagnation)
    hoặc monetize (inflation).
```

**Source foundation:** [RAW-BOOK Lipschitz p.2720] "sterilization operation reduces the profits... reduces transfers to... calls on the government budget. Governments are usually loath to allow such policies to continue indefinitely." + [RAW-BOOK IMF p.2288] quasi-fiscal costs phải cộng vào conventional fiscal deficit.

---

### Pathway 3 — Fiscal Dominance Completion: NCG↑ + NFA↓ Simultaneously (Crisis Precursor)

**Cơ chế — double deterioration:**

```
Fiscal expansion (deficit) + FX target defense → CB bị kéo 2 hướng:
    ↓
[Direction A] Government deficit → NCG↑ (CB accommodation, direct/indirect)
    ↓ monetization → RM↑ → lạm phát
    ↓
[Direction B] BOP deficit → CB bán FX → NFA↓
    ↓ reserves depleting
    ↓
Net balance sheet: NCG↑↑, NFA↓↓ — M2 ≈ stable nhưng chất lượng backing xấu hơn
    ↓
Fiscal dominance threshold crossed: CB mất khả năng tăng lãi suất
  → inflation unanchored                                               [INFLATION]
  → government spending forced to contract (reserves critical)         [STAGNATION]
  → "vicious circle of self-perpetuating depreciation, increasing inflation,
     and rising inflation expectations" [RAW-BOOK Lipschitz p.2757]
```

**Bulgaria 1994–1996 canonical case:**
NFA: +12.1 → −234.5 billion lev (2 năm), NDA expanding để compensate → hyperinflation + currency collapse → currency board 1997. [RAW-BOOK Lipschitz p.2771–2792]

[LLM] Đây là dạng stagflation extreme nhất: lạm phát phi mã + kinh tế sụp đổ (không chỉ stagnation mà là contraction).

---

## Ma Trận Chẩn Đoán

| Pathway | Trigger | Inflation Source | Stagnation Source | Severity |
|---------|---------|-----------------|-------------------|---------|
| **P1** — Impossible trinity trap | Depreciation pressure + open CA | Cost-push import prices (unresolved) | Interest rates high, credit tight | Medium |
| **P2** — Quasi-fiscal fiscal drain | Capital inflows + sterilization carry | Covert monetization (NCG route) or demand suppression | Fiscal squeeze, crowding out | Medium-High |
| **P3** — Fiscal dominance completion | Sustained deficit + FX defense | Unanchored expectations, direct monetization | Fiscal contraction forced by reserve depletion | Severe |

---

## Early Warning Signals (CB Balance Sheet Reads)

**Signal P1 — Monetary trap:**
```
- NFA declining steadily (reserves being spent on FX defense)
- Policy rate held above neutral (tightening to defend FX)
- Growth decelerating despite no fiscal stimulus
- Import price CPI component elevated, core not falling
```

**Signal P2 — Quasi-fiscal drain:**
```
- CB profit transfer to Treasury declining YoY (check annual report)
- OMO absorption stock growing (sterilization expanding)
- NCG/M2 ratio rising quarter-over-quarter
- Government deficit widening despite revenue stability
```

**Signal P3 — Fiscal dominance incoming:**
```
- NFA↓ AND NCG↑ simultaneously (dual deterioration)
- NFA/RM ratio approaching Greenspan-Guidotti floor (1.0)
- Policy rate held below neutral despite inflation above target
- CB sterilization halted (political pressure)
```

[RAW-BOOK Lipschitz p.2757] "in situations like this (known as 'fiscal dominance') there is no scope for independent monetary policy."

---

## Policy Exit Options [LLM]

| Option | Mechanism | Risk |
|--------|-----------|------|
| **Exchange rate adjustment** (abandon peg/widen band) | Remove FX constraint → CB regains rate independence → can fight inflation | Depreciation pass-through spike: short-term inflation worsens before improving |
| **Fiscal consolidation** | Reduce deficit → NCG pressure falls → quasi-fiscal cost becomes manageable | Political economy difficulty; contraction risk during stagnation |
| **Capital flow management (CFM)** | Reduce volume of flows requiring sterilization → quasi-fiscal cost↓ | Partial measure; capital controls have side effects on investment |
| **Recapitalization + CB independence restoration** | Government injects equity, removes quasi-fiscal mandates | Fiscal cost upfront; requires political credibility |
| **IMF program + FX adjustment** | External anchor replaces FX target credibility during transition | Conditionality, procyclical fiscal adjustment |

[LLM] Không có exit option nào không gây đau. Lựa chọn thực tế là giữa đau ngắn (peg adjustment) và đau dài (stagflation persistence). IMF kinh nghiệm cho thấy các nước trì hoãn peg adjustment thường phải điều chỉnh lớn hơn và tốn kém hơn sau đó.

---

## Wiki Promotion Assessment

**Không promote ngay** — confidence 2 (LLM synthesis từ building block nodes, không có dedicated source về
"stagflation under FX target" mechanism). Cần source xác nhận trước khi promote.

**Blocking issues:**
1. No dedicated source on stagflation + FX target + quasi-fiscal as integrated mechanism
2. Pathway 1 và P2 là synthesis — cần IMF WP hoặc BIS WP xác nhận
3. Historical examples beyond Bulgaria cần verify (Vietnam SBV OMO data là [LLM] estimate)

**Source candidates:**
- IMF WP on "Exchange Rate Regimes and Inflation" (Ghosh, Gulde, Wolf)
- BIS WP on "Sterilization costs and monetary policy effectiveness in EMEs"
- NBER WP on "Fiscal Dominance and Stagflation in Developing Countries"
