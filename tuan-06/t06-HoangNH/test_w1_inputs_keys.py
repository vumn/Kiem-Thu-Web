import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestW1InputsAndKeypresses(unittest.TestCase):

    def setUp(self):
        """Khởi tạo trình duyệt trước mỗi bài test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        """Đóng trình duyệt sau khi test xong"""
        self.driver.quit()

    # --- KIỂM THỬ TRANG /inputs ---
    def test_tc01_input_number_and_clear(self):
        """TC01: Nhập dữ liệu dạng số, kiểm tra value và thực hiện clear()"""
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/inputs")

        # Thẻ input trên trang này nằm trong thẻ div.example
        input_element = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

        # 1. Nhập số '123'
        input_element.send_keys("123")
        current_value = input_element.get_attribute("value")
        self.assertEqual(current_value, "123", "Giá trị nhập vào chưa đúng!")

        # 2. Xóa dữ liệu bằng clear()
        input_element.clear()
        value_after_clear = input_element.get_attribute("value")
        self.assertEqual(value_after_clear, "", "Ô nhập chưa được xóa sạch!")

    def test_tc02_input_arrow_up(self):
        """TC02: Dùng phím Keys.ARROW_UP để tăng giá trị số"""
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/inputs")

        input_element = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        input_element.send_keys("5")
        
        # Nhấn phím mũi tên lên
        input_element.send_keys(Keys.ARROW_UP)
        updated_value = input_element.get_attribute("value")
        self.assertEqual(updated_value, "6", "Phím mũi tên lên không tăng giá trị số!")

    # --- KIỂM THỬ TRANG /key_presses ---
    def test_tc03_key_press_enter(self):
        """TC03: Kiểm tra bấm phím đặc biệt Keys.ENTER"""
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/key_presses")

        # Ô target có id="target"
        target_box = driver.find_element(By.ID, "target")
        target_box.send_keys(Keys.ENTER)

        # Kết quả hiển thị tại thẻ id="result"
        result_label = driver.find_element(By.ID, "result")
        self.assertEqual(result_label.text, "You entered: ENTER")

    def test_tc04_key_press_tab(self):
        """TC04: Kiểm tra bấm phím đặc biệt Keys.TAB"""
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/key_presses")

        target_box = driver.find_element(By.ID, "target")
        target_box.send_keys(Keys.TAB)

        result_label = driver.find_element(By.ID, "result")
        self.assertEqual(result_label.text, "You entered: TAB")


if __name__ == "__main__":
    unittest.main()