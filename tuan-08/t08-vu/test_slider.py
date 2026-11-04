from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/horizontal_slider")
    yield browser
    browser.quit()
@pytest.fixture(autouse=True)
def reset_slider(driver):
    driver.refresh()

def test_slider__default_values(driver):  
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    assert (
        slider.get_attribute("min"), 
        slider.get_attribute("max"),
        slider.get_attribute("step"),
        slider.get_attribute("value")
    ) == ('0.0', '5.0', '0.5', '0')

def test_slider_keyboard_interactions(driver):
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    value = driver.find_element(By.CSS_SELECTOR, "span[id='range']")
    action = ActionChains(driver)
    action.click(slider).perform()
    assert value.text == "2.5"
    action.send_keys(Keys.ARROW_UP).perform()
    assert value.text == "3"
    action.send_keys(Keys.ARROW_RIGHT).perform()
    assert value.text == "3.5"
    action.send_keys(Keys.ARROW_DOWN).perform()
    assert value.text == "3"
    action.send_keys(Keys.ARROW_LEFT).perform()
    assert value.text == "2.5"

def test_slider_mouse_interaction(driver):
    slider  = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    value = driver.find_element(By.CSS_SELECTOR, "span[id='range']")

    left_edge = -(slider.size["width"]/2)
    action = ActionChains(driver)
    action.move_to_element_with_offset(
        slider, left_edge, 0
    ).click().perform()
    assert value.text == '0'

    step_forward = slider.size["width"]/10
    step_backward = -step_forward
    print(step_backward)

    action.drag_and_drop_by_offset(
        slider, step_forward, 0
    ).perform()
    assert value.text == '3'
    action.drag_and_drop_by_offset(
        slider, step_backward, 0
    ).perform()
    assert value.text == '2'