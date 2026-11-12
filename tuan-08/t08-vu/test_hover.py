from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/hovers")
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def auto_back_to_hovers(driver):
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
    figures = driver.find_elements(By.CSS_SELECTOR, ".figure")
    ActionChains(driver).move_to_element(figures[index]).perform()
    driver.find_element(By.CSS_SELECTOR, f"a[href*='{expected_url}']").click()

    assert expected_url in driver.current_url