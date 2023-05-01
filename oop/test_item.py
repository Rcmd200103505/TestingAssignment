from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

        self.add_item_to_basket = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]'))
        )

        self.go_to_basket = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]'))
        )

        self.go_homepage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_eshop_wrap"]/header/div/div/div[1]/div/a[1]/img'))
        )


    def add_item(self):
        self.add_item_to_basket.click()

    def go_basket(self):
        self.go_to_basket.click()

    def go_home(self):
        self.go_homepage.click()
