## Kiến thức học được

# 1. Wait

- Implicit Wait: Chờ ngầm định khi tìm kiếm phần tử, Implicit Wait thuộc về vòng đời của driver
- Driver có Implicit Wait mặc định là 0 giây.
- Explicit Wait: Chờ một điều kiện cụ thể
- WebDriverWait: Thiết lập thời gian chờ tối đa
- until(): Chờ đến khi điều kiện thỏa mãn

# 2.Sự khác nhau giữa các Expected Conditions

- presence_of_element_located: Chờ và lấy phần tử tồn tại trong DOM
- visibility_of_element_located: Chờ và lấy phần tử tồn tại và hiển thị
- invisibility_of_element_located: Chờ và lấy phần tử biến mất hoặc bị ẩn

# 3.Pytest.raise()

- Kiểm tra ngoại lệ có xảy ra đúng dự kiến hay không
- một số ngoại lệ phổ biến: TimeoutException, NoSuchElementException, NoSuchDriverException, NoAlertPresentException...
