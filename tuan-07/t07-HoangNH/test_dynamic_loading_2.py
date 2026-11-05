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

# Test case minh họa lỗi nếu không dùng Explicit Wait (đã comment để lưu ý)
# def test_failed_rendered_element(driver):
#     driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
#     driver.find_element(By.TAG_NAME, "button").click()
#     # Lỗi NoSuchElementException do phần tử chưa được render vào DOM ngay lập tức
#     element = driver.find_element(By.CSS_SELECTOR, "#finish h4")
#     assert element.text == "Hello World!"

def test_rendered_element_after(driver):
    """Kiểm tra xử lý phần tử được render động (Rendered Element) ở Dynamic Loading trang 2"""
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    # 1. Tìm và bấm nút Start
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    
    # 2. Sử dụng Explicit Wait chờ phần tử xuất hiện sau khi render động
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    
    # 3. Kiểm tra kết quả
    assert element.text == "Hello World!"