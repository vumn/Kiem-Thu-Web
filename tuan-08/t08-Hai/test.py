from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_hover():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/hovers")

    # Tìm tất cả các phần tử hình ảnh
    images = driver.find_elements(By.CLASS_NAME, "figure")
    
    for i in images:
        actions = ActionChains(driver)
        # Di chuột qua từng hình ảnh
        actions.move_to_element(i).perform()
        sleep(2)  # Thêm thời gian chờ để quan sát kết quả
        
        # Kiểm tra xem thông tin xuất hiện khi hover
        caption = i.find_element(By.CLASS_NAME, "figcaption")
        assert caption.is_displayed()
    
    driver.quit()

def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    source_element = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    target_element = driver.find_element(By.ID, "range")
    #khởi tạo đối tượng ActionChains thực thi các hành động
    actions = ActionChains(driver)
    #thực hiện kéo và thả thanh trượt
    actions.drag_and_drop(source_element, target_element).perform()
    # Thêm thời gian chờ để quan sát kết quả
    sleep(2) 
    # Kiểm tra giá trị của thanh trượt sau khi kéo và thả
    assert target_element.text == "5"
    
    driver.quit()

def test_click_and_hold():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    source_element = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    target_element = driver.find_element(By.ID, "range")
    
    # Khởi tạo đối tượng ActionChains thực thi các hành động
    actions = ActionChains(driver)
    # Thực hiện kéo và thả bằng cách click và giữ
    actions.click_and_hold(source_element).move_by_offset(129, 0).release().perform()
    
    # Thêm thời gian chờ để quan sát kết quả
    sleep(2) 
    
    # Kiểm tra vị trí của các cột sau khi kéo và thả
    assert target_element.text == "5"
    
    driver.quit()
    
def test_click_and_hold_with_offset():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    source_element = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    target_element = driver.find_element(By.ID, "range")
    
    # Khởi tạo đối tượng ActionChains thực thi các hành động
    actions = ActionChains(driver)
    # Thực hiện kéo và thả bằng cách click và giữ với offset
    actions.click_and_hold(source_element).move_by_offset(129, 0).release().perform()
    
    # Thêm thời gian chờ để quan sát kết quả
    sleep(2) 
    
    # Kiểm tra vị trí của các cột sau khi kéo và thả
    assert target_element.text == "5"
    
    driver.quit()
    
def test_keyboard_interaction():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    source_element = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    target_element = driver.find_element(By.ID, "range")
    
    # Khởi tạo đối tượng ActionChains thực thi các hành động
    actions = ActionChains(driver)
    actions.click(source_element).perform()
    sleep(1)
    assert target_element.text == "2.5"
    # Thực hiện các thao tác bàn phím để thay đổi giá trị thanh trượt
    actions.send_keys(Keys.ARROW_UP).perform()
    assert target_element.text == "3"
    sleep(1) 
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    assert target_element.text == "3.5"
    sleep(1) 
    actions.send_keys(Keys.ARROW_DOWN).perform()
    assert target_element.text == "3"
    sleep(1) 
    actions.send_keys(Keys.ARROW_LEFT).perform()
    assert target_element.text == "2.5"
    sleep(1)
    actions.send_keys(Keys.HOME).perform()
    assert target_element.text == "0"
    sleep(1)

    driver.quit()

