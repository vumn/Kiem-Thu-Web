# Nguyễn Minh Vũ

1. Với ô tên đăng nhập ở /login, nên xác định bằng id, vì id là độc nhất trên trang, đồng thời nó cũng đơn giản và ngắn gọn hơn XPath hay CSS Selector.
2. Muốn nhập chữ vào một ô thì dùng phương thức send_keys()
3. Để biết id của một ô trên trang: chọn F12 để mở DevTools, chọn vào nút ![alt text](image.png) hoặc bấm phím tắt Ctrl Shift C, sau đó nhấn vào phần tử mình muốn xem, id sẽ hiện lên ![alt text](image-1.png).
4. Nếu kết quả thực tế khác với mong đợi, pytest sẽ báo AssertionError.

# Ngô Huy Hoàng

## I. Kiến Thức Trọng Tâm

1. **Xác định phần tử (Locator):** Ở màn Login, với trường tên đăng nhập, nên ưu tiên xác định bằng `id`. `id` là độc nhất, đơn giản và tối ưu hơn so với XPath hay CSS selector.
2. **Nhập dữ liệu:** Nhập chữ/chuỗi vào một ô input > dùng phương thức `send_keys("nội dung")`.
3. **Đánh giá kết quả (Assertion):** Nếu kết quả thực tế khác với kết quả mong đợi, pytest sẽ báo lỗi `AssertionError`.

---

## II. Hướng Dẫn Tìm ID Của Phần Tử Trên Trang Web

### 1. Mở công cụ Inspect (Kiểm tra phần tử)

- **Cách 1:** Nhấp chuột phải trực tiếp vào ô input / nút bấm cần kiểm tra > Chọn **Inspect** (hoặc **Kiểm tra**).
- **Cách 2:** Sử dụng phím tắt:
  - **macOS:** `Cmd + Option + C` (bật chế độ trỏ chuột chọn phần tử) hoặc `Cmd + Option + I` (mở DevTools).
  - **Windows:** `Ctrl + Shift + C` hoặc `F12`.

### 2. Lấy giá trị ID trong mã HTML
Trong tab **Elements**, dòng mã tương ứng sẽ được tô sáng. Tìm thuộc tính `id="..."`:

```html
<!-- Ví dụ: ô input nhập username -->
<input type="text" id="user-name" name="user-name" placeholder="Username" />
```

# Nguyễn Nhân Thành Long

1. Sử dụng ID để định vị ô đăng nhập: Tại giao diện /login, việc dùng thuộc tính id cho ô tên đăng nhập là tối ưu nhất. Vì mỗi id trên trang là độc nhất, cách này vừa đơn giản, ngắn gọn lại hiệu quả hơn nhiều so với việc dùng XPath hay CSS Selector.
2. Nhập dữ liệu vào ô trống: có thể sử dụng phương thức send_keys() khi muốn điền ký tự hoặc văn bản vào một ô nhập liệu bất kỳ.
3. Cách tìm ID của phần tử trên trang: Đầu tiên, nhấn phím F12 để mở bộ công cụ DevTools. Tiếp theo, click vào biểu tượng mũi tên chọn phần tử hoặc bấm tổ hợp phím Ctrl + Shift + C rồi trỏ thẳng vào ô cần kiểm tra; thuộc tính id của ô đó sẽ hiển thị chi tiết trong mã nguồn.
4. Cơ chế báo lỗi của Pytest: Trong quá trình chạy kiểm thử, nếu kết quả thực tế thu được không trùng khớp với kết quả kỳ vọng, hệ thống pytest sẽ ngay lập tức trả về lỗi AssertionError.

# Nguyễn Đức Hải

1. Với ô tên đăng nhập ở trang /login, nên xác định bằng id, vì id là độc nhất trên trang.
2. Dùng send_keys() để nhập chữ vào ô nhập liệu
3. Để biết id của 1 ô nhập trên trang :
   - Nhấn F12 trên bàn phím -> chọn tab Elements
   - Nhấn tổ hợp phím Ctrl + Shift + C rồi chọn ô nhập muốn lấy id
     -> Trang Elements bôi xanh dòng chứa thông tin ô nhập
4. Nếu kết quả thực tế khác kết quả mong đợi, pytest báo FAILED với lỗi AssertionError.
## Hỏi AI

1. Cách kiểm chuyển element thành String và check bàng in
2. Luôn có time_sleep() để trang web có thể load sau khi thao tác với các element
