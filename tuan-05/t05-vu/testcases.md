### TC01: Nhập sai username, đúng password.
1. Bước 1: tìm phần tử trên màn hình (ô đăng nhập, mật khẩu và nút bấm)
- Tìm phần tử input có name="username" bằng find_element()
- Tìm phần tử input có id="password" bằng find_element()
- Tìm phần tử button có class="radius" bằng find_element()
- Sử dụng phương thức sendkeys() để nhập username và password
- Sử dụng phương thức click() để thao tác bấm nút
2. Kiểm tra
- Khi nhập sai username, góc trên sẽ có 1 div có id="flash" và text="Your username is invalid!\n×". Chỉ cần kiểm tra nếu div đó tồn tại.
### TC01: Nhập đúng username, sai password.
1. Bước 1: Như trên
2. Bước 2: Khi nhập sai password, góc trên sẽ có 1 div có id="flash" và text="Your password is invalid!\n×". Chỉ cần kiểm tra nếu div đó tồn tại.
### TC01: Nhập đúng username và password.
1. Bước 1: Như trên
2. Bước 2: Sử dụng WebDriverWait để đợi cho trang web chuyển hướng, kiểm tra url có đang là https://the-internet.herokuapp.com/secure và kiểm tra phần tử div id="flash" có đang hiện lên không.