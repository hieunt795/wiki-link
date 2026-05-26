## CƠ CHẾ TRUYỀN DẪN FTP ĐẾN CÁC RISK FACTORS

Nghiên cứu chi tiết về vai trò của Funds Transfer Pricing trong Quản trị Rủi ro Ngân hàng

## TÓM TẮT ĐIỀU HÀNH

Funds Transfer Pricing (FTP) không chỉ đơn thuần là công cụ định giá nội bộ mà đóng vai trò như một hệ thống điều khiển trung tâm (unified control mechanism) trong quản trị bảng cân đối ngân hàng. FTP tác động đồng thời đến ba loại rủi ro chính thông qua các kênh truyền dẫn riêng biệt nhưng có tương tác lẫn nhau: Rủi ro Thanh khoản (RRTK), Rủi ro Lãi suất (RRLS), và Rủi ro Tín dụng (RRTD).

Nghiên cứu này trình bày chi tiết cơ chế truyền dẫn từ FTP đến từng risk factor, bao gồm: (i) phân rã cấu trúc FTP rate, (ii) kênh truyền dẫn đến từng loại rủi ro, (iii) vòng phản hồi và cơ chế cân bằng, (iv) tích hợp với Basel III, và (v) framework định lượng ứng dụng thực tiễn.

## PHẦN 1: PHÂN RÃ CẤU TRÚC FTP RATE

## 1.1 Công thức tổng quát

FTP Rate được cấu thành từ bốn thành phần chính, mỗi thành phần tác động đến một hoặc nhiều loại rủi ro:

FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost

Trong đó:

Base Rate là lãi suất tham chiếu phi rủi ro (VNIBOR, lãi suất SBV), phản ánh chi phí cơ hội của vốn và chính sách tiền tệ. Thành phần này tác động trực tiếp đến RRLS thông qua cơ chế truyền dẫn lãi suất thị trường.

Liquidity Spread là phần bù thanh khoản theo kỳ hạn (term liquidity premium), phản ánh chi phí huy động vốn biên tế (marginal cost of funding) và yêu cầu tuân thủ LCR/NSFR. Thành phần này tác động trực tiếp đến RRTK.

Credit Spread bao gồm chi phí rủi ro tín dụng (expected loss charge) và chi phí vốn kinh tế (economic capital cost), phản ánh xếp hạng tín dụng của chính ngân hàng và đối tác. Thành phần này tác động trực tiếp đến RRTD.

Optionality Cost là chi phí của các quyền chọn ngầm (embedded options) như rủi ro trả nợ trước hạn (prepayment risk) và rút tiền sớm (early redemption), tác động đến rủi ro hành vi (behavioral risk).

## 1.2 Cấu trúc FTP Curve

FTP Curve được xây dựng theo các nguyên tắc sau theo Lubinska (2020):

Ngắn hạn (O/N đến 3M): Dựa trên đường cong liên ngân hàng (VNIBOR) nếu thị trường đủ thanh khoản. Trong trường hợp thị trường không thanh khoản, sử dụng lãi suất trái phiếu chính phủ hoặc CD yields với nội suy.

Trung hạn (6M đến 2Y): Phản ánh chi phí phát hành nợ cao cấp (senior debt issuance) của ngân hàng tại các kỳ hạn tương ứng, điều chỉnh theo hệ số dampening do ALCO quyết định.

Dài hạn (3Y trở lên): Dựa trên chi phí phát hành trái phiếu dài hạn, cộng thêm term premium phản ánh độ bất định về thanh khoản và lãi suất.

## PHẦN 2: KÊNH TRUYỀN DẪN FTP → RRTK (Rủi ro Thanh khoản)

## 2.1 Cơ chế truyền dẫn

FTP tác động đến RRTK thông qua Liquidity Spread Component . Cơ chế này hoạt động như sau:

Bước 1 - Nhận tín hiệu: ALM theo dõi liên tục các chỉ số thanh khoản bao gồm LCR (Liquidity Coverage Ratio), NSFR (Net Stable Funding Ratio), Survival Horizon, và Structural Ratio. Khi các chỉ số này tiến gần hoặc vi phạm ngưỡng cảnh báo, tín hiệu điều chỉnh được kích hoạt.

Bước 2 - Điều chỉnh FTP Curve: Dựa trên tín hiệu, ALM điều chỉnh Liquidity Spread theo tenor. Nếu LCR thấp (thiếu thanh khoản ngắn hạn), tăng spread cho các tenor ngắn (O/N đến 30 ngày). Nếu NSFR thấp (thiếu nguồn vốn ổn định), tăng spread cho các tenor dài (6M đến 2Y trở lên).

Bước 3 - Thay đổi hành vi của Business Units: Liability Center phản ứng với FTP cao hơn bằng cách tăng cường huy động vốn ở các kỳ hạn được khuyến khích (vì họ nhận được FTP rate cao hơn khi bán vốn cho ALM). Asset Center phản ứng bằng cách giảm cho vay ở các kỳ hạn có chi phí vốn cao (vì margin bị thu hẹp).

Bước 4 - Cải thiện chỉ số: Kết quả là cấu trúc tài sản-nợ thay đổi theo hướng cải thiện LCR và NSFR.

## 2.2 Công thức điều chỉnh định lượng

Mối quan hệ giữa tín hiệu Basel III và FTP adjustment có thể mô hình hóa như sau:

Điều chỉnh ngắn hạn: Nếu LCR &lt; LCR\_target (ví dụ 110%), thì Liquidity Spread cho tenor ngắn hạn tăng thêm một lượng tỷ lệ với khoảng cách: ΔSpread\_short = α × (LCR\_target - LCR\_actual), trong đó α là hệ số nhạy cảm do ALCO quyết định.

Điều chỉnh dài hạn: Nếu NSFR &lt; NSFR\_target (ví dụ 105%), thì Liquidity Spread cho tenor dài hạn tăng thêm: ΔSpread\_long = β × (NSFR\_target - NSFR\_actual).

## 2.3 Ví dụ minh họa

Giả sử ngân hàng X có LCR = 105% (target 115%) và NSFR = 102% (target 108%). ALM sẽ thực hiện các điều chỉnh sau:

Tăng Liquidity Spread cho tenor 1W-1M thêm 30-50 bps để khuyến khích Liability Center đẩy mạnh huy động ngắn hạn, qua đó tăng HQLA hoặc giảm net outflow projection.

Tăng Liquidity Spread cho tenor 6M-2Y thêm 50-80 bps để khuyến khích huy động tiền gửi kỳ hạn dài, đồng thời làm cho cho vay dài hạn đắt hơn, thu hẹp maturity transformation.

Kết quả sau 3-6 tháng: LCR tăng lên 118%, NSFR tăng lên 108%, đạt target.

## PHẦN 3: KÊNH TRUYỀN DẪN FTP → RRLS (Rủi ro Lãi suất)

## 3.1 Cơ chế truyền dẫn

FTP tác động đến RRLS thông qua Base Rate Component và cơ chế matched maturity pricing . Điểm mấu chốt là FTP tự động tách biệt IRRBB từ Business Units và chuyển giao toàn bộ về ALM để quản lý tập trung.

Cơ chế chuyển giao rủi ro: Khi Asset Center cho vay một khoản vay cố định 5 năm, họ nhận vốn từ ALM với FTP rate cố định 5 năm. Khi Liability Center huy động tiền gửi 3 tháng, họ bán vốn cho ALM với FTP rate 3 tháng. Business Units không còn exposure với repricing risk vì họ chỉ thấy fixed margin (customer rate - FTP rate). ALM kế thừa toàn bộ mismatch giữa asset repricing và liability repricing.

Tác động đến Gap Analysis: FTP rate theo tenor tạo incentive tự nhiên cho matched funding. Nếu Asset Center cho vay 2 năm fixed rate, họ bị charge FTP 2 năm. Nếu Liability Center huy động 3 tháng để fund khoản vay này, ALM chịu repricing gap. Để giảm gap, ALM có thể điều chỉnh FTP curve theo hướng penalize mismatch: tăng spread cho các tenor có gap lớn, giảm spread (hoặc thêm reward) cho matched funding.

## 3.2 Tín hiệu điều chỉnh

ALM theo dõi các chỉ số IRRBB bao gồm ΔNII (NII sensitivity dưới các kịch bản lãi suất ±200bps), ΔEVE (Economic Value of Equity sensitivity), và Gap position theo từng time bucket.

Khi ΔNII hoặc ΔEVE tiến gần hoặc vi phạm limit, ALM có thể điều chỉnh FTP curve để steering hành vi của BUs. Ví dụ: nếu ngân hàng có positive gap lớn (asset sensitive) trên short end và kỳ vọng lãi suất giảm, ALM có thể tăng FTP spread cho floating rate assets để discourage origination thêm floating rate loans.

## 3.3 Basis Risk Management

FTP cũng đóng vai trò quan trọng trong quản lý basis risk. Basis risk phát sinh khi assets và liabilities được repriced theo các benchmark khác nhau (ví dụ VNIBOR 1M vs VNIBOR 3M, hoặc VNIBOR vs lãi suất điều hành SBV).

Bằng cách thiết lập FTP curve riêng cho từng benchmark và áp dụng cross-currency/cross-index adjustment, ALM có thể theo dõi và kiểm soát basis risk exposure. Chi phí hedge basis risk có thể được incorporate vào FTP để pass through cho BUs.

## PHẦN 4: KÊNH TRUYỀN DẪN FTP → RRTD (Rủi ro Tín dụng)

## 4.1 Cơ chế truyền dẫn

FTP tác động đến RRTD thông qua Credit Spread Component và Capital Allocation Charge . Cơ chế này đảm bảo rằng mỗi giao dịch đều cover đầy đủ chi phí rủi ro tín dụng và chi phí vốn kinh tế.

Expected Loss (EL) Charge: FTP bao gồm một khoản charge để cover expected loss của danh mục. EL = PD × LGD × EAD, trong đó PD (Probability of Default) phụ thuộc vào rating của khách hàng, LGD (Loss Given Default) phụ thuộc vào tài sản đảm bảo, và EAD (Exposure at Default) là dư nợ dự kiến tại thời điểm default.

Capital Charge: Ngoài EL, FTP còn bao gồm chi phí vốn cho Unexpected Loss. Capital Charge = RWA × Capital Ratio × Cost of Equity. Thành phần này phản ánh chi phí cơ hội của việc phân bổ vốn cho một giao dịch cụ thể.

## 4.2 Rating-based Pricing Grid

FTP thiết lập một pricing grid theo rating bucket. Khách hàng có rating cao (AAA-A) có credit spread thấp, trong khi khách hàng có rating thấp (BB trở xuống) có credit spread cao. Điều này tạo incentive cho BUs chase quality assets và avoid high-risk deals.

Khi CAR (Capital Adequacy Ratio) của ngân hàng tiến gần regulatory minimum, ALM có thể tăng Capital Charge component trong FTP để discourage asset growth và encourage BUs tìm kiếm các deal có RWA density thấp hơn.

## 4.3 Kết nối với RAROC

FTP là công cụ quan trọng để operationalize RAROC (Risk-Adjusted Return on Capital) framework. Mỗi deal được pricing dựa trên FTP đảm bảo rằng return đủ cover tất cả risk-adjusted costs bao gồm funding cost, expected loss, và cost of capital.

RAROC tại deal level = (Revenue - Funding Cost - EL - Operating Cost) / Economic Capital

Nếu RAROC &lt; hurdle rate, deal không được chấp thuận hoặc phải reprice. FTP đảm bảo BUs internalize toàn bộ chi phí này trong quá trình origination.

## PHẦN 5: VÒNG PHẢN HỒI VÀ CƠ CHẾ CÂN BẰNG

## 5.1 Integrated Feedback System

Ba kênh truyền dẫn không hoạt động độc lập mà tương tác qua một hệ thống phản hồi tích hợp. Luồng hoạt động như sau:

Basel III Signals (LCR, NSFR, ΔNII, ΔEVE, CAR) → FTP Engine Calibration → Business Unit Behavior Change → Balance Sheet Reshape → Risk Metrics Improve → Re-monitor → Re-calibration

Chu kỳ này diễn ra liên tục, thường là hàng tháng hoặc hàng quý tùy theo mức độ biến động của thị trường và bảng cân đối.

## 5.2 Equilibrium Mechanism

RRTK Equilibrium: Khi LCR/NSFR đạt target, ALM giảm liquidity spread về mức "normal". BUs không còn bị over-incentivize để huy động hoặc giảm cho vay tại các tenor cụ thể. Balance sheet đạt trạng thái cân bằng về thanh khoản.

RRLS Equilibrium: Khi Gap trong limit và ΔNII/ΔEVE ổn định, FTP curve không cần điều chỉnh. Repricing profile được duy trì, NIM stable.

RRTD Equilibrium: Khi CAR có đủ buffer, credit spread reflect true risk của từng rating bucket. Portfolio tự điều chỉnh về target RAROC.

## 5.3 Cross-risk Interactions

Một điều chỉnh FTP để address một loại rủi ro có thể ảnh hưởng đến các loại rủi ro khác. Ví dụ:

Tăng liquidity spread dài hạn để cải thiện NSFR → Asset Center giảm cho vay dài hạn → Duration của asset portfolio ngắn lại → ΔEVE giảm → RRLS cải thiện.

Tăng capital charge để cải thiện CAR → BUs tập trung vào low-RWA assets (ví dụ HQLA) → Liquidity buffer tăng → LCR cải thiện.

Đây là lý do FTP được coi là "unified control mechanism" có thể tác động đồng thời cả ba loại rủi ro.

## PHẦN 6: FRAMEWORK ĐỊNH LƯỢNG

## 6.1 FTP Rate Formula tổng hợp

FTP\_Asset(t,T) = BaseRate(t,T) + LiqSpread(T) × LCR\_adj × NSFR\_adj + CreditSpread(rating) × PD × LGD + OptionCost(prepay) + CapitalCharge(RWA × CoE)

## Trong đó: t = origination date, T = maturity LCR\_adj = f(LCR\_current / LCR\_target), tăng khi LCR thấp NSFR\_adj = f(NSFR\_current / NSFR\_target), tăng khi NSFR thấp CoE = Cost of Equity hurdle rate (thường 12-15%) 6.2 Steering Adjustment Formulas RRTK Steering: If LCR &lt; 110%, LiqSpread\_short += α × (110% - LCR). If NSFR &lt; 105%, LiqSpread\_long += β × (105% - NSFR). RRLS Steering: If |Gap| &gt; Limit, Spread\_mismatch += γ × |Gap| / Limit. Reward\_match = -δ × (matched\_funding / total\_funding). RRTD Steering: If CAR &lt; target, CapCharge += ε × (target - CAR). Concentration\_penalty = ζ × HHI\_exposure. 6.3 Optimization Model FTP là control variable trong bài toán tối ưu hóa bảng cân đối: Objective Function: MAX [NII] = Σ(Asset\_i × Rate\_i) - Σ(Liability\_j × Cost\_j) Subject to: LCR = HQLA / Net\_Outflows ≥ 100% NSFR = ASF / RSF ≥ 100% |ΔNII| ≤ NII\_Limit (ví dụ 5% NII)

CAR = Capital / RWA ≥ 8%

Funding\_Concentration ≤ Max%

Bằng cách calibrate FTP curve, ALM có thể steering balance sheet đạt được optimal profile thỏa mãn tất cả constraints.

## PHẦN 7: KẾT LUẬN VÀ KHUYẾN NGHỊ

## 7.1 Tổng kết

FTP đóng vai trò như engine tối ưu hóa bảng cân đối thông qua ba kênh truyền dẫn chính: Liquidity Spread tác động RRTK, Base Rate và repricing mechanism tác động RRLS, Credit Spread và Capital Charge tác động RRTD.

Basel III metrics (LCR, NSFR) và IRRBB metrics (ΔNII, ΔEVE) đóng vai trò tín hiệu đầu vào, FTP calibration là công cụ điều khiển, và optimized balance sheet là kết quả đầu ra.

Hệ thống phản hồi tích hợp đảm bảo balance sheet liên tục được điều chỉnh về trạng thái cân bằng, maximizing profitability while minimizing risk.

## 7.2 Khuyến nghị triển khai

Đầu tiên , thiết lập FTP governance framework rõ ràng với vai trò của ALCO trong việc approve FTP curve và steering adjustments.

Thứ hai , xây dựng hệ thống monitoring real-time cho Basel III metrics và IRRBB metrics để kịp thời phát hiện tín hiệu điều chỉnh.

Thứ ba , đảm bảo transparency trong FTP methodology để BUs hiểu và internalize các incentives, từ đó hành vi tự điều chỉnh theo hướng mong muốn.

Thứ tư , định kỳ review và back-test effectiveness của FTP steering để calibrate các hệ số α, β, γ, δ, ε, ζ cho phù hợp với đặc thù của từng ngân hàng.

## TÀI LIỆU THAM KHẢO

Lubinska, B. (2020). Asset Liability Management Optimisation: A Practitioner's Guide to Balance Sheet Management and Remodelling. Wiley Finance.

Basel Committee on Banking Supervision (2016). Interest Rate Risk in the Banking Book (BCBS 368).

European Banking Authority (2018). Guidelines on the Management of Interest Rate Risk Arising from NonTrading Book Activities.

Cadamagnani, F., et al. (2015). Cross-firm Review of FTP Practices. Prudential Regulation Authority.

Tài liệu này được biên soạn dựa trên framework lý thuyết từ sách "Asset Liability Management Optimisation" của Beata Lubinska (2020) kết hợp với ứng dụng thực tiễn cho bối cảnh ngân hàng Việt Nam.