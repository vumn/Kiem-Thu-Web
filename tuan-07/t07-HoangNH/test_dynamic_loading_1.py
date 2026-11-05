import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    """Khởi tạo và dọn dẹp trình duyệt tự động cho mỗi test case"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hidden_element(driver):
    """Kiểm tra xử lý phần tử bị ẩn (Hidden Element) ở Dynamic Loading trang 1"""
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 1. Tìm và bấm nút Start
    start_button = driver.find_element(By.TAG_NAME, "button")
    start_button.click()
    
    # 2. Sử dụng Explicit Wait để chờ phần tử ẩn hiện ra
    hidden_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    
    # 3. Kiểm tra kết quả
    assert hidden_element.text == "Hello World!"