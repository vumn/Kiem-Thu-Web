from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

# print("Tag:", username.tag_name)
# print("ID: ", username.get_attribute("id"))
# print("Name: ", username.get_attribute("name"))
# print("Displayed: ", username.is_displayed())

# print("Tag:", password.tag_name)
# print("ID: ", password.get_attribute("id"))
# print("Name: ", password.get_attribute("name"))
# print("Displayed: ", password.is_displayed())

# print("Tag:", submit_button.tag_name)
# print("ID: ", submit_button.get_attribute("id"))
# print("Name: ", submit_button.get_attribute("name"))
# print("Displayed: ", submit_button.is_displayed())



# TC01: Nhập sai username -> đăng nhập thất bại
def test_login_failed_username():
    # tìm phần tử trên màn hình (ô đăng nhập, ô mật khẩu, nút bấm)
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("randomUserName")
    password.send_keys("SuperSecretPassword!")
    submit_button.click()

    failed_username = driver.find_element(By.ID, value="flash")
    assert failed_username.text =="Your username is invalid!\n×"

# TC02: Nhập sai password -> đăng nhập thất bại
def test_login_failed_password():
    # tìm phần tử trên màn hình (ô đăng nhập, ô mật khẩu, nút bấm)
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("tomsmith")
    password.send_keys("wrongPassword")
    submit_button.click()
    
    failed_password = driver.find_element(By.ID, value="flash")
    assert failed_password.text =="Your password is invalid!\n×"

# TC03: Login thành công
def test_login_success():
    # tìm phần tử trên màn hình (ô đăng nhập, ô mật khẩu, nút bấm)
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    submit_button.click()
    # đợi 10s cho đến khi url là /secure
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://the-internet.herokuapp.com/secure") 
    )
    # kiểm tra phần thông báo đã đăng nhập thành công
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "flash")
        )
    )
    assert success.is_displayed()


