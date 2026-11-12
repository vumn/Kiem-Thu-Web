# Kịch bản Kiểm thử - Chức năng 3: Thêm vào giỏ hàng

## Test Case 1: Thêm sản phẩm thành công (TC_CART_01)
- **Mục đích:** Đảm bảo khi bấm "Thêm vào giỏ", sản phẩm xuất hiện trong giỏ hàng.
- **Các bước:**
  1. Truy cập trang chi tiết sản phẩm.
  2. Nhấn nút "Thêm vào giỏ hàng".
  3. Truy cập trang Giỏ hàng.
- **Kết quả kỳ vọng:** Số lượng sản phẩm tăng lên 1 và hiển thị đúng tên sản phẩm.

## Test Case 2: Thêm số lượng sản phẩm không hợp lệ (Trường hợp sai - TC_CART_02)
- **Mục đích:** Đảm bảo không cho phép nhập số lượng <= 0.
- **Các bước:**
  1. Nhập số lượng là `0` hoặc `-1` vào ô số lượng.
  2. Bấm nút "Thêm vào giỏ hàng".
- **Kết quả kỳ vọng:** Hiển thị thông báo lỗi "Số lượng phải lớn hơn 0".
