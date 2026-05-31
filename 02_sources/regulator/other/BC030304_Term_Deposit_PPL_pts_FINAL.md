



# **Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)**

# **Giao phẩm BC03.03.04: Phương pháp luận cho mô hình hành vi tái tục và rút trước hạn cho tiền gửi có kì hạn**

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

| 1. Định nghĩa hành vi                           | 4  |
|-------------------------------------------------|----|
| 2. Quy trình xây dựng mô hình                   | 5  |
| 2.1. Chuẩn bị dữ liệu                           | 7  |
| 2.2. Lựa chọn phân khúc và lập giả định mô hình | 8  |
| 2.2.1. Lựa chọn phân khúc mô hình               | 8  |
| 2.2.2. Giả định và lưu ý đối với mô hình        | 9  |
| 2.2.3. Triển khai dữ liệu                       | 11 |
| 2.3. Xây dựng mô hình                           | 15 |
| 2.4. Kiểm tra hồi tố                            | 19 |
| 2.5. Bảo trì và rà soát mô hình                 | 22 |
| 3. Ứng dụng kết quả mô hình                     | 23 |
| 4. Phụ lục – Hiệu chỉnh mô hình                 | 24 |

# <span id="page-3-0"></span>*1. Định nghĩa hành vi*

Trong phạm vi dự án, ABBank cùng PwC Việt Nam xây dựng mô hình hành vi cho sản phẩm Tiền gửi có kỳ hạn (TGKH).

Tài liệu Phương pháp luận cho tiền gửi có kỳ hạn cung cấp phương pháp luận chi tiết mà PwC thực hiện cho danh mục TGKH của Ngân hàng.

#### **Mục đích xây dựng mô hình**

Dự báo dòng tiền cho các khoản tiền gửi trong Ngân hàng dựa trên hành vi của khách hàng.

#### **Hành vi được theo dõi**

Hành vi tái tục: Việc khách hàng tiếp tục gửi tiền có kì hạn trong Ngân hàng sau khi tiền gửi có kỳ hạn trước đó của khách hàng đó đáo hạn

Hành vi rút trước hạn: Việc khách hàng rút toàn bộ hoặc 1 phần số tiền gửi kì hạn trước ngày đáo hạn của khoản tiền gửi đó.

#### **Kết quả mô hình mong đợi**

Tỷ lệ tiền được rút ra khỏi danh mục trong vòng đời của khoản tiền gửi.

# <span id="page-4-0"></span>*2. Quy trình xây dựng mô hình*

Sơ đồ dưới đây thể hiện quy trình tổng thể cho quản trị mô hình từ bước bắt đầu xây dựng cho bước đến bước cập nhật và duy trì mô hình, cùng với vai trò của các phòng/ban/đơn vị liên quan tương ứng với từng giai đoạn triển khai.

*(\*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trạng hỗ trợ từ cơ sở hạ tầng dữ liệu của Ngân hàng.*

| Bước | Trách nhiệm    | Các bước thực hiện                     | Tài liệu liên<br>quan | Thời gian               |
|------|----------------|----------------------------------------|-----------------------|-------------------------|
| 1    | XDMH &<br>CBDL | Chuẩn bị dữ liệu                       |                       | Định kỳ hàng quý<br>(*) |
| 2    | XDMH & KKD     | Thực hiện phân khúc và<br>lập giả định |                       | Định kỳ hàng quý<br>(*) |
| 3    | XDMH           | Xây dựng mô hình                       |                       | Định kỳ hàng quý<br>(*) |
| 4    | XDMH &<br>CBDL | Kiểm tra hồi tố mô hình                |                       | Định kỳ hàng quý<br>(*) |
| 5    | XDMH           | Hiệu chỉnh mô hình                     |                       | Định kỳ hàng quý<br>(*) |
| 6    | XDMH &<br>CBDL | Bảo trì và rà soát<br>mô hình          |                       | Định kỳ hàng quý<br>(*) |

| STT       | Công việc                                 | Ai                                                       | Khi nào                 | Cách làm                                                                                                                                                                           | Bằng chứng |  |
|-----------|-------------------------------------------|----------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--|
| Bước<br>1 | Chuẩn bị<br>dữ<br>liệu                    | XDMH<br>Định kỳ<br>hàng quý<br>(*)<br>•<br>Chuẩn bị<br>• |                         | yêu cầu dữ<br>liệu<br>Kiểm tra và phát hiện vấn đề<br>dữ<br>liệu, nếu có                                                                                                           |            |  |
|           |                                           | CBDL                                                     | Định kỳ<br>hàng quý (*) | •<br>Thu thập dữ<br>liệu theo yêu cầu                                                                                                                                              |            |  |
| Bước<br>2 | Thực hiện phân khúc<br>và lập giả<br>định | XDMH                                                     | Định kỳ<br>hàng quý (*) | •<br>Xác định các tiêu chí phân khúc mô hình cần thiết<br>•<br>Lập giả<br>định cần thiết cho mô hình<br>•<br>Thực hiện phân khúc và triển khai dữ<br>liệu                          |            |  |
|           |                                           | ĐVKD                                                     | Định kỳ<br>hàng quý (*) | •<br>Mô tả<br>nhu cầu nghiệp vụ<br>•<br>Phối hợp với đội ngũ XDMH để<br>phân tích các nhu cầu<br>nghiệp vụ                                                                         |            |  |
| Bước<br>3 | Xây dựng mô hình                          | XDMH                                                     | Định kỳ<br>hàng quý (*) | •<br>Lựa chọn phương pháp xây dựng mô hình<br>•<br>Phối hợp với đội ngũ xây dựng mô hình để<br>xác định<br>các yếu tố<br>chính<br>•<br>Xây dựng mô hình dựa trên đặc tính sản phẩm |            |  |
| Bước<br>4 | Kiểm tra hồi tố mô hình                   | XDMH                                                     | Định kỳ<br>hàng quý (*) | •<br>Thực hiện kiểm tra hồi tố<br>và phân tích kết quả                                                                                                                             |            |  |
|           |                                           | CBDL                                                     | Định kỳ<br>hàng quý (*) | •<br>Thu thập dữ<br>liệu kiểm tra hồi tố                                                                                                                                           |            |  |
| Bước<br>5 | Hiệu chỉnh mô hình                        | XDMH                                                     | Định kỳ<br>hàng quý (*) | •<br>Hiệu chỉnh mô hình để<br>có kết quả<br>thận trọng hơn nếu<br>cần thiết                                                                                                        |            |  |
| Bước<br>6 | Bảo trì và rà soát mô<br>hình             | XDMH                                                     | Định kỳ<br>hàng quý (*) | •<br>Tái vận hành mô hình trên bộ<br>dữ<br>liệu cập nhật<br>•<br>Đánh giá kết quả<br>mô hình tại từng lần tái vận hành                                                             |            |  |
|           |                                           | CBDL                                                     | Định kỳ<br>hàng quý (*) | •<br>Thu thập dữ<br>liệu cập nhật theo yêu cầu                                                                                                                                     |            |  |

## <span id="page-6-0"></span>*2.1. Chuẩn bị dữ liệu*

Dữ liệu cho tiền gửi CKH được lấy theo cấp độ **số dư hàng ngày của tài khoản, trong thời gian tối thiểu 5 năm gần nhất so với ngày bắt đầu xây dựng mô hình.**

**Trong phạm vi giao phẩm dự án, dữ liệu được trích xuất từ 1/10/2015 đến 30/9/2020.**

Dữ liệu được trích xuất theo yêu cầu trong Giao phẩm BC03.03.01: Yêu cầu dữ liệu.

# <span id="page-7-0"></span>*2.2. Lựa chọn phân khúc và lập giả định mô hình*

### <span id="page-7-1"></span>*2.2.1. Lựa chọn phân khúc mô hình*

Mô hình hành vi cho sản phẩm Tiền gửi có kỳ hạn được phân khúc theo tiêu chí và nguyên tắc sau:

- 1. Phân khúc đó chiếm từ **5% số dư tổng danh mục** của sản phẩm tương ứng.
- 2. Nếu thỏa mãn tiêu chí 1, Ngân hàng nên cân nhắc đến số lượng tài khoản của phân khúc đó. Nếu phân khúc có **dưới 10 tài khoản**, Ngân hàng được khuyến nghị không cần thiết phải xây dựng mô hình hành vi mà thay vào đó có thể quản lý riêng phân khúc đó do có số lượng tài khoản ít (dưới 10).

Dựa trên các tiêu chí và nguyên tắc trên, mô hình TGCKH có kết quả phân khúc như sau (dữ liệu được lấy tại ngày cuối cùng của bộ dữ liệu – 30/09/2020):

![](_page_7_Figure_6.jpeg)

| Đơn vị tiền<br>tệ | Khối khách<br>hang | Kỳ hạn | % Tổng danh<br>mục | Số lượng tài<br>khoản |
|-------------------|--------------------|--------|--------------------|-----------------------|
| VND               | CN                 | 12     | 29.39%             | 80,808                |
| VND               | CN                 | 6      | 12.23%             | 36,289                |
| VND               | DN                 | 6      | 10.84%             | 176                   |
| VND               | DN                 | 12     | 7.37%              | 342                   |
| VND               | TCTD               | 1      | 6.90%              | 13                    |
| VND               | CN                 | 1      | 5.79%              | 22,569                |
| VND               | DN                 | 1      | 5.69%              | 321                   |
|                   | Các phân khúc khác |        | 21.79%             | 12,743                |
|                   | Tổng               |        | 100%               | 153,261               |

\*Ngoài ra, yêu cầu dữ liệu hiện tại đã có các tiêu chí phân khúc tham khảo khác, như:

- Nhóm ngành nghề khách hang
- Nhóm tuổi khách hàng
- Khu vực, vùng miền
- Loại tài khoản /Mục đích sử dụng tài khoản

*(\*) Tiêu chí bắt buộc phải có trong mô hình hành vi cho TGCKH*

## <span id="page-8-0"></span>*2.2.2. Giả định và lưu ý đối với mô hình*

**Mô hình được xây dựng trên các giả định cơ bản sau:**

| Giả định                             | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      | Một tài khoản TGCKH cần được cố định với chỉ duy nhất một mã Khách hàng,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Tính duy nhất của tài khoản          | nhằm phục vụ cho giả định về tái tục khác tài khoản được định nghĩa ở phần<br>tiếp theo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Định nghĩa tái tục<br>khác tài khoản | 2 tài khoản có mã khác nhau được xem là tái tục khi thỏa mãn các điều kiện:<br>•<br>Thuộc cùng một phân khúc (theo các tiêu chí là cùng kỳ hạn, đơn vị tiền<br>tệ, khối kinh doanh, sản phẩm), và<br>•<br>Cùng mã khách hàng, và<br>•<br>Tài khoản mới có ngày mở bằng hoặc không trễ hơn 3 ngày (cho phép<br>độ trễ vì có thể có ngày nghỉ lễ như thứ 7, Chủ nhật, …, Ngân hàng có<br>thể điều chỉnh số ngày cho phép tuy nhiên khuyến nghị không nên lấy<br>nhiều hơn 3 ngày) so với ngày đóng của tài khoản cũ, và<br>•<br>Các cặp tài khoản được nối 1-1 (tức là chỉ có 1 tài khoản đóng và 1 tài<br>khoản mở trong cùng 1 ngày)*.<br>Các tài khoản khác nhau được nối theo quy tắc tái tục khác tài khoản sẽ được<br>lựa chọn theo tính ưu tiên khoảng cách ngày mở - (trừ) ngày đóng nhỏ nhất,<br>nhằm đảm bảo 1 tài khoản chỉ được nối với 1 tài khoản khác.<br>Giả định được minh họa theo ví dụ 3, 2.2.3. Triển khai dữ liệu.<br>(*) Mô hình sẽ không phân tích các trường hợp nhiều tài khoản đóng có thể nối<br>được với nhiều tài khoản mở trong cùng một ngày, do trường hợp này diễn ra rất<br>ít và rất phức tạp để lập giả định lựa chọn. Do đó, trong phạm vi 3 ngày cho phép<br>theo giả định, tại mỗi ngày, mô hình chỉ lấy những trường hợp mà khách hàng<br>chỉ có duy nhất một cặp đóng – mở (nối 1-1), và sau đó ưu tiên lấy cặp có khoảng<br>cách ngày đóng – mở gần nhất. |
| Các ngày bị thiếu                    | Dữ liệu vào ngày Chủ nhật và các ngày nghỉ lễ không được lưu lại sẽ được<br>điền theo ngày có gần nhất trước nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Tính duy nhất của mã doanh<br>nghiệp | Tài khoản khách hàng có doanh nghiệp (Biz_line) thay đổi theo thời gian, mô<br>hình sẽ chọn doanh khúc theo phân khúc gốc ban đầu. Những trường hợp có<br>mã doanh nghiệp không tồn tại sẽ được lược bỏ khỏi mô hình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| Giả định                         | Mô tả                                                                                                                                                                                                                 |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mã doanh nghiệp thuộc khối<br>NV | Các tài khoản mã doanh nghiệp thuộc khối NV chỉ được hệ thống ghi nhận đến<br>26/03/2020 sau đó bị ghi sang thành các mã doanh nghiệp khác, sẽ được lọc<br>lại vào phân khúc TCTD nếu đầu GL của tài khoản này là 41. |

## <span id="page-10-0"></span>*2.2.3. Triển khai dữ liệu*

**Số dư (hay balance)** là số dư của tài khoản tiền gửi theo từng ngày trong vòng đời của tài khoản đó.

**Để có được dữ liệu đầu vào cho mô hình, dữ liệu thô từ Ngân hàng sẽ được triển khai theo thứ tự các bước như sau:**

| BƯỚC | NỘI DUNG                          | LƯU Ý                                                                                                                                                                                                                     |
|------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Nhóm các tài khoản theo phân khúc | ▪ Các tài khoản được nhóm theo các tiêu chí<br>phân khúc đã xác định, do đó các bước tiếp<br>theo sẽ được thực hiện cho các tài khoản<br>thuộc cùng một phân khúc (đơn vị tiền tệ,<br>khối kinh doanh, kỳ hạn, sản phẩm). |
| 2    | Nối tái tục khác tài khoản        | ▪ Nối các tài khoản khác nhau thuộc cùng<br>một phân khúc theo giả định tái tục khác tài<br>khoản.                                                                                                                        |
| 3    | Tính tuổi của tài khoản           | Không có                                                                                                                                                                                                                  |
| 4    | Tính drawdown của tài khoản       | Không có                                                                                                                                                                                                                  |

### **Chi tiết các bước thực hiện**

#### **Bước 1: Nhóm các tài khoản theo phân khúc (bảng ALM\_dps first)**

Các tài khoản được nhóm phân khúc theo các tiêu chí (đơn vị tiền tệ, khối kinh doanh, kỳ hạn, sản phẩm). Mỗi nhóm phân khúc lọc lấy ngày đầu tiên của từng tài khoản nhằm xác định trong phân khúc đó gồm những tài khoản nào (bảng ALM\_dps\_first khi xây dựng mô hình).

**Ví dụ 1:**

| Rep_Date  | Acc_ID  | Cus_ID | Accid       | Biz_Line | Ccy | Tenor | Prod_Code | Op_Date   |
|-----------|---------|--------|-------------|----------|-----|-------|-----------|-----------|
| 31-Dec-15 | 1111WES | 1234   | 1111WES1234 | KHCN     | VND | 6M    | 001       | 31-Dec-15 |
| 29-Jan-16 | 2222WES | 4123   | 2222WES4123 | KHCN     | VND | 6M    | 001       | 29-Jan-16 |
| 30-Jan-16 | 3333WES | 3412   | 3333WES3412 | KHCN     | VND | 6M    | 001       | 30-Jan-16 |
| 28-Feb-16 | 4444WES | 4321   | 4444WES4321 | KHCN     | VND | 6M    | 001       | 28-Feb-16 |

*\*Lưu ý: Các tài khoản được lấy ví dụ trong các bước tiếp theo phải thuộc cùng một phân khúc đã được nhóm, theo các tiêu chí đã đề cập là cùng kỳ hạn, đơn vị tiền tệ, khối kinh doanh, sản phẩm.*

#### **Bước 2: Nối tái tục khác tài khoản**

Giả định tái tục khác tài khoản chỉ áp dụng cho những tài khoản thỏa điều kiện:

- Thuộc cùng một phân khúc (theo các tiêu chí là cùng kỳ hạn, đơn vị tiền tệ, khối kinh doanh, sản phẩm).
- Tài khoản đóng và Tài khoản mở Cùng mã khách hàng (Cus\_ID)
- Tài khoản mới có ngày mở bằng hoặc không trễ hơn 3 ngày (cho phép độ trễ vì có thể có ngày nghỉ lễ như thứ 7, Chủ nhật, …, Ngân hàng có thể điều chỉnh số ngày cho phép tuy nhiên khuyến nghị không nên lấy nhiều hơn 3 ngày) so với ngày đóng của tài khoản cũ.
- Các cặp tài khoản được nối 1-1 (tức là chỉ có 1 tài khoản đóng và 1 tài khoản mở trong cùng 1 ngày) \*.

Sau khi xác định được các tài khoản tái tục vào tài khoản mới, mô hình sẽ sử dụng mã tài khoản cũ thay cho mã tài khoản mới, để làm mã tài khoản duy nhất trong chuỗi nối, nhằm quan sát đúng tuổi đời của khoản tiền gửi này.

#### **Ví dụ 2:**

Có tài khoản 987654321WES1234 và tài khoản 123456789WES1234 thuộc phân khúc tiền gửi 6 tháng và có cùng một khách hàng có mã là 1234:

#### **Trước khi nối tài khoản**:

| Rep_Date  | Accid             | Tenor | Op_Date   | Mat_Date  | Bal |
|-----------|-------------------|-------|-----------|-----------|-----|
| 31-Dec-14 | 1234567689WES1234 | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 29-Jan-15 | 1234567689WES1234 | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 30-Jan-15 | 987654321WES1234  | 6M    | 30-Jan-15 | 01-Mar-15 | 200 |
| 28-Feb-15 | 987654321WES1234  | 6M    | 30-Jan-15 | 01-Mar-15 | 200 |

Trong ví dụ này, tài khoản cũ (1234567689WES1234) đã đóng sau ngày 29/01/2015 với số dư là 200, và tài khoản mới (987654321WES1234) được mở tại ngày 30/1/2015 (tức là sau đó 1 ngày) với số dư là 200 (bằng số dư tài khoản cũ khi đóng).

2 tài khoản này thỏa mãn những điều kiện về ngày đóng – mở nên có thể nối với nhau dù khác mã tài khoản, để thể hiện hành vi tái tục thực sự của khách hàng có mã là 1234.

Sau khi nối tài khoản, mã tài khoản cũ sẽ được dùng thay thế cho mã tài khoản mới, cùng với thông tin về ngày mở tài khoản (Val\_Date) nhằm xác định đúng tuổi của khoản tiền gửi này.

### **Sau khi nối tài khoản**:

| Rep_Date  | accid (trước khi nối) | accid (sau khi nối) | Tenor | Op_Date   | Mat_Date  | Bal |
|-----------|-----------------------|---------------------|-------|-----------|-----------|-----|
| 31-Dec-14 | 1234567689WES1234     | 1234567689WES1234   | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 29-Jan-15 | 1234567689WES1234     | 1234567689WES1234   | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 30-Jan-15 | 987654321WES1234      | 1234567689WES1234   | 6M    | 31-Dec-14 | 01-Mar-15 | 200 |
| 28-Feb-15 | 987654321WES1234      | 1234567689WES1234   | 6M    | 31-Dec-14 | 01-Mar-15 | 200 |

Cặp tài khoản này sẽ không được nối nếu vi phạm một trong những điều kiện sau đây:

- Khoảng cách ngày mở tài khoản mới (trừ) ngày đóng tài khoản cũ > 3 ngày: Ngày mở của tài khoản mở 987654321WES1234 sau ngày 2/2/2015 (là hơn 3 ngày từ sau ngày đóng tài khoản cũ), hoặc
- Nhiều tài khoản mở mới: Tại ngày 30/1/2015, ngoài tài khoản mở 987654321WES1234 còn có nhiều tài khoản khác cũng thỏa mãn điều kiện nối được với tài khoản đóng 1234567689WES1234, hoặc
- Nhiều tài khoản đóng: Tại ngày 29/1/2015, ngoài tài khoản đóng 1234567689WES1234 còn có nhiều tài khoản khác cũng thỏa mãn điều kiện nối được với tài khoản mở 987654321WES1234.

Nếu tại ngày 31/1/2015, tài khoản đóng 1234567689WES1234 cũng nối được với 1 tài khoản khác mà không phải tài khoản mở 987654321WES1234, mô hình chỉ lấy cặp nối 1234567689WES1234 - 987654321WES1234 do ưu tiên khoảng cách ngày là gần nhất.

#### **Lưu ý**:

Nếu sau khi nối tái tục khác tài khoản, ta có một chuỗi các tài khoản nối được với nhau, thì sẽ chỉ nối từng tài khoản tái tục theo tài khoản gốc đầu tiên (là tài khoản được mở đầu tiên trong chuỗi này).

Tiếp tục với ví dụ trên, giả sử tài khoản 987654321WES1234 có thể nối được với 1 tài khoản khác sau đó là 00001111WES1234 (với điều kiện thỏa mãn các tiêu chí nối tái tục), thì tài khoản mới 00001111WES1234 sẽ có tài khoản gốc là 123456789WES1234 do tài khoản này mở đầu tiên trong chuỗi 3 tài khoản nối với nhau.

#### **Trước khi nối**

| Rep_Date  | accid             | Tenor | Op_Date   | Mat_Date  | Bal |
|-----------|-------------------|-------|-----------|-----------|-----|
| 31-Dec-14 | 1234567689WES1234 | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 29-Jan-15 | 1234567689WES1234 | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 30-Jan-15 | 987654321WES1234  | 6M    | 30-Jan-15 | 01-Mar-15 | 200 |
| 28-Feb-15 | 987654321WES1234  | 6M    | 30-Jan-15 | 01-Mar-15 | 200 |
| 1-Mar-15  | 00001111WES1234   | 6M    | 1-Mar-15  | 31-Mar-15 | 150 |
| 31-Mar-15 | 00001111WES1234   | 6M    | 1-Mar-15  | 31-Mar-15 | 150 |

### **Sau khi nối**

| Rep_Date  | accid (trước khi nối) | accid (sau khi nối) | Tenor | Op_Date   | Mat_Date  | Bal |
|-----------|-----------------------|---------------------|-------|-----------|-----------|-----|
| 31-Dec-14 | 1234567689WES1234     | 1234567689WES1234   | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 29-Jan-15 | 1234567689WES1234     | 1234567689WES1234   | 6M    | 31-Dec-14 | 30-Jan-15 | 200 |
| 30-Jan-15 | 987654321WES1234      | 1234567689WES1234   | 6M    | 31-Dec-14 | 01-Mar-15 | 200 |
| 28-Feb-15 | 987654321WES1234      | 1234567689WES1234   | 6M    | 31-Dec-14 | 01-Mar-15 | 200 |

| Rep_Date  | accid (trước khi nối) | accid (sau khi nối) | Tenor | Op_Date   | Mat_Date  | Bal |
|-----------|-----------------------|---------------------|-------|-----------|-----------|-----|
| 1-Mar-15  | 00001111WES1234       | 1234567689WES1234   | 6M    | 31-Dec-14 | 31-Mar-15 | 150 |
| 31-Mar-15 | 00001111WES1234       | 1234567689WES1234   | 6M    | 31-Dec-14 | 31-Mar-15 | 150 |

### **Bước 3: Tính tuổi mỗi tài khoản**

Lấy dữ liệu ngày mở tài khoản (Op\_Date) từ bảng dữ liệu ngày đầu tiên (bảng ALM\_dps\_first) Tuổi của mỗi khoản tài khoản a tại ngày t được tính trên dữ liệu rút gọn:

$$age_{a,t} = Rep_Date_{a,t} - Op_Date_a + 1$$

#### Trong đó:

agea,t là tuổi tài khoản a tại ngày t Rep\_Datea,t là ngày báo cáo t Op\_Datea,t là ngày mở tải khoản a

#### **Ví dụ 3:**

1 tài khoản được mở từ ngày 31/12/2013, tuổi của 1 tài khoản được tính như sau:

| Rep_Date   | Accid        | Op_Date   | age |
|------------|--------------|-----------|-----|
| 01/01/2014 | 999999WES123 | 31-Dec-13 | 2   |
| 02/01/2014 | 999999WES123 | 31-Dec-13 | 3   |
| 03/01/2014 | 999999WES123 | 31-Dec-13 | 4   |
| 04/01/2014 | 999999WES123 | 31-Dec-13 | 5   |
| 05/01/2014 | 999999WES123 | 31-Dec-13 | 6   |
| 06/01/2014 | 999999WES123 | 31-Dec-13 | 7   |

#### **Bước 4: Tính drawdown mỗi tài khoản**

**Drawdown** là lượng giảm của số dư tiền gửi qua từng ngày (hoặc tuổi)

Drawdown mỗi ngày của mỗi tài khoản được tính bằng số dư ngày trước trừ đi số dư ngày sau.

$$drawdown_{a,t} = balance_{a,t} - balance_{a,(t-1)}$$

#### Trong đó:

drawdowna,t là drawdown của tài khoản a ngày t

balancea,t là số dư của tài khoản a ngày t

balancea,(t−1) là số dư của tài khoản a ngày t-1

#### **Ví dụ 4**

| Rep_Date   | accid        | Bal | DRAWDOWN |
|------------|--------------|-----|----------|
| 01/01/2014 | 999999WES123 | 400 | 0        |
| 02/01/2014 | 999999WES123 | 200 | 200      |
| 03/01/2014 | 999999WES123 | 200 | 0        |
| 04/01/2014 | 999999WES123 | 200 | 0        |
| 05/01/2014 | 999999WES123 | 200 | 0        |
| 06/01/2014 | 999999WES123 | 100 | 100      |

## <span id="page-14-0"></span>*2.3. Xây dựng mô hình*

Sơ đồ dưới đây thể hiện quy trình phân tích tương quan để lựa chọn phương pháp xây dựng mô hình cho từng phân khúc của mô hình Tiền gửi có kỳ hạn:

![](_page_14_Figure_2.jpeg)

Từng mô hình sẽ có những ưu điểm và hạn chế theo như phân tích dưới đây

### Mô hình phi tham số

- ✓ Mô hình có phương pháp luận đơn giản, trực quan và có thể áp dụng dễ dàng.
- ✓ Các bước tính toán trong mô hình được thực hiện đơn giản.
- ✓ Phương pháp đã được chấp nhận và thực hiện ở nhiều ngân hàng với quy mô khác nhau trong nước, trong khu vực và trên toàn thế giới.
- Phương pháp không thể hiện rõ các yếu tố ngoại sinh vì đã giả định rằng tác động của những yếu tố này được thể hiện trong biến động số dư của danh mục.

### Mô hình tham số

- ✓ Phương pháp được áp dụng tại nhiều ngân hàng trong và ngoài nước với quy mô khác nhau
- × Phương pháp luận xây dựng mô hình và các bước tính toán trong mô hình được thực hiện tương đối phức tạp.

#### Phân chia dữ liêu:

Dữ liệu bao gồm tổng số dư của tất cả các tài khoản tiền gửi có kỳ hạn từ 01/10/2015 - 30/09/2020.

Dữ liệu này sẽ được chia thành 2 bộ dữ liệu:

- Dữ liệu xây dựng mô hình (XDMH): bao gồm 4 năm đầu tiên của dữ liệu (từ 01/10/2015 30/09/2019)
- Dữ liệu kiểm tra hồi tố (KTHT): bao gồm năm cuối cùng của dữ liệu (từ 01/10/2019 30/09/2020),
  được sử dụng để kiểm tra hồi tố và hiệu chỉnh mô hình

\*Theo ý kiến được thống nhất từ Ngân hàng, mô hình có thể chia bộ dữ liệu XDMH là 70% và bộ dữ liệu KTHT là 30% số lượng quan sát trên toàn bộ dữ liệu 5 năm.

Mô hình được xây dựng cho từng phân khúc lựa chon trước đó, trên **bô dữ liêu XDMH** theo 2 bước sau

#### Bước 1: Nhóm hành vi theo tuổi

Lấy tổng drawdown cho mỗi phân khúc theo từng tuổi:

$$study\_total\_drawdown_T = \sum drawdown_T$$

Với

 ${\rm drawdown_T}$  là drawdown của một tài khoản tại tuổi T từ 2/10/2015 đến 30/09/2019 study\_total\_drawdown\_T là tổng drawdown tại tuổi T từ 2/10/2015 đến 30/09/2018

(\*) Hành vi drawdown chỉ có thể quan sát từ ngày 2/10/2015 trở đi vì đối với hành vi drawdown tại ngày 1/10/2015, ta không có quan sát cho số dư trước khi có hành vi drawdown này (tức là số dư tại 30/09/2015). Theo đó, số dư sẽ quan sát tương ứng trong giai đoạn lùi đi 1 ngày so với quan sát hành vi drawdown, tức là từ 1/10/2015 đến 30/09/2019.

#### Ví du

Trong một phân khúc quan sát từ 1/1/2016 đến 1/3/2016 có những tài khoản với độ tuổi như sau:

| Reporting date | Age | ACCID        | Balance | Drawdown |
|----------------|-----|--------------|---------|----------|
| 1/1/2016       | 31  | 000111WES123 | 100     | 0        |
| 1/1/2016       | 31  | 000333WES456 | 200     | 0        |
| 2/1/2016       | 32  | 000111WES123 | 90      | 10       |
| 2/1/2016       | 32  | 000333WES456 | 195     | 5        |
| 3/1/2016       | 33  | 000111WES123 | 75      | 15       |
| 3/1/2016       | 33  | 000333WES456 | 180     | 15       |

| Age | Balance | Drawdown |
|-----|---------|----------|
| 31  | 300     | 0        |
| 32  | 285     | 15       |
| 33  | 255     | 30       |

#### Bước 2: Xác định tỷ lê giảm số dư theo tuổi

Tỷ lệ rút tiền ở tuổi t được xác định dựa trên lượng tiền rút tại tuổi T và tổng số dư của phân khúc tại tuổi (T -1):

$$CDR_{T} = \frac{study\_total\_drawdown_{T}}{total\_balance_{T-1}}$$

Với:

 ${\rm CDR_T}$ : Tỷ lệ giảm số dư của phân khúc tại tuổi T (Conditional Drawdown Rate)  ${\rm total\_balance_T}$ : Lượng tiền giảm của phân khúc tại tuổi T được tính ở bước 2

total\_balance<sub>T-1</sub>: Số dư của tổng phân khúc tại tuổi T-1

## Ví dụ: Với một phân khúc tiền gửi quan sát trong 9 tuổi:

| Age (T) | total_<br>outstanding_<br>principal (T-1) | study_<br>total_<br>drawdown (T) | CDR (T) |
|---------|-------------------------------------------|----------------------------------|---------|
| 1       | 100                                       | 20                               | 20.00%  |
| 2       | 80                                        | 9                                | 11.25%  |
| 3       | 71                                        | 0                                | 0.00%   |
| 4       | 71                                        | 1                                | 1.41%   |
| 5       | 70                                        | 2                                | 2.86%   |
| 6       | 68                                        | 23                               | 33.82%  |
| 7       | 45                                        | 5                                | 11.11%  |
| 8       | 40                                        | 3                                | 7.50%   |
| 9       | 40                                        | 0                                | 00.00%  |

## <span id="page-18-0"></span>2.4. Kiểm tra hồi tố

Mục đích của kiểm tra hồi tố nhằm đánh giá tính cẩn trọng của kết quả từ bộ dữ liệu XDMH.

Kiểm tra hồi tố được thực hiện trên bộ **dữ liệu KTHT năm cuối cùng (1/10/2019 đến 30/09/2020)**, cho từng phân khúc mô hình và từng dải kỳ hạn, theo 3 bước sau:

#### Bước 1:

#### Xác định CDR cho phân khúc trong giai đoạn kiểm tra hồi tố

CDR trong giai đoạn kiểm tra hồi tố được tính toán tương tự như các bước xây dựng mô hình:

$$test\_total\_drawdown_T = \sum drawdown_T$$

Với

 $drawdown_T$  là drawdown của một tài khoản tại tuổi T trong giai đoạn kiểm tra hồi tố  $test_total_drawdown_T$  là tổng drawdown tại tuổi T trong giai đoạn kiểm tra hồi tố

(\*) Hành vi drawdown trong giai đoạn kiểm tra hồi tố có thể quan sát từ 1/10/2019 do dữ liệu có số dư tại 30/09/2019. Theo đó, số dư sẽ quan sát cho kiểm tra hồi tố tương ứng trong giai đoạn lùi đi 1 ngày so với quan sát hành vi drawdown, tức là từ 30/09/2019 đến 29/09/2020.

$$CDR\_test_T = \frac{test\_total\_drawdown_T}{total\_balance_{T-1}}$$

Với:

 ${\rm CDR_T}$ : Tỷ lệ giảm số dư của phân khúc tại tuổi T (Conditional Drawdown Rate)  ${\rm test\_total\_drawdown_T}$ : Lượng tiền giảm của phân khúc tại tuổi T  ${\rm total\_balance_{T-1}}$ : Tổng số dư của phân khúc tại tuổi T-1 trong giai đoạn kiểm tra hồi tố

#### Bước 2:

# Xây dựng đường cong duy trì (Survival Curve) và khoảng tin cậy (confident\_level) cho dữ liệu mô hình và dữ liệu kiểm tra hồi tố

Đường cong duy trì của dữ liệu xây dựng mô hình được xây dựng như sau:

Xác định tỷ lệ duy trì (survival\_rate) tại từng tuổi:

Survival rate<sub>T</sub> = 
$$1 - CDR_T$$

Vớ

Survival rate<sub>T</sub> là tỷ lệ duy trì tại tuổi T Survival rate<sub>0</sub> = 1

• Xác định khoảng tin cậy cho tỷ lệ duy trì tại từng tuổi theo phương pháp Greenwood:

$$Confidence_{T} = -z_{(1-c)/2} * Survival \ rate_{T} * \sqrt{\sum_{i \leq T} \frac{study\_total\_drawdown_{i}}{Balance_{i-1} * (Balance_{i-1} - study\_total\_drawdown_{i})}}$$

Với

Confidence<sub>T</sub> là khoảng tin cậy tại tuổi T  $Balance_{i-1} = total\_balance_{i-1}$  là tổng số dư phân khúc tại tuổi i-1  $study\_total\_drawdown_i$  là tổng drawdown tại tuổi i c là độ tin cậy (khuyến nghị lấy 99%)  $z_c$  là Z-Score của xác xuất (1-c)/2

• Xác định tỷ lệ duy trì biên trên và dưới trong khoảng tin cậy:

Upper<sup>T</sup> = Survival rate<sup>T</sup> + Confidence<sup>T</sup>

Lower<sup>T</sup> = Survival rate<sup>T</sup> − Confidence<sup>T</sup>

• Tại các tuổi không có dữ liệu, giả định là tỷ lệ duy trì và các biên không thay đổi, ta điền các tuổi đó theo dữ liệu của tuổi trước đó

Tương tự, với dữ liệu kiểm tra hồi tố ta cũng có được tỷ lệ duy trì biên (Upper\_test<sup>T</sup> và Lower\_testT) và đường cong duy trì (Survival\_rate\_testT)

#### **Bước 3:**

#### **Đánh giá kết quả mô hình**

Tại từng tuổi, đánh giá đường cong duy trì của bộ kết quả 4 năm. Kết quả được xem là "đạt" tại tuổi T nếu: Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup>

Dưới đây là hình ảnh minh họa cho các trường hợp có thể xảy ra của 2 bộ đường cong duy trì của kết quả 4 năm (nét liền) và 1 năm (nét đứt):

![](_page_19_Figure_9.jpeg)

Lower<sup>T</sup> > Upper\_test<sup>T</sup> => Không ĐẠT

![](_page_19_Figure_11.jpeg)

Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup> => ĐẠT

![](_page_19_Figure_13.jpeg)

Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup> => ĐẠT

![](_page_19_Figure_15.jpeg)

Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup> => ĐẠT

![](_page_19_Figure_17.jpeg)

Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup> => ĐẠT

![](_page_19_Figure_19.jpeg)

Lower<sup>T</sup> ≤ Upper\_test<sup>T</sup> => ĐẠT

Ví dụ: Xây dựng đường cong duy trì cho dữ liệu xây dựng mô hình (study):

| Age | total_<br>outstanding<br>principal (T-<br>1) | study_<br>total_<br>drawdow<br>n (T)<br>B | CDR<br>(T)<br>B/A | Survival<br>rate (T)<br>S | Confiden<br>t (T) | Lower (T)<br>S-C | Upper(T)<br>S+C |
|-----|----------------------------------------------|-------------------------------------------|-------------------|---------------------------|-------------------|------------------|-----------------|
|     | Α                                            |                                           |                   |                           |                   |                  |                 |
| 1   | 100                                          | 20                                        | 20.00%            | 80%                       | 10.2%             | 69.8%            | 90.2%           |
| 2   | 80                                           | 9                                         | 11.25%            | 71%                       | 11.6%             | 59.4%            | 82.6%           |
| 3   | 71                                           | 0                                         | 0.00%             | 71%                       | 11.6%             | 59.4%            | 82.6%           |
| 4   | 71                                           | 1                                         | 1.41%             | 70%                       | 11.7%             | 58.3%            | 81.7%           |
| 5   | 70                                           | 2                                         | 2.86%             | 68%                       | 11.9%             | 56.1%            | 79.9%           |
| 6   | 68                                           | 23                                        | 33.82%            | 45%                       | 12.7%             | 32.3%            | 57.7%           |
| 7   | 45                                           | 5                                         | 11.11%            | 40%                       | 12.5%             | 27.5%            | 52.5%           |
| 8   | 40                                           | 3                                         | 7.50%             | 37%                       | 12.4%             | 24.6%            | 49.4%           |

Xây dựng đường cong duy trì cho dữ liệu kiểm tra hồi tố (test):

| Age | total_<br>outstanding_<br>principal (T-1)<br>A | test_<br>total_<br>drawdown<br>(T)<br>B | CDR_test<br>(T)<br>B/A | Survival_<br>rate (T)<br>S | Confident_test<br>(T) | Lower_<br>test (T) | Upper_<br>test(T)<br>S+C |
|-----|------------------------------------------------|-----------------------------------------|------------------------|----------------------------|-----------------------|--------------------|--------------------------|
| 1   | 100                                            | 0                                       | 0.00%                  | 100.00%                    | 0.00%                 | 100.00%            | 100.00%                  |
| 2   | 100                                            | 20                                      | 20.00%                 | 80.00%                     | 10.30%                | 69.70%             | 90.30%                   |
| 3   | 80                                             | 1                                       | 1.25%                  | 79.00%                     | 10.49%                | 68.51%             | 89.49%                   |
| 4   | 79                                             | 18                                      | 22.78%                 | 61.00%                     | 12.56%                | 48.44%             | 73.56%                   |
| 5   | 61                                             | 0                                       | 0.00%                  | 61.00%                     | 12.56%                | 48.44%             | 73.56%                   |
| 6   | 61                                             | 31                                      | 50.82%                 | 30.00%                     | 11.80%                | 18.20%             | 41.80%                   |
| 7   | 30                                             | 9                                       | 30.00%                 | 21.00%                     | 10.49%                | 10.51%             | 31.49%                   |
| 8   | 21                                             | 3                                       | 14.29%                 | 18.00%                     | 9.90%                 | 8.10%              | 27.90%                   |

### Kiểm tra hồi tố:

| Age | Lower (T) | Upper_<br>test(T) | Backtest |
|-----|-----------|-------------------|----------|
| 1   | 69.8%     | 100.00%           | ÐẠT      |
| 2   | 59.4%     | 90.30%            | ÐẠT      |
| 3   | 59.4%     | 89.49%            | ĐẠT      |
| 4   | 58.3%     | 73.56%            | ĐẠT      |
| 5   | 56.1%     | 73.56%            | ĐẠT      |
| 6   | 32.3%     | 41.80%            | ĐẠT      |
| 7   | 27.5%     | 31.49%            | ĐẠT      |
| 8   | 24.6%     | 27.90%            | ĐẠT      |

### <span id="page-21-0"></span>2.5. Bảo trì và rà soát mô hình

Đội ngũ xây dựng mô hình tiến hành bảo trì mô hình bao gồm việc tái vận hành mô hình hàng quý (\*), và thực hiện phân tích tương quan hàng năm.

![](_page_21_Figure_2.jpeg)

**Ngân hàng được khuyến nghị cần thực hiện rà soát mô hình độc lập** nhằm xác nhận rằng mô hình vẫn hoạt động đúng chức năng như thời điểm mới xây dựng và vẫn có thể áp dụng cho thực trạng của Ngân hàng.

- Một đội ngũ kiểm định độc lập (QLRR) sẽ thực hiện kiểm định độc lập và báo cáo tổng thể để trình lên Hôi đồng quản tri.
- Báo cáo này bao gồm khuyến nghị dự báo, có thể là định lượng hoặc định tính.
- Hội đồng quản trị sẽ ra quyết định sau cùng dựa trên khuyến nghị và vấn đề của báo cáo rà soát độc lập cho từng mô hình.

(\*) Tần suất có thể điều chỉnh phù hợp với tần suất thực hiện phân tích khe hở thanh khoản và khe hở tái định giá hoặc hiện trang hỗ trợ từ cơ sở ha tầng dữ liêu của Ngân hàng.

# <span id="page-22-0"></span>*3. Ứng dụng kết quả mô hình*

Ví dụ có kết quả mô hình cho tiền gửi có kỳ hạn hợp đồng là 7 ngày.

Dự báo cho một khoản tiền gửi 7 ngày tại tuổi 3 có số dư là 1,000,000 VND:

| Age | CDR    | Dòng tiền theo hợp<br>đồng | Dòng tiên rút ra có hành vi | Số dư sau điều chỉnh hành<br>vi |
|-----|--------|----------------------------|-----------------------------|---------------------------------|
| 1   | 20.00% |                            |                             |                                 |
| 2   | 11.25% |                            |                             |                                 |
| 3   | 0.00%  |                            |                             | 1,000,000                       |
| 4   | 1.41%  | 0                          | 14,100                      | 985,900                         |
| 5   | 2.86%  | 0                          | 28,197                      | 957,703                         |
| 6   | 33.82% | 0                          | 323,895                     | 633,808                         |
| 7   | 30.00% | 1,000,000                  | 190,142                     | 443,666                         |
| 8   | 14.29% |                            | 63,400                      | 380,266                         |

Dòng tiền rút ra có hành vi được tính bằng cách:

Dòng tiền hành vi 
$$_{\mathrm{T}}=\mathrm{S\acute{o}}\;\mathrm{d}\mathrm{u}_{\mathrm{T-1}}*\mathrm{CDR}_{\mathrm{T}}$$

Số d
$$w_T = Số dw_{T-1} - Dòng tiền hành vi_T$$

với T là tuổi tương ứng

Trong ví dụ,

- Dòng tiền rút ra có hành vi tại tuổi 4 = 1.41% x 1,000,000 = 14,100 (VND)
- Số dư điều chỉnh sau hành vi tại tuổi 4 = 1,000,000 14,100 = 985,900 (VND)
- Dòng tiền rút ra có hành vi tại tuổi 5 = 2.86% x 985,900 = 28,197 (VND)
- Số dư điều chỉnh sau hành vi tại tuổi 5 = 985,900 28,197 = 957,703 (VND)

...

Dòng tiền rút ra có hành vi được phân bổ lại vào các dải kỳ hạn tương ứng như sau

| Dài kì hạn | Qua đêm | 2-7D | 8-30D | 31-90D | 91-180D | 181-360D |
|------------|---------|------|-------|--------|---------|----------|
| Số ngày    | 1       | 7    | 30    | 90     | 180     | 360      |

Số ngày trong từng dải kỳ hạn được lấy theo số ngày đếm thực tế cộng thêm độ trễ, nhằm phản ánh đúng thời điểm diễn ra hành vi khách hàng.

Dòng tiền rút ra có hành vi được phân bổ tại các dải kỳ hạn được sử dụng để tính toán chênh lệch tái định giá.

Tham khảo file excel **030304\_Term\_Deposit\_Application.xlsm** để nắm rõ hơn về phương pháp áp dụng kết quả của mô hình hành vi cho tiền gửi có kỳ hạn.

# <span id="page-23-0"></span>4. Phụ lục – Hiệu chỉnh mô hình

Mục đích của hiệu chỉnh nhằm đảm bảo tính cẩn trọng của kết quả mô hình theo dữ liệu cập nhật nhất.

Theo thông lệ về mô hình đã được PwC tư vấn/sử dụng tại một số Ngân hàng tại Việt Nam, phương pháp hiệu chỉnh như trình bày dưới đây.

Trong trường hợp tại 1 tuổi nhất định mà mô hình không đạt kiểm tra hồi tố ở bước trước đó, kết quả CDR tại tuổi đó sẽ được lấy theo CDR\_test của bộ. Bộ CDR cuối cùng sau khi hiệu chỉnh sẽ là kết quả của mô hình.

Ví dụ: Tiếp tục với ví dụ phần Kiểm tra hồi tố:

| Age | Lower (T) | Upper_<br>test(T) | Backtest | CDR (T) | CDR_test (T) | CDR (T) (Đã<br>hiệu chỉnh) |
|-----|-----------|-------------------|----------|---------|--------------|----------------------------|
| 1   | 69.8%     | 100.00%           | ĐẠT      | 20.00%  | 0.00%        | 20.00%                     |
| 2   | 59.4%     | 90.30%            | ÐẠT      | 11.25%  | 20.00%       | 11.25%                     |
| 3   | 59.4%     | 89.49%            | ÐẠT      | 0.00%   | 1.25%        | 0.00%                      |
| 4   | 58.3%     | 73.56%            | ÐẠT      | 1.41%   | 22.78%       | 1.41%                      |
| 5   | 56.1%     | 73.56%            | ĐẠT      | 2.86%   | 0.00%        | 2.86%                      |
| 6   | 32.3%     | 41.80%            | ĐẠT      | 33.82%  | 50.82%       | 33.82%                     |
| 7   | 27.5%     | 31.49%            | ÐẠT      | 11.11%  | 30.00%       | 11.11%                     |
| 8   | 24.6%     | 27.90%            | ÐẠT      | 7.50%   | 14.29%       | 7.50%                      |

Sau khi thu được kết quả CDR hiệu chỉnh, thực hiện xây dựng bộ kết quả Tỷ lệ duy trì cộng dồn, nhằm áp dung kết quả mô hình cho danh mục hiện tại ở các bước sau

Cumulative Survival rate<sub>T</sub> = Cumulative Survival rate<sub>T-1</sub>  $\times$  (1 - CDR caibrate<sub>T</sub>)

| Age | CDR (T) (Đã hiệu chỉnh) | CumulativeSurvival rate (T) (Đã hiệu chỉnh) |
|-----|-------------------------|---------------------------------------------|
| 1   | 20.00%                  | 80.00%                                      |
| 2   | 11.25%                  | 71.00%                                      |
| 3   | 0.00%                   | 71.00%                                      |
| 4   | 1.41%                   | 70.00%                                      |
| 5   | 2.86%                   | 68.00%                                      |
| 6   | 33.82%                  | 45.00%                                      |
| 7   | 11.11%                  | 40.00%                                      |
| 8   | 7.50%                   | 37.00%                                      |

Tai tuổi T = 1:

Cumulative Survival rate<sub>T=1</sub> = 100% \* (1 - 20.00%) = 80%

Tại tuổi T = 2:

Cumulative Survival rate<sub>T=2</sub> = 80% \* (1 - 11.25%) = 71%

\*Theo ý kiến đã được thống nhất từ Ngân hàng, mô hình có thể không lựa chọn phương pháp hiệu chỉnh này.