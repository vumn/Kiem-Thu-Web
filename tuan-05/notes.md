### Nguyễn Minh Vũ
1. Với ô tên đăng nhập ở /login, nên xác định bằng id, vì id là độc nhất trên trang, đồng thời nó cũng đơn giản và ngắn gọn hơn XPath hay CSS Selector.
2. Muốn nhập chữ vào một ô thì dùng phương thức send_keys()
3. Để biết id của một ô trên trang: chọn F12 để mở DevTools, chọn vào nút ![alt text](image.png) hoặc bấm phím tắt Ctrl Shift C, sau đó nhấn vào phần tử mình muốn xem, id sẽ hiện lên ![alt text](image-1.png).
4. Nếu kết quả thực tế khác với mong đợi, pytest sẽ báo AssertionError.