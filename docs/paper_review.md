# Task 1 — Review bài báo tham khảo

## 1. Thông tin bài báo

- **Tên bài báo:** Big Data Trip Classification on the New York City Taxi and Uber Sensor Network
- **Tác giả:** Huiyu Sun, Siyuan Hu, Suzanne McIntosh, Yi Cao
- **Năm xuất bản:** 2018
- **Tạp chí:** Journal of Internet Technology
- **Tập, số, trang:** Volume 19, Issue 2, pp. 591–598
- **DOI:** https://doi.org/10.3966/160792642018031902027
- **Trang bài báo:** https://jit.ndhu.edu.tw/article/view/1679
- **Toàn văn PDF:** https://jit.ndhu.edu.tw/article/viewFile/1679/1687

## 2. Mục tiêu và động lực nghiên cứu

Dữ liệu chuyến đi taxi và Uber tại New York có quy mô lớn, được thu thập trong thời gian dài và chứa thông tin có thể sử dụng để phân tích hoạt động vận chuyển theo không gian và thời gian.

Nghiên cứu của Sun và cộng sự (2018) hướng đến việc khai thác dữ liệu này bằng công nghệ Big Data, xác định khu vực có hoạt động đón khách chiếm ưu thế của từng dịch vụ và phân tích sự thay đổi trong hoạt động của taxi vàng, taxi xanh và Uber.

Các tác giả xem phương tiện vận chuyển như những nút cảm biến di động. Khi chia thành phố thành các vùng không gian nhỏ, dữ liệu đón khách có thể được tổng hợp để xây dựng bản đồ hoạt động vận chuyển và xác định dịch vụ chiếm ưu thế tại từng vùng.

Động lực của nghiên cứu là chuyển dữ liệu chuyến đi quy mô lớn thành thông tin có thể sử dụng trong phân tích đô thị và gợi ý dịch vụ vận chuyển.

## 3. Bài toán nghiên cứu

Bài báo giải quyết các nhiệm vụ chính:

1. Phân tích số lượt đón khách theo khu vực và thời gian.
2. Trực quan hóa phân bố hoạt động của taxi vàng, taxi xanh và Uber.
3. Phân loại một vùng không gian theo dịch vụ có số lượt đón khách chiếm ưu thế.
4. Khai thác kết quả phân loại để phân tích sự thay đổi hoạt động của Uber và xây dựng ứng dụng gợi ý dịch vụ.

Trong bài toán phân loại, nhãn đầu ra thuộc một trong ba lớp: Yellow Taxi, Green Taxi hoặc Uber. Nhãn biểu thị dịch vụ chiếm ưu thế về số lượt đón khách trong vùng, không nhất thiết là dịch vụ duy nhất hoạt động tại đó.

**Phân biệt với đồ án:** Bài báo không xây dựng mô hình phát hiện chuyến taxi bất thường. Đây là bài toán phân loại dịch vụ theo vùng không gian, kết hợp phân tích dữ liệu vận chuyển.

## 4. Dữ liệu nghiên cứu

### 4.1. Nguồn dữ liệu

Bài báo sử dụng dữ liệu chuyến đi taxi vàng và taxi xanh tại New York trong giai đoạn 2009–2015, cùng dữ liệu Uber trong giai đoạn 2014–2015.

Trong thí nghiệm phân loại, các tác giả xây dựng sáu bộ dữ liệu theo tháng, từ tháng 4 đến tháng 9 năm 2014. Mỗi bộ dữ liệu bao gồm tọa độ đón khách của ba dịch vụ.

### 4.2. Biểu diễn dữ liệu không gian

Các tác giả chia bản đồ thành các vùng nhỏ dựa trên tọa độ đón khách. Tọa độ vĩ độ và kinh độ được làm tròn đến ba chữ số thập phân để xác định vùng.

Theo bài báo, cách chia này tạo ra vùng có diện tích ước tính khoảng 10.000 m²; Manhattan được ước tính chia thành khoảng 60.000 vùng.

Sau khi ánh xạ các điểm đón khách vào vùng, dữ liệu được sử dụng để xác định dịch vụ có số lượt đón khách chiếm ưu thế và xây dựng tập dữ liệu phân loại.

### 4.3. Phương pháp chia tập dữ liệu

Trong thí nghiệm phân loại theo tháng, 80% dữ liệu được sử dụng để huấn luyện và 20% còn lại để kiểm thử. Mô hình Logistic Regression được huấn luyện cho từng vùng; accuracy được tổng hợp để tính kết quả trung bình theo tháng.

### 4.4. Giới hạn thông tin dữ liệu

Bài báo không cung cấp một con số tổng quát, đầy đủ về tổng số bản ghi thô trong toàn bộ dữ liệu đầu vào hoặc dung lượng dữ liệu gốc.

Thí nghiệm lấy ngẫu nhiên ba triệu điểm vị trí là một phân tích cụ thể về sự thay đổi các vùng do Uber chiếm ưu thế, không phải bằng chứng rằng toàn bộ dataset gốc chỉ có ba triệu bản ghi.

Bài báo cũng không cung cấp đầy đủ các thống kê chất lượng dữ liệu như tỷ lệ thiếu, bản ghi trùng lặp, timestamp không hợp lệ và dung lượng sau tiền xử lý.

Do đó, đồ án cần thực hiện profiling trực tiếp trên dữ liệu TLC thực tế và ghi nhận số liệu đo được thay vì suy diễn từ mô tả của bài báo.

## 5. Kiến trúc và phương pháp

### 5.1. Kiến trúc xử lý Big Data

Pipeline được mô tả trong bài báo gồm:

1. Nạp dữ liệu chuyến đi vào cụm xử lý.
2. Lưu trữ dữ liệu bằng HDFS và tổ chức dữ liệu bằng Hive.
3. Sử dụng MapReduce để profiling và thực hiện phân tích ban đầu.
4. Sử dụng Spark để xử lý dữ liệu và phân loại.
5. Tổng hợp, trực quan hóa hoạt động đón khách theo khu vực và thời gian.
6. Sử dụng kết quả phân loại để phân tích xu hướng và xây dựng ứng dụng gợi ý dịch vụ.

Bài báo không triển khai MapReduce và Spark như hai hệ thống thực hiện cùng một bộ tác vụ benchmark. Vì vậy, không thể dùng kết quả trong bài báo để kết luận nền tảng nào có thời gian xử lý thấp hơn.

### 5.2. Thuật toán phân loại

Bài báo sử dụng Logistic Regression thông qua Spark MLlib.

Quy trình khái quát:

1. Chia bản đồ thành các vùng không gian.
2. Ánh xạ tọa độ đón khách vào các vùng.
3. Xác định nhãn dịch vụ chiếm ưu thế theo dữ liệu đón khách.
4. Huấn luyện Logistic Regression để phân loại vùng.
5. Đánh giá trên tập kiểm thử.

Các tác giả sử dụng phương pháp tối ưu L-BFGS để học tham số của mô hình.

Cần phân biệt rõ:

- HDFS là hệ thống lưu trữ phân tán.
- MapReduce là mô hình xử lý dữ liệu phân tán.
- Spark là nền tảng xử lý dữ liệu.
- Logistic Regression là thuật toán học máy.

Các thành phần này có vai trò khác nhau và không thể dùng tên thay thế cho nhau.

## 6. Kết quả thực nghiệm của bài báo

Bài báo báo cáo accuracy trung bình khoảng 85% trên các bộ dữ liệu theo tháng từ tháng 4 đến tháng 9 năm 2014. Accuracy cao nhất đạt 90% trên dữ liệu tháng 4 năm 2014.

Trong một phân tích bổ sung, các tác giả lấy ngẫu nhiên ba triệu điểm vị trí. Khi sử dụng mô hình huấn luyện trên dữ liệu tháng 4 năm 2014, khoảng 600.000 điểm được phân loại vào vùng do Uber chiếm ưu thế. Khi sử dụng mô hình huấn luyện trên dữ liệu tháng 9 năm 2014, con số này tăng lên khoảng 800.000 điểm.

Các kết quả này được dùng để minh họa sự mở rộng của các vùng có hoạt động Uber chiếm ưu thế trong giai đoạn khảo sát.

### Giới hạn khi diễn giải kết quả

Accuracy 85%–90% là chỉ số của bài toán phân loại dịch vụ theo vùng. Nó không thể được dùng làm baseline cho bài toán phát hiện chuyến đi bất thường.

Bài báo cũng không đưa ra một benchmark đối đầu trực tiếp giữa MapReduce và Spark trên cùng tác vụ, cùng dữ liệu và cùng điều kiện tài nguyên. Vì vậy, bài báo không chứng minh Spark nhanh hơn MapReduce theo một tỷ lệ cụ thể.

## 7. Đánh giá ưu điểm và hạn chế

### 7.1. Ưu điểm

- Xây dựng pipeline khai thác dữ liệu chuyến đi quy mô lớn.
- Kết hợp HDFS, Hive, MapReduce và Spark.
- Phân tích cả không gian và thời gian.
- Kết hợp xử lý dữ liệu với một thuật toán phân loại cụ thể.
- Có kết quả thực nghiệm trên sáu bộ dữ liệu theo tháng.
- Minh họa khả năng ứng dụng kết quả phân tích trong gợi ý dịch vụ vận chuyển.

### 7.2. Hạn chế đối với hướng phát triển của đồ án

**Hạn chế 1 — Chưa có benchmark MapReduce–Spark trực tiếp**

Hai nền tảng đảm nhiệm các vai trò khác nhau trong pipeline. Chưa có cơ sở để kết luận nền tảng nào nhanh hơn khi xử lý cùng một tác vụ.

**Hạn chế 2 — Chưa giải quyết phát hiện bất thường**

Logistic Regression trong bài báo phân loại dịch vụ chiếm ưu thế theo vùng, không xác định chuyến đi bất thường.

**Hạn chế 3 — Chưa báo cáo đầy đủ các chỉ số hiệu suất hệ thống**

Kết quả được nhấn mạnh là accuracy phân loại. Bài báo không cung cấp một ma trận benchmark đầy đủ về thời gian thực thi, throughput, speedup và mức sử dụng tài nguyên của MapReduce so với Spark trên cùng tác vụ.

**Hạn chế 4 — Cần xác minh dữ liệu khi tái lập**

Dữ liệu TLC hiện nay có thể khác về schema, định dạng và phạm vi thời gian so với dữ liệu được sử dụng trong nghiên cứu năm 2018. Cần kiểm tra nguồn dữ liệu thực tế trước khi tái lập pipeline.

## 8. Phần kế thừa và phần mở rộng của đồ án

### 8.1. Phần kế thừa

- Nguồn dữ liệu chuyến taxi công khai tại New York.
- HDFS làm hệ thống lưu trữ.
- Pipeline xử lý dữ liệu lớn.
- Phân tích hoạt động đón khách theo thời gian và khu vực.
- Tư tưởng kết hợp xử lý dữ liệu với trực quan hóa.

### 8.2. Phần mở rộng thứ nhất — Đánh giá hiệu suất hệ thống

Đồ án triển khai một bộ tác vụ phân tích tương đương bằng Hadoop MapReduce và Spark, bao gồm:

- Đếm chuyến đi theo ngày và giờ.
- Thống kê chuyến đi theo khu vực đón/trả.
- Tính thời lượng và quãng đường trung bình.
- Tổng hợp doanh thu hoặc tiền tip nếu dữ liệu hỗ trợ.

Hai nền tảng phải nhận cùng dữ liệu đầu vào, sử dụng cùng định nghĩa phép tính và tạo kết quả có thể đối chiếu.

Các chỉ số đánh giá gồm:

- Thời gian thực thi.
- Throughput, tính theo số bản ghi xử lý mỗi giây.
- Speedup giữa cấu hình hoặc quy mô dữ liệu.
- Mức sử dụng CPU, RAM và các tài nguyên có thể đo được.
- Tính đúng đắn của kết quả.

MapReduce có thể được dùng làm baseline hệ thống ban đầu. Spark được đo ở cấu hình cơ sở trước, sau đó mới thử nghiệm tối ưu để xác định liệu hiệu suất có được cải thiện hay không.

### 8.3. Phần mở rộng thứ hai — Phát hiện bất thường

Đồ án xây dựng một bài toán riêng nhằm phát hiện chuyến taxi có các đặc trưng bất thường, chẳng hạn thời lượng, quãng đường hoặc tỷ lệ quãng đường trên thời gian.

Các phương pháp phải được so sánh trên cùng tập kiểm thử có nhãn.

Baseline có thể là ngưỡng cố định hoặc median/MAD. Phương pháp đề xuất cần có cơ sở kỹ thuật rõ ràng và được đánh giá bằng Precision, Recall, F1-score cùng thời gian thực thi.

Nhãn kiểm thử phải được tạo theo quy tắc độc lập hoặc quy trình gán nhãn được xác định trước. Không được tạo nhãn bằng chính phương pháp đề xuất rồi sử dụng chúng làm bằng chứng độc lập rằng phương pháp đó tốt hơn.

## 9. Thiết kế baseline và tiêu chí đánh giá

Đồ án sử dụng hai baseline độc lập vì hai nhiệm vụ có mục tiêu và đầu ra khác nhau.

| Thành phần | Baseline | Phương pháp so sánh | Chỉ số chính |
|---|---|---|---|
| Xử lý Big Data | Hadoop MapReduce | Spark cơ sở và Spark tối ưu | Thời gian, throughput, speedup, tài nguyên |
| Phát hiện bất thường | Ngưỡng cố định hoặc median/MAD | Phương pháp phát hiện cải tiến | Precision, Recall, F1-score, thời gian |

Để kết quả có ý nghĩa, các thí nghiệm cần sử dụng cùng tập dữ liệu, định nghĩa tác vụ thống nhất, cùng điều kiện tài nguyên và nhiều lần chạy khi điều kiện cho phép.

Kết quả phải được ghi nhận từ chương trình thực nghiệm. Không đặt trước kết luận rằng Spark hoặc phương pháp đề xuất chắc chắn tốt hơn baseline.

Nếu phương pháp đề xuất không vượt baseline, cần phân tích nguyên nhân, thử nghiệm bổ sung có kiểm soát hoặc điều chỉnh phạm vi đóng góp. Không được loại bỏ kết quả bất lợi chỉ để làm đẹp báo cáo.

## 10. Kết luận

Sun và cộng sự (2018) là tài liệu tham khảo phù hợp cho việc xây dựng pipeline Big Data trên dữ liệu taxi và Uber, đặc biệt ở khía cạnh lưu trữ phân tán, phân tích không gian–thời gian và kết hợp các công cụ Hadoop với Spark.

Tuy nhiên, bài báo không trực tiếp giải quyết hai yêu cầu trọng tâm của đồ án: benchmark đối đầu MapReduce–Spark và phát hiện chuyến đi bất thường.

Do đó, đồ án kế thừa bối cảnh dữ liệu và tư tưởng xây dựng pipeline, đồng thời tự thiết kế hai nhóm thực nghiệm:

1. So sánh hiệu suất xử lý các tác vụ tương đương giữa MapReduce và Spark.
2. So sánh chất lượng phát hiện bất thường giữa baseline và phương pháp đề xuất trên tập kiểm thử có nhãn.

Hai nhóm thực nghiệm này cung cấp bằng chứng riêng về hiệu suất hệ thống và chất lượng thuật toán, giúp kết luận của đồ án rõ ràng, có thể kiểm chứng và tái lập.

## Tài liệu tham khảo

Sun, H., Hu, S., McIntosh, S., & Cao, Y. (2018). Big Data Trip Classification on the New York City Taxi and Uber Sensor Network. *Journal of Internet Technology, 19*(2), 591–598. https://doi.org/10.3966/160792642018031902027