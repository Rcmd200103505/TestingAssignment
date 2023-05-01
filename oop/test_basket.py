from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage:
    def __init__(self, driver):
        self.driver = driver

        self.delete_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'cart__rem-item'))
        )


    def click_delete_item(self):
        self.delete_item.click()


