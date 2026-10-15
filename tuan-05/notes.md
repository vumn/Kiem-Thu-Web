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
