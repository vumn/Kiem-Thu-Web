# Kịch bản Kiểm thử - Chức năng 2: Tìm kiếm sản phẩm

## Test Case 1: Tìm kiếm sản phẩm hợp lệ (TC_SEARCH_01)
- **Mục đích:** Đảm bảo tìm thấy sản phẩm khi nhập đúng từ khóa.
- **Các bước:**
  1. Truy cập trang web.
  2. Nhập từ khóa "MacBook" vào ô tìm kiếm.
  3. Bấm nút Tìm kiếm (hoặc nhấn ENTER).
- **Kết quả kỳ vọng:** Danh sách kết quả hiển thị ít nhất 1 sản phẩm có chứa chữ "MacBook".

## Test Case 2: Tìm kiếm với từ khóa không tồn tại (Trường hợp sai/biên - TC_SEARCH_02)
- **Mục đích:** Đảm bảo hệ thống hiển thị thông báo phù hợp khi không tìm thấy kết quả.
- **Các bước:**
  1. Truy cập trang web.
  2. Nhập từ khóa "xyz123invalid" vào ô tìm kiếm.
  3. Bấm nút Tìm kiếm.
- **Kết quả kỳ vọng:** Hiển thị thông báo "Không tìm thấy sản phẩm phù hợp".
