Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)

## Giao phẩm BC03.03.06: Phương pháp luận cho mô hình thấu chi phi tham số

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

| 1. Định nghĩa hành vi                           |   4 |
|-------------------------------------------------|-----|
| 2. Quy trình xây dựng mô hình                   |   5 |
| 2.1. Chuẩn bị dữ liệu                           |   7 |
| 2.2. Lựa chọn phân khúc và lập giả định mô hình |   8 |
| 2.2.1. Lựa chọn phân khúc mô hình               |   8 |
| 2.2.2. Giả định và lưu ý đối với mô hình        |   9 |
| 2.2.3. Triển khai dữ liệu                       |  10 |
| 2.3. Xây dựng mô hình                           |  11 |
| 2.4. Kiểm tra hồi tố                            |  16 |
| 2.5. Bảo trì và rà soát mô hình                 |  20 |
| 3. Ứng dụng kết quả mô hình                     |  21 |
| 4. Phụ lục - Hiệu chỉnh mô hình                 |  23 |

## 1. Định nghĩa hành vi

Trong phạm vi dự án, ABBank cùng PwC Việt Nam xây dựng mô hình hành vi cho sản phẩm Thấu chi (TC).

Tài liệu Phương pháp luận cho sản phẩm thấu chi cung cấp phương pháp luận chi tiết mà PwC thực hiện cho danh mục TC của Ngân hàng.

## Mục đích xây dựng mô hình

Dự báo dòng tiền cho các khoản thấu chi trong Ngân hàng dựa trên hành vi của khách hàng.

## Hành vi được theo dõi

Hành vi sử dụng thấu chi: Hành vi khách hàng tiêu dùng thấu chi trên một hạn mức được cấp.

Hành vi trả nợ: việc khách hàng gửi tiền vào tài khoản thấu chi sẽ thanh toán một phần hoặc toàn bộ dư nợ thấu chi. Đây được xem là hành vi trả nợ trong mô hình thấu chi.

Hai hành vi nêu trên đều làm biến động dư nợ và dòng tiền vào / ra trong ngân hàng một cách ngẫu nhiên. Do đó, cần theo dõi và dự báo các hành vi trên.

## Kết quả mô hình mong đợi

Tỷ lệ trả nợ và tỉ lệ vay thấu chi / rút thêm tiền của danh mục trong vòng đời của khoản thấu chi.

## 2. Quy trình xây dựng mô hình

Sơ đồ dưới đây thể hiện quy trình tổng thể cho quản trị mô hình từ bước bắt đầu xây dựng cho đến bước cập nhật và duy trì mô hình, cùng với vai trò của các phòng/ban/đơn vị liên quan tương ứng với từng giai đoạn triển khai.

(*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trạng hỗ trợ từ cơ sở hạ tầng dữ liệu của Ngân hàng.

|   Bước | Trách nhiệm   | Các bước thực hiện                  | Tài liệu liên quan   | Thời gian            |
|--------|---------------|-------------------------------------|----------------------|----------------------|
|      1 | XDMH & CBDL   | Chuẩn bị dữ liệu                    |                      | Định kỳ hàng quý (*) |
|      2 | XDMH & KKD    | Thực hiện phân khúc và lập giả định |                      | Định kỳ hàng quý (*) |
|      3 | XDMH          | Xây dựng mô hình                    |                      | Định kỳ hàng quý (*) |
|      4 | XDMH & CBDL   | Kiểm tra hồi tố mô hình             |                      | Định kỳ hàng quý (*) |
|      5 | XDMH          | Hiệu chỉnh mô hình                  |                      | Định kỳ hàng quý (*) |
|      6 | XDMH & CBDL   | Bảo trì và rà soát mô hình          |                      | Định kỳ hàng quý (*) |

| STT    | Công việc                           | Ai   | Khi nào              | Cách làm                                                                                                                                                   | Bằng chứng   |
|--------|-------------------------------------|------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Bước 1 | Chuẩn bị dữ liệu                    | XDMH | Định kỳ hàng quý (*) | • Chuẩn bị yêu cầu dữ liệu • Kiểm tra và phát hiện vấn đề dữ liệu, nếu có                                                                                  |              |
| Bước 1 | Chuẩn bị dữ liệu                    | CBDL | Định kỳ hàng quý (*) | • Thu thập dữ liệu theo yêu cầu                                                                                                                            |              |
| Bước 2 | Thực hiện phân khúc và lập giả định | XDMH | Định kỳ hàng quý (*) | • Xác định các tiêu chí phân khúc mô hình cần thiết • Lập giả định cần thiết cho mô hình • Thực hiện phân khúc và triển khai dữ liệu                       |              |
| Bước 2 | Thực hiện phân khúc và lập giả định | ĐVKD | Định kỳ hàng quý (*) | • Mô tả nhu cầu nghiệp vụ • Phối hợp với đội ngũ XDMH để phân tích các nhu cầu nghiệp vụ                                                                   |              |
| Bước 3 | Xây dựng mô hình                    | XDMH | Định kỳ hàng quý (*) | • Lựa chọn phương pháp xây dựng mô hình • Phối hợp với đội ngũ xây dựng mô hình để xác định các yếu tố chính • Xây dựng mô hình dựa trên đặc tính sản phẩm |              |
| Bước 4 | Kiểm tra hồi tố môhình              | XDMH | Định kỳ hàng quý (*) | • Thực hiện kiểm tra hồi tố và phân tích kết quả                                                                                                           |              |
| Bước 4 | Kiểm tra hồi tố môhình              | CBDL | Định kỳ hàng quý (*) | • Thu thập dữ liệu kiểm tra hồi tố                                                                                                                         |              |
| Bước 5 | Hiệu chỉnh mô hình                  | XDMH | Định kỳ hàng quý (*) | • Hiệu chỉnh mô hình để có kết quả thận trọng hơn nếu cần thiết                                                                                            |              |
| Bước 6 | Bảo trì và rà soát mô hình          | XDMH | Định kỳ hàng quý (*) | • Tái vận hành mô hình trên bộ dữ liệu cập nhật • Đánh giá kết quả mô hình tại từng lần tái vận hành                                                       |              |
| Bước 6 | Bảo trì và rà soát mô hình          | CBDL | Định kỳ hàng quý (*) | • Thu thập dữ liệu cập nhật theo yêu cầu                                                                                                                   |              |

## 2.1. Chuẩn bị dữ liệu

Dữ liệu cho Thấu chi được lấy theo cấp độ số dư hàng ngày, hạn mức được cấp, số tiền vay thấu chi (số tiền vay thêm tại thời điểm báo cáo) của tài khoản trong thời gian tối thiểu 5 năm gần nhất so với ngày bắt đầu xây dựng mô hình.

Trong phạm vi giao phẩm dự án, dữ liệu được trích xuất từ 1/10/2015 đến 30/9/2020.

Dữ liệu được trích xuất theo yêu cầu trong Giao phẩm BC03.03.01: Yêu cầu dữ liệu.

## 2.2. Lựa chọn phân khúc và lập giả định mô hình

## 2.2.1. Lựa chọn phân khúc mô hình

Mô hình hành vi cho sản phẩm Thấu chi được phân khúc theo tiêu chí và nguyên tắc sau:

1. Phân khúc đó chiếm từ 5% số dư tổng danh mục của sản phẩm tương ứng.
2. Nếu thỏa mãn tiêu chí 1, Ngân hàng nên cân nhắc đến số lượng tài khoản của phân khúc đó. Nếu phân khúc có dưới 10 tài khoản , Ngân hàng được khuyến nghị không cần thiết phải xây dựng mô hình hành vi mà thay vào đó có thể quản lý riêng phân khúc đó do có số lượng tài khoản ít (dưới 10).

Dựa trên các tiêu chí và nguyên tắc trên, mô hình TC có kết quả phân khúc như sau (dữ liệu được lấy tại ngày cuối cùng của bộ dữ liệu - 30/09/2020):

<!-- image -->

01

<!-- image -->

<!-- image -->

| Khối khách hàng   | %Số dư tổng danh mục   | Số lượng tài khoản   |
|-------------------|------------------------|----------------------|
| CN                | 91.14%                 | 2,488                |
| DN, SME           | 8.86%                  | 61                   |
| Tổng              | 100%                   | 2,549                |

*Ngoài ra, yêu cầu dữ liệu hiện tại đã có các tiêu chí phân khúc tham khảo khác, như:

- -Nhóm ngành nghề khách hàng
- -Đơn vị tiền tệ (Trong mô hình TC, đơn vị tiền tệ không được xem xét là một tiêu chí phân khúc do dữ liệu quá khứ chỉ có đơn vị VND). Nếu về sau, sản phẩm thấu chi phục vụ cho những loại tiền tệ khác, ngân hàng có thể xem xét đưa vào tiêu chi phân khúc
- -Nhóm khoảng cách khách hàng
- -Khu vực, vùng miền
- (*) Tiêu chí bắt buộc phải có trong mô hình hành vi cho sản phẩm Thấu chi

## 2.2.2. Giả định và lưu ý đối với mô hình

Mô hình được xây dựng trên các giả định cơ bản sau:

| Giả định                                    | Mô tả                                                                                                                                                                                                                                |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hạn mức của tài khoản                       | Nếu không có dữ liệu về hạn mức được cấp của tài khoản, các tài khoản này sẽ bị đưa ra khỏi mô hình.                                                                                                                                 |
| Tính duy nhất của phân loại khối kinh doanh | Với những tài khoản có phân loại khối kinh doanh (trường Biz_line) thay đổi theo thời gian, mô hình sẽ chọn doanh khúc theo phân khúc gốc ban đầu. Những trường hợp không có phân loại khối kinh doanh sẽ được lược bỏ khỏi mô hình. |
| Dư nợ thấu chi là số dương                  | Mô hình loại bỏ các trường hợp dư nợ thấu chi > 0, do khi đó sản phẩm thấu chi đã chuyển thành sản phẩm CASA.                                                                                                                        |
| Ngày trả nợ theo hợp đồng                   | Mô hình loại bỏ các trường hợp thiếu ngày trả nợ theo hợp đồng (được xác định bởi trường Expiry_date và Pmt_date) và các bản ghi có ngày trả nợ theo hợp đồng vào ngày 01/01/1990.                                                   |

## 2.2.3. Triển khai dữ liệu

Số dư (hay balance) là số dư của tài khoản thấu chi theo từng ngày trong vòng đời của tài khoản đó.

Để có được dữ liệu đầu vào cho mô hình, dữ liệu thô từ Ngân hàng sẽ được triển khai theo thứ tự các bước như sau:

|   BƯỚC | NỘI DUNG                                                                                                                                      | LƯU Ý                                                                                                                                                                                                                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      1 | Trích xuất các trường dữ liệu cần dùng cho hành vi tiêu dùng thẻ thấu chi                                                                     | ▪ Tạo bảng dữ liệu gồm các trường dữ liệu sau: - Ngày báo cáo (Rep_date) - Số tài khoản (Acc_ID) - Ngày đáo hạn / ngày trả nợ theo hợp đồng của tài khoản (Expiry_date) - Hạn mức thấu chi (EOD_limit) - Số tiền thấu chi sử dụng tại ngày báo cáo (Use_amt) - Số dư hàng ngày (EOD_Bal) ▪ Ngày trả nợ theo hợp đồng (Pmt_date) |
|      2 | Cố định khối kinh doanh, khắc phục 1 số lỗi dữ liệu cho hành vi tiêu dùng thẻ thấu chi                                                        | ▪ Cố định khối kinh doanh của các tài khoản theo ngày báo cáo đầu tiên ▪ Loại bỏ khỏi mô hình những bản ghi không có hạn mức. ▪ Loại bỏ các trường hợp không có ngày đáo hạn / ngày trả nợ theo hợp đồng của tài khoản (Expiry_date) ▪ Loại bỏ các bản ghi dư nợ thấu chi lớn hơn 0                                             |
|      3 | Tạo bảng dữ liệu cho hành vi trả nợ                                                                                                           | Loại bỏ các trường hợp không có ngày trả nợ theo hợp đồng                                                                                                                                                                                                                                                                       |
|      4 | Tính khoảng cách từ ngày trả nợ thực tế so với ngày trả nợ theo hợp đồng (khoảng cách). Xác định hành vi trả nợ, hành vi sử dụng Thẻ tín dụng | ▪ Không lấy những khoản ngày trả nợ tín dụng quá hạn (ngày trả nợ thực tế sau ngày trả nợ theo hợp đồng). ▪ Các bản ghi không có giá trị số tiền trả nợ/số tiền sử dụng Thẻ tín dụng (null) được xem là 0.                                                                                                                      |

## 2.3. Xây dựng mô hình

Sơ đồ dưới đây thể hiện quy trình phân tích tương quan để lựa chọn phương pháp xây dựng mô hình cho từng phân khúc của mô hình Thấu chi:

<!-- image -->

2

Từng mô hình sẽ có những ưu điểm và hạn chế theo như phân tích dưới đây

## Mô hình phi tham số

Mô hình tham số

- Mô hình có phương pháp luận đơn giản, trực quan và có thể áp dụng dễ dàng.
- Các bước tính toán trong mô hình được thực hiện đơn giản.
- Phương pháp đã được chấp nhận và thực hiện ở nhiều ngân hàng với quy mô khác nhau trong nước, trong khu vực và trên toàn thế giới.
- × Phương pháp không thể hiện rõ các yếu tố ngoại sinh vì đã giả định rằng tác động của những yếu tố này được thể hiện trong biến động số dư của danh mục.
- Phương pháp được áp dụng tại nhiều ngân hàng trong và ngoài nước với quy mô khác nhau
- × Phương pháp luận xây dựng mô hình và các bước tính toán trong mô hình được thực hiện tương đối phức tạp.

1

## Phân chia dữ liệu:

Dữ liệu bao gồm số dư, hạn mức thấu chi, sử dụng thấu chi, số tiền trả nợ của tất cả các tài khoản thấu chi từ 01/10/2015 - 30/09/2020 .

Dữ liệu này sẽ được chia thành 2 bộ dữ liệu:

- Dữ liệu xây dựng mô hình (XDMH): bao gồm 4 năm đầu tiên của dữ liệu (từ 01/10/2015 - 30/09/2019 )
- Dữ liệu kiểm tra hồi tố (KTHT): bao gồm năm cuối cùng của dữ liệu (từ 01/10/2019 - 30/09/2020 ), được sử dụng để kiểm tra hồi tố và hiệu chỉnh mô hình

*Theo ý kiến được thống nhất từ Ngân hàng, mô hình có thể chia bộ dữ liệu XDMH là 70% và bộ dữ liệu KTHT là 30% số lượng quan sát trên toàn bộ dữ liệu 5 năm.

Mô hình được xây dựng cho từng phân khúc lựa chọn trước đó, trên bộ dữ liệu XDMH theo 2 bước sau

## Bước 1 : Nhóm hành vi theo khoảng cách

Lấy tổng hành vi trả nợ (payment) và hành vi sử dụng thấu chi (usage) cho mỗi phân khúc theo từng khoảng cách:

<!-- formula-not-decoded -->

Với

paymentT ( usageT) là số tiền trả nợ (sử dụng thấu chi) của một tài khoản tại khoảng cách T trong giai đoạn từ 2/10/2015 đến 30/09/2019

study\_total\_paymentT ( study\_total\_usage T ) là tổng trả nợ (sử dụng thấu chi) tại khoảng cách T từ 2/10/2015 đến 30/09/2019

(*) Hành vi trả nợ hoặc sử dụng thấu chi chỉ có thể quan sát từ ngày 2/10/2015 trở đi vì đối với hành vi tại ngày 1/10/2015, ta không có thông tin số dư/hạn mức trước khi có hành vi này (tức là số dư tại 30/09/2015). Theo đó, số dư/hạn mức sẽ quan sát tương ứng trong giai đoạn lùi đi 1 ngày so với quan sát hành vi, tức là từ 1/10/2015 đến 30/09/2019.

## Ví dụ

Trong một phân khúc quan sát từ 1/1/2016 đến 1/3/2016 có những tài khoản có khoảng cách đến kỳ trả nợ tiếp theo như sau:

| Reporting date   |   Khoảng cách (ngày) | ACCID        |   Balance |   Payment | Khoảng cách (ngày)   | Balance   | Drawdown   |
|------------------|----------------------|--------------|-----------|-----------|----------------------|-----------|------------|
| 1/1/2016         |                   31 | 000111WES123 |       100 |         0 | 31                   | 300       | 0          |
| 1/1/2016         |                   31 | 000333WES456 |       200 |         0 | 32                   | 285       | 15         |
| 2/1/2016         |                   32 | 000111WES123 |        90 |        10 | 33                   | 255       | 30         |
| 2/1/2016         |                   32 | 000333WES456 |       195 |         5 |                      |           |            |
| 3/1/2016         |                   33 | 000111WES123 |        75 |        15 |                      |           |            |
| 3/1/2016         |                   33 | 000333WES456 |       180 |        15 |                      |           |            |

## Bước 2: Nhóm hành vi theo khoảng cách

Sau khi xác định khoảng cách tại từng thời điểm t của từng tài khoản, xác định và nhóm hành vi trả nợ và sử dụng thấu chi (gọi chung là hành vi) theo khoảng cách

*Các bước tính toán được thực hiện riêng cho mỗi loại hành vi

<!-- formula-not-decoded -->

2

1

Với:

BehaviourT

: Hành vi của phân khúc tại khoảng cách T.

BehaviourT,i

: Hành vi của tài khoản i tại khoảng cách T.

Ví dụ:

Bước 3: Xác định tỷ lệ sử dụng thấu chi, tỷ lệ trả nợ theo khoảng cách

| Reporting date   |   Khoảng cách (ngày) | ACCID        |   Balance |   Payment | Khoảng cách (ngày)   | Balance   | Drawdown   |
|------------------|----------------------|--------------|-----------|-----------|----------------------|-----------|------------|
| 1/1/2016         |                   31 | 000111WES123 |       100 |       100 | 31                   | 300       | 200        |
| 1/1/2016         |                   31 | 000333WES456 |       200 |       100 | 32                   | 285       | 300        |
| 2/1/2016         |                   32 | 000111WES123 |       285 |       100 |                      |           |            |
| 2/1/2016         |                   32 | 000333WES456 |         0 |       200 |                      |           |            |

## Xác định tỷ lệ trả nợ tại từng khoảng cách

Tỷ lệ trả nợ ở khoảng cách t được xác định dựa trên tổng lượng trả nợ tại khoảng cách T và số dư của tổng phân khúc tại khoảng cách T-1

<!-- formula-not-decoded -->

Với:

PRT : Tỷ lệ trả nợ của phân khúc tại khoảng cách T (Payment Rate)

PaymentT

: Lượng trả nợ của phân khúc tại khoảng cách T được tính ở bước 2

EOD balanceT-1

: Số dư của tổng phân khúc tại khoảng cách T-1

## Xác định tỷ lệ sử dụng thấu chi theo từng khoảng cách

Tỷ lệ sử dụng thấu chi ở khoảng cách T được xác định dựa trên tổng số tiền sử dụng thấu chi tại T và tổng hạn mức được cấp tại T

<!-- formula-not-decoded -->

Với:

WRT

: Tỷ lệ sử dụng thấu chi của phân khúc tại khoảng cách T (Withdrawal Rate)

𝑊𝑖𝑡ℎ𝑑𝑟𝑎𝑤𝑎𝑙𝑇 Lượng sử dụng thấu chi của phân khúc tại T

Limit T

: Hạn mức thấu chi của phân khúc tại khoảng cách T

Ví dụ mẫu về tính toán PR cho một phân khúc mô hình (*Số liệu chỉ mang tính minh họa)

2

1

2

|   Khoảng cách | Tổng trả nợ   | Số dư tại khoảng cách T-1   |        PR |
|---------------|---------------|-----------------------------|-----------|
|            10 | 5,986,321,627 | 10,597,446,587,173          | 0.0005649 |
|             9 | 581,360,035   | 10,574,971,883,342          | 0.0000550 |
|             8 | 1,097,690,043 | 10,561,920,382,395          | 0.0001039 |
|             7 | 293,266,334   | 10,550,381,777,981          | 0.0000278 |
|             6 | 9,448,839,727 | 10,549,102,133,647          | 0.0008957 |
|             5 | 1,615,770,958 | 10,533,490,477,143          | 0.0001534 |
|             4 | 1,268,418,661 | 10,513,694,515,074          | 0.0001206 |
|             3 | 1,660,710,842 | 10,512,381,508,413          | 0.0001580 |
|             2 | 1,924,601,049 | 10,504,974,287,853          | 0.0001832 |
|             1 | 2,492,551,589 | 10,477,752,643,413          | 0.0002379 |

1

## 2.4. Kiểm tra hồi tố

Mục đích của kiểm tra hồi tố nhằm đánh giá tính cẩn trọng của kết quả từ bộ dữ liệu XDMH.

Kiểm tra hồi tố được thực hiện trên bộ dữ liệu KTHT năm cuối cùng (1/10/2019 đến 30/09/2020) , cho từng phân khúc mô hình, theo 3 bước sau:

Bước 1:

## Xác định PR, WR cho phân khúc trong giai đoạn kiểm tra hồi tố

PR trong giai đoạn kiểm tra hồi tố được tính toán tương tự như các bước xây dựng mô hình:

<!-- formula-not-decoded -->

Với

PaymentT là Lượng trả nợ của một tài khoản tại khoảng cách T trong giai đoạn kiểm tra hồi tố test\_paymentT là tổng lượng trả nợ tại khoảng cách T trong giai đoạn kiểm tra hồi tố EOD balanceT-1 : Tổng số dư của phân khúc tại khoảng cách T-1 trong giai đoạn kiểm tra hồi tố

<!-- formula-not-decoded -->

Với:

PRT : Tỷ lệ trả nợ của phân khúc tại khoảng cách T (Payment Rate)

test\_total\_payment T : Lượng trả nợ của phân khúc tại khoảng cách T

EOD balanceT-1 : Tổng số dư của phân khúc tại khoảng cách T-1 trong giai đoạn kiểm tra hồi tố

<!-- formula-not-decoded -->

Với:

WRT : Tỷ lệ sử dụng thấu chi của phân khúc tại khoảng cách T (Withdrawal Rate)

𝑇𝑒𝑠𝑡\_ 𝑊𝑖𝑡ℎ𝑑𝑟𝑎𝑤𝑎𝑙𝑇 Lượng sử dụng thấu chi của phân khúc tại khoảng cách T

(*) Hành vi trả nợ (sử dụng thấu chi),  trong giai đoạn kiểm tra hồi tố có thể quan sát từ 1/10/2019 do dữ liệu có số dư tại 30/09/2019. Theo đó, số dư (hạn mức) quan sát cho kiểm tra hồi tố tương ứng trong giai đoạn lùi đi 1 ngày so với quan sát hành vi trả nợ (sử dụng thấu chi), tức là từ 30/09/2019 đến 29/09/2020.

Bước 2:

Xây dựng đường cong duy trì (Survival Curve) và khoảng tin cậy (confident\_level) cho dữ liệu mô hình và dữ liệu kiểm tra hồi tố

Đường cong duy trì của dữ liệu xây dựng mô hình được xây dựng như sau:

- Xác định tỷ lệ duy trì (survival\_rate) cho hành vi trả nợ và sử dụng thấu chi tại từng khoảng cách:

<!-- formula-not-decoded -->

Survival rate \_WT = 1 -WRT

Với

Survival rate T là tỷ lệ duy trì tại khoảng cách T

PRT

: Tỉ lệ trả nợ tại khoảng cách T

PRT

: Tỉ lệ trả nợ tại khoảng cách T

WR

T : Tỉ lệ sử dụng thấu chi tại khoảng cách T

- Xác định khoảng tin cậy cho tỷ lệ duy trì tại từng khoảng cách theo phương pháp Greenwood: Confidence T

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Với

ConfidenceT là khoảng tin cậy tại khoảng cách T Balancei-1 = EOD balancei-1 là tổng số dư phân khúc tại khoảng cách i-1 Limit i là tổng hạn mức tại khoảng cách i Withdrawali là tổng vay thấu chi tại khoảng cách i c là độ tin cậy (khuyến nghị lấy 99%) z c là Z-Score của xác xuất (1-c)/2

- Xác định tỷ lệ duy trì biên trên và dưới trong khoảng tin cậy:

UpperT = Survival rateT + ConfidenceT

LowerT = Survival rateT ConfidenceT

- Tại các khoảng cách không có dữ liệu, giả định là tỷ lệ duy trì và các biên không thay đổi, ta điền các khoảng cách đó theo dữ liệu của khoảng cách trước đó

Tương tự, với dữ liệu kiểm tra hồi tố ta cũng có được tỷ lệ duy trì biên ( Upper\_testT và Lower\_testT ) và đường cong duy trì ( Survival\_rate\_test T )

## Bước 3:

## Đánh giá kết quả mô hình

## Hành vi trả nợ

Tại từng khoảng cách, đánh giá đường cong duy trì của bộ kết quả 4 năm. Kết quả được xem là 'đạt' tại khoảng cách T nếu:

<!-- formula-not-decoded -->

## Hành vi sử dụng thấu chi

Tại từng khoảng cách, đánh giá đường cong duy trì của bộ kết quả 4 năm. Kết quả được xem là 'đạt' tại khoảng cách T nếu:

<!-- formula-not-decoded -->

Dưới đây là hình ảnh minh họa cho các trường hợp có thể xảy ra của 2 bộ đường cong duy trì của kết quả 4 năm (nét liền) và 1 năm (nét đứt):

1

<!-- image -->

## Ví dụ:

Xây dựng đường cong duy trì cho dữ liệu xây dựng mô hình (study) của hành vi sử dụng thấu chi:

|   Khoảng cách |   Limit (T) A |   study_ total_ withdrawa l (T) B | WR (T) B/A   | Survival _ rate (T) S   | Confiden t (T) C   | Lower (T) S-C   | Upper(T) S+C   |
|---------------|---------------|-----------------------------------|--------------|-------------------------|--------------------|-----------------|----------------|
|             8 |           100 |                                20 | 20.00%       | 80%                     | 10.2%              | 69.8%           | 90.2%          |
|             7 |            80 |                                 9 | 11.25%       | 71%                     | 11.6%              | 59.4%           | 82.6%          |
|             6 |            71 |                                 0 | 0.00%        | 71%                     | 11.6%              | 59.4%           | 82.6%          |
|             5 |            71 |                                 1 | 1.41%        | 70%                     | 11.7%              | 58.3%           | 81.7%          |
|             4 |            70 |                                 2 | 2.86%        | 68%                     | 11.9%              | 56.1%           | 79.9%          |
|             3 |            68 |                                23 | 33.82%       | 45%                     | 12.7%              | 32.3%           | 57.7%          |
|             2 |            45 |                                 5 | 11.11%       | 40%                     | 12.5%              | 27.5%           | 52.5%          |
|             1 |            40 |                                 3 | 7.50%        | 37%                     | 12.4%              | 24.6%           | 49.4%          |

Xây dựng đường cong duy trì cho dữ liệu kiểm tra hồi tố (test) của hành vi trả nợ:

1

|   Khoảng cách |   EOD Balance (T-1) A |   test_ total_ payment (T) B | PR_test (T) B/A   | Survival_ rate (T) S   | Confident_test (T) C   | Lower_ test (T) S-C   | Upper_ test(T) S+C   |
|---------------|-----------------------|------------------------------|-------------------|------------------------|------------------------|-----------------------|----------------------|
|             8 |                   100 |                            0 | 0.00%             | 100.00%                | 0.00%                  | 100.00%               | 100.00%              |
|             7 |                   100 |                           20 | 20.00%            | 80.00%                 | 10.30%                 | 69.70%                | 90.30%               |
|             6 |                    80 |                            1 | 1.25%             | 79.00%                 | 10.49%                 | 68.51%                | 89.49%               |
|             5 |                    79 |                           18 | 22.78%            | 61.00%                 | 12.56%                 | 48.44%                | 73.56%               |
|             4 |                    61 |                            0 | 0.00%             | 61.00%                 | 12.56%                 | 48.44%                | 73.56%               |
|             3 |                    61 |                           31 | 50.82%            | 30.00%                 | 11.80%                 | 18.20%                | 41.80%               |
|             2 |                    30 |                            9 | 30.00%            | 21.00%                 | 10.49%                 | 10.51%                | 31.49%               |
|             1 |                    21 |                            3 | 14.29%            | 18.00%                 | 9.90%                  | 8.10%                 | 27.90%               |

## Kiểm tra hồi tố:

|   Khoảng cách | Lower (T)   | Upper_ test(T)   | Backtest   |
|---------------|-------------|------------------|------------|
|             8 | 69.8%       | 100.00%          | ĐẠT        |
|             7 | 59.4%       | 90.30%           | ĐẠT        |
|             6 | 59.4%       | 89.49%           | ĐẠT        |
|             5 | 58.3%       | 73.56%           | ĐẠT        |
|             4 | 56.1%       | 73.56%           | ĐẠT        |
|             3 | 32.3%       | 41.80%           | ĐẠT        |
|             2 | 27.5%       | 31.49%           | ĐẠT        |
|             1 | 24.6%       | 27.90%           | ĐẠT        |

## 2.5. Bảo trì và rà soát mô hình

Đội ngũ xây dựng mô hình tiến hành bảo trì mô hình bao gồm việc tái vận hành mô hình hàng quý (*), và thực hiện phân tích tương quan hàng năm.

<!-- image -->

Ngân hàng được khuyến nghị cần thực hiện rà soát mô hình độc lập nhằm xác nhận rằng mô hình vẫn hoạt động đúng chức năng như thời điểm mới xây dựng và vẫn có thể áp dụng cho thực trạng của Ngân hàng.

- Một đội ngũ kiểm định độc lập (QLRR) sẽ thực hiện kiểm định độc lập và báo cáo tổng thể để trình lên Hội đồng quản trị.
- Báo cáo này bao gồm khuyến nghị dự báo, có thể là định lượng hoặc định tính.
- Hội đồng quản trị sẽ ra quyết định sau cùng dựa trên khuyến nghị và vấn đề của báo cáo rà soát độc lập cho từng mô hình.

(*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trạng hỗ trợ từ cơ sở hạ tầng dữ liệu của Ngân hàng.

1

## 3. Ứng dụng kết quả mô hình

Ví dụ có kết quả mô hình cho tài khoản thấu chi đến hạn trong vòng 7 ngày có dư nợ là 1,000,000 VND, hạn mức được cấp là 10,000,000 VND. Giả định hạn mức này của tài khoản thấu chi sẽ không thay đổi cho đến ngày đáo hạn.

Dự báo cho một khoản thấu chi 7 ngày tại khoảng cách 3 có số dư là 1,000,000 VND và phần chưa sử dụng là 2,000,000 VND:

|   Khoảng cách | PR   | WR   | Hạn mức    | Dòng tiền hợp đồng   | Dòng tiền trả nợ (1)   | Dòng tiền sử dụng thấu chi (2)   | Dòng tiền hành vi (3)   | Dư nợ hành vi (4)   |
|---------------|------|------|------------|----------------------|------------------------|----------------------------------|-------------------------|---------------------|
|             6 | 0%   | 2%   | 10,000,000 | 0                    | -                      | 200,000                          | -200,000                | 1,200,000           |
|             5 | 0%   | 0%   | 10,000,000 | 0                    | -                      | -                                | -                       | 1,200,000           |
|             4 | 0%   | 0%   | 10,000,000 | 0                    | -                      | -                                | -                       | 1,200,000           |
|             3 | 5%   | 0%   | 10,000,000 | 0                    | 60,000                 | -                                | 60,000                  | 1,140,000           |
|             2 | 0%   | 0%   | 10,000,000 | 0                    | -                      | -                                | -                       | 1,140,000           |
|             1 | 0%   | 0%   | 10,000,000 | 1,000,000            | -                      | -                                | -                       | 1,140,000           |
|             0 | 95%  | 0%   | 10,000,000 | 0                    | 1,083,000              | -                                | 1,083,000               | 57,000              |

Dòng tiền hành vi được tính theo các bước:

1. Dòng tiền trả nợ
2. Dòng tiền sử dụng thấu chi

Dòng tiền sử dụng thấu chi T = Hạn mứcT ∗ WRT

3. Dòng tiền hành vi

Dòng tiền hành vi T = Dòng tiền trả nợ T -Dòng tiền sử dụng thấu chiT

Dư nợ hành viT = Dư nợ hành viT-1 -Dòng tiền hành viT

với T là khoảng cách tương ứng

Trong ví dụ, tại khoảng cách 6 ngày

- Dòng tiền trả nợ = 0% x 1,000,000 = 0 (VND)
- Dòng tiền sử dụng thấu chi = 2% * 10,000,000 = 200,000 (VND)
- Dòng tiền hành vi = 0 - 200,000 = -200,000 (VND)
- Dư nợ hành vi = 1,000,000 - (-200,000) = 1,200,000 (VND)
4. Dư nợ hành vi

...

Dòng tiền hành vi được phân bổ lại vào các dải kỳ hạn tương ứng như sau

Dòng tiền trả nợ T = Số dưT-1 ∗ PRT

| Dài kì hạn   |   Qua đêm |   2-7D |   8-30D |   31-90D |   91-180D |   181-360D | >360D   |
|--------------|-----------|--------|---------|----------|-----------|------------|---------|
| Số ngày      |         1 |      7 |      30 |       90 |       180 |        360 | >360    |

## 4. Phụ lục - Hiệu chỉnh mô hình

Mục đích của hiệu chỉnh nhằm đảm bảo tính cẩn trọng của kết quả mô hình theo dữ liệu cập nhật nhất.

Theo thông lệ về mô hình đã được PwC tư vấn/sử dụng tại một số Ngân hang tại Việt Nam, phương pháp hiệu chỉnh như trình bày dưới đây.

Trong trường hợp tại 1 khoảng cách nhất định mà mô hình không đạt kiểm tra hồi tố ở bước trước đó, kết quả PR (WR) tại khoảng cách đó sẽ được lấy theo bộ test. Bộ PR (WR) cuối cùng sau khi hiệu chỉnh sẽ là kết quả của mô hình.

Ví dụ: Tiếp tục với ví dụ phần

Kiểm tra hồi tố cho hành vi sử dụng thấu chi:

|   Khoảng cách | Lower (T)   | Upper_ test(T)   | Backtest   | WR (T)   | WR_test (T)   | WR (T) (Đã hiệu chỉnh)   |
|---------------|-------------|------------------|------------|----------|---------------|--------------------------|
|             8 | 69.8%       | 100.00%          | ĐẠT        | 20.00%   | 0.00%         | 20.00%                   |
|             7 | 59.4%       | 90.30%           | ĐẠT        | 11.25%   | 20.00%        | 11.25%                   |
|             6 | 59.4%       | 89.49%           | ĐẠT        | 0.00%    | 1.25%         | 0.00%                    |
|             5 | 58.3%       | 73.56%           | ĐẠT        | 1.41%    | 22.78%        | 1.41%                    |
|             4 | 56.1%       | 73.56%           | ĐẠT        | 2.86%    | 0.00%         | 2.86%                    |
|             3 | 32.3%       | 41.80%           | ĐẠT        | 33.82%   | 50.82%        | 33.82%                   |
|             2 | 27.5%       | 31.49%           | ĐẠT        | 11.11%   | 30.00%        | 11.11%                   |
|             1 | 24.6%       | 27.90%           | ĐẠT        | 7.50%    | 14.29%        | 7.50%                    |

Sau khi thu được kết quả CPR hiệu chỉnh (tương tự đối với WR hiệu chỉnh), thực hiện xây dựng bộ kết quả Tỷ lệ duy trì cộng dồn, nhằm áp dụng kết quả mô hình cho danh mục hiện tại ở các bước sau

Cumulative Survival rate T-1 = Cumulative Survival rate T ×(1 -CPR caibrate T-1 )

<!-- image -->

|   Khoảng cách | CPR (T) (Đã hiệu chỉnh)   | CumulativeSurvival rate (T) (Đã hiệu chỉnh)   |
|---------------|---------------------------|-----------------------------------------------|
|             8 | 0.05%                     | 99.95%                                        |
|             7 | 0.00%                     | 99.95%                                        |
|             6 | 0.01%                     | 99.94%                                        |
|             5 | 0.00%                     | 99.94%                                        |
|             4 | 0.07%                     | 99.87%                                        |
|             3 | 0.01%                     | 99.86%                                        |
|             2 | 0.01%                     | 99.85%                                        |
|             1 | 0.01%                     | 99.84%                                        |

Tại khoảng cách T = 8:

Cumulative Survival rate T=8 = 1 - 0.05% = 99.95%

Tại khoảng cách T = 7:

Cumulative Survival rate T=7 = 99.95% ∗ (1 - 0.00%) = 99.95%

*Theo ý kiến đã được thống nhất từ Ngân hàng, mô hình có thể không lựa chọn phương pháp hiệu chỉnh này.