import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    """Khởi tạo trình duyệt cho nhóm test Hovers"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://the-internet.herokuapp.com/hovers")
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def auto_back_to_hovers(driver):
    """Tự động quay lại trang hovers nếu URL bị thay đổi sau mỗi test"""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".figure"))
    )
    yield
    if not driver.current_url.endswith("/hovers"):
        driver.back()

@pytest.mark.parametrize(
    "index, expected_url", [(0, "/users/1"), (1, "/users/2"), (2, "/users/3")]
)
def test_hover_users(driver, index, expected_url):
    """Kiểm tra hành vi rê chuột (Hover) và điều hướng đúng profile người dùng"""
    figures = driver.find_elements(By.CSS_SELECTOR, ".figure")
    
    # Thực hiện rê chuột vào hình ảnh tại vị trí index
    ActionChains(driver).move_to_element(figures[index]).perform()
    
    # Click vào link xem chi tiết profile tương ứng
    driver.find_element(By.CSS_SELECTOR, f"a[href*='{expected_url}']").click()

    # Kiểm tra URL đích
    assert expected_url in driver.current_url