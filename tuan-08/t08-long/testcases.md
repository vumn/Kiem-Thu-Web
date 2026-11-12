# KỊCH BẢN KIỂM THỬ

## Chức năng 1: Di chuột
### Test Case 1: Xác minh hiển thị thông tin khi di chuột vào ảnh đại diện
* **Mục tiêu:** Đảm bảo hệ thống hiển thị đúng thông tin ẩn khi người dùng rê chuột qua đối tượng.
* **Đường dẫn kiểm thử:** `/hovers`
* **Các bước thực hiện:**
  1. Truy cập vào URL của trang kiểm thử `/hovers`.
  2. Xác định phần tử ảnh đại diện của User 1.
  3. Thực hiện hành động di chuột vào ảnh đại diện của User 1 bằng `move_to_element`.
  4. Kiểm tra sự xuất hiện của hộp thông tin phía dưới ảnh.
* **Kết quả mong đợi:**
  * Hộp thông tin của User 1 hiển thị thành công trên giao diện (`is_displayed()` trả về giá trị True).
  * Văn bản hiển thị chính xác tên người dùng (ví dụ: `"name: user1"`).
  * Đường dẫn `"view profile"` xuất hiện và có thể nhấp vào được.

---

## Chức năng 2: Thanh trượt
### Test Case 2: Kéo thanh trượt bằng hành động chuột
* **Mục tiêu:** Xác minh người dùng có thể dùng chuột kéo thanh trượt để thay đổi giá trị số.
* **Đường dẫn kiểm thử:** `/horizontal_slider`
* **Các bước thực hiện:**
  1. Truy cập vào URL của trang kiểm thử `/horizontal_slider`.
  2. Xác định vị trí của thanh trượt và thẻ hiển thị giá trị số bên cạnh.
  3. Sử dụng hành động kéo thả `drag_and_drop_by_offset` để dịch chuyển thanh trượt sang phải một khoảng tọa độ.
  4. Đọc giá trị số hiển thị mới trên màn hình.
* **Kết quả mong đợi:**
  * Thanh trượt di chuyển mượt mà về phía bên phải.
  * Giá trị số bên cạnh cập nhật tăng lên tương ứng với khoảng cách kéo.

### Test Case 3: Điều khiển thanh trượt bằng bàn phím
* **Mục tiêu:** Xác minh thanh trượt hoạt động chính xác khi tương tác bằng các phím mũi tên.
* **Đường dẫn kiểm thử:** `/horizontal_slider`
* **Các bước thực hiện:**
  1. Truy cập vào URL của trang kiểm thử `/horizontal_slider`.
  2. Click chuột vào thanh trượt để kích hoạt trạng thái tập trung.
  3. Gửi phím `Keys.HOME` để đưa thanh trượt chắc chắn về vị trí ban đầu.
  4. Gửi liên tiếp 3 lần phím `Keys.ARROW_RIGHT` để tăng giá trị.
* **Kết quả mong đợi:**
  * Mỗi lần gửi phím mũi tên phải, thanh trượt dịch chuyển sang phải đúng 1 nấc cố định.
  * Giá trị số hiển thị cập nhật chính xác theo từng nấc.