from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

def test_hidden_element():
    start_button = driver.find_element(By.TAG_NAME, "button")
    start_button.click()
    hidden_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert hidden_element.text == "Hello World!"
    driver.quit()

if __name__ == "__main__":
    test_hidden_element()
