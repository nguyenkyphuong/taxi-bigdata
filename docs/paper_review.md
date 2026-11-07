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

Bài báo giới thiệu kho dữ liệu Yellow Taxi tại New York từ năm 2009, Green Taxi được bổ sung từ năm 2013, và dữ liệu Uber giai đoạn 2014–2015. Phạm vi phân loại chính được công bố cụ thể là tháng 4–9/2014, không phải toàn bộ các năm kể trên.

Trong thí nghiệm phân loại, các tác giả xây dựng sáu bộ dữ liệu theo tháng, từ tháng 4 đến tháng 9 năm 2014. Mỗi bộ dữ liệu bao gồm tọa độ đón khách của ba dịch vụ.

### 4.2. Biểu diễn dữ liệu không gian

Các tác giả chia bản đồ thành các vùng nhỏ dựa trên tọa độ đón khách. Tọa độ vĩ độ và kinh độ được làm tròn đến ba chữ số thập phân để xác định vùng.

Theo bài báo, cách chia này tạo ra vùng có diện tích ước tính khoảng 10.000 m²; Manhattan được ước tính chia thành khoảng 60.000 vùng.

Sau khi ánh xạ các điểm đón khách vào vùng, dữ liệu được sử dụng để xác định dịch vụ có số lượt đón khách chiếm ưu thế và xây dựng tập dữ liệu phân loại.

### 4.3. Phương pháp chia tập dữ liệu

Trong thí nghiệm phân loại theo tháng, tác giả nhóm các tọa độ đón khách vào từng vùng; mỗi vùng hình thành một tập dữ liệu riêng. Theo mô tả tại mục 5.3, mỗi tháng có phép chia ngẫu nhiên **80% huấn luyện / 20% kiểm thử**, Logistic Regression được huấn luyện theo vùng, sau đó accuracy của các vùng được lấy trung bình để thu được accuracy theo tháng.

**Lưu ý về khả năng tái lập:** Bài báo chưa công bố đủ chi tiết về vector đặc trưng đầu vào, định nghĩa nhãn huấn luyện ở cấp từng bản ghi, mã hóa ba lớp, cách xử lý vùng quá ít quan sát hoặc chỉ có một dịch vụ, seed chia dữ liệu và tham số mô hình. Do đó, phần triển khai của nhóm phải **công bố rõ các giả định tái lập**; không được mặc nhiên xem kết quả triển khai mới là bản sao chính xác của thí nghiệm gốc.

### 4.4. Giới hạn thông tin dữ liệu

Bài báo không cung cấp một con số tổng quát, đầy đủ về tổng số bản ghi thô trong toàn bộ dữ liệu đầu vào hoặc dung lượng dữ liệu gốc.

Thí nghiệm lấy ngẫu nhiên ba triệu điểm vị trí là một phân tích cụ thể về sự thay đổi các vùng do Uber chiếm ưu thế, không phải bằng chứng rằng toàn bộ dataset gốc chỉ có ba triệu bản ghi.

Bài báo cũng không cung cấp đầy đủ các thống kê chất lượng dữ liệu như tỷ lệ thiếu, bản ghi trùng lặp, timestamp không hợp lệ và dung lượng sau tiền xử lý.

**Nguồn dữ liệu có thể lấy lại:** Yellow/Green Taxi tháng 4–9/2014 có thể truy cập từ [NYC TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) hoặc [NYC Open Data – Yellow](https://data.cityofnewyork.us/Transportation/2014-Yellow-Taxi-Trip-Data/gkne-dk5s), [NYC Open Data – Green](https://data.cityofnewyork.us/Transportation/2014-Green-Taxi-Trip-Data/2np7-5jsg). Uber tháng 4–9/2014 có bản công khai trong [FiveThirtyEight Uber TLC FOIL Response](https://github.com/fivethirtyeight/uber-tlc-foil-response), gồm hơn 4,5 triệu điểm đón khách trên **toàn bộ sáu tháng** (không phải 4,5 triệu/tháng). Các nguồn này giúp tái tạo phạm vi thí nghiệm, nhưng **chưa xác nhận từng bản ghi trùng tuyệt đối với dữ liệu nhóm tác giả đã dùng**.

Cần kiểm tra schema thực tế trước khi hợp nhất: dữ liệu Uber 2014 chủ yếu có thời điểm/tọa độ đón khách, không có đầy đủ các trường giá cước, quãng đường, điểm trả khách như taxi. Vì vậy, các feature so sánh cả ba dịch vụ phải lấy từ **giao các trường thực sự có** (đặc biệt là thời điểm và tọa độ đón khách).

Do đó, đồ án cần thực hiện profiling trực tiếp trên dữ liệu được tải về, ghi nhận số liệu đo được và lưu bản kê file/hash thay vì suy diễn từ mô tả của bài báo.

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

Quy trình khái quát theo mô tả của bài báo:

1. Chia bản đồ thành các vùng không gian bằng cách làm tròn tọa độ đến ba chữ số thập phân.
2. Ánh xạ các điểm đón khách của Yellow/Green/Uber vào những vùng này.
3. Tạo bộ dữ liệu huấn luyện và kiểm thử theo vùng, sử dụng dữ liệu lịch sử để phân loại dịch vụ chiếm ưu thế tại vị trí được truy vấn.
4. Huấn luyện Logistic Regression qua Spark MLlib và đánh giá accuracy.
5. Tổng hợp nhãn dự đoán để phân tích khu vực hoạt động của dịch vụ.

Các tác giả sử dụng phương pháp tối ưu L-BFGS để học tham số mô hình. **Tuy nhiên**, phần mô tả và công thức của bài báo không đủ để khẳng định chính xác cách triển khai Logistic Regression **ba lớp**. Cũng cần phân biệt hai khái niệm: (a) dịch vụ thực tế của **mỗi lượt đón khách** và (b) dịch vụ **chiếm ưu thế trong một vùng**. Chúng có liên quan nhưng không phải cùng một nhãn; phần triển khai phải định nghĩa rõ đơn vị dự đoán, nhãn và phép tổng hợp.

Cần phân biệt rõ:

- HDFS là hệ thống lưu trữ phân tán.
- MapReduce là mô hình xử lý dữ liệu phân tán.
- Spark là nền tảng xử lý dữ liệu.
- Logistic Regression là thuật toán học máy.

Các thành phần này có vai trò khác nhau và không thể dùng tên thay thế cho nhau.

## 6. Kết quả thực nghiệm của bài báo

Bài báo báo cáo accuracy trung bình khoảng **85%** trên sáu bộ dữ liệu theo tháng từ tháng 4 đến tháng 9 năm 2014. Accuracy cao nhất đạt **90%** trên dữ liệu tháng 4 năm 2014. Theo mục 5.3, tác giả lấy trung bình accuracy **theo vùng** để thu được accuracy **theo tháng**; chưa có bảng đầy đủ giá trị accuracy từng tháng hay chi tiết về cách xử lý vùng không thể huấn luyện.

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

### 7.2. Hạn chế và khoảng trống có thể phát triển

**Hạn chế 1 — Chưa có benchmark MapReduce–Spark trực tiếp.** MapReduce và Spark đảm nhiệm các vai trò khác nhau. Paper không chứng minh nền tảng nào nhanh hơn trên cùng một tác vụ/dataset/cấu hình, đồng thời chưa công bố đầy đủ runtime, throughput, speedup, p95/p99 latency.

**Hạn chế 2 — Thiếu chi tiết để tái lập Logistic Regression ba lớp.** Paper mô tả huấn luyện theo vùng nhưng chưa chỉ rõ toàn bộ feature, phép gán nhãn ở cấp bản ghi, xử lý vùng thiếu lớp, siêu tham số và seed. Đây là khoảng trống về **reproducibility**, không phải bằng chứng mô hình gốc triển khai sai.

**Hạn chế 3 — Đánh giá mô hình chưa đầy đủ.** Chủ yếu dùng accuracy, trong khi số chuyến Yellow Taxi lớn hơn Green Taxi và Uber. Cần bổ sung Macro-F1, precision/recall từng lớp, confusion matrix và baseline dự đoán lớp đa số; đồng thời phân biệt trung bình **các vùng** với trung bình **các chuyến**.

**Hạn chế 4 — Phân loại chủ yếu theo không gian, chưa có đánh giá dự đoán theo thời gian ngoài mẫu.** Có thể khảo sát thêm tác động của giờ trong ngày, thứ trong tuần và thống kê lịch sử, hoặc thiết kế bài toán dự báo dịch vụ chiếm ưu thế ở thời điểm tiếp theo. Tuy nhiên, nếu đổi mục tiêu dự đoán thì **không được so sánh trực tiếp** accuracy với con số 85% của paper.

**Hạn chế 5 — Thiếu đánh giá thời gian phản hồi khi vận hành.** Mô hình gợi ý dịch vụ được giới thiệu ở mức ứng dụng; paper chưa cung cấp bộ số liệu phục vụ đánh giá p50/p95/p99 latency, tải đầu vào, độ trễ xử lý luồng, hoặc khả năng mở rộng theo kích thước cụm.

**Không nên coi "chưa phát hiện chuyến đi bất thường" là thiếu sót chính của paper.** Phát hiện bất thường là một **bài toán khác**. Đặc biệt, dữ liệu Uber 2014 thiếu những trường quan trọng của chuyến đi (chẳng hạn quãng đường/giá cước) nên việc chuyển trọng tâm sang bất thường sẽ khiến nhóm khó đối chiếu chất lượng thuật toán với baseline đã chọn.

**Lưu ý diễn giải khoa học:** Sự tăng hoạt động của Uber đồng thời với giảm thị phần Yellow Taxi không tự nó chứng minh quan hệ nhân quả; phần trình bày đồ án nên nói "mối liên hệ/biến động cùng thời kỳ" trừ khi có thiết kế kiểm định nhân quả.

## 8. Phần kế thừa và phần mở rộng của đồ án

### 8.1. Phần kế thừa — tái lập baseline (bắt buộc)

Đồ án giữ **bối cảnh, mục tiêu phân loại dịch vụ và toàn bộ phạm vi dữ liệu thí nghiệm chính** của Sun và cộng sự (2018):

1. **Dữ liệu:** ba nguồn Yellow Taxi, Green Taxi, Uber, đủ **sáu tháng từ 04/2014 đến 09/2014**. Dự kiến 18 phần dữ liệu theo cặp `(dịch vụ, tháng)`; số lượng file vật lý có thể khác vì cách nhà cung cấp đóng gói. Không lấy mẫu 3 triệu điểm để thay cho tập huấn luyện đầy đủ; thí nghiệm 3 triệu điểm trong paper chỉ phục vụ phân tích thay đổi vùng Uber.
2. **Cơ sở hạ tầng:** đưa dữ liệu thô lên Hadoop HDFS; dùng Hive Metastore/bảng ngoại hoặc Spark SQL trên HDFS để quản lý và truy vấn; dùng Spark để làm sạch, ánh xạ vùng, trích xuất feature và huấn luyện ML.
3. **Phân vùng không gian:** làm tròn pickup latitude/longitude đến **ba chữ số thập phân** để tạo mã vùng theo paper. Ghi rõ cách làm tròn, hệ tọa độ và trường hợp biên; dùng cùng một cách cho cả ba dịch vụ.
4. **Baseline ML:** Logistic Regression đa lớp trên Apache Spark, chia ngẫu nhiên 80/20 theo thiết kế thí nghiệm, lưu seed, tập mẫu và phiên bản thư viện. Cố gắng tái lập quy trình huấn luyện và lấy trung bình accuracy theo vùng như mục 5.3.
5. **Kết quả nền:** heatmap, tỷ lệ pickup theo dịch vụ/vùng/tháng; accuracy từng tháng; trung bình sáu tháng; báo cáo số vùng hợp lệ và bị loại. So sánh định tính với các mô tả trong paper và đối chiếu 85% trung bình/90% tháng 4.

**Phân định ba mức tái lập:**

- **Paper-reported:** số 85% và 90% do tác giả công bố, **không phải** kết quả nhóm đã tự chạy.
- **Paper-inspired reproduction:** thí nghiệm do nhóm triển khai trên sáu tháng dữ liệu tương đương, dùng giả định có tài liệu hóa ở nơi paper thiếu chi tiết.
- **Exact reproduction:** chỉ được sử dụng nếu có đủ quy trình, feature, nhãn, split, code và nguồn dữ liệu để chứng minh gần như giống nguyên bản; với tài liệu hiện có, **không nên nhận đã tái lập chính xác**.

**Rủi ro kỹ thuật quan trọng:** paper viết "mỗi vùng một classifier", nhưng có thể có vùng quá ít dữ liệu hoặc chỉ một lớp. Nhóm cần thử tái lập cách này trên dữ liệu thực và công bố số vùng không thể huấn luyện. Nếu chi phí quá lớn hoặc không thể thực hiện nhất quán, được phép xây dựng **baseline Logistic Regression toàn cục theo từng tháng** (với tọa độ/mã vùng là feature) như một *phiên bản điều chỉnh*, nhưng phải công bố đây là thay đổi phương pháp và **không so sánh đồng nhất tuyệt đối** với 85% của paper.

### 8.2. Phần mở rộng thứ nhất — cải tiến mô hình phân loại không gian–thời gian (trọng tâm ML)

**Đề xuất:** *Spatio-Temporal Feature Engineering + Random Forest Classifier* (có thể thử XGBoost phân tán khi tài nguyên cho phép). Mục đích là kiểm định xem đặc trưng không gian–thời gian và mô hình phi tuyến có cải thiện việc dự đoán lớp dịch vụ so với Logistic Regression không.

**Thiết kế theo hai nhánh để bảo đảm so sánh công bằng:**

**Nhánh A — so sánh trực tiếp trên cùng một nhiệm vụ và cùng tập kiểm thử (bắt buộc):**

- Duy trì **đơn vị dự đoán và cách xác định nhãn như baseline nhóm đã định nghĩa**. Một phương án tái lập thực dụng là: **mỗi bản ghi = một lượt đón khách; nhãn gốc = Yellow/Green/Uber của lượt đó**; sau khi mô hình dự đoán theo điểm, mới tổng hợp dự đoán trong một vùng để suy ra dịch vụ có tần suất cao nhất. Đây là một **giả định triển khai**, vì paper không mô tả nhãn cấp bản ghi đủ rõ.
- Cùng dữ liệu tháng 4–9/2014, cùng quy tắc làm sạch, cùng train/test 80/20, cùng seed, cùng phép đo accuracy theo vùng và cùng tập vùng có thể đánh giá.
- So sánh ít nhất ba cấu hình: `A1 = Logistic Regression + tọa độ` (baseline của nhóm); `A2 = Random Forest + cùng bộ feature A1` (đo đóng góp thuật toán); `A3 = Random Forest + tọa độ + giờ/thứ + các feature lịch sử hợp lệ` (đo đóng góp feature engineering). Nếu huấn luyện theo vùng như paper không khả thi, cả A1/A2/A3 phải dùng **cùng thiết kế toàn cục đã công bố**, không đổi cách đánh giá giữa chừng.
- Feature có thể gồm `pickup_latitude`, `pickup_longitude`, `hour_of_day`, `day_of_week`, `is_weekend`, `region_id`/đặc trưng vùng. Các thống kê như mật độ/tỷ lệ pickup lịch sử chỉ được tính từ **tập huấn luyện** (ưu tiên out-of-fold cho từng điểm train để tránh target encoding leakage) hoặc từ thời gian **trước thời điểm dự đoán**; không được lấy thông tin từ tập test để tạo feature cho test.
- `service_type` dùng làm nhãn, **không được đưa vào feature**. Không đưa các trường chỉ taxi có mà Uber 2014 không có vào phép so sánh chung. Nếu dùng dữ liệu đón khách cùng cửa sổ để tính sẵn nhãn "dịch vụ chiếm ưu thế", phải tránh dùng chính các số đếm đó như feature dự đoán nhãn vì sẽ gây **target leakage**.

**Nhánh B — bài toán mở rộng theo thời gian (giá trị nghiên cứu bổ sung, đo riêng):**

- Mục tiêu mới: dự đoán **dịch vụ sẽ chiếm ưu thế tại `(vùng, khung giờ kế tiếp)`** từ các lượt đón khách **đã quan sát trong quá khứ**. Đây là dự báo về phân bố dịch vụ, hữu ích hơn cho quyết định theo giờ nhưng **không giống** nhãn/vấn đề của paper.
- Vì vùng 0,001 độ có thể rất thưa trong từng giờ, khảo sát thêm độ phân giải không gian lớn hơn (ví dụ nhóm nhiều ô nhỏ thành ô lớn), cửa sổ 3–6 giờ hoặc quy tắc mức hỗ trợ tối thiểu. Báo cáo số ô-thời gian thiếu dữ liệu và cách xử lý.
- Feature: số chuyến ba dịch vụ trong những khung giờ trước, tỷ lệ thị phần quá khứ, `hour`, `day_of_week`, số chuyến ở vùng lân cận trong quá khứ. Nhãn: dịch vụ có số pickup cao nhất ở **khung giờ mục tiêu** (quy tắc hòa rõ ràng). Không sử dụng số chuyến tương lai để tạo feature.
- Tách thời gian gợi ý: tháng 4–7 train, tháng 8 validation, tháng 9 test; có thể kiểm chứng thêm bằng rolling-origin backtesting. So sánh `LR_temporal` và `RF_temporal` trên **cùng** tập dự báo, báo cáo Accuracy/Macro-F1/Recall từng lớp. **Không đem accuracy nhánh B so trực tiếp với 85% của Sun et al.**

**Tiêu chí thành công:** A2/A3 cải thiện được A1 trên **cùng protocol**, đồng thời nhóm báo cáo trung thực việc kết quả có vượt mốc bài báo công bố hay không. 85% (trung bình sáu tháng) và 90% (tháng 4) là các **mốc tham chiếu**, không phải mục tiêu có thể cam kết trước thực nghiệm; nếu protocol khác phải nêu rõ lý do không so sánh trực tiếp.

### 8.3. Phần mở rộng thứ hai — Big Data benchmark và đo độ trễ (trọng tâm hệ thống)

**Mục đích:** Bù vào khoảng trống đo lường hiệu suất của paper, đáp ứng yêu cầu **Hadoop + Spark + đo thời gian/độ trễ**.

**(a) Benchmark batch trên toàn bộ dữ liệu:**

- Chọn một tác vụ tương đương trên cùng input HDFS, ví dụ: `groupBy(month, region_id, service_type).count()` để tính số pickup theo vùng/tháng/dịch vụ.
- Cài đặt bằng **Hadoop MapReduce** và **Spark SQL**; dùng cùng điều kiện dữ liệu, phần cứng, số worker, tài nguyên, cách lưu kết quả; phân biệt chạy nóng/lạnh, tránh để chỉ một bên có lợi thế cache.
- Đo trên 25%, 50%, 75%, **100%** dữ liệu (mức 100% **bắt buộc**), chọn các tập con bằng quy tắc hash/seed cố định để có thể lặp lại; ít nhất ba lần/mức. Báo cáo `elapsed_seconds`, `records_per_second`, `speedup = T_MapReduce / T_Spark` trên mỗi quy mô. Đây là **thí nghiệm mới của nhóm**, không phải benchmark đã có trong paper.
- Có thể bổ sung scalability theo 1/2/3 worker (nếu triển khai được cụm nhiều node) và lưu log Spark UI/YARN/MapReduce job history. **Spark chạy ở local mode không đủ để chứng minh khả năng mở rộng cụm phân tán**; nếu dùng local phải ghi hạn chế.

**(b) Đo thời gian pipeline ML:**

- Đo riêng `read`, `clean`, `spatial_mapping`, `feature_generation`, `training`, `inference`, `write`, `end_to_end` bằng đồng hồ monotonic trước–sau hành động thực thi Spark. Trong Spark có lazy evaluation: phải gọi một **action** thích hợp để phép đo thực sự bao gồm công việc, không chỉ đo bước khai báo DataFrame.
- Báo cáo thêm số record trước/sau làm sạch, kích thước dữ liệu, số partition, CPU/RAM/worker, Spark/Hadoop version, số lần thử. So sánh thời gian huấn luyện và suy luận A1/A2/A3, kiểm tra đánh đổi *accuracy ↔ runtime*.

**(c) Structured Streaming và latency (phần tăng sức thuyết phục, ưu tiên khi đủ thời gian):**

- Phát lại các bản ghi lịch sử theo luồng thông qua **Kafka → Spark Structured Streaming**, hoặc triển khai nhẹ hơn bằng **file source → Spark Structured Streaming**. Đây là **mô phỏng dữ liệu thời gian thực từ dữ liệu cũ**, không phải nguồn sự kiện live 2014.
- Dùng model đã huấn luyện để dự đoán nhãn hoặc thống kê pickup theo vùng/khung giờ, ghi kết quả xuống storage/serving table và đưa lên dashboard. Không bắt buộc huấn luyện lại model trên từng micro-batch.
- Đóng dấu `ingest_timestamp` lúc phát lại và `output_timestamp` khi bản ghi thực sự đến nơi nhận kết quả để đo **end-to-end latency = output_timestamp − ingest_timestamp**. Báo cáo **p50, p95, p99** và throughput tại nhiều tốc độ phát thử. Phân biệt với `triggerExecution`/`durationMs` của Spark (thời gian xử lý micro-batch), vốn **không tự động bằng end-to-end latency**.
- Ghi rõ tốc độ replay (records/s), trigger interval, watermark, tỷ lệ bản ghi trễ/bị loại (nếu có), trường hợp hệ thống backlog và độ lệch đồng hồ nếu sender/receiver ở hai máy.

**Kiến trúc đề xuất:**

```text
NYC TLC 2014 (Yellow + Green)          FiveThirtyEight 2014 (Uber)
                \                              /
                 \                            /
                   --> HDFS / raw (Bronze) <--
                              |
                 Spark ETL / Data Quality
                              |
              HDFS Parquet + Hive (Silver)
                              |
           Spatial/Temporal Features (Gold)
                          /           \
                         /             \
            Spark ML (LR, RF)      MapReduce vs Spark
                         |           Batch benchmark
                     Model artifacts
                         |
       Historical replay -> Structured Streaming
                         |
          Predictions / Aggregates / Dashboard
                         |
         Throughput + p50/p95/p99 latency
```

**Mức tối thiểu để đồ án không bị dàn trải:** hoàn thành **full six-month ingestion → HDFS → Spark ETL → Logistic Regression → Random Forest → so sánh ML → benchmark batch và runtime** trước. Structured Streaming/Kafka và dashboard là bước nâng cấp sau; không nên hy sinh việc chạy đủ dữ liệu và phép đo chính để có demo bắt mắt.

## 9. Thiết kế baseline và tiêu chí đánh giá

### 9.1. Bộ dữ liệu và quy trình tái lập

| Thành phần | Quy định bắt buộc | Chứng cứ bàn giao |
|---|---|---|
| Nguồn | Yellow, Green, Uber: đủ sáu tháng 04–09/2014 | `data_manifest.csv` gồm URL, tên file, số byte, checksum |
| Phạm vi | Dùng **100% các bản ghi hợp lệ** của sáu tháng; không lấy mẫu thay bài chạy chính | row count theo tháng/dịch vụ; số dòng bị loại theo nguyên nhân |
| Quy tắc làm sạch | Kiểm tra null, lat/lon ngoài NYC, timestamp sai, bản ghi trùng; nêu ngưỡng rõ | `data_quality_report.md/json` |
| Phân vùng | Lat/lon làm tròn 3 chữ số sau dấu phẩy như paper | code + ví dụ mapping; số vùng theo tháng |
| Train/test | Random 80/20 cho nhánh so sánh paper; seed và mã vùng cố định | tập ID train/test hoặc manifest và seed |
| Train/test theo thời gian | Nếu làm nhánh dự báo: Apr–Jul / Aug / Sep; không random trộn tương lai vào quá khứ | cấu hình + số mẫu train/val/test |
| Nhãn | Định nghĩa chính xác **nhãn cấp chuyến** và **dịch vụ chiếm ưu thế cấp vùng**; quy tắc hòa | `label_definition.md` |
| Feature | Đặc trưng khả dụng cho cả ba dịch vụ, xây dựng không dùng test/tương lai | `feature_schema.md` và kiểm tra leakage |
| Hạ tầng | HDFS, Spark, Hive tùy chọn, MapReduce benchmark nếu triển khai | cấu hình cluster, phiên bản, tài nguyên |

**Điểm cần chốt trước khi viết code:** Paper không cho công thức đầy đủ từ tọa độ → nhãn huấn luyện → Logistic Regression → nhãn vùng. Nhóm cần ghi một **spec tái lập** ngắn, mô tả hàng dữ liệu, nhãn, feature và cách lấy trung bình accuracy. Mọi model được so sánh trong nhánh A phải dùng chung spec này.

### 9.2. Ma trận thí nghiệm Machine Learning

| Mã | Mô hình | Feature | Cách đánh giá | Vai trò |
|---|---|---|---|---|
| P | Logistic Regression paper | Chưa được công bố đủ chi tiết | 85% trung bình, 90% tháng 4 (paper-reported) | Mốc tham chiếu lịch sử, **không phải kết quả tự chạy** |
| A1 | Logistic Regression (PySpark ML) | Lat/lon, xử lý không gian tối giản theo spec nhóm | Sáu tháng, 80/20, cùng tập test | Baseline tái lập có công bố giả định |
| A2 | Random Forest (PySpark ML) | **Giống A1** | Sáu tháng, **cùng split và metric với A1** | Đánh giá lợi ích đổi thuật toán |
| A3 | Random Forest (PySpark ML) | A2 + giờ, thứ, cuối tuần, các đặc trưng lịch sử không leakage | Sáu tháng, **cùng split và metric** | Đánh giá lợi ích thêm feature |
| B1 | Logistic Regression | Feature lịch sử cho `(vùng, khung giờ)` | Temporal holdout riêng | Baseline dự báo thời gian mở rộng |
| B2 | Random Forest | Giống B1 | Temporal holdout riêng | Cải tiến dự báo thời gian; **không so 85%** |

**Mỗi thí nghiệm ML cần báo cáo:**

- Accuracy **từng tháng**; trung bình sáu tháng; chênh lệch so với A1 bằng **điểm phần trăm**.
- **Macro-F1**, weighted-F1, precision/recall từng lớp và confusion matrix để không che giấu việc lớp Yellow Taxi quá lớn.
- Accuracy **trung bình theo vùng** (theo paper) và accuracy **trên toàn bộ bản ghi** (có trọng số theo quy mô vùng); hai cách tính có thể khác nhau.
- Số vùng/record đủ điều kiện đánh giá; cách xử lý vùng chỉ có một lớp hoặc rất ít điểm; kết quả của majority-class baseline.
- Thời gian train, inference, tổng thời gian pipeline, tài nguyên tiêu thụ; nhiều lần chạy với seed được lưu.

**Cách phát biểu kết quả đúng:** Chỉ khi cùng task/nhãn/đơn vị đo, phạm vi sáu tháng, phương pháp chia và cách tổng hợp accuracy đủ tương đương mới được tuyên bố "vượt accuracy của paper". Nếu không, chỉ nên nói **"A2/A3 cải thiện so với baseline A1 do nhóm tái lập"**, kèm mức 85%/90% để tham chiếu, không gán quan hệ thắng thua trực tiếp.

### 9.3. Ma trận thí nghiệm hệ thống

| Bài test | Input | Biến so sánh | Chỉ số đầu ra |
|---|---|---|---|
| T1 – Batch engine | Dữ liệu đủ sáu tháng | Hadoop MapReduce vs Spark SQL trên **cùng group-by** | Runtime, records/s, speedup |
| T2 – Data scalability | 25/50/75/100% dữ liệu, **không thay kết quả chính full-data** | Quy mô dữ liệu | Runtime, throughput, đường tăng chi phí |
| T3 – Cluster scalability | Toàn bộ dữ liệu | Số worker/cores cố định theo từng cấu hình | Runtime, speedup, scaling efficiency |
| T4 – ML trade-off | Cùng sáu tháng/split | LR vs RF, feature cơ bản vs feature mở rộng | Accuracy/Macro-F1 vs train/inference time |
| T5 – Streaming replay | Luồng dữ liệu lịch sử được phát lại | Tốc độ đầu vào/trigger interval | p50/p95/p99 latency, throughput, backlog |

**Công thức và cách đo:**

- `Accuracy = số dự đoán đúng / số quan sát kiểm thử` (áp dụng ở **cùng đơn vị đánh giá**).
- `Macro-F1 = (F1_Yellow + F1_Green + F1_Uber) / 3`.
- `Throughput = số bản ghi xử lý thành công / số giây thực thi`.
- `Speedup_batch = T_MapReduce / T_Spark` (chỉ trên **cùng task và điều kiện**).
- `Scaling_efficiency = (T_1 / T_p) / p` khi so sánh `p` worker cùng loại với 1 worker.
- `End-to-end latency = thời điểm output được nhận − thời điểm input được bơm vào hệ thống replay`.
- `P95 latency`: 95% quan sát có latency **không lớn hơn** giá trị này.

Để kết quả tin cậy, chạy thử tối thiểu ba lần, báo cáo **median** và độ biến thiên; ghi rõ các lần warm-up/cache, đặt tên cột đơn vị (`seconds`, `records/s`, `milliseconds`) và lưu raw log. Không suy diễn độ trễ thực tế ở năm 2014 từ hiệu giữa timestamp lịch sử với đồng hồ hiện tại.

### 9.4. Tiêu chí đạt yêu cầu của giảng viên

| Yêu cầu giảng viên | Cách chứng minh trên đồ án |
|---|---|
| 1. Hadoop, Spark, ML | Data nằm trong HDFS, chạy Spark ETL/Spark ML; có job/log/screenshot cluster; benchmark thêm MapReduce |
| 2. Baseline là paper | Review có dẫn chính xác; code LR tái lập với spec giả định rõ; trích 85% và 90% đúng ngữ cảnh |
| 3. Thuật toán vượt paper, chạy đủ dữ liệu | Chạy **đủ sáu tháng, cả ba dịch vụ**; so A1/A2/A3 cùng protocol; kiểm tra mốc 85%/90% **nếu thật sự đủ điều kiện so sánh**; không cam kết kết quả chưa đo |
| 4. Hay, có tính thời đại | Phân loại dịch vụ theo thời gian, heatmap động, streaming/replay, dashboard; mô tả rõ giá trị vận hành, không gọi dữ liệu 2014 là "real-time data" |
| 5. Đo thời gian và độ trễ | Thời gian từng bước batch/ML, throughput, speedup; nếu có streaming thì đo end-to-end p50/p95/p99 |

### 9.5. Thứ tự triển khai và sản phẩm bàn giao

1. **Chốt baseline spec**: nhãn/feature/đơn vị đánh giá và những giả định paper thiếu; nêu rõ có/không huấn luyện được classifier cho từng vùng.
2. **Tải đủ dữ liệu** 04–09/2014; tạo manifest và kiểm tra số dòng/hash theo nguồn.
3. **Dựng HDFS + Spark**; lưu raw và bảng chuẩn hóa; profiling bằng Spark, sau đó thử cùng tác vụ bằng MapReduce.
4. **Huấn luyện LR và RF trên cùng tập test**; báo cáo accuracy/Macro-F1, data leakage check và các giá trị đo được.
5. **Benchmark runtime** dữ liệu 100% và các mức tỷ lệ; ít nhất ba lần/cấu hình.
6. **Nếu còn thời gian**, làm mô-đun dự báo theo khung giờ + streaming replay/dashboard/latency.

**Các file/report nên có:** `paper_review.md` (tài liệu này), `reproduction_spec.md`, `data_manifest.csv`, `data_quality_report.md`, `baseline_lr.ipynb/py`, `model_comparison.csv`, `benchmark_batch.csv`, `benchmark_ml.csv`, `streaming_latency.csv` (nếu có) và báo cáo kết quả có biểu đồ.

## 10. Kết luận

Sun và cộng sự (2018) là một baseline phù hợp cho **phân loại dịch vụ có hoạt động đón khách chiếm ưu thế theo không gian** trên dữ liệu Yellow Taxi, Green Taxi và Uber. Paper cung cấp phạm vi thí nghiệm rõ ràng ở mức sáu bộ dữ liệu theo tháng 04–09/2014, Logistic Regression qua Spark MLlib, chia dữ liệu 80/20, và accuracy được báo cáo khoảng 85% trung bình/90% cao nhất. Tuy nhiên, thiếu một số chi tiết cần để tái lập hoàn toàn phép gán nhãn, feature và huấn luyện theo vùng.

Vì vậy, đồ án nên triển khai ba lớp kết quả tách biệt:

1. **Tái lập có kiểm soát**: thu thập đủ sáu tháng dữ liệu của ba dịch vụ, dựng HDFS–Spark, thực hiện phân vùng và Logistic Regression, ghi rõ giả định và sai khác so với paper.
2. **Cải tiến có đối chứng**: dùng Random Forest và đặc trưng không gian–thời gian để đánh giá cùng baseline trên cùng dữ liệu, cùng split và cùng metric; đưa các con số vượt paper ra kết luận **chỉ khi thực nghiệm chứng minh**.
3. **Đánh giá hệ thống**: benchmark MapReduce–Spark trên cùng task và quy mô, đo throughput/runtime, mở rộng thêm Structured Streaming để đo latency p50/p95/p99 nếu có đủ thời gian và tài nguyên.

**Định hướng ưu tiên:** lựa chọn phương án *"Spatio-Temporal Classification + Full-Data Spark/Hadoop Benchmark"*, thay vì chuyển sang phát hiện bất thường. Hướng này có liên hệ trực tiếp với paper, đáp ứng đồng thời các tiêu chí ML/Big Data và cung cấp một luận điểm mở rộng có thể đo lường, kiểm chứng và bảo vệ trước giảng viên.

## Tài liệu tham khảo

1. Sun, H., Hu, S., McIntosh, S., & Cao, Y. (2018). *Big Data Trip Classification on the New York City Taxi and Uber Sensor Network*. Journal of Internet Technology, 19(2), 591–598. https://doi.org/10.3966/160792642018031902027. **Các kết quả 85%/90% và mô tả phương pháp được trích từ nguồn này.**
2. New York City Taxi & Limousine Commission. *TLC Trip Record Data*. https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page.
3. NYC Open Data. *2014 Yellow Taxi Trip Data*. https://data.cityofnewyork.us/Transportation/2014-Yellow-Taxi-Trip-Data/gkne-dk5s.
4. NYC Open Data. *2014 Green Taxi Trip Data*. https://data.cityofnewyork.us/Transportation/2014-Green-Taxi-Trip-Data/2np7-5jsg.
5. FiveThirtyEight. *Uber TLC FOIL Response*. https://github.com/fivethirtyeight/uber-tlc-foil-response.
6. Apache Spark. *RandomForestClassifier* (API). https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassifier.html.
7. Apache Spark. *Structured Streaming Programming Guide*. https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html.

> **Phạm vi xác minh:** Nội dung mô tả paper đã được đối chiếu với bản PDF chính thức. Các phần 8–9 là **thiết kế đề xuất cho đồ án**, chưa phải các kết quả thí nghiệm đã chạy. Mọi chỉ số ML và benchmark ngoài mốc paper-reported cần được nhóm đo thực tế.