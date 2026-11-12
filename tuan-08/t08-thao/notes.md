# Ghi chú Học tập Tuần 08 

## 1. Trả lời Câu hỏi Đọc Tài liệu Tuần 8

### Q1: Vì sao nên tạo báo cáo dạng một file duy nhất (`--self-contained-html`) khi gửi cho người khác?
- **Tiện lợi & Không lỗi giao diện:** File duy nhất chứa sẵn toàn bộ mã CSS/JS/Hình ảnh bên trong. Khi gửi qua Email, Slack, Teams hoặc nộp bài, người nhận chỉ cần nhấp đúp để mở trên bất kỳ trình duyệt nào mà không bị lỗi đứt gãy giao diện hay thiếu file đính kèm đi kèm.

### Q2: (Team W3, W4) Đếm số phần tử trên trang bằng cách nào?
- Sử dụng phương thức `find_elements()` (trả về một danh sách các phần tử) kết hợp hàm `len()` trong Python:
  ```python
  elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
  count = len(elements)
  print("Số lượng phần tử là:", count)
