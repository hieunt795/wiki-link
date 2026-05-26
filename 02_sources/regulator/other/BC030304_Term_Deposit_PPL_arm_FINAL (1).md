Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)

Giao phẩm BC03.03.04: Phương pháp luận cho mô hình hành vi tái tục và rút trước hạn cho tiền gửi có kì hạn có tham số

Tháng 08, năm 2021

## BẢN CHÍNH THỨC

<!-- image -->

<!-- image -->

<!-- image -->

## Lưu ý quan trọng

Báo cáo này được thực hiện theo Hợp  đồng cung cấp dịch vụ giữa Công  ty  TNHH  Tư  vấn PricewaterhouseCooper Việt Nam (PwC Việt Nam) và Ngân hàng TMCP An Bình ('ABBank') ngày 24 tháng 09 năm 2020 với các điều khoản và điều kiện đi kèm. Báo cáo này dành riêng cho việc sử dụng nội bộ và nhằm phục vụ lợi ích của ABBank và không được sử dụng bởi hoặc phục vụ cho lợi ích của bất kỳ đối tượng nào khác ('Bên Thứ Ba').

Bên thứ ba không được phép sử dụng Báo cáo này trừ khi đã ký Cam kết miễn trừ trách nhiệm cho PwC Việt Nam và gửi Cam kết này đến PwC Việt Nam hoặc nhận được một thông báo từ PwC Việt Nam về các trách nhiệm liên quan của công ty đối với Bên Thứ Ba.

Bất kỳ Bên Thứ Ba nào sử dụng và đọc báo cáo này trái với các điều khoản nêu trên, thì Bên Thứ Ba đó phải chấp nhận và đồng ý với các điều khoản sau:

1. Công việc được thực hiện bởi PwC Việt Nam theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và được thực hiện chỉ dành riêng cho lợi ích và mục đích sử dụng của chính khách hàng mà báo cáo này được gửi đến.
2. Báo cáo này được thực hiện theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và có thể không bao gồm tất cả những quy trình/ thủ tục có thể được cho là cần thiết cho mục đích của Bên Thứ Ba.
3. PwC Việt Nam, các giám đốc, nhân viên và các bên có liên quan của PwC Việt Nam sẽ không gánh chịu hay chấp nhận bất kỳ nghĩa vụ hay trách nhiệm nào đối với Bên Thứ Ba, dù là nghĩa vụ theo hợp đồng hay ngoài hợp đồng (bao gồm nhưng không giới hạn bởi sự bất cẩn và vi phạm các nghĩa vụ theo quy định của pháp luật), và sẽ không chịu trách nhiệm đối với bất kỳ tổn thất, thiệt hại hoặc phí tổn dưới bất kỳ hình thức nào phát sinh bởi hoặc liên quan đến Bên Thứ Ba do việc sử dụng báo cáo này, hoặc bất kỳ hậu quả nào khác do việc Bên Thứ Ba sử dụng báo cáo này. Ngoài ra, Bên Thứ Ba chấp nhận rằng báo cáo này không được dùng để tham chiếu hoặc trích dẫn toàn bộ hoặc từng phần, trong bất kỳ bản cáo bạch, bản đăng ký, tài liệu chào bán, tài liệu công bố ra công chúng, các hồ sơ vay, các thỏa thuận hoặc tài liệu khác và không công bố báo cáo này nếu không được sự chấp thuận trước bằng văn bản của PwC Việt Nam.

Các thông tin, số liệu thống kê và các ý kiến (gọi là 'thông tin') trong báo cáo này được thực hiện bởi PwC Việt Nam từ các nguồn tài liệu có sẵn do ABBank cung cấp và trên trang web của ABBank trong khuôn khổ của dự án này và qua các buổi thảo luận được tổ chức với các lãnh đạo Ngân hàng.

PwC Việt Nam lập báo cáo này dựa trên các thông tin nhận được và có được và trên cơ sở rằng các thông tin được cung cấp bởi Ngân hàng là chính xác và hoàn chỉnh. Các thông tin trong báo cáo này không nhằm mục đích kiểm toán, không được sao chép, mô phỏng, phân phát, sử dụng một phần hoặc toàn bộ báo cáo này cho các mục đích khác ngoài mục đích đã được nêu trong Thỏa thuận giữa hai bên về Nội dung công việc thực hiện.

## Mục lục

| 1. Giới thiệu mô hình ARIMAX                                    |   4 |
|-----------------------------------------------------------------|-----|
| 1.1. Tổng quan về ARIMAX                                        |   4 |
| 1.1.1. Quá trình tự hồi quy AR                                  |   4 |
| 1.1.2. Quá trình trung bình trượt MA                            |   4 |
| 1.1.3. ARIMAX tổng hợp                                          |   4 |
| 2. Quy trình xây dựng mô hình                                   |   6 |
| 2.1. Chuẩn bị dữ liệu                                           |   8 |
| 2.2. Phân khúc và lập giả định                                  |   8 |
| 2.3. Phân tích tương quan                                       |   9 |
| 2.3.1. Lựa chọn các yếu tố phân tích tương quan                 |  11 |
| 2.3.2. Quy trình phân tích tương quan                           |  11 |
| 2.4. Xây dựng mô hình                                           |  12 |
| 2.4.1. Kiểm định tính dừng                                      |  14 |
| 2.4.2. Kiểm định nhân quả (Chỉ áp dụng cho mô hình ARIMAX)      |  16 |
| 2.4.3. Kiểm định đa cộng tuyến (Chỉ áp dụng cho mô hình ARIMAX) |  17 |
| 2.4.4. Ước lượng và kiểm định phần dư                           |  17 |
| 2.5. Kiểm tra hồi tố                                            |  19 |
| 2.6. Bảo trì và rà soát mô hình                                 |  22 |
| 3. Phụ lục - Chi tiết các kiểm định trong mô hình               |  23 |
| 3.1. Kiểm định Augmented Dickey - Fuller (ADF)                  |  23 |
| 3.2. Kiểm định nhân quả Granger                                 |  24 |
| 3.3. Kiểm định Box - Pierce(BP)                                 |  24 |
| 3.4. Kiểm định Jarque - Bera(JB)                                |  24 |
| 3.5. Đánh giá MAPE                                              |  25 |

## 1. Giới thiệu mô hình ARIMAX

Với mục đích phân tích sự ảnh hưởng của các biến kinh tế vĩ mô vào mô hình, PwC giới thiệu phương pháp Hồi quy chuỗi thời gian ARIMAX (Autoregressive integrated moving average with exogenous variable - Tự hồi quy tích hợp trung bình trượt có biến ngoại sinh).

## 1.1. Tổng quan về ARIMAX

Arimax là một phương pháp hồi quy chuỗi thời gian, bao gồm quá trình tự hồi quy (AR - autoregression), quá trình trung bình trượt (MA - moving average) và các biến ngoại sinh (X - exogenous variable, tương ứng với các biến kinh tế vĩ mô đưa vào mô hình).

## 1.1.1. Quá trình tự hồi quy AR

Quá trình tự hồi quy (Auto Regression - AR): là quá trình trong đó một chuỗi chịu ảnh hưởng của chính nó trong quá khứ.

<!-- formula-not-decoded -->

.

Một quá trình như trên được gọi là quá trình tự hồi quy bậc 𝑝 Trong đó:

- Yt là biến cần dự báo
- Yt-i là giá trị trễ i của biến Y , αi là hệ số ước lượng tương ứng
- 𝑝 là bậc của 𝐴𝑅
- ε t là phần ngẫu nhiên (error term)

## 1.1.2. Quá trình trung bình trượt MA

Quá trình trung bình trượt (Moving Average- MA): là quá trình trong đó một chuỗi chịu ảnh hưởng của thành phần ngẫu nhiên (error term) trong quá khứ.

<!-- formula-not-decoded -->

Một quá trình như trên được gọi là quá trình MA(q) . Trong đó:

- Yt là biến cần dự báo
- ε t là phần ngẫu nhiên (error term)
- ε t-i là giá trị trễ i của phần ngẫu nhiên ε t , βi là hệ số ước lượng tương ứng
- q là bậc của MA

## 1.1.3. ARIMAX tổng hợp

Kết hợp 2 quá trình AR, MA và các biến ngoại sinh X (các yếu tố kinh tế vĩ mô) ta sẽ được mô hình ARIMAX:

<!-- formula-not-decoded -->

Trong đó:

- Xt i là biến ngoại sinh thứ i. γt i là hệ số ước lượng tương ứng

Điều kiện:

Mô hình có thể được ước lượng nếu thỏa mãn điều kiện ε t là nhiễu trắng, tức là:

- ε t có kì vọng = 0
- ε t có phương sai không đổi theo thời gian.
- ε t không tự tương quan với chính nó.

Và các biến ngoại sinh X không có hiện tượng đa cộng tuyến, tức là các biến X không tương quan chặt với nhau.

Khi các điều kiện trên thỏa mãn, ta sẽ có ước lượng điểm không chệch của các hệ số ước lượng αi , βi , γ i , từ đó dự báo cho biến Y .

## 2. Quy trình xây dựng mô hình

Sơ đồ dưới đây thể hiện quy trình tổng thể cho quản trị mô hình từ bước bắt đầu xây dựng cho đến bước cập nhật và duy trì mô hình, cùng với vai trò của các phòng/ban/đơn vị liên quan tương ứng với từng giai đoạn triển khai.

(*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trạng hỗ trợ từ cơ sở hạ tầng dữ liệu của Ngân hàng.

<!-- image -->

|   Bước | Trách nhiệm   | Các bước thực hiện                                            | Tài liệu liên quan   | Thời gian        |
|--------|---------------|---------------------------------------------------------------|----------------------|------------------|
|      1 | XDMH & CBDL   | Chuẩn bị dữ liệu                                              |                      | Định kỳ hàng quý |
|      2 | XDMH & KKD    | Phân khúc và lập giả định                                     |                      | Định kỳ hàng quý |
|      3 | XDMH & KKD    | Phân tích tương quan và lựa chọn phương pháp XDMH             |                      | Định kỳ hàng quý |
|      4 | XDMH          | Xây dựng mô hình                                              |                      | Định kỳ hàng quý |
|      5 | XDMH & CBDL   | Kiểm tra hồi tố mô hình Phương pháp phi tham số KHÔNG ĐẠT ĐẠT |                      | Định kỳ hàng quý |
|      6 | XDMH & CBDL   | Bảo trì và rà soát mô hình                                    |                      | Định kỳ hàng quý |

| STT    | Công việc                  | Đơn vị   | Khi nào          | Cách làm                                                                                                                                        |
|--------|----------------------------|----------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Bước 1 | Chuẩn bị dữ liệu           | XDMH     | Định kỳ hàng quý | • Chuẩn bị yêu cầu dữ liệu • Kiểm tra và phát hiện vấn đề dữ liệu, nếu có                                                                       |
| Bước 1 | Chuẩn bị dữ liệu           | CBDL     | Định kỳ hàng quý | • Thu thập dữ liệu theo yêu cầu                                                                                                                 |
| Bước 2 | Phân khúc và lập giả định  | XDMH     | Định kỳ hàng quý | • Xác định các tiêu chí phân khúc mô hình cần thiết • Lập giả định cần thiết cho mô hình • Thực hiện phân khúc và triển khai dữ liệu            |
| Bước 2 | Phân khúc và lập giả định  | KKD      | Định kỳ hàng quý | • Mô tả nhu cầu nghiệp vụ • Phối hợp với đội ngũ XDMH để phân tích các nhu cầu nghiệp vụ                                                        |
| Bước 3 | Phân tích tương quan       | XDMH     | Định kỳ hàng quý | • Xác định các yếu tố vĩ mô chính chi phối hành vi khách hàng • Thực hiện phân tích tương quan • Lựa chọn phương pháp xây dựng mô hình          |
| Bước 3 | Phân tích tương quan       | KKD      | Định kỳ hàng quý | • Phối hợp với đội ngũ xây dựng mô hình để xác định các yếu tố vĩ mô chính                                                                      |
| Bước 4 | Xây dựng mô hình           | XDMH     | Định kỳ hàng quý | • Xây dựng mô hình dựa trên đặc tính sản phẩm                                                                                                   |
| Bước 5 | Kiểm tra hồi tố mô hình    | XDMH     | Định kỳ hàng quý | • Thực hiện kiểm tra hồi tố và phân tích kết quả • Thực hiện lại mô hình theo phương pháp khác (phi tham số) nếu như kết quả kiểm tra không đạt |
| Bước 5 | Kiểm tra hồi tố mô hình    | CBDL     | Định kỳ hàng quý | • Thu thập dữ liệu kiểm tra hồi tố                                                                                                              |
| Bước 6 | Bảo trì và rà soát mô hình | XDMH     | Định kỳ hàng quý | • Tái vận hành mô hình trên bộ dữ liệu cập nhật • Đánh giá kết quả mô hình tại từng lần tái vận hành                                            |
| Bước 6 | Bảo trì và rà soát mô hình | CBDL     | Định kỳ hàng quý | • Thu thập dữ liệu cập nhật theo yêu cầu                                                                                                        |

## 2.1. Chuẩn bị dữ liệu

Phương pháp cho bước Chuẩn bị và triển khai dữ liệu được trình bày trong tài liệu phương pháp phi tham số.

Tài liệu này sẽ không trình bày lại về bước này mà tập trung vào phương pháp luận cho mô hình ARIMAX

## 2.2. Phân khúc và lập giả định

Phương pháp cho bước Phân khúc và lập giả định được trình bày trong tài liệu phương pháp phi tham số. Tài liệu này sẽ không trình bày lại về bước này mà tập trung vào phương pháp luận cho mô hình ARIMAX.

## 2.3. Phân tích tương quan

Sơ đồ dưới đây thể hiện quy trình phân tích tương quan để lựa chọn phương pháp xây dựng mô hình cho từng phân khúc của mô hình Tiền gửi CKH.

<!-- image -->

Từng mô hình sẽ có những ưu điểm và hạn chế theo như phân tích dưới đây

## Mô hình phi tham số

Mô hình tham số

- Mô hình có phương pháp luận đơn giản, trực quan và có thể áp dụng dễ dàng.
- Các bước tính toán trong mô hình được thực hiện đơn giản.
- Phương pháp đã được chấp nhận và thực hiện ở nhiều ngân hàng với quy mô khác nhau trong nước, trong khu vực và trên toàn thế giới.
- × Phương pháp không thể hiện rõ các yếu tố ngoại sinh vì đã giả định rằng tác động của những yếu tố này được thể hiện trong biến động số dư của danh mục.
- Phương pháp được áp dụng tại nhiều ngân hàng trong và ngoài nước với quy mô khác nhau
- × Phương pháp luận xây dựng mô hình và các bước tính toán trong mô hình được thực hiện tương đối phức tạp.

## 2.3.1. Lựa chọn các yếu tố phân tích tương quan

Phân tích tương quan nhằm xác định mức độ của mối tương quan giữa phân khúc cần xây dựng mô hình và các biến động từ các yếu tố ngoại sinh, từ đó lựa chọn phương pháp xây dựng mô hình phù hợp ở các bước tiếp theo.

Các yếu tố phổ biến (bao gồm yếu tố kinh tế vĩ mô và dữ liệu thị trường) được lựa chọn để phân tích tương quan

- Tỷ giá ngoại tệ (VND/USD)
- Giá vàng
- Chỉ số VNINDEX
- Lãi suất thị trường liên ngân hàng
- Lãi suất trái phiếu chính phủ
- Giá trị GDP
- Tỷ lệ thất nghiệp
- Tỷ lệ lạm phát
- Lãi suất tiền gửi các ngân hàng khác

Dữ liệu của các yếu tố được lựa chọn trên nên được thu thập ở tần suất hàng ngày hoặc tần suất nhỏ nhất có thể.

## 2.3.2. Quy trình phân tích tương quan

Chuỗi hành vi theo dõi được lấy là tỷ lệ biến động số dư theo ngày

<!-- formula-not-decoded -->

Cách tính toán các biến trên được trình bày cụ thể trong tài liệu phương pháp luận tương ứng.

Phân tích tương quan được thực hiện trên bộ các yếu tố lựa chọn với từng phân khúc cần xây dựng mô hình, và được thực hiện theo từng lần tái vận hành mô hình.

Với từng phân khúc, chuỗi hành vi theo ngày sẽ được phân tích tương quan với từng yếu tố vĩ mô/thị trường theo công thức

Với:

Correlation: Hệ số tương quan

rate: chuỗi hành vi ngày trong từng phân khúc

y: chuỗi giá trị dữ liệu hàng ngày của yếu tố vĩ mô/thị trường cần phân tích tương quan

rate ̅̅̅̅ ̅ : giá trị trung bình của chuỗi rate

- y ̅ : giá trị trung bình của chuỗi y
- Dựa trên kết quả phân tích tương quan, các chuỗi dữ liệu yếu tố vĩ mà có hệ số tương quan cao (&gt;40% hoặc &lt;-40%) sẽ được đưa vào mô hình.

## Ví dụ minh họa

| Ngày     | Tỷ lệ trả trước hạn   |
|----------|-----------------------|
| 1/4/2018 | 20%                   |
| 2/4/2018 | 8.33%                 |
| 3/4/2018 | 18.2%                 |

| Ngày     | Lãi suất tiền gửi ngân hàng A   |
|----------|---------------------------------|
| 1/4/2018 | 2%                              |
| 2/4/2018 | 3.33%                           |
| 3/4/2018 | 4.2%                            |

Hệ số tương quan trong chuỗi quan sát 3 ngày có thể được tính theo hàm công thức CORREL trong excel, với công thức tương tự

CORREL(Chuỗi Runoff, Chuỗi y) =  - 100%

Với kết quả hệ số tương quan là -100% và nhỏ hơn -40%, ta có thể kết luận rằng chuỗi tỷ lệ trả trước hạn và lãi suất tiền gửi ở ngân hàng A trong 3 ngày có tương quan với nhau.

<!-- formula-not-decoded -->

## 2.4. Xây dựng mô hình

Sau khi đã xác định được các biến được đưa vào mô hình tại bước phân tích tương quan, ghép chuỗi hành vi và các chuỗi kinh tế vĩ mô có tương quan vào thành một bộ dữ liệu. Dữ liệu 5 năm được chia thành dữ liệu nghiên cứu (4 năm đầu) và dữ liệu kiểm tra (1 năm cuối).

Quy trình cho mô hình ARIMAX được chia thành 5 bước, trong đó 4 bước đầu sử dụng dữ liệu nghiên cứu xây dựng mô hình và so sánh kết quả với số liệu thực tế của dữ liệu kiểm tra tại bước 5: kiểm tra hồi tố.

<!-- image -->

Trong mô hình ARIMAX, chuỗi hành vi được coi như biến cần được dự báo (Y) trong mô hình, trong khi các chuỗi kinh tế vĩ mô là các biến ngoại sinh (X).

Quy trình cho mô hình ARIMA được chia thành 3 bước, trong đó 2 bước đầu sử dụng dữ liệu nghiên cứu xây dựng mô hình và so sánh kết quả với số liệu thực tế của dữ liệu kiểm tra tại bước 3: kiểm tra hồi tố.

<!-- image -->

Trong mô hình ARIMA, chuỗi hành vi được coi như biến cần được dự báo (Y) trong mô hình và không có các biến ngoại sinh (X) nào.

## 2.4.1. Kiểm định tính dừng

Định nghĩa chuỗi dừng (Stationary series): Một chuỗi dừng là khi:

1. Có trung bình và phương sai không đổi theo thời gian
2. Không có hiện tượng tự tương quan

Dưới đây là ví dụ của một chuỗi dừng:

<!-- image -->

Ví dụ về chuỗi trung bình thay đổi theo thời gian

<!-- image -->

Ví dụ về chuỗi phương sai thay đổi theo thời gian

<!-- image -->

Ví dụ về chuỗi tự tương quan

<!-- image -->

Trong mô hình chuỗi thời gian, tính dừng được xem như ổn định và có thể dự báo (có quy luật). Nếu các chuỗi đưa vào mô hình (Chuỗi hành vi hoặc kinh tế vĩ mô) không dừng, cần biến đổi để các chuỗi dừng.

Sai phân: Sai phân của một chuỗi y có dạnh như sau:

- Bậc 1: ∆yt = yt -yt-1
- Bậc d: ∆ d yt = ∆ d-1 yt -∆ d-1 y t-1

Y

<!-- image -->

Các ước lượng ARIMAX của biến sai phân bằng với ước lượng của biến gốc, và các chuỗi sai phân thường sẽ dừng. Đây là phương pháp để khắc phục khi các chuỗi đầu vào không dừng. Mục đích của bước này là tìm được bậc sai phân mà trong đó tất cả các biến đều dừng. Bậc sai phân d khi tất cả các chuỗi dừng là tham số integrated trong mô hình ARIMAX.

Quy trình Kiểm đinh tính dừng:

Tính dừng được kiểm định bằng kiểm định ADF (Augmented Dickey - Fuller test)

1. Kiểm định tính dừng biến hành vi và kinh tế vĩ mô với 95% độ tin cậy.

Giả thiết H0: biến không dừng

Giả thiết H1: biến dừng

p-value ≤ 0.05 thì bác bỏ H0 và thừa nhận biến dừng

2. Nếu có một chuỗi không dừng, sai phân tất cả các chuỗi và lặp lại kiểm định đến khi tất cả các chuỗi đầu vào dừng. Xác định d.

Tham khảo phụ lục 3.1. Kiểm định Augmented Dickey - Fuller (ADF) về kiểm định chi tiết

## Ví dụ:

P-value của kiểm định ADF được tính trong R bằng code:

adf.test(x)$p.value

#thay x bằng chuỗi cần kiểm định

|    | Biến Y   | Sai phân bậc 1   | Sai phân bậc 2   | Sai phân bậc 3   |
|----|----------|------------------|------------------|------------------|
|    | Y t-1    | A t = Y t -Y t-1 | B t = A t -A t-1 | C t = B t -B t-1 |
| 1  | 6250001  |                  |                  |                  |
| 2  | 6765201  | 515200.1         |                  |                  |
| 3  | 7311617  | 546416.3         | 31216.22         |                  |
| 4  | 7890481  | 578864           | 32447.72         | 1231.497         |

<!-- image -->

## 2.4.2. Kiểm định nhân quả (Chỉ áp dụng cho mô hình ARIMAX)

Kiểm định nhân quả sử dụng kiểm định Granger, nhằm mục đích đảm bảo các chuỗi kinh tế vĩ mô có năng lực dự báo với chuỗi hành vi. Kiểm định cho biết một biến X có tác động (granger cause) đến biến Y hay không Quy trình kiểm định nhân quả

1. Kiểm định nhân quả của từng chuỗi kinh tế vĩ mô (X) đến chuỗi hành vi (Y) với 95% độ tin cậy.

Giả thiết H0: biến X không ảnh hưởng đến biến Y

Giả thiết H1: biến X ảnh hưởng đến biến Y

p-value ≤ 0.05 thì bác bỏ H0, chấp nhận biến X trong mô hình

2. Loại bỏ các biến không ảnh hưởng đến Y và đưa bộ dữ liệu mới vào bước tiếp theo

Tham khảo phụ lục 3.2. Kiểm định nhân quả Granger về kiểm định chi tiết

Ví dụ:

Kiểm định Granger cho chuỗi drawdown của tiền gửi có kì hạn (chuỗi hành vi - runoff) với chỉ số VNINDEX và lãi suất VNIBOR 6 tháng

Code: grangertest(runoff, vnindex, order = 365)$`Pr(&gt;F)`[2]

P-value kiểm định chuỗi drawdown với VNINDEX = 2.6432E-10 &lt; 0.05

-  Giữ chuỗi VNINDEX trong mô hình
-  Loại chuỗi VNIBOR\_6M ra khỏi mô hình

Code: grangertest(runoff, vnibor\_6m, order = 365)$`Pr(&gt;F)`[2]

P-value kiểm định chuỗi drawdown với VNIBOR\_6M = 0.283017295 &gt; 0.05

## 2.4.3. Kiểm định đa cộng tuyến (Chỉ áp dụng cho mô hình ARIMAX)

Đa cộng tuyến: Là hiện tượng một biến ngoại sinh có thể được tổng hợp từ các biến ngoại sinh còn lại.

Ví dụ {Xt 1 , X t 2 , … , X t n } là các biến được đưa vào mô hình. Nếu phương trình

Xt 1 = α0 +α2Xt 2 +⋯+α3Xt n có ý nghĩa, tức các biến Xt 2 , … X t n có thể giải thích cho Xt 1 , thì mô hình có hiện tượng đa cộng tuyến.

Các biến gây ra đa cộng tuyến cao cần được loại bỏ khỏi mô hình.

Quy trình kiểm định đa cộng tuyến:

1. Hồi quy từng biến ngoại sinh X với các biến ngoại sinh còn lại và lấy giá trị R 2 :

<!-- formula-not-decoded -->

…

3. Nếu VIFi ≥ 5 thì có hiện tượng đa cộng tuyến giữa biến Xt i với các biến còn lại. Loại bỏ Xt i và lặp lại bước 1
2. Tính giá trị VIFi = 1 1-R i 2 cho mỗi giá trị R 2 .
4. Khi không còn hiện tượng đa cộng tuyến (tất cả VIFi &lt; 5 ), các biến còn lại sẽ được đưa vào mô hình

Ví dụ: Với VNINDEX và VNIBOR\_6M, VNIBOR\_12M là 3 biến vĩ mô được đưa vào mô hình Hồi quy 3 phương trình

```
VNINDEX = α0 + α1VNIBOR_6M + α2VNIBOR_12M  + ε  → VIFvnindex = 2.34 VNIBOR_6M = α0 + α1VNINDEX + α2VNIBOR_12M  + ε → VIFvnibor_6m = 5.24 VNIBOR_12M = α0 + α1VNINDEX + α2VNIBOR_6M  + ε → VIFvnbor_12m = 6.34
```

Có VIFvnibor\_6m = 5.24 &gt; 5 và VIFvnbor\_12m = 6.34 &gt; 5 , bỏ biến VNIBOR\_12M có VIF cao nhất và hồi quy lại

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

-  Loại bỏ VNIBOR\_12M và đưa 2 biến còn lại vào tổ hợp các biến kinh tế vĩ mô cho bước sau

Tổng hợp các tổ hợp có thể có của X:

Nếu có nhiều hơn 1 biến X được đưa vào mô hình, cần tổng hợp các tổ hợp của X. Xây dựng mô hình với từng tổ hợp và chọn ra 1 tổ hợp với kết quả dự báo tốt nhất làm mô hình chính.

Ví dụ: Với VNINDEX và VNIBOR\_6M là 2 biến vĩ mô được đưa vào mô hình. Các tổ hợp của X bao gồm

- VNINDEX
- VNIBOR
- VNINDEX, VNIBOR

## 2.4.4. Ước lượng và kiểm định phần dư

Xác định p, q: Các tham số p, q là bậc hồi quy của mô hình ARIMAX

AIC - Akaike Information Criteria là chỉ số xác định độ mất thông tin của một mô hình. Với d đã biết từ bước 1, lấy giá trị lớn nhất của p, q là 10, hồi quy ARIMA (không có biến ngoại sinh) để tìm chỉ số AIC của mỗi tổ hợp p, q và chọn 5 tổ hợp (p, q) có AIC nhỏ nhất.

Giá trị lớn nhất của p, q càng nhiều thì càng có nhiều tổ hợp mô hình. Mặc định giá trị lớn nhất của p, q là 10, tuy nhiên Ngân hàng có thể lựa chọn giá trị tùy theo năng lực tính toán của hệ thống.

Ví dụ:

Có d = 1, p, q lớn nhất bằng 5, ta sẽ có 5 mô hình ARIMAX là:

| AIC   |   p = 1 |   p = 2 |   p = 3 |   p = 4 |   p = 5 |
|-------|---------|---------|---------|---------|---------|
| q = 1 |     109 |     100 |     106 |     110 |     100 |
| q = 2 |     109 |     109 |     110 |     109 |     108 |
| q = 3 |     107 |     105 |     109 |     108 |     108 |
| q = 4 |     105 |     105 |     102 |     101 |     103 |
| q = 5 |     104 |     110 |     107 |     108 |     101 |

Với d = 1, ta sẽ có 5 mô hình ARIMAX ARIMAX(p,d,q) là: (Đối với mô hình ARIMA, bỏ các tổ hợp X)

- ARIMAX(5,1,1): ∆ 1 Yt = ∑ αi ∆ d Yt-i 5 i=1 +∑ βi ε t-i 1 i=1 +∑ γ i ∆ 1 Xt i n i=1 +εt
- ARIMAX(5,1,5): ∆ 1 Yt = ∑ αi ∆ d Yt-i 5 i=1 +∑ βi ε t-i 5 i=1 +∑ γ i ∆ 1 Xt i n i=1 +εt
- ARIMAX(5,1,4): ∆ 1 Yt = ∑ αi ∆ d Yt-i 5 i=1 +∑ βi ε t-i 4 i=1 +∑ γ i ∆ 1 Xt i n i=1 +εt
- ARIMAX(4,1,4): ∆ 1 Yt = ∑ αi ∆ d Yt-i 4 i=1 +∑ βi ε t-i 4 i=1 +∑ γ i ∆ 1 Xt i n i=1 +εt
- ARIMAX(3,1,4): ∆ 1 Yt = ∑ αi ∆ d Yt-i 3 i=1 +∑ βi ε t-i 4 i=1 +∑ γ i ∆ 1 Xt i n i=1 +εt

Xác định các tổ hợp của mô hình: Với từng tổ hợp (p, q), kết hợp với các tổ hợp của X tạo thành 1 tổ hợp mô hình.

Ví dụ:

Kết hợp (p,d,q) = (5,1,1) với các tổ hợp X của ví dụ phần kiểm định đa cộng tuyến ta có 3 mô hình: (Đối với mô hình ARIMA bỏ các tổ hợp X)

- ARIMAX(5,1,1) + Xt 1
- ARIMAX(5,1,1) + Xt 1 , X t 2
- ARIMAX(5,1,1) + Xt 2

Phần dư của mô hình: Xét mô hình ARIMAX (Đối với mô hình ARIMA bỏ các tổ hợp X)

Gọi Y ̂ t là ước lượng của mô hình

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Phần dư, tức sai số ngẫu nhiên ước lượng ε ̂ t = Yt -Y ̂ t cần phải là nhiễu trắng để ước lượng là ước lượng không chệch.

Các kiểm định sau khi chạy mô hình nhằm kiểm tra phần dư có phải là nhiễu trắng không.

Quy trình ước lượng mô hình (Đối với mô hình ARIMA bỏ các tổ hợp X)

1. Xác định các tổ hợp (p, q) với AIC nhỏ nhất
2. Kết hợp các tổ hợp (p, q) với các tổ hợp X tạo thành các tổ hợp mô hình
3. Ước lượng mỗi tổ hợp
4. Kiểm định tính dừng cho phần dư

Kiểm định ADF cho phần dư tương tự như kiểm định biến đầu vào của bước 1.

Nếu phần dư không dừng, loại bỏ  tổ hợp mô hình

5. Kiểm định tư tương quan của phần dư

Kiểm định Box - Pierce (BP - test)

H0: Phần dư không có tự tương quan

H1: Phần dư có tự tương quan

p - value &gt; 0.05, chấp nhận H0, phần dư không có tự tương quan

Nếu phần dư có tự tương quan, loại bỏ mô hình

6. Kiểm định phân phối chuẩn của phần dư

Kiểm định Jarque - Bera (JB)

H0: Phần dư phân phối chuẩn

H1: Phần dư không phân phối chuẩn

p - value &gt; 0.05, chấp nhận H0, phần dư phân phối chuẩn

Nếu phần dư không phân phối chuẩn, loại bỏ mô hình

7. Kết quả cuối cùng bao gồm tất cả các tổ hợp thỏa mãn cùng phương trình ước lượng tương ứng

Tham khảo phụ lục 3.3. Kiểm định Box - Pierce(BP) và phụ lục 3.4. Kiểm định Jarque - Bera(JB)  về kiểm định chi tiết

## 2.5. Kiểm tra hồi tố

Kiểm tra hồi tố:

Từ tất cả các tổ hợp đạt kiểm định tại bước 4, ta sẽ có bấy nhiêu phương trình. Từ các phương trình trên dự báo cho 1 năm tiếp theo (năm thứ 5) và kiểm tra hồi tố bằng cách so sánh dự báo của mỗi phương trình với dữ liệu thực tế năm thứ 5 (dữ liệu kiểm tra).

Tính chỉ số MAPE (Mean Absolute Percentage Error) cho từng kết quả dự báo:

Trong đó

𝑚 là số điểm dự báo (tương ứng với 1 năm)

Ai là giá trị thực tế của điểm i

Fi là giá trị dự báo của điểm i

Chỉ số MAPE thể hiện năng lực dự báo của mô hình, MAPE &gt; 50% thể hiện dự báo kém và thiếu chính xác. Lấy phương trình với kết quả dự báo cho ra MAPE nhỏ nhất làm kết quả cuối cùng của mô hình. Nếu kết quả cuối cùng có MAPE &gt; 50% thì Ngân hàng cần cân nhắc lựa chọn phương pháp phi tham số hoặc phương pháp mô hình khác có thể dự báo chính xác hơn.

Trong thực tế nếu chuỗi hành vi có giá trị 0, tức tồn tại Ai = 0 thì sẽ không thể dùng MAPE. Khi đó ta sử dụng WAPE (Weighted Absolute Percentage Error) thay thế:

<!-- formula-not-decoded -->

| FORECAST   | ACTUA L    | C      | WAPE =SUM(ABS(C))/SUM(ABS(A)   | D         | MAPE             |
|------------|------------|--------|--------------------------------|-----------|------------------|
|            | A          | A - F  | )                              | (A - F)/A | =SUM(ABS(D))/2 8 |
| 0.82       | 0.65 -0.17 | 43.17% |                                | -0.27     | 58.88%           |
| 0.31       | 0.27       | -0.05  |                                | -0.17     |                  |
| 0.19       | 0.61       | 0.42   |                                | 0.68      |                  |
| 0.02       | 0.09       | 0.07   |                                | 0.76      |                  |
| 0.20       | 0.21       | 0.01   |                                | 0.06      |                  |
| 0.68       | 0.47       | -0.21  |                                | -0.43     |                  |
| 0.35       | 0.71       | 0.36   |                                | 0.50      |                  |
| 0.83       | 0.81       | -0.02  |                                | -0.03     |                  |
| 0.76       | 0.15       | -0.61  |                                | -4.09     |                  |
| 0.20       | 0.65       | 0.45   |                                | 0.69      |                  |
| 0.56       | 0.87       | 0.31   |                                | 0.35      |                  |

<!-- formula-not-decoded -->

Ví dụ:

<!-- image -->

|    |   FORECAST |   ACTUA L |     C |     D | MAPE   |
|----|------------|-----------|-------|-------|--------|
| 12 |       0.27 |      0.40 |  0.13 |  0.32 |        |
| 13 |       0.62 |      0.62 |  0.00 | -0.01 |        |
| 14 |       0.88 |      0.64 | -0.24 | -0.37 |        |
| 15 |       0.62 |      0.74 |  0.12 |  0.16 |        |
| 16 |       0.01 |      0.08 |  0.07 |  0.90 |        |
| 17 |       0.21 |      0.91 |  0.70 |  0.77 |        |
| 18 |       0.08 |      0.28 |  0.19 |  0.70 |        |
| 19 |       0.42 |      0.25 | -0.17 | -0.66 |        |
| 20 |       0.89 |      0.85 | -0.05 | -0.06 |        |
| 21 |       0.68 |      0.35 | -0.33 | -0.96 |        |
| 22 |       0.76 |      0.65 | -0.11 | -0.16 |        |
| 23 |       0.62 |      0.62 |  0.00 |  0.00 |        |
| 24 |       0.92 |      0.34 | -0.58 | -1.72 |        |
| 25 |       0.88 |      0.62 | -0.26 | -0.42 |        |
| 26 |       0.49 |      0.51 |  0.02 |  0.04 |        |
| 27 |       0.07 |      0.24 |  0.17 |  0.72 |        |
| 28 |       0.44 |      0.86 |  0.42 |  0.49 |        |

Như ví dụ trên thì kết quả sẽ là 'ĐẠT' với WAPE và 'KHÔNG ĐẠT' với MAPE.

## Dự báo

Nếu kiểm tra hồi tố ra kết quả 'đạt', sử dụng phương trình với số liệu của toàn bộ 5 năm để dự báo cho 1 năm tiếp theo (năm thứ 6).

## Dự báo cho các biến kinh tế vĩ mô:

Để xác định chuỗi hành vi trong tương lại, ta cần dự báo các biến kinh tế vĩ mô trong tương lai.

Các dự báo này nên được lấy tại các nguồn sau, theo thứ tự từ trên xuống dưới:

- Nguồn tổng hợp từ nội bộ Ngân hang
- Các tổ chức kinh tế có dự báo (World Bank, Reuter, IMF,…)
- Dự báo ARIMA từ chuỗi dữ liệu quá khứ

Hiện tại, trong mô hình giao phẩm, các biến kinh tế vĩ mô đang được dự báo giản đơn bằng ARIMA. Tuy nhiên trong tương lại, PwC khuyến nghị Ngân hàng nên lấy các nguồn trên để đảm bảo tính chính xác của dự báo.

## Đưa chuỗi tỷ lệ theo ngày về các dải kì hạn:

Dòng tiền sau điều chỉnh hành vi được phân bổ lại vào các dải kỳ hạn tương ứng như sau

| Dải kì hạn   |   Qua đêm |   2-7D |   8-30D |   31-90D |   91-180D |   181-360D |
|--------------|-----------|--------|---------|----------|-----------|------------|
| Số ngày      |         1 |      7 |      30 |       90 |       180 |        360 |

Giả sử có dự báo {Y ̂ t+1 , … , Y ̂ t+365 } Dải kì hạn b có giá trị cộng dồn:

<!-- image -->

| Ví dụ   | Ví dụ    | Ví dụ      |
|---------|----------|------------|
|         | Y dự báo | 1-Y dự báo |
| 1       | 0.21     | 0.79       |
| 2       | 0.16     | 0.84       |
| 3       | 0.12     | 0.88       |

<!-- formula-not-decoded -->

| 4      |   0.05 0.95 |
|--------|-------------|
| 5 0.05 |        0.95 |
| 6 0.07 |        0.93 |
| 7 0.14 |        0.86 |
| 8 0.09 |        0.91 |

Dải kì hạn 1 ngày (b = 1) có giá trị dòng tiền ra cộng dồn = 1 - 0.79 = 0.21 Dải kì hạn 2 - 7 ngày (b = 7) có giá trị dòng tiền ra cộng dồn = 1 - 0.79*0.84*0.88*0.95*0.95*0.93*0.86 = 0.58

Giá trị không cộng dồn của dòng tiền sẽ có giá trị:

Outflowb = MIN{0, (Runoffb -MIN{Runoffi| i &lt; b})}

Ví dụ: Với dải kì hạn bao gồm 3 mức

|                | ON     | 2 - 7D   | 8 - 30D   |
|----------------|--------|----------|-----------|
| Cộng dồn       | 40.28% | 44.50%   | 37.29%    |
| Không cộng dồn | 40.28% | 4.22%    | 0.00%     |

## Lưu ý:

Với mô hình ARIMAX, mô hình không thể hiệu chỉnh để kết quả cẩn trọng hơn. Kết quả cuối cùng của bước xây dựng mô hình là kết quả tốt nhất trong tất cả các tổ hợp mà ta có thể chọn ra.

Nếu kết quả cuối cùng không có một mô hình ARIMAX nào thỏa mãn hết tất cả các kiểm định. Ngân hàng có thể cân nhắc quay trở lại lựa chọn phương pháp xây dựng mô hình phi tham số.

## 2.6. Bảo trì và rà soát mô hình

Đội ngũ xây dựng mô hình tiến hành bảo trì mô hình bao gồm việc tái vận hành mô hình hàng quý, và thực hiện phân tích tương quan hàng năm.

<!-- image -->

Ngân hàng được khuyến nghị cần thực hiện rà soát mô hình độc lập nhằm xác nhận rằng mô hình vẫn hoạt động đúng chức năng như thời điểm mới xây dựng và vẫn có thể áp dụng cho thực trạng của Ngân hàng.

## 3. Phụ lục - Chi tiết các kiểm định trong mô hình

## 3.1. Kiểm định Augmented Dickey - Fuller (ADF)

Kiểm định Augmented Dickey - Fuller (ADF) hay còn được gọi là kiểm định nghiệm đơn vị (Unit root test) được chấp nhận rộng rãi như là một cách để kiểm định tính dừng của một chuỗi thời gian.

Random walk (Bước ngẫu nhiên):

Random walk là một quy trình AR(1) đơn giản: Yt = Yt-1 +εt trong đó ε t là nhiễu trắng.

Xét chuỗi Yt tuân theo random walk:

- E(Yt ) = E(Y t-1 ) + E(εt ) = E(Y t-1 ) ⇒ Chuỗi Yt có kỳ vọng không đổi theo t
- Yt = Yt-1 +εt = Yt-2 +εt-1 +εt = ⋯ = Y0 +ε1 + ⋯εt với Y0 là giá trị đầu tiên của chuỗi Y và là 1 hằng số.
- Var(Yt ) = tσ 2 với σ 2 là phương sai không đổi của nhiễu trắng ε t

Chuỗi Y có phương sai thay đổi theo thời gian

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Chuỗi Y có hiện tượng tự tương quan

Chuỗi Y không dừng

Tuy nhiên, sai phân của Y là ΔYt = Yt -Yt-1 = εt lại là chuỗi dừng và ta có thể sử dụng để hồi quy để kiểm định các giả thuyết thống kê

Tiêu chuẩn Dickey - Fuller (DF):

Dickey - Fuller đã nghiên cứu chuỗi AR(1) và lấy random walk (Unit root) là một phép thử cho 1 chuỗi bất kì xem chuỗi đó có dừng hay không.

Với một chuỗi bất kì, biếu diễn chuỗi đó bằng quá trình AR(1):

<!-- formula-not-decoded -->

Đặt ρ - 1 = δ Ta sẽ kiểm định giả thuyết:

Ho: δ = 0 (Chuỗi có unit root =&gt; Chuỗi không dừng)

H1: δ &lt; 0 (Chuỗi không có unit roots =&gt; Chuỗi dừng)

Hồi quy và tính thống kê

<!-- formula-not-decoded -->

Tuân theo phân bố DF, τ &lt; τ α thì bác bỏ H0, và chuỗi sẽ là chuỗi dừng

Logic tương tự được áp dụng cho phương trình ΔYt = β0 +β1t + δYt-1 +∑ αi ΔYt-i q i=1 +εt , tính thống kê τ = δ ̂ SE(δ ̂ )

cho phương trình trên thì kiểm định trở thành Augmented Dickey - Fuller.

Augmented Dickey - Fuller (ADF):

Logic tương tự được áp dụng cho phương trình

<!-- formula-not-decoded -->

ADF là phiên bản tổng quát hơn của DF với

- Hệ số chặn: β0
- Thành phần xu hướng β1 t
- Độ trễ của các sai phân ∑ αi ΔYt-i q i=1

Ta vẫn tính thống kê

<!-- formula-not-decoded -->

cho phương trình trên và sử dụng các giá trị τα của phân bố DF để bác bỏ và thừa nhận các giả thuyết.

## 3.2. Kiểm định nhân quả Granger

Nhân quả Granger (Granger Causality) là một khái niệm trong thống kê, khi một biến Xt có tác dụng dự báo đáng kể một cách thống kê cho biến Yt thì ta nói Xt ảnh hưởng Granger (Granger cause) Yt .

Kiểm định Granger:

Xét 2 chuỗi Yt và Xt với 2 phương trình:

<!-- formula-not-decoded -->

Giả thuyết thống kê:

Ho:

β1 = β2 = ⋯ = βq = 0 , tức không có một biến X nào có tác dụng dự báo biến Y

H1:

β1 2 +β2 2 +⋯+βq 2 ≠ 0 , tức có ít nhất một biến X có tác dụng giải thích cho Y

Ta ước lượng và sử dụng kiểm định F cho 2 phương trình ta sẽ có 2 giá trị R1 2 và R2 2 cho mỗi phương trình (1), (2) (residual sum of squares)

<!-- formula-not-decoded -->

F sẽ tuân theo phân bố Fisher với bậc tự do (q, n - p - q) với n là số lượng quan sát của biến Y. Nếu F &gt; f α (q, n - p - q) thì ta loại bỏ giả thuyết H0, biến X có ảnh hưởng đến Y

## 3.3. Kiểm định Box - Pierce(BP)

Kiểm định Box - Pierce (BP) là kiểm định về tính tự tương quan của phần dư cho mô hình ARIMA(X).

Giả sử ta có 1 chuỗi phần dư et của một ước lượng.

Gọi ρi = Cor(et , e t-i ) là hệ số tự tương quan bậc i của chuỗi et

Giả thuyết thống kê:

H0:

ρ1 = ρ2 = … = ρk = 0 , tức là không có tự tương quan

H1: Có ít nhất 1 ρi ≠ 0

Xét thống kê

<!-- formula-not-decoded -->

được chọn đủ lớn sao cho ảnh hưởng của hệ số tự tương quạn bậc cao có thể bỏ qua. p, q là các bậc ARIMA(X) của phương trình ước lượng Nếu Q &gt; χ (k-p-q) 2 thì bác bỏ H0, tức là phần dư có tự tương quan

Q tiệm cận phân bố Khi bình phương χ 2 với bậc tự do (k - p - q) trong đó k

## 3.4. Kiểm định Jarque - Bera(JB)

Kiểm định Jarque - Bera là kiểm định mỗi chuỗi có phân bố chuẩn hay không. Do phân bố chuẩn có phân bố hình chuông đối xứng, tức hệ số bất đối xứng S = 0 và hệ số nhọn K =3.

H0: S = 0 và K = 3 , Chuỗi phân bố chuẩn

H1: S ≠ 0 và K ≠ 3 , Chuỗi không phân bố chuẩn

Tính hệ số bất đối xứng mẫu và hệ số nhọn mẫu:

<!-- formula-not-decoded -->

Với xi là giá trị thứ i của chuỗi cần kiểm định, x ̅ là trung bình mẫu và n là số quan sát trong chuỗi Khi chuỗi phân phối chuẩn, thống kê:

phân bố khi bình phương χα 2 (2) Nếu JB &gt; χ α 2 (2) thì H0 bị bác bỏ

## 3.5. Đánh giá MAPE

Kết quả MAPE có thể được đánh giá theo thông lệ tham khảo sau:

| MAPE (%)   | Ý nghĩa kết quả                                    |
|------------|----------------------------------------------------|
| <10        | Highly accurate forecasting (Dự báo chính xác cao) |
| 10 - 20    | Good forecasting (Dự báo tốt)                      |
| 20 - 50    | Reasonable forecasting (Dự báo chấp nhận được)     |
| > 50       | Inaccurate forecasting (Dự báo thiếu chính xác)    |

*Nguồn tài liệu tham khảo : Industrial and business forecasting methods. London: Butterworths, của  Lewis, C.D. (1982).

<!-- formula-not-decoded -->