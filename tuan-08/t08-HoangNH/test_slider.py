import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def driver():
    """Khởi tạo trình duyệt cho nhóm test Horizontal Slider"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://the-internet.herokuapp.com/horizontal_slider")
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def reset_slider(driver):
    """Làm mới trang để đưa slider về trạng thái ban đầu trước mỗi test"""
    driver.refresh()

def test_slider_default_values(driver):  
    """Kiểm tra các thuộc tính mặc định của thanh trượt"""
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    assert (
        slider.get_attribute("min"), 
        slider.get_attribute("max"),
        slider.get_attribute("step"),
        slider.get_attribute("value")
    ) == ('0.0', '5.0', '0.5', '0')

def test_slider_keyboard_interactions(driver):
    """Kiểm tra tương tác tăng giảm giá trị thanh trượt bằng bàn phím"""
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    value_label = driver.find_element(By.CSS_SELECTOR, "span[id='range']")
    
    action = ActionChains(driver)
    action.click(slider).perform()
    assert value_label.text == "2.5"
    
    action.send_keys(Keys.ARROW_UP).perform()
    assert value_label.text == "3"
    
    action.send_keys(Keys.ARROW_RIGHT).perform()
    assert value_label.text == "3.5"
    
    action.send_keys(Keys.ARROW_DOWN).perform()
    assert value_label.text == "3"
    
    action.send_keys(Keys.ARROW_LEFT).perform()
    assert value_label.text == "2.5"

def test_slider_mouse_interaction(driver):
    """Kiểm tra tương tác kéo thả thanh trượt bằng chuột"""
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    value_label = driver.find_element(By.CSS_SELECTOR, "span[id='range']")

    left_edge = -(slider.size["width"] / 2)
    action = ActionChains(driver)
    
    # Click vào rìa trái để đưa về giá trị 0
    action.move_to_element_with_offset(slider, left_edge, 0).click().perform()
    assert value_label.text == '0'

    step_forward = slider.size["width"] / 10
    step_backward = -step_forward

    # Kéo tiến lên để tăng giá trị
    action.drag_and_drop_by_offset(slider, step_forward, 0).perform()
    assert value_label.text == '3'
    
    # Kéo lùi về để giảm giá trị
    action.drag_and_drop_by_offset(slider, step_backward, 0).perform()
    assert value_label.text == '2'