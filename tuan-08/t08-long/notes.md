# GHI CHÚ LÝ THUYẾT

## 1. Phân biệt Dropdown List
Trong Selenium, để làm việc với thẻ `<select>`, ta sử dụng class `Select`. Hai phương thức lựa chọn có sự khác biệt rõ rệt:

| Tiêu chí | Chọn theo chữ hiển thị (`select_by_visible_text`) | Chọn theo giá trị (`select_by_value`) |
| :--- | :--- | :--- |
| **Bản chất** | Chọn option dựa trên **văn bản hiển thị trên màn hình** mà người dùng nhìn thấy. | Chọn option dựa trên **thuộc tính `value`** của thẻ `<option>` trong mã HTML. |
| **Ví dụ HTML** | `<option value="html_val">Màu Đỏ</option>` | `<option value="html_val">Màu Đỏ</option>` |
| **Cách gọi** | `select.select_by_visible_text("Màu Đỏ")` | `select.select_by_value("html_val")` |
| **Ưu điểm** | Trực quan, mô phỏng chính xác hành vi của người dùng thực tế. | Ổn định hơn nếu giao diện thay đổi đa ngôn ngữ nhưng code hệ thống giữ nguyên giá trị value. |

---

## 2. Ghi chú kỹ thuật về Di chuột & Thanh trượt
Để giả lập các hành động tương tác phức tạp của chuột và bàn phím, Selenium sử dụng class `ActionChains`.

### Quy trình thực hiện chung:
1. Khởi tạo đối tượng: `actions = ActionChains(driver)`
2. Gọi các chuỗi hành động nối tiếp nhau.
3. Bắt buộc kết thúc bằng `.perform()` để thực thi toàn bộ lệnh.

### Các hàm cốt lõi cần nhớ:
* **`move_to_element(element)`**: Di chuyển con trỏ chuột đến chính giữa phần tử.
* **`click_and_hold(element)`**: Nhấn và giữ chuột trái tại phần tử chỉ định.
* **`move_by_offset(x, y)`**: Di chuyển chuột một khoảng `x` (ngang) và `y` (dọc) so với vị trí hiện tại.
* **`release()`**: Thả chuột trái đang giữ.
* **`drag_and_drop_by_offset(element, x, y)`**: Kéo phần tử đi một khoảng trục X và Y.
* **`is_displayed()`**: Kiểm tra xem phần tử đã hiển thị trên màn hình hay chưa.
* **`Keys.HOME` / `Keys.ARROW_RIGHT`**: Các hằng số bàn phím phối hợp dùng lệnh `.send_keys()` để điều khiển thanh trượt chính xác từng nấc.
