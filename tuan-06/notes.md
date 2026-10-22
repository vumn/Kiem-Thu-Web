## PHẦN I: TRẢ LỜI CÂU HỎI ĐỌC TÀI LIỆU TRƯỚC BUỔI HỌC

### Câu 1: WebDriver khác Selenium IDE và Selenium Grid ở đâu?

| Tiêu chí             | Selenium IDE                                                                     | Selenium WebDriver                                                                                   | Selenium Grid                                                                        |
| :------------------- | :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **Bản chất**         | Extension/Add-on trên trình duyệt (Record & Playback).                           | Bộ thư viện API lập trình điều khiển trình duyệt.                                                    | Hệ thống quản lý máy chủ phân tán (Server Hub/Nodes).                                |
| **Cách sử dụng**     | Bấm ghi thao tác chuột/phím và phát lại kịch bản, xuất script cơ bản.            | Viết mã nguồn bằng ngôn ngữ lập trình (Python, Java, C#, JS) kết hợp test runner (pytest, unittest). | Cấu hình mạng lưới gồm 1 Hub quản lý nhiều Node (máy ảo, container Docker).          |
| **Ưu điểm**          | Nhanh, dễ dùng, không cần kiến thức lập trình chuyên sâu.                        | Linh hoạt tối đa, xử lý logic phức tạp, vòng lặp, điều kiện, kết nối database/API.                   | Chạy song song hàng loạt test case cùng lúc, giảm thiểu tổng thời gian chạy hồi quy. |
| **Hạn chế**          | Khó bảo trì, kịch bản dễ hỏng khi giao diện thay đổi, không chạy được logic lớn. | Cần cài đặt driver, thiết lập môi trường và kỹ năng lập trình tốt.                                   | Phức tạp trong khâu cấu hình hạ tầng mạng và tài nguyên máy chủ.                     |
| **Mục đích áp dụng** | Tạo nhanh kịch bản kiểm thử mẫu (POC), học tập làm quen.                         | **Dự án thực tế**, kiểm thử hồi quy tự động trong quy trình phát triển phần mềm.                     | Chạy kiểm thử đa nền tảng (Cross-browser, Cross-OS) trên hệ thống CI/CD quy mô lớn.  |

---

### Câu 2: Đường đi của một lệnh kiểm thử (Từ Code $\to$ Driver $\to$ Trình duyệt)

Luồng hoạt động tuân theo chuẩn hóa quốc tế **W3C WebDriver Standard**:

```text
[ Test Script (Python / unittest / pytest) ]
                     │
                     │  (1) Gửi lệnh qua HTTP Request (JSON Payload / W3C Protocol)
                     ▼
[ Browser Driver (chromedriver / geckodriver) ]
                     │
                     │  (2) Biên dịch sang lệnh Native Browser API / Chrome DevTools Protocol
                     ▼
[ Web Browser (Google Chrome / DOM Engine) ]
                     │
                     │  (3) Trình duyệt thực thi hành động trực tiếp trên trang web
                     ▼
[ Phản hồi kết quả: HTTP Response (Status Code, Data JSON, Error) về Test Script ]
```

#### Chi tiết 4 chặng của lệnh:

1. **Chặng 1 - Client (Test Script):** Khi chạy lệnh (ví dụ: `driver.find_element(By.ID, "username").send_keys("tomsmith")`), thư viện Selenium phía client đóng gói yêu cầu thành một HTTP POST Request có chứa dữ liệu định dạng JSON gửi đến cổng cục bộ (local port) mà Browser Driver đang lắng nghe.
2. **Chặng 2 - Trung gian (Browser Driver):** Driver (ví dụ: `chromedriver`) đóng vai trò như một HTTP Server. Nó tiếp nhận JSON payload từ client, phân tích cú pháp và chuyển đổi thành các tập lệnh nội bộ mà trình duyệt hiểu được.
3. **Chặng 3 - Thực thi (Web Browser):** Trình duyệt nhận lệnh trực tiếp từ driver thông qua cơ chế điều khiển native hoặc giao thức DevTools, thực hiện thao tác vật lý trên cây DOM (tìm thẻ HTML, đưa con trỏ vào ô nhập liệu, gõ từng ký tự).
4. **Chặng 4 - Phản hồi (Response Callback):** Trình duyệt trả kết quả về cho Driver. Driver đóng gói kết quả thành HTTP Response kèm mã HTTP 200 (nếu thành công) hoặc mã lỗi (ví dụ: `404 Not Found` tương ứng với ngoại lệ `NoSuchElementException`) ngược lại cho Test Script để thực hiện bước assert tiếp theo.

---

### Câu 3: Vì sao kiểm thử qua giao diện (UI Test) nên ít và có chọn lọc?

Dựa trên mô hình **Tháp kiểm thử (The Practical Test Pyramid)** của Martin Fowler:

1. **Tốc độ thực thi rất chậm (Slow Execution):**
   - Khởi động trình duyệt, tải tài nguyên HTML/CSS/JS, chờ hình ảnh và render giao diện tốn từ vài giây đến hàng chục giây cho mỗi kịch bản.
   - So sánh: Hàng nghìn Unit Test có thể chạy xong trong vài giây, nhưng 100 UI Test có thể mất hàng giờ.
2. **Độ ổn định kém, dễ báo lỗi giả (Flaky Tests):**
   - UI phụ thuộc nhiều vào yếu tố ngoại cảnh: tốc độ mạng giật lag, hiệu ứng hoạt họa (animation) chưa chạy xong, popup/banner xuất hiện bất ngờ.
   - Rất thường xuyên bài test báo thất bại dù mã nguồn logic của hệ thống không hề bị lỗi.
3. **Chi phí bảo trì rất tốn kém (High Maintenance Cost):**
   - Giao diện người dùng là phần thường xuyên thay đổi nhất trong vòng đời sản phẩm.
   - Một chỉnh sửa nhỏ về CSS class, đổi cấu trúc thẻ hoặc đổi ID có thể làm tê liệt hàng loạt kịch bản kiểm thử tự động, buộc kỹ sư QA phải tốn nhiều giờ sửa lại locator.
4. **Khó cô lập nguyên nhân gây lỗi (Difficult Debugging):**
   - Khi một UI test thất bại, rất khó xác định ngay nguyên nhân: do lỗi giao diện, do API backend chết, do dữ liệu database hay do mạng lag.
5. 👉 **Chiến lược đúng đắn:**
   - Đặt nền móng vững chắc ở chân tháp: Nhiều **Unit Test** và **API / Service Test**.
   - UI Test chỉ nằm ở đỉnh tháp, được áp dụng có chọn lọc cho các luồng nghiệp vụ sinh tử của người dùng cuối (Happy Path, Đăng nhập, Thanh toán, Đặt hàng).

---

## PHẦN II: TỔNG HỢP GÓP Ý SAU BUỔI BÁO CÁO & KẾ HOẠCH CẢI THIỆN
