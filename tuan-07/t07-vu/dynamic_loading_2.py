from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

# def test_failed_rendered_element_after():
#     driver.find_element(By.TAG_NAME, "button").click()
#     element = driver.find_element((By.CSS_SELECTOR, "#finish h4"))
#     assert element.text == "Hello World!"


def test_renderd_element_after():
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    assert element.text == "Hello World!"
    driver.quit()

if __name__ == "__main__":
    test_renderd_element_after()