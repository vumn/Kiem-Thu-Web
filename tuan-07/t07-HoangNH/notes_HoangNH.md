# Ghi chú Tuần 7: Cơ chế Chờ (Waits) trong Selenium

## 1. Phân biệt Chờ ngầm định và Chờ tường minh

- **Chờ ngầm định (Implicit Wait):**
  - Selenium sẽ chờ tối đa một khoảng thời gian định sẵn khi tìm kiếm phần tử nếu chưa thấy ngay lập tức.
  - Áp dụng phạm vi toàn cục cho toàn bộ các thao tác tìm kiếm phần tử (`find_element`) trong suốt phiên làm việc của driver.
- **Chờ tường minh (Explicit Wait):**
  - Selenium chờ cho đến khi một **điều kiện cụ thể** thỏa mãn trước khi thực thi dòng lệnh tiếp theo (ví dụ: `visibility_of_element_located` hoặc `element_to_be_clickable`).
  - Giúp kịch bản kiểm thử linh hoạt, tối ưu thời gian chờ và tránh các lỗi `TimeoutException` không đáng có.

## 2. Phân biệt các trạng thái của phần tử

- **Chờ phần tử hiển thị (Visible):** Phần tử đã tồn tại trong cấu trúc DOM của trang web và đang hiển thị trực quan trên giao diện người dùng (có chiều rộng, chiều cao lớn hơn 0).
- **Chờ phần tử bấm được (Clickable):** Phần tử không chỉ hiển thị mà trạng thái phải là `enabled` (cho phép tương tác), không bị vô hiệu hóa hoặc bị che khuất.
- **Ví dụ thực tế:** Một nút bấm "Submit" có thể đã tồn tại trên giao diện nhưng đang ở trạng thái mờ/vô hiệu hóa (`disabled`) cho đến khi người dùng điền đủ thông tin hợp lệ vào form.
