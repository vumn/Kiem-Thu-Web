# Ghi chú Tuần 8: Xử lý Báo cáo, Dropdown, Upload File và Tương tác Nâng cao (Hover, Slider)

## 1. Vì sao nên tạo báo cáo dạng một file duy nhất (`self-contained report`) khi gửi cho người khác?

- **Tránh mất định dạng:** Khi gửi file báo cáo `.html` qua email, chat hoặc ticket, nếu thiếu thư mục `assets` (CSS, JS, hình ảnh), người nhận mở lên sẽ bị lỗi giao diện hoặc mất định dạng.
- **Tiện lợi khi chia sẻ:** Báo cáo dạng một file duy nhất nhúng toàn bộ mã nguồn, kiểu dáng CSS và dữ liệu vào bên trong, giúp người nhận mở lên xem được ngay lập tức, gọn gàng và hiển thị nguyên vẹn.

## 2. Phân biệt `select_by_visible_text` và `select_by_value` trong Dropdown

- **`select_by_visible_text` (Chọn theo chữ hiển thị):**
  - Chọn dựa trên nội dung văn bản hiển thị trực quan trên giao diện.
  - _Ứng dụng:_ Khi kiểm thử từ góc nhìn người dùng cuối hoặc khi các giá trị `value` được sinh tự động ngầm bên dưới khó đọc.
- **`select_by_value` (Chọn theo giá trị thuộc tính):**
  - Chọn dựa trên giá trị của thuộc tính `value="..."` bên trong thẻ `<option>`.
  - _Ứng dụng:_ Khi cần chọn chính xác theo mã định danh (ID/Code) trong hệ thống cơ sở dữ liệu hoặc khi văn bản hiển thị có thể thay đổi ngôn ngữ nhưng `value` được giữ nguyên cố định.

## 3. Vì sao tải file (Upload) bằng cách gõ đường dẫn vào ô chọn file?

- Thư viện Selenium không thể trực tiếp thao tác với hộp thoại chọn file gốc của hệ điều hành (Native OS File Dialog).
- Do đó, nếu phần tử trên trang web là một thẻ `<input type="file">`, ta chỉ cần sử dụng phương thức `send_keys()` truyền vào **đường dẫn tuyệt đối** của file để hệ thống tự động nhận diện và tải lên.

## 4. Cách đếm số lượng phần tử xuất hiện trên trang web

- Sử dụng phương thức `driver.find_elements()` (có chữ **s** ở cuối): Trả về một danh sách (`list`) chứa tất cả các `WebElement` khớp với điều kiện tìm kiếm.
- Sử dụng hàm tích hợp `len()` của Python để lấy độ dài của danh sách đó (ví dụ: `tong_so_phan_tu = len(elements)`).
