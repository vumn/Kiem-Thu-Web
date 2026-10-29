# Kịch bản kiểm thử chức năng Dynamic Loading (Tuần 07)

Các bài kiểm thử tập trung vào việc thí nghiệm và chứng minh tầm quan trọng của cơ chế chờ trong kiểm thử tự động.

---

## 1. Kịch bản kiểm thử cho trang Example 1 (Element on page that is hidden)
* **URL mục tiêu:** `https://the-internet.herokuapp.com/dynamic_loading/1`
* **Đặc điểm trang:** Phần tử kết quả đã tồn tại sẵn trong mã nguồn nhưng ở trạng thái ẩn. Khi bấm nút Start, một thanh tải dữ liệu xuất hiện và sau đó phần tử mới hiển thị.

### Test Case 1.1: Kiểm thử không sử dụng lệnh chờ (No Wait)
* **Mục đích:** Thí nghiệm quan sát hành vi của Selenium khi tương tác ngay lập tức với phần tử đang bị ẩn.
* **Các bước thực hiện:**
  1. Mở trình duyệt Chrome.
  2. Truy cập vào đường dẫn trang Example 1.
  3. Tìm và Click vào nút **"Start"**.
  4. Ngay lập tức tìm phần tử dòng chữ kết quả và đọc nội dung văn bản của nó mà không đợi thanh loading chạy xong.
  5. Đóng trình duyệt.
* **Kết quả mong đợi:** 
  * Bài test **PASSED** về mặt kỹ thuật của Selenium vì phần tử có sẵn trong DOM nên không báo lỗi tìm kiếm, nhưng giá trị text lấy ra bị rỗng (`""`) do phần tử chưa hiển thị. Kết quả Assert sẽ FAILED nếu kiểm tra nội dung text.

### Test Case 1.2: Kiểm thử sử dụng lệnh chờ tường minh (Explicit Wait)
* **Mục đích:** Đảm bảo bài test chạy ổn định và lấy đúng dữ liệu khi áp dụng cơ chế chờ phù hợp.
* **Các bước thực hiện:**
  1. Mở trình duyệt Chrome.
  2. Truy cập vào đường dẫn trang Example 1.
  3. Tìm và Click vào nút **"Start"**.
  4. Sử dụng lệnh chờ tường minh (`WebDriverWait`), thiết lập thời gian chờ tối đa 10 giây cho đến khi phần tử dòng chữ kết quả (`#finish h4`) đạt trạng thái hiển thị rõ ràng trên màn hình (`visibility_of_element_located`).
  5. Kiểm tra văn bản của phần tử xem có khớp với chuỗi `"Hello World!"` hay không.
  6. Đóng trình duyệt.
* **Kết quả mong đợi:** 
  * Bài test **PASSED**. Trình duyệt chờ thanh loading biến mất, dòng chữ `"Hello World!"` hiển thị và được lấy ra chính xác.

---

## 2. Kịch bản kiểm thử cho trang Example 2 (Element rendered after the fact)
* **URL mục tiêu:** `https://the-internet.herokuapp.com/dynamic_loading/2`
* **Đặc điểm trang:** Phần tử kết quả hoàn toàn chưa tồn tại trong mã nguồn. Khi bấm nút Start, JavaScript mới bắt đầu khởi tạo, nạp phần tử vào HTML và hiển thị lên giao diện.

### Test Case 2.1: Kiểm thử không sử dụng lệnh chờ (No Wait)
* **Mục đích:** Thí nghiệm quan sát lỗi hệ thống khi Selenium cố tình tìm một phần tử chưa được sinh ra trong mã nguồn.
* **Các bước thực hiện:**
  1. Mở trình duyệt Chrome.
  2. Truy cập vào đường dẫn trang Example 2.
  3. Tìm và Click vào nút **"Start"**.
  4. Ngay lập tức yêu cầu Selenium tìm phần tử dòng chữ kết quả (`#finish h4`).
  5. Đóng trình duyệt.
* **Kết quả mong đợi:** 
  * Bài test **FAILED**. Hệ thống ném ra lỗi `NoSuchElementException` do tại thời điểm tìm kiếm, phần tử kết quả chưa hề được tạo ra trong cây thư mục DOM của trang web.

### Test Case 2.2: Kiểm thử sử dụng lệnh chờ tường minh (Explicit Wait)
* **Mục đích:** Ứng dụng lệnh chờ để đồng bộ hóa tốc độ xử lý của mã kiểm thử với tốc độ sinh phần tử của JavaScript.
* **Các bước thực hiện:**
  1. Mở trình duyệt Chrome.
  2. Truy cập vào đường dẫn trang Example 2.
  3. Tìm và Click vào nút **"Start"**.
  4. Sử dụng lệnh chờ tường minh (`WebDriverWait`), thiết lập thời gian chờ tối đa 10 giây cho đến khi phần tử kết quả (`#finish h4`) xuất hiện trong DOM và hiển thị hoàn toàn trên giao diện (`visibility_of_element_located`).
  5. Kiểm tra khẳng định (Assert) nội dung văn bản của phần tử phải là `"Hello World!"`.
  6. Đóng trình duyệt.
* **Kết quả mong đợi:** 
  * Bài test **PASSED**. Hệ thống tự động đợi vài giây cho đến khi JavaScript tạo xong phần tử rồi mới thực hiện kiểm tra, đảm bảo kịch bản chạy mượt mà, ổn định.
