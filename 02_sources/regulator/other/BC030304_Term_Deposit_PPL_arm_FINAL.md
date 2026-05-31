



# **Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)**

**Giao phẩm BC03.03.04: Phương pháp luận cho mô hình hành vi tái tục và rút trước hạn cho tiền gửi có kì hạn có tham số**

Tháng 08, năm 2021 **BẢN CHÍNH THỨC**

![](_page_0_Picture_3.jpeg)

![](_page_0_Picture_4.jpeg)

![](_page_0_Picture_5.jpeg)

# **Lưu ý quan trọng**

Báo cáo này được thực hiện theo Hợp đồng cung cấp dịch vụ giữa Công ty TNHH Tư vấn PricewaterhouseCooper Việt Nam (PwC Việt Nam) và Ngân hàng TMCP An Bình ("ABBank") ngày 24 tháng 09 năm 2020 với các điều khoản và điều kiện đi kèm. Báo cáo này dành riêng cho việc sử dụng nội bộ và nhằm phục vụ lợi ích của ABBank và không được sử dụng bởi hoặc phục vụ cho lợi ích của bất kỳ đối tượng nào khác ("Bên Thứ Ba").

Bên thứ ba không được phép sử dụng Báo cáo này trừ khi đã ký Cam kết miễn trừ trách nhiệm cho PwC Việt Nam và gửi Cam kết này đến PwC Việt Nam hoặc nhận được một thông báo từ PwC Việt Nam về các trách nhiệm liên quan của công ty đối với Bên Thứ Ba.

Bất kỳ Bên Thứ Ba nào sử dụng và đọc báo cáo này trái với các điều khoản nêu trên, thì Bên Thứ Ba đó phải chấp nhận và đồng ý với các điều khoản sau:

- 1. Công việc được thực hiện bởi PwC Việt Nam theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và được thực hiện chỉ dành riêng cho lợi ích và mục đích sử dụng của chính khách hàng mà báo cáo này được gửi đến.
- 2. Báo cáo này được thực hiện theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và có thể không bao gồm tất cả những quy trình/ thủ tục có thể được cho là cần thiết cho mục đích của Bên Thứ Ba.
- 3. PwC Việt Nam, các giám đốc, nhân viên và các bên có liên quan của PwC Việt Nam sẽ không gánh chịu hay chấp nhận bất kỳ nghĩa vụ hay trách nhiệm nào đối với Bên Thứ Ba, dù là nghĩa vụ theo hợp đồng hay ngoài hợp đồng (bao gồm nhưng không giới hạn bởi sự bất cẩn và vi phạm các nghĩa vụ theo quy định của pháp luật), và sẽ không chịu trách nhiệm đối với bất kỳ tổn thất, thiệt hại hoặc phí tổn dưới bất kỳ hình thức nào phát sinh bởi hoặc liên quan đến Bên Thứ Ba do việc sử dụng báo cáo này, hoặc bất kỳ hậu quả nào khác do việc Bên Thứ Ba sử dụng báo cáo này. Ngoài ra, Bên Thứ Ba chấp nhận rằng báo cáo này không được dùng để tham chiếu hoặc trích dẫn toàn bộ hoặc từng phần, trong bất kỳ bản cáo bạch, bản đăng ký, tài liệu chào bán, tài liệu công bố ra công chúng, các hồ sơ vay, các thỏa thuận hoặc tài liệu khác và không công bố báo cáo này nếu không được sự chấp thuận trước bằng văn bản của PwC Việt Nam.

Các thông tin, số liệu thống kê và các ý kiến (gọi là "thông tin") trong báo cáo này được thực hiện bởi PwC Việt Nam từ các nguồn tài liệu có sẵn do ABBank cung cấp và trên trang web của ABBank trong khuôn khổ của dự án này và qua các buổi thảo luận được tổ chức với các lãnh đạo Ngân hàng.

PwC Việt Nam lập báo cáo này dựa trên các thông tin nhận được và có được và trên cơ sở rằng các thông tin được cung cấp bởi Ngân hàng là chính xác và hoàn chỉnh. Các thông tin trong báo cáo này không nhằm mục đích kiểm toán, không được sao chép, mô phỏng, phân phát, sử dụng một phần hoặc toàn bộ báo cáo này cho các mục đích khác ngoài mục đích đã được nêu trong Thỏa thuận giữa hai bên về Nội dung công việc thực hiện.

# *Mục lục*

| 1. Giới thiệu mô hình ARIMAX                                    | 4  |
|-----------------------------------------------------------------|----|
| 1.1. Tổng quan về ARIMAX                                        | 4  |
| 1.1.1. Quá trình tự hồi quy AR                                  | 4  |
| 1.1.2. Quá trình trung bình trượt MA                            | 4  |
| 1.1.3. ARIMAX tổng hợp                                          | 4  |
| 2. Quy trình xây dựng mô hình                                   | 6  |
| 2.1. Chuẩn bị dữ liệu                                           | 8  |
| 2.2. Phân khúc và lập giả định                                  | 8  |
| 2.3. Phân tích tương quan                                       | 9  |
| 2.3.1. Lựa chọn các yếu tố phân tích tương quan                 | 11 |
| 2.3.2. Quy trình phân tích tương quan                           | 11 |
| 2.4. Xây dựng mô hình                                           | 12 |
| 2.4.1. Kiểm định tính dừng                                      | 14 |
| 2.4.2. Kiểm định nhân quả (Chỉ áp dụng cho mô hình ARIMAX)      | 16 |
| 2.4.3. Kiểm định đa cộng tuyến (Chỉ áp dụng cho mô hình ARIMAX) | 17 |
| 2.4.4. Ước lượng và kiểm định phần dư                           | 17 |
| 2.5. Kiểm tra hồi tố                                            | 19 |
| 2.6. Bảo trì và rà soát mô hình                                 | 22 |
| 3. Phụ lục – Chi tiết các kiểm định trong mô hình               | 23 |
| 3.1. Kiểm định Augmented Dickey – Fuller (ADF)                  | 23 |
| 3.2. Kiểm định nhân quả Granger                                 | 24 |
| 3.3. Kiểm định Box – Pierce(BP)                                 | 24 |
| 3.4. Kiểm định Jarque – Bera(JB)                                | 24 |
| 3.5. Đánh giá MAPE                                              | 25 |

# <span id="page-3-0"></span>1. Giới thiệu mô hình ARIMAX

Với mục đích phân tích sự ảnh hưởng của các biến kinh tế vĩ mô vào mô hình, PwC giới thiệu phương pháp Hồi quy chuỗi thời gian ARIMAX (Autoregressive integrated moving average with exogenous variable – Tự hồi quy tích hợp trung bình trượt có biến ngoại sinh).

## <span id="page-3-1"></span>1.1. Tổng quan về ARIMAX

Arimax là một phương pháp hồi quy chuỗi thời gian, bao gồm quá trình tự hồi quy (AR – autoregression), quá trình trung bình trượt (MA – moving average) và các biến ngoại sinh (X – exogenous variable, tương ứng với các biến kinh tế vĩ mô đưa vào mô hình).

## <span id="page-3-2"></span>1.1.1. Quá trình tự hồi quy AR

Quá trình tự hồi quy (Auto Regression – AR): là quá trình trong đó một chuỗi chịu ảnh hưởng của chính nó trong quá khứ.

$$Y_{t} = \mu + \alpha_{1}Y_{t-1} + \alpha_{2}Y_{t-2} + \dots + \alpha_{p}Y_{t-p} + \epsilon_{t} = \mu + \sum_{i=1}^{p} \alpha_{i}Y_{t-i} + \epsilon_{t}$$

Một quá trình như trên được gọi là quá trình tự hồi quy bậc p.

Trong đó:

- Y<sub>t</sub> là biến cần dự báo
- Y<sub>t-i</sub> là giá trị trễ i của biến Y, α<sub>i</sub> là hệ số ước lượng tương ứng
- p là bâc của AR
- ε<sub>τ</sub> là phần ngẫu nhiên (error term)

### <span id="page-3-3"></span>1.1.2. Quá trình trung bình trượt MA

Quá trình trung bình trượt (Moving Average– MA): là quá trình trong đó một chuỗi chịu ảnh hưởng của thành phần ngẫu nhiên (error term) trong quá khứ.

$$Y_{t} = \mu + \beta_{1} \varepsilon_{t-1} + \beta_{2} \varepsilon_{t-2} + \dots + \beta_{q} \varepsilon_{t-q} = \mu + \sum_{i=1}^{q} \beta_{i} \varepsilon_{t-i} + \varepsilon_{t}$$

Một quá trình như trên được gọi là quá trình MA(q).

Trong đó:

- Y<sub>t</sub> là biến cần dự báo
- ε<sub>t</sub> là phần ngẫu nhiên (error term)
- $\epsilon_{t-i}$  là giá trị trễ i của phần ngẫu nhiên  $\epsilon_t$ ,  $\beta_i$  là hệ số ước lượng tương ứng
- q là bậc của MA

## <span id="page-3-4"></span>1.1.3. ARIMAX tổng hợp

Kết hợp 2 quá trình AR, MA và các biến ngoại sinh X (các yếu tố kinh tế vĩ mô) ta sẽ được mô hình ARIMAX:

$$Y_t = AR(p) + MA(q) + X + \epsilon_t$$
  

$$Y_t = \sum_{i=1}^{p} \alpha_i Y_{t-i} + \sum_{i=1}^{q} \beta_i \epsilon_{t-i} + \sum_{i=1}^{n} \gamma^i X_t^i + \epsilon_t$$

Trong đó:

X<sub>t</sub><sup>i</sup> là biến ngoại sinh thứ i. γ<sub>t</sub><sup>i</sup> là hệ số ước lượng tương ứng

Điều kiên:

Mô hình có thể được ước lượng nếu thỏa mãn điều kiện  $\varepsilon_{t}$  là nhiễu trắng, tức là:

- ε<sup>t</sup> có kì vọng = 0
- ε<sup>t</sup> có phương sai không đổi theo thời gian.
- ε<sup>t</sup> không tự tương quan với chính nó.

Và các biến ngoại sinh X không có hiện tượng đa cộng tuyến, tức là các biến X không tương quan chặt với nhau.

Khi các điều kiện trên thỏa mãn, ta sẽ có ước lượng điểm không chệch của các hệ số ước lượng α<sup>i</sup> , β<sup>i</sup> , γ i , từ đó dự báo cho biến Y.

# <span id="page-5-0"></span>*2. Quy trình xây dựng mô hình*

Sơ đồ dưới đây thể hiện quy trình tổng thể cho quản trị mô hình từ bước bắt đầu xây dựng cho đến bước cập nhật và duy trì mô hình, cùng với vai trò của các phòng/ban/đơn vị liên quan tương ứng với từng giai đoạn triển khai.

(\*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trạng hỗ trợ từ cơ sở hạ tầng dữ liệu của Ngân hàng.

| Bước | Trách nhiệm | Các bước thực hiện                                                           | Tài liệu<br>liên quan | Thời gian           |
|------|-------------|------------------------------------------------------------------------------|-----------------------|---------------------|
| 1    | XDMH & CBDL | Chuẩn bị dữ liệu                                                             |                       | Định kỳ<br>hàng quý |
| 2    | XDMH & KKD  | Phân khúc và lập giả định                                                    |                       | Định kỳ<br>hàng quý |
| 3    | XDMH & KKD  | Phân tích tương quan và<br>lựa chọn phương pháp<br>XDMH                      |                       | Định kỳ<br>hàng quý |
| 4    | XDMH        | Xây dựng mô hình                                                             |                       | Định kỳ<br>hàng quý |
| 5    | XDMH & CBDL | Kiểm tra hồi tố mô hình<br>KHÔNG<br>ĐẠT<br>Phương pháp<br>phi tham số<br>ĐẠT |                       | Định kỳ<br>hàng quý |
| 6    | XDMH & CBDL | Bảo trì và rà soát mô<br>hình                                                |                       | Định kỳ<br>hàng quý |

| STT       | Công việc                     | Đơn vị | Khi nào             | Cách làm                                                                                                                                                             |
|-----------|-------------------------------|--------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bước<br>1 | Chuẩn bị<br>dữ<br>liệu        | XDMH   | Định kỳ<br>hàng quý | •<br>Chuẩn bị<br>yêu cầu dữ<br>liệu<br>•<br>Kiểm tra và phát hiện vấn đề<br>dữ<br>liệu, nếu có                                                                       |
|           |                               | CBDL   | Định kỳ<br>hàng quý | •<br>Thu thập dữ<br>liệu theo yêu cầu                                                                                                                                |
| Bước<br>2 | Phân khúc và lập giả<br>định  | XDMH   | Định kỳ<br>hàng quý | •<br>Xác định các tiêu chí phân khúc mô hình cần thiết<br>•<br>Lập giả<br>định cần thiết cho mô hình<br>•<br>Thực hiện phân khúc và triển khai dữ<br>liệu            |
|           |                               | KKD    | Định kỳ<br>hàng quý | •<br>Mô tả<br>nhu cầu nghiệp vụ<br>•<br>Phối hợp với đội ngũ XDMH để<br>phân tích các nhu<br>cầu nghiệp vụ                                                           |
| Bước<br>3 | Phân<br>tích<br>tương<br>quan | XDMH   | Định kỳ<br>hàng quý | •<br>Xác định các yếu tố<br>vĩ mô chính chi phối hành vi<br>khách hàng<br>•<br>Thực hiện phân tích tương quan<br>•<br>Lựa chọn phương pháp xây dựng mô hình          |
|           |                               | KKD    |                     | •<br>Phối hợp với đội ngũ xây dựng mô hình để<br>xác<br>định các yếu tố<br>vĩ mô chính                                                                               |
| Bước<br>4 | Xây dựng mô hình              | XDMH   | Định kỳ<br>hàng quý | •<br>Xây dựng mô hình dựa trên đặc tính sản phẩm                                                                                                                     |
| Bước<br>5 | Kiểm tra hồi tố mô<br>hình    | XDMH   | Định kỳ<br>hàng quý | •<br>Thực hiện kiểm tra hồi tố<br>và phân tích kết quả<br>•<br>Thực hiện lại mô hình theo phương pháp khác<br>(phi<br>tham số) nếu như kết quả<br>kiểm tra không đạt |
|           |                               | CBDL   | Định kỳ<br>hàng quý | •<br>Thu thập dữ<br>liệu kiểm tra hồi tố                                                                                                                             |
| Bước<br>6 | Bảo trì và rà soát mô<br>hình | XDMH   | Định kỳ<br>hàng quý | •<br>Tái vận hành mô hình trên bộ<br>dữ<br>liệu cập nhật<br>•<br>Đánh giá kết quả<br>mô hình tại từng lần tái vận hành                                               |
|           |                               | CBDL   | Định kỳ<br>hàng quý | •<br>Thu thập dữ<br>liệu cập nhật theo yêu cầu                                                                                                                       |

## <span id="page-7-0"></span>*2.1. Chuẩn bị dữ liệu*

Phương pháp cho bước **Chuẩn bị và triển khai dữ liệu** được trình bày trong tài liệu phương pháp phi tham số.

Tài liệu này sẽ không trình bày lại về bước này mà tập trung vào phương pháp luận cho mô hình ARIMAX

### <span id="page-7-1"></span>*2.2. Phân khúc và lập giả định*

Phương pháp cho bước **Phân khúc và lập giả định** được trình bày trong tài liệu phương pháp phi tham số. Tài liệu này sẽ không trình bày lại về bước này mà tập trung vào phương pháp luận cho mô hình ARIMAX.

### <span id="page-8-0"></span>*2.3. Phân tích tương quan*

Sơ đồ dưới đây thể hiện quy trình phân tích tương quan để lựa chọn phương pháp xây dựng mô hình cho từng phân khúc của mô hình Tiền gửi CKH.

![](_page_8_Figure_2.jpeg)

Từng mô hình sẽ có những ưu điểm và hạn chế theo như phân tích dưới đây

### **Mô hình phi tham số**

- ✓ Mô hình có phương pháp luận đơn giản, trực quan và có thể áp dụng dễ dàng.
- ✓ Các bước tính toán trong mô hình được thực hiện đơn giản.
- ✓ Phương pháp đã được chấp nhận và thực hiện ở nhiều ngân hàng với quy mô khác nhau trong nước, trong khu vực và trên toàn thế giới.
- × Phương pháp không thể hiện rõ các yếu tố ngoại sinh vì đã giả định rằng tác động của những yếu tố này được thể hiện trong biến động số dư của danh mục.

## **Mô hình tham số**

- ✓ Phương pháp được áp dụng tại nhiều ngân hàng trong và ngoài nước với quy mô khác nhau
- × Phương pháp luận xây dựng mô hình và các bước tính toán trong mô hình được thực hiện tương đối phức tạp.

# <span id="page-10-0"></span>2.3.1. Lựa chọn các yếu tố phân tích tương quan

Phân tích tương quan nhằm xác định mức độ của mối tương quan giữa phân khúc cần xây dựng mô hình và các biến động từ các yếu tố ngoại sinh, từ đó lựa chọn phương pháp xây dựng mô hình phù hợp ở các bước tiếp theo.

Các yếu tố phổ biến (bao gồm yếu tố kinh tế vĩ mô và dữ liệu thị trường) được lựa chọn để phân tích tương quan

- Tỷ giá ngoại tệ (VND/USD)
- · Giá vàng
- Chỉ số VNINDEX
- Lãi suất thi trường liên ngân hàng
- Lãi suất trái phiếu chính phủ
- · Giá tri GDP
- Tỷ lệ thất nghiệp
- Tỷ lệ lạm phát
- Lãi suất tiền gửi các ngân hàng khác

Dữ liệu của các yếu tổ được lựa chọn trên nên được thu thập ở tần suất hàng ngày hoặc tần suất nhỏ nhất có thể

### <span id="page-10-1"></span>2.3.2. Quy trình phân tích tương quan

Chuỗi hành vi theo dõi được lấy là tỷ lệ biến động số dư theo ngày

$$Rate(t) = \frac{(Balance_{t} - Balance_{t-1})}{Balance_{t-1}}$$

Cách tính toán các biến trên được trình bày cụ thể trong tài liệu phương pháp luận tương ứng.

Phân tích tương quan được thực hiện trên bộ các yếu tố lựa chọn với từng phân khúc cần xây dựng mô hình, và được thực hiện theo từng lần tái vân hành mô hình.

Với từng phân khúc, chuỗi hành vi theo ngày sẽ được phân tích tương quan với từng yếu tố vĩ mô/thị trường theo công thức

$$\text{Correlation(rate,y)} = \frac{\sum_{i=1}^{n} (\text{rate}_i - \overline{\text{rate}})(y_i - \overline{y})}{\sqrt{\sum_{i=1}^{n} (\text{rate}_i - \overline{\text{rate}})^2 \sum_{i=1}^{n} (y_i - \overline{y})^2}}$$

Với:

Correlation: Hê số tương quan

rate: chuỗi hành vi ngày trong từng phân khúc

y: chuỗi giá trị dữ liệu hàng ngày của yếu tố vĩ mô/thị trường cần phân tích tương quan

rate : giá trị trung bình của chuỗi rate v̄ : giá trị trung bình của chuỗi y

• Dựa trên kết quả phân tích tương quan, các chuỗi dữ liệu yếu tố vĩ mà có hệ số tương quan cao (>40% hoặc <-40%) sẽ được đưa vào mô hình.

Ví du minh hoa

| Ngày     | Tỷ lệ trả trước hạn |
|----------|---------------------|
| 1/4/2018 | 20%                 |
| 2/4/2018 | 8.33%               |
| 3/4/2018 | 18.2%               |

| Ngày     | Lãi suất tiền gửi ngân hàng A |
|----------|-------------------------------|
| 1/4/2018 | 2%                            |
| 2/4/2018 | 3.33%                         |
| 3/4/2018 | 4.2%                          |

Hệ số tương quan trong chuỗi quan sát 3 ngày có thể được tính theo hàm công thức CORREL trong excel, với công thức tương tự

CORREL(Chuỗi Runoff, Chuỗi y) = - 100%

Với kết quả hệ số tương quan là -100% và nhỏ hơn -40%, ta có thể kết luận rằng chuỗi tỷ lệ trả trước hạn và lãi suất tiền gửi ở ngân hàng A trong 3 ngày có tương quan với nhau.

### <span id="page-11-0"></span>*2.4. Xây dựng mô hình*

Sau khi đã xác định được các biến được đưa vào mô hình tại bước phân tích tương quan, ghép chuỗi hành vi và các chuỗi kinh tế vĩ mô có tương quan vào thành một bộ dữ liệu. Dữ liệu 5 năm được chia thành dữ liệu nghiên cứu (4 năm đầu) và dữ liệu kiểm tra (1 năm cuối).

**Quy trình cho mô hình ARIMAX** được chia thành 5 bước, trong đó 4 bước đầu sử dụng dữ liệu nghiên cứu xây dựng mô hình và so sánh kết quả với số liệu thực tế của dữ liệu kiểm tra tại bước 5: kiểm tra hồi tố.

![](_page_11_Figure_3.jpeg)

Trong mô hình ARIMAX, chuỗi hành vi được coi như biến cần được dự báo (Y) trong mô hình, trong khi các chuỗi kinh tế vĩ mô là các biến ngoại sinh (X).

**Quy trình cho mô hình ARIMA** được chia thành 3 bước, trong đó 2 bước đầu sử dụng dữ liệu nghiên cứu xây dựng mô hình và so sánh kết quả với số liệu thực tế của dữ liệu kiểm tra tại bước 3: kiểm tra hồi tố.

![](_page_12_Figure_1.jpeg)

Trong mô hình ARIMA, chuỗi hành vi được coi như biến cần được dự báo (Y) trong mô hình và không có các biến ngoại sinh (X) nào.

## <span id="page-13-0"></span>*2.4.1. Kiểm định tính dừng*

Định nghĩa chuỗi dừng (Stationary series): Một chuỗi dừng là khi:

- 1. Có trung bình và phương sai không đổi theo thời gian
- 2. Không có hiện tượng tự tương quan

Dưới đây là ví dụ của một chuỗi dừng:

![](_page_13_Figure_5.jpeg)

Ví dụ về chuỗi trung bình thay đổi theo thời gian

![](_page_13_Figure_7.jpeg)

Ví dụ về chuỗi phương sai thay đổi theo thời gian

![](_page_13_Figure_9.jpeg)

Ví dụ về chuỗi tự tương quan

![](_page_13_Figure_11.jpeg)

Trong mô hình chuỗi thời gian, tính dừng được xem như ổn định và có thể dự báo (có quy luật). Nếu các chuỗi đưa vào mô hình (Chuỗi hành vi hoặc kinh tế vĩ mô) không dừng, cần biến đổi để các chuỗi dừng.

Sai phân: Sai phân của một chuỗi y có dạnh như sau:

Bậc 1:  $\Delta y_t = y_t - y_{t-1}$ Bậc d:  $\Delta^d y_t = \Delta^{d-1} y_t - \Delta^{d-1} y_{t-1}$ 

![](_page_14_Figure_3.jpeg)

Các ước lượng ARIMAX của biến sai phân bằng với ước lượng của biến gốc, và các chuỗi sai phân thường sẽ dừng. Đây là phương pháp để khắc phục khi các chuỗi đầu vào không dừng. Mục đích của bước này là tìm được bậc sai phân mà trong đó tất cả các biến đều dừng. Bậc sai phân d khi tất cả các chuỗi dừng là tham số integrated trong mô hình ARIMAX.

Quy trình Kiểm đinh tính dừng:

Tính dừng được kiểm định bằng kiểm định ADF (Augmented Dickey – Fuller test)

1. Kiểm định tính dừng biến hành vi và kinh tế vĩ mô với 95% độ tin cậy.

Giả thiết H0: biến không dừng

Giả thiết H1: biến dừng

p-value ≤ 0.05 thì bác bỏ H0 và thừa nhân biến dừng

2. Nếu có một chuỗi không dừng, sai phân tất cả các chuỗi và lặp lại kiểm định đến khi tất cả các chuỗi đầu vào dừng. Xác định d.

Tham khảo phu luc 3.1. Kiểm định Augmented Dickey – Fuller (ADF) về kiểm định chi tiết

#### Ví du:

P-value của kiểm định ADF được tính trong R bằng code:

adf.test(x)\$p.value

#thay x bằng chuỗi cần kiểm định

|   | Biến Y    | Sai phân<br>bậc 1             | Sai phân<br>bậc 2     | Sai phân<br>bậc 3             |
|---|-----------|-------------------------------|-----------------------|-------------------------------|
|   | $Y_{t-1}$ | $A_{t}$ $= Y_{t}$ $- Y_{t-1}$ | $B_t = A_t - A_{t-1}$ | $C_{t}$ $= B_{t}$ $- B_{t-1}$ |
| 1 | 6250001   |                               |                       |                               |
| 2 | 6765201   | 515200.1                      |                       |                               |
| 3 | 7311617   | 546416.3                      | 31216.22              |                               |
| 4 | 7890481   | 578864                        | 32447.72              | 1231.497                      |

|      | Biến Y        | Sai phân          | Sai phân          | Sai phân          |
|------|---------------|-------------------|-------------------|-------------------|
| 5    | 8503056       | bậc 1<br>612574.8 | bậc 2<br>33710.79 | bậc 3<br>1263.068 |
| 6    | 9150626       | 647569.3          | 34994.49          | 1283.704          |
| 7    | 9834495       | 683869.1          | 36299.81          | 1305.323          |
| 8    | 10556000      | 721505.6          | 37636.44          | 1336.625          |
| 9    | 11316498      | 760497.6          | 38992.06          | 1355.619          |
| 10   | 12117361      | 800863.2          | 40365.61          | 1373.548          |
| 11   | 12960002      | 842640.7          | 41777.48          | 1411.871          |
| 12   | 13845840      | 885838.7          | 43197.97          | 1420.494          |
| 13   | 14776335      | 930494.8          | 44656.13          | 1458.155          |
| 14   | 15752962      | 976627            | 46132.16          | 1476.031          |
| 15   | 16777216      | 1024253           | 47626.42          | 1494.263          |
| 16   | 17850625      | 1073409           | 49155.77          | 1529.347          |
| 17   | 18974737      | 1124112           | 50703.25          | 1547.481          |
| 18   | 20151119      | 1176382           | 52269.58          | 1566.337          |
| 19   | 21381376      | 1230256           | 53874.5           | 1604.914          |
| 20   | 22667120      | 1285744           | 55487.98          | 1613.478          |
| 21   | 24010000      | 1342880           | 57135.23          | 1647.251          |
| 22   | 25411681      | 1401681           | 58801.36          | 1666.136          |
| 23   | 26873856      | 1462176           | 60494.68          | 1693.316          |
| 24   | 28398242      | 1524386           | 62209.8           | 1715.118          |
| 25   | 29986575      | 1588333           | 63947.75          | 1737.949          |
| 26   | 31640625      | 1654050           | 65716.39          | 1768.646          |
| 27   | 33362178      | 1721553           | 67503.31          | 1786.916          |
| 28   | 35153042      | 1790865           | 69311.55          | 1808.244          |
| 29   | 37015056      | 1862013           | 71148.67          | 1837.116          |
| 30   | 38950083      | 1935027           | 73013.97          | 1865.295          |
| 31   | 40960000      | 2009917           | 74889.92          | 1875.958          |
| Adf  | 0.99          | 0.99              | 0.99              | 0.01              |
| test |               |                   |                   |                   |
|      | Không<br>dừng | Không<br>dừng     | Không<br>dừng     | Dừng              |

# <span id="page-15-0"></span>*2.4.2. Kiểm định nhân quả (Chỉ áp dụng cho mô hình ARIMAX)*

Kiểm định nhân quả sử dụng kiểm định Granger, nhằm mục đích đảm bảo các chuỗi kinh tế vĩ mô có năng lực dự báo với chuỗi hành vi. Kiểm định cho biết một biến X có tác động (granger cause) đến biến Y hay không Quy trình kiểm định nhân quả

1. Kiểm định nhân quả của từng chuỗi kinh tế vĩ mô (X) đến chuỗi hành vi (Y) với 95% độ tin cậy. Giả thiết H0: biến X không ảnh hưởng đến biến Y

Giả thiết H1: biến X ảnh hưởng đến biến Y

p-value ≤ 0.05 thì bác bỏ H0, chấp nhận biến X trong mô hình

2. Loại bỏ các biến không ảnh hưởng đến Y và đưa bộ dữ liệu mới vào bước tiếp theo

Tham khảo phụ lục 3.2. Kiểm định nhân quả Granger về kiểm định chi tiết

Ví dụ:

Kiểm định Granger cho chuỗi drawdown của tiền gửi có kì hạn (chuỗi hành vi – runoff) với chỉ số VNINDEX và lãi suất VNIBOR 6 tháng

Code: grangertest(runoff, vnindex, order = 365)\$`Pr(>F)`[2]

P-value kiểm định chuỗi drawdown với VNINDEX = 2.6432E-10 < 0.05

⇒ Giữ chuỗi VNINDEX trong mô hình

Code: grangertest(runoff, vnibor\_6m, order = 365)\$`Pr(>F)`[2]

P-value kiểm định chuỗi drawdown với VNIBOR 6M = 0.283017295 > 0.05

⇒ Loại chuỗi VNIBOR\_6M ra khỏi mô hình

# <span id="page-16-0"></span>2.4.3. Kiểm định đa cộng tuyến (Chỉ áp dụng cho mô hình ARIMAX)

Đa cộng tuyến: Là hiện tượng một biến ngoại sinh có thể được tổng hợp từ các biến ngoại sinh còn lại.

Ví dụ  $\{X_t^1, X_t^2, ..., X_t^n\}$  là các biến được đưa vào mô hình. Nếu phương trình

 $X_t^1 = \alpha_0 + \alpha_2 X_t^2 + \dots + \alpha_3 X_t^n$  có ý nghĩa, tức các biến  $X_t^2, \dots X_t^n$  có thể giải thích cho  $X_t^1$ , thì mô hình có hiện tượng đa công tuyến.

Các biến gây ra đa cộng tuyến cao cần được loại bỏ khỏi mô hình.

Quy trình kiểm định đa cộng tuyến:

1. Hồi quy từng biến ngoại sinh X với các biến ngoại sinh còn lại và lấy giá trị R<sup>2</sup>:

$$\begin{array}{lll} X_t^1 = & \alpha_0 + \alpha_2 X_t^2 + \alpha_3 X_t^3 + \cdots + \ \epsilon \longrightarrow R_1^2 \\ X_t^2 = & \alpha_0 + \alpha_1 X_t^1 + \alpha_3 X_t^3 + \cdots + \ \epsilon \longrightarrow R_2^2 \end{array}$$

...

- 2. Tính giá trị  $VIF_i = \frac{1}{1-R_i^2}$  cho mỗi giá trị  $R^2$ .
- 3. Nếu  $VIF_i \ge 5$  thì có hiện tượng đa cộng tuyến giữa biến  $X_t^i$  với các biến còn lại. Loại bỏ  $X_t^i$  và lặp lại bước 1
- 4. Khi không còn hiện tượng đa cộng tuyến (tất cả  $VIF_i < 5$ ), các biến còn lại sẽ được đưa vào mô hình

Ví dụ: Với VNINDEX và VNIBOR\_6M, VNIBOR\_12M là 3 biến vĩ mô được đưa vào mô hình Hồi quy 3 phương trình

```
\begin{array}{l} \text{VNINDEX} = \ \alpha_0 + \alpha_1 \text{VNIBOR\_6M} + \alpha_2 \text{VNIBOR\_12M} + \epsilon \rightarrow \text{VIF}_{vnindex} = 2.34 \\ \text{VNIBOR\_6M} = \ \alpha_0 + \alpha_1 \text{VNINDEX} + \alpha_2 \text{VNIBOR\_12M} + \epsilon \rightarrow \text{VIF}_{vnibor\_6m} = 5.24 \\ \text{VNIBOR\_12M} = \ \alpha_0 + \alpha_1 \text{VNINDEX} + \alpha_2 \text{VNIBOR\_6M} + \epsilon \rightarrow \text{VIF}_{vnbor\_12m} = 6.34 \\ \end{array}
```

Có  $VIF_{vnibor\_6m} = 5.24 > 5$  và  $VIF_{vnbor\_12m} = 6.34 > 5$ , bỏ biến  $VNIBOR\_12M$  có VIF cao nhất và hồi quy lại  $VNINDEX = \alpha_0 + \alpha_1 VNIBOR\_6M + \epsilon \rightarrow VIF_{vnindex} = 1.34$   $VNIBOR\_6M = \alpha_0 + \alpha_1 VNINDEX + \epsilon \rightarrow VIF_{vnibor_6m} = 2.54$ 

⇒ Loai bỏ VNIBOR 12M và đưa 2 biến còn lai vào tổ hợp các biến kinh tế vĩ mô cho bước sau

Tổng hợp các tổ hợp có thể có của X:

Nếu có nhiều hơn 1 biến X được đưa vào mô hình, cần tổng hợp các tổ hợp của X. Xây dựng mô hình với từng tổ hợp và chon ra 1 tổ hợp với kết quả dự báo tốt nhất làm mô hình chính.

Ví du: Với VNINDEX và VNIBOR 6M là 2 biến vĩ mô được đưa vào mô hình. Các tổ hợp của X bao gồm

- VNINDEX
- VNIBOR
- VNINDEX, VNIBOR

# <span id="page-16-1"></span>2.4.4. Ước lượng và kiểm định phần dư

Xác định p, q: Các tham số p, q là bậc hồi quy của mô hình ARIMAX

AIC – Akaike Information Criteria là chỉ số xác định đô mất thông tin của một mô hình. Với d đã biết từ bước 1, lấy giá tri lớn nhất của p, q là 10, hồi quy ARIMA (không có biến ngoại sinh) để tìm chỉ số AIC của mỗi tổ hợp p, q và chọn 5 tố hợp (p, q) có AIC nhỏ nhất.

Giá trị lớn nhất của p, q càng nhiều thì càng có nhiều tổ hợp mô hình. Mặc định giá trị lớn nhất của p, q là 10, tuy nhiên Ngân hàng có thể lựa chọn giá trị tùy theo năng lực tính toán của hệ thống.

Ví dụ:

Có d = 1, p, q lớn nhất bằng 5, ta sẽ có 5 mô hình ARIMAX là:

| AIC   | p = 1 | p = 2 | p = 3 | p = 4 | p = 5 |
|-------|-------|-------|-------|-------|-------|
| q = 1 | 109   | 100   | 106   | 110   | 100   |
| q = 2 | 109   | 109   | 110   | 109   | 108   |
| q = 3 | 107   | 105   | 109   | 108   | 108   |
| q = 4 | 105   | 105   | 102   | 101   | 103   |
| q = 5 | 104   | 110   | 107   | 108   | 101   |

Với d = 1, ta sẽ có 5 mô hình ARIMAX ARIMAX(p,d,q) là: (Đối với mô hình ARIMA, bỏ các tổ hợp X)

- $\begin{array}{lll} \text{ARIMAX}(5,1,1): \Delta^{1}Y_{t} = & \sum_{i=1}^{5} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{1} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(5,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{5} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(5,1,5): \Delta^{1}Y_{t} = & \sum_{i=1}^{5} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{5} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(4,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{4} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t} = & \sum_{i=1}^{4} \alpha_{i}\Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i}\epsilon_{t-i} + \sum_{i=1}^{4} \gamma^{i}\Delta^{1}X_{t}^{i} + \epsilon_{t} \\ \text{ARIMAX}(2,1,4): \Delta^{1}Y_{t$

- ARIMAX(3,1,4):  $\Delta^{1}Y_{t} = \sum_{i=1}^{3} \alpha_{i} \Delta^{d}Y_{t-i} + \sum_{i=1}^{4} \beta_{i} \epsilon_{t-i} + \sum_{i=1}^{n} \gamma^{i} \Delta^{1}X_{t}^{i} + \epsilon_{t}$

Xác định các tổ hợp của mô hình: Với từng tổ hợp (p, q), kết hợp với các tổ hợp của X tạo thành 1 tổ hợp mô hình.

Ví du:

Kết hợp (p.d.g) = (5.1.1) với các tổ hợp X của ví du phần kiểm định đa công tuyến tạ có 3 mô hình; (Đối với mô hình ARIMA bỏ các tổ hợp X)

- $ARIMAX(5,1,1) + X_t^1$
- $ARIMAX(5,1,1) + X_t^2$
- $ARIMAX(5,1,1) + X_{t}^{1}, X_{t}^{2}$

Phần dư của mô hình: Xét mô hình ARIMAX (Đối với mô hình ARIMA bỏ các tổ hợp X)

$$\textbf{Y}_t = \sum_{i=1}^p \alpha_i \textbf{Y}_{t-i} + \sum_{i=1}^q \beta_i \epsilon_{t-i} + \sum_{i=1}^n \gamma^i \textbf{X}_t^i + \epsilon_t$$

Gọi Ŷ<sub>t</sub> là ước lượng của mô hình

$$\widehat{Y}_t = \sum_{i=1}^p \alpha_i Y_{t-i} + \sum_{i=1}^q \beta_i \epsilon_{t-i} + \sum_{i=1}^n \gamma^i X_t^i$$

$$Y_t = \widehat{Y}_t + \varepsilon_t$$

Phần dư, tức sai số ngẫu nhiên ước lượng  $\hat{\epsilon}_t = Y_t - \hat{Y}_t$  cần phải là nhiễu trắng để ước lượng là ước lượng khôna chệch.

Các kiểm định sau khi chạy mô hình nhằm kiểm tra phần dư có phải là nhiễu trắng không.

Quy trình ước lượng mô hình (Đối với mô hình ARIMA bỏ các tổ hợp X)

- 1. Xác định các tổ hợp (p, q) với AIC nhỏ nhất
- 2. Kết hợp các tổ hợp (p, q) với các tổ hợp X tạo thành các tổ hợp mô hình
- 3. Ước lượng mỗi tố hợp
- 4. Kiểm định tính dừng cho phần dư

Kiếm định ADF cho phần dư tương tự như kiếm định biến đầu vào của bước 1.

Nếu phần dư không dừng, loại bỏ tố hợp mô hình

5. Kiếm định tư tương quan của phần dư

Kiếm định Box - Pierce (BP - test)

H0: Phần dư không có tự tương quan

H1: Phần dư có tự tương quan

p – value > 0.05, chấp nhận H0, phần dư không có tự tương quan

Nếu phần dư có tự tương quan, loại bỏ mô hình

6. Kiểm định phân phối chuẩn của phần dư

Kiểm định Jarque – Bera (JB)

H0: Phần dư phân phối chuẩn

H1: Phần dư không phân phối chuẩn

p – value > 0.05, chấp nhận H0, phần dư phân phối chuẩn

Nếu phần dư không phân phối chuẩn, loại bỏ mô hình

7. Kết quả cuối cùng bao gồm tất cả các tổ hợp thỏa mãn cùng phương trình ước lượng tương ứng

Tham khảo phụ lục 3.3. Kiểm định Box – Pierce(BP) và phụ lục 3.4. Kiểm định Jarque – Bera(JB) về kiểm định chi tiết

### <span id="page-18-0"></span>2.5. Kiểm tra hồi tố

#### Kiểm tra hồi tố:

Từ tất cả các tổ hợp đạt kiểm định tại bước 4, ta sẽ có bấy nhiều phương trình. Từ các phương trình trên dự báo cho 1 năm tiếp theo (năm thứ 5) và kiểm tra hồi tố bằng cách so sánh dư báo của mỗi phương trình với dữ liêu thực tế năm thứ 5 (dữ liêu kiểm tra).

Tính chỉ số MAPE (Mean Absolute Percentage Error) cho từng kết quả dự báo:

MAPE = 
$$\frac{100\%}{m} \sum_{i=1}^{m} \left| \frac{A_i - F_i}{A_i} \right|$$

Trong đó

m là số điểm dự báo (tương ứng với 1 năm)

A, là giá tri thực tế của điểm i

F, là giá tri dư báo của điểm i

Chỉ số MAPE thể hiện năng lực dự báo của mô hình, MAPE > 50% thể hiện dự báo kém và thiếu chính xác. Lấy phương trình với kết quả dự báo cho ra MAPE nhỏ nhất làm kết quả cuối cùng của mô hình. Nếu kết quả cuối cùng có MAPE > 50% thì Ngân hàng cần cân nhắc lưa chon phương pháp phi tham số hoặc phương pháp mô hình khác có thể dự báo chính xác hơn.

Trong thực te neu chươi nam vi có giá si, s, WAPE (Weighted Absolute Percentage Error) thay thế:  $WAPE = \frac{\sum_i^m |A_i - F_i|}{\sum_i^m |A_i|}$ Trong thực tế nếu chuỗi hành vi có giá trị 0, tức tồn tại  $A_i = 0$  thì sẽ không thể dùng MAPE. Khi đó ta sử dụng

WAPE = 
$$\frac{\sum_{i=1}^{m} |A_i - F_i|}{\sum_{i=1}^{m} |A_i|}$$

Wi du

| vi dụ. |          |       |       |                           |           |                     |
|--------|----------|-------|-------|---------------------------|-----------|---------------------|
|        |          | ACTUA |       |                           |           |                     |
|        | FORECAST | L     | С     | WAPE                      | D         | MAPE                |
|        | F        | Α     | A - F | =SUM(ABS(C))/SUM(ABS(A) ) | (A - F)/A | =SUM(ABS(D))/2<br>8 |
| 1      | 0.82     | 0.65  | -0.17 | 43.17%                    | -0.27     | 58.88%              |
| 2      | 0.31     | 0.27  | -0.05 |                           | -0.17     |                     |
| 3      | 0.19     | 0.61  | 0.42  |                           | 0.68      |                     |
| 4      | 0.02     | 0.09  | 0.07  |                           | 0.76      |                     |
| 5      | 0.20     | 0.21  | 0.01  |                           | 0.06      |                     |
| 6      | 0.68     | 0.47  | -0.21 |                           | -0.43     |                     |
| 7      | 0.35     | 0.71  | 0.36  |                           | 0.50      |                     |
| 8      | 0.83     | 0.81  | -0.02 |                           | -0.03     |                     |
| 9      | 0.76     | 0.15  | -0.61 |                           | -4.09     |                     |
| 10     | 0.20     | 0.65  | 0.45  |                           | 0.69      |                     |
| 11     | 0.56     | 0.87  | 0.31  |                           | 0.35      |                     |

|    | FORECAST | ACTUA<br>L | C     | WAPE | D     | MAPE |
|----|----------|------------|-------|------|-------|------|
| 12 | 0.27     | 0.40       | 0.13  |      | 0.32  |      |
|    |          |            |       |      |       |      |
| 13 | 0.62     | 0.62       | 0.00  |      | -0.01 |      |
| 14 | 0.88     | 0.64       | -0.24 |      | -0.37 |      |
| 15 | 0.62     | 0.74       | 0.12  |      | 0.16  |      |
| 16 | 0.01     | 0.08       | 0.07  |      | 0.90  |      |
| 17 | 0.21     | 0.91       | 0.70  |      | 0.77  |      |
| 18 | 0.08     | 0.28       | 0.19  |      | 0.70  |      |
| 19 | 0.42     | 0.25       | -0.17 |      | -0.66 |      |
| 20 | 0.89     | 0.85       | -0.05 |      | -0.06 |      |
| 21 | 0.68     | 0.35       | -0.33 |      | -0.96 |      |
| 22 | 0.76     | 0.65       | -0.11 |      | -0.16 |      |
| 23 | 0.62     | 0.62       | 0.00  |      | 0.00  |      |
| 24 | 0.92     | 0.34       | -0.58 |      | -1.72 |      |
| 25 | 0.88     | 0.62       | -0.26 |      | -0.42 |      |
| 26 | 0.49     | 0.51       | 0.02  |      | 0.04  |      |
| 27 | 0.07     | 0.24       | 0.17  |      | 0.72  |      |
| 28 | 0.44     | 0.86       | 0.42  |      | 0.49  |      |

Như ví dụ trên thì kết quả sẽ là "ĐẠT" với WAPE và "KHÔNG ĐẠT" với MAPE.

#### Dự báo

Nếu kiểm tra hồi tố ra kết quả "đạt", sử dụng phương trình với số liệu của toàn bộ 5 năm để dự báo cho 1 năm tiếp theo (năm thứ 6).

Dự báo cho các biến kinh tế vĩ mô:

Để xác định chuỗi hành vi trong tương lại, ta cần dự báo các biến kinh tế vĩ mô trong tương lai.

Các dự báo này nên được lấy tại các nguồn sau, theo thứ tự từ trên xuống dưới:

- Nguồn tổng hợp từ nội bộ Ngân hang
- Các tổ chức kinh tế có dự báo (World Bank, Reuter, IMF,…)
- Dự báo ARIMA từ chuỗi dữ liệu quá khứ

Hiện tại, trong mô hình giao phẩm, các biến kinh tế vĩ mô đang được dự báo giản đơn bằng ARIMA. Tuy nhiên trong tương lại, PwC khuyến nghị Ngân hàng nên lấy các nguồn trên để đảm bảo tính chính xác của dự báo.

Đưa chuỗi tỷ lệ theo ngày về các dải kì hạn:

Dòng tiền sau điều chỉnh hành vi được phân bổ lại vào các dải kỳ hạn tương ứng như sau

| Dải kì hạn | Qua đêm | 2-7D | 8-30D | 31-90D | 91-180D | 181-360D |
|------------|---------|------|-------|--------|---------|----------|
| Số<br>ngày | 1       | 7    | 30    | 90     | 180     | 360      |

Giả sử có dự báo {Ŷt+1 , … , Ŷt+365} Dải kì hạn b có giá trị cộng dồn:

$$Runoff_b = 1 - \prod_{i=1}^{b} (1 - \widehat{Y}_{t+i})$$

Ví dụ

| i | Y dự báo | 1-Y dự báo |
|---|----------|------------|
| 1 | 0.21     | 0.79       |
| 2 | 0.16     | 0.84       |
| 3 | 0.12     | 0.88       |

| 4 | 0.05 | 0.95 |
|---|------|------|
| 5 | 0.05 | 0.95 |
| 6 | 0.07 | 0.93 |
| 7 | 0.14 | 0.86 |
| 8 | 0.09 | 0.91 |

Dải kì hạn 1 ngày (b = 1) có giá trị dòng tiền ra cộng dồn = 1 – 0.79 = 0.21 Dải kì hạn 2 – 7 ngày (b = 7) có giá trị dòng tiền ra cộng dồn = 1 – 0.79\*0.84\*0.88\*0.95\*0.95\*0.93\*0.86 = 0.58

Giá trị không cộng dồn của dòng tiền sẽ có giá trị:

Outflow<sup>b</sup> = MIN{0, (Runoff<sup>b</sup> − MIN{Runoff<sup>i</sup> | i < b})}

Ví dụ: Với dải kì hạn bao gồm 3 mức

|                | ON     | 2 – 7D | 8 – 30D |
|----------------|--------|--------|---------|
| Cộng dồn       | 40.28% | 44.50% | 37.29%  |
| Không cộng dồn | 40.28% | 4.22%  | 0.00%   |

#### Lưu ý:

*Với mô hình ARIMAX, mô hình không thể hiệu chỉnh để kết quả cẩn trọng hơn. Kết quả cuối cùng của bước xây dựng mô hình là kết quả tốt nhất trong tất cả các tổ hợp mà ta có thể chọn ra.*

*Nếu kết quả cuối cùng không có một mô hình ARIMAX nào thỏa mãn hết tất cả các kiểm định. Ngân hàng có thể cân nhắc quay trở lại lựa chọn phương pháp xây dựng mô hình phi tham số.*

### <span id="page-21-0"></span>*2.6. Bảo trì và rà soát mô hình*

**Đội ngũ xây dựng mô hình tiến hành bảo trì mô hình** bao gồm việc tái vận hành mô hình hàng quý, và thực hiện phân tích tương quan hàng năm.

![](_page_21_Figure_2.jpeg)

**Ngân hàng được khuyến nghị cần thực hiện rà soát mô hình độc lập** nhằm xác nhận rằng mô hình vẫn hoạt động đúng chức năng như thời điểm mới xây dựng và vẫn có thể áp dụng cho thực trạng của Ngân hàng.

# <span id="page-22-0"></span>3. Phụ lục – Chi tiết các kiểm định trong mô hình

## <span id="page-22-1"></span>3.1. Kiểm đinh Augmented Dickey – Fuller (ADF)

Kiểm định Augmented Dickey - Fuller (ADF) hay còn được gọi là kiểm định nghiệm đơn vị (Unit root test) được chấp nhận rộng rãi như là một cách để kiểm định tính dừng của một chuỗi thời gian.

Random walk (Bước ngẫu nhiên):

Random walk là một quy trình AR(1) đơn giản:  $Y_t = Y_{t-1} + \varepsilon_t$  trong đó  $\varepsilon_t$  là nhiễu trắng.

Xét chuỗi Y<sub>t</sub> tuân theo random walk:

- $E(Y_t) = E(Y_{t-1}) + E(\varepsilon_t) = E(Y_{t-1}) \Rightarrow Chuỗi Y_t có kỳ vọng không đổi theo t <math>Y_t = Y_{t-1} + \varepsilon_t = Y_{t-2} + \varepsilon_{t-1} + \varepsilon_t = \cdots = Y_0 + \varepsilon_1 + \cdots + \varepsilon_t$  với  $Y_0$  là giá trị đầu tiên của chuỗi Y và là 1 hằng
- $Var(Y_t) = t\sigma^2 \text{ với } \sigma^2 \text{ là phương sai không đổi của nhiễu trắng } \epsilon_t$

Chuỗi Y có phương sai thay đổi theo thời gian

$$Cov(Y_t, Y_{t-1}) = Cov(Y_{t-1}, Y_{t-1}) + 0 = Var(Y_{t-1})$$

$$Cov(Y_t, Y_{t-1}) = (t-1)\sigma^2$$

Turong tự 
$$Cov(Y_t, Y_{t-k}) = (t - k)\sigma^2 \Rightarrow Cor(Y_t, Y_{t-k}) = \frac{(t-k)\sigma^2}{\sqrt{Var(Y_t)Var(Y_{t-k})}} = \sqrt{(t-k)/t}$$

Chuỗi Y có hiện tương tư tương quan

Chuỗi Y không dừng

Tuy nhiên, sai phân của Y là  $\Delta Y_t = Y_t - Y_{t-1} = \varepsilon_t$  lại là chuỗi dừng và ta có thể sử dụng để hồi quy để kiểm định các giả thuyết thống kê

Tiêu chuẩn Dickey - Fuller (DF):

Dickey – Fuller đã nghiên cứu chuỗi AR(1) và lấy random walk (Unit root) là một phép thử cho 1 chuỗi bất kì xem chuỗi đó có dừng hay không.

Với một chuỗi bất kì, biếu diễn chuỗi đó bằng quá trình AR(1):

$$Y_{t} = \rho Y_{t-1} + \varepsilon_{t}$$
  
$$\Delta Y_{t} = (\rho - 1)Y_{t-1} + \varepsilon_{t}$$

Đặt  $\rho - 1 = \delta$  Ta sẽ kiểm định giả thuyết:

Ho: $\delta = 0$  (Chuỗi có unit root => Chuỗi không dừng)

H1: $\delta$  < 0 (Chuỗi không có unit roots => Chuỗi dừng)

Hồi quy và tính thống kê

$$\tau = \frac{\hat{\delta}}{SE(\hat{\delta})}$$

Tuân theo phân bố DF,  $\tau < \tau_{\alpha}$  thì bác bỏ H0, và chuỗi sẽ là chuỗi dừng

Logic tương tự được áp dụng cho phương trình  $\Delta Y_t = \beta_0 + \beta_1 t + \delta Y_{t-1} + \sum_{i=1}^q \alpha_i \Delta Y_{t-i} + \epsilon_t$ , tính thống kê  $\tau =$  $SE(\hat{\delta})$ 

cho phương trình trên thì kiểm định trở thành Augmented Dickey – Fuller.

Augmented Dickey - Fuller (ADF):

Logic tương tự được áp dụng cho phương trình

$$\Delta Y_{t} = \beta_{0} + \beta_{1}t + \delta Y_{t-1} + \sum_{i=1}^{q} \alpha_{i} \Delta Y_{t-i} + \epsilon_{t}$$

ADF là phiên bản tổng quát hơn của DF với

- Hệ số chặn: β<sub>0</sub>
- Thành phần xu hướng β<sub>1</sub>t
- Độ trễ của các sai phân  $\sum_{i=1}^{q} \alpha_i \Delta Y_{t-i}$

Ta vẫn tính thống kê

$$\tau = \frac{\hat{\delta}}{SE(\hat{\delta})}$$

cho phương trình trên và sử dụng các giá trị  $\tau_{\alpha}$  của phân bố DF để bác bỏ và thừa nhận các giả thuyết.

### <span id="page-23-0"></span>3.2. Kiểm đinh nhân quả Granger

Nhân quả Granger (Granger Causality) là một khái niệm trong thống kê, khi một biến X<sub>t</sub> có tác dụng dự báo đáng kế một cách thống kê cho biến Y<sub>r</sub> thì ta nói X<sub>r</sub> ảnh hưởng Granger (Granger cause) Y<sub>r</sub>.

Kiểm định Granger:

Xét 2 chuỗi Y<sub>t</sub> và X<sub>t</sub> với 2 phương trình:

$$Y_{t} = \alpha_{0} + \alpha_{1}Y_{t-1} + \dots + \alpha_{p}Y_{t-p} + \varepsilon_{t}$$

$$Y_{t} = \alpha_{0} + \alpha_{1}Y_{t-1} + \dots + \alpha_{p}Y_{t-p} + \beta_{1}X_{t-1} + \dots + \beta_{q}X_{t-q} + \varepsilon_{t}$$
(1)

$$Y_{t} = \alpha_{0} + \alpha_{1}Y_{t-1} + \dots + \alpha_{p}Y_{t-p} + \beta_{1}X_{t-1} + \dots + \beta_{q}X_{t-q} + \varepsilon_{t}$$
 (2)

Giả thuyết thống kê:

Ho:  $\beta_1=\beta_2=\widetilde{\cdots}=\beta_q=0$ , tức không có một biến X nào có tác dụng dự báo biến Y

H1:  $\beta_1^2 + \beta_2^2 + \cdots + \beta_q^2 \neq 0$ , tức có ít nhất một biến X có tác dụng giải thích cho Y

Ta ước lượng và sử dụng kiểm định F cho 2 phương trình ta sẽ có 2 giá trị  $R_1^2$  và  $R_2^2$  cho mỗi phương trình (1), (2) (residual sum of squares)

$$F = \frac{(R_1^2 - R_2^2)/q}{R_2^2/(n - p - q)}$$

F sẽ tuân theo phân bố Fisher với bậc tự do (q, n-p-q) với n là số lượng quan sát của biến Y. Nếu  $F > f_{\alpha}(q, n - p - q)$  thì ta loại bỏ giả thuyết H0, biến X có ảnh hưởng đến Y

## <span id="page-23-1"></span>3.3. Kiểm đinh Box - Pierce(BP)

Kiểm đinh Box - Pierce (BP) là kiểm đinh về tính tự tương quan của phần dư cho mô hình ARIMA(X).

Giả sử ta có 1 chuỗi phần dư e, của một ước lượng.

Gọi  $\rho_i = \text{Cor}(e_t, e_{t-i})$  là hệ số tự tương quan bậc i của chuỗi  $e_t$ 

Giả thuyết thống kê:

H0:  $\rho_1=\rho_2=\ ...=\rho_k=0,$  tức là không có tự tương quan

H1: Có ít nhất 1  $\rho_i \neq 0$ 

Xét thống kê

$$Q = n \sum_{i=1}^{k} \hat{\rho}_{i}^{2}$$

Q tiệm cận phân bố Khi bình phương  $\chi^2$  với bậc tự do (k-p-q) trong đó

k được chọn đủ lớn sao cho ảnh hưởng của hệ số tự tương quạn bậc cao có thể bỏ qua.

p, q là các bậc ARIMA(X) của phương trình ước lượng

Nếu  $Q > \chi^2_{(k-p-q)}$  thì bác bỏ H0, tức là phần dư có tự tương quan

# <span id="page-23-2"></span>3.4. Kiểm định Jarque – Bera(JB)

Kiểm đinh Jarque - Bera là kiểm đinh mỗi chuỗi có phân bố chuẩn hay không. Do phân bố chuẩn có phân bố hình chuông đối xứng, tức hệ số bất đối xứng S = 0 và hệ số nhon K = 3.

H0: S = 0 và K = 3, Chuỗi phân bố chuẩn

H1:  $S \neq 0$  và  $K \neq 3$ , Chuỗi không phân bố chuẩn

Tính hệ số bất đối xứng mẫu và hệ số nhọn mẫu:

$$S = \frac{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^3}{\left(\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2\right)^{3/2}}$$

$$K = \frac{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^4}{\left(\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2\right)^2}$$

Với  $x_i$  là giá trị thứ i của chuỗi cần kiểm định,  $\bar{x}$  là trung bình mẫu và n là số quan sát trong chuỗi Khi chuỗi phân phối chuẩn, thống kê:

$$JB = \frac{n}{6} \left( S^2 + \frac{1}{4} (K - 3)^2 \right)$$

phân bố khi bình phương  $\chi^2_{\alpha}(2)$  Nếu JB >  $\chi^2_{\alpha}(2)$  thì H0 bị bác bỏ

# <span id="page-24-0"></span>3.5. Đánh giá MAPE

Kết quả MAPE có thể được đánh giá theo thông lệ tham khảo sau:

| MAPE (%) | Ý nghĩa kết quả                                    |
|----------|----------------------------------------------------|
| <10      | Highly accurate forecasting (Dự báo chính xác cao) |
| 10 – 20  | Good forecasting (Dự báo tốt)                      |
| 20 - 50  | Reasonable forecasting (Dự báo chấp nhận được)     |
| > 50     | Inaccurate forecasting (Dự báo thiếu chính xác)    |

<sup>\*</sup>Nguồn tài liệu tham khảo: Industrial and business forecasting methods. London: Butterworths, của Lewis, C.D. (1982).