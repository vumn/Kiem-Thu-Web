import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver():
    """Fixture khởi tạo trình duyệt Chrome trước khi chạy test và đóng sau khi hoàn thành."""
    options = webdriver.ChromeOptions() # Khởi tạo WebDriver
    # options.add_argument("--headless") # Bỏ comment nếu muốn chạy ngầm không bật giao diện
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestW1Interactions:
    
    # TEST CASE 1: Kiểm thử chức năng Di chuột tại trang /hovers
    def test_hover_user_profile(self, driver):
        # 1. Truy cập vào trang demo hovers
        driver.get("https://the-internet.herokuapp.com/hovers")
        
        # 2. Tìm phần tử ảnh đại diện của User thứ nhất (chỉ mục 0 trong danh sách)
        avatars = driver.find_elements(By.CSS_SELECTOR, ".figure img")
        assert len(avatars) > 0, "Không tìm thấy ảnh đại diện nào trên trang!"
        user1_avatar = avatars[0]
        
        # 3. Sử dụng ActionChains để thực hiện di chuột vào ảnh đại diện
        actions = ActionChains(driver)
        actions.move_to_element(user1_avatar).perform()
        
        # 4. Tìm và kiểm tra thông tin chi tiết hiển thị dưới ảnh đại diện của User 1
        user1_details = driver.find_element(By.CSS_SELECTOR, ".figcaption")
        
        # Kiểm tra hộp thông tin có hiển thị hay không
        assert user1_details.is_displayed(), "Hộp thông tin không hiển thị khi hover chuột!"
        
        # Kiểm tra văn bản hiển thị tên người dùng chính xác
        user_name_text = user1_details.find_element(By.TAG_NAME, "h5").text
        assert user_name_text == "name: user1", f"Tên người dùng sai! Kỳ vọng 'name: user1' nhưng nhận '{user_name_text}'"
        
        # Kiểm tra liên kết 'view profile' có tồn tại
        profile_link = user1_details.find_element(By.TAG_NAME, "a")
        assert profile_link.is_displayed(), "Đường dẫn 'view profile' không hiển thị!"

    # TEST CASE 2: Kiểm thử chức năng Kéo thanh trượt bằng chuột
    def test_slider_drag_with_mouse(self, driver):
        # 1. Truy cập vào trang demo horizontal_slider
        driver.get("https://the-internet.herokuapp.com/horizontal_slider")
        
        # 2. Xác định vị trí thanh trượt và vùng text hiển thị giá trị số số bên cạnh
        slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer input")
        value_text = driver.find_element(By.ID, "range")
        
        # Đảm bảo giá trị ban đầu là 0
        assert value_text.text == "0", "Giá trị ban đầu của thanh trượt không phải là 0!"
        
        # 3. Sử dụng drag_and_drop_by_offset để kéo thanh trượt sang phải
        # Lưu ý: Trục X dương kéo sang phải, giá trị offset tùy thuộc độ rộng màn hình thực tế.
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(slider, 30, 0).perform()
        
        # 4. Đọc giá trị mới hiển thị trên màn hình
        updated_value = value_text.text
        
        # Xác minh thanh trượt đã thay đổi trạng thái dịch chuyển và giá trị lớn hơn 0
        assert float(updated_value) > 0, f"Thanh trượt không di chuyển bằng chuột! Giá trị vẫn là {updated_value}"

    # TEST CASE 3: Kiểm thử điều khiển thanh trượt bằng Bàn phím (Phối hợp với Keys)
    def test_slider_control_with_keyboard(self, driver):
        # 1. Tải lại trang để reset trạng thái thanh trượt về mặc định
        driver.get("https://the-internet.herokuapp.com/horizontal_slider")
        
        slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer input")
        value_text = driver.find_element(By.ID, "range")
        
        # 2. Click chuột vào thanh trượt để đưa phần tử vào trạng thái kích hoạt
        slider.click()
        
        # 3. Gửi phím Keys.HOME để chắc chắn thanh trượt đưa về vạch 0 ban đầu
        slider.send_keys(Keys.HOME)
        assert value_text.text == "0", "Thanh trượt không về mức 0 sau khi nhấn phím HOME!"
        
        # 4. Gửi liên tiếp 3 lần phím mũi tên phải (Keys.ARROW_RIGHT) để tăng giá trị số
        # Mỗi lần ấn ARROW_RIGHT trên trang demo này tăng 0.5 đơn vị
        for _ in range(3):
            slider.send_keys(Keys.ARROW_RIGHT)
            
        # 5. Xác minh giá trị text hiển thị cập nhật chính xác
        final_value = value_text.text
        assert final_value == "1.5", f"Thanh trượt điều khiển phím sai! Kỳ vọng '1.5' nhưng nhận '{final_value}'"
