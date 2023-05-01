from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(self.driver, 10)

        self.search_click = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'search-hover__submit'))
        )

        self.search = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'multi-input'))
        )

    def click_search(self):
        self.search_click.click()

    def search(self, item):
        self.search.send_keys("item")
        self.search.send_keys(Keys.ENTER)