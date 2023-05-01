from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeItemAddedPage:
    def __init__(self, driver):
        self.driver = driver

        self.go_to_basket = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'splash-button'))
        )


    def click_basket(self):
        self.go_to_basket.click()


