from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(4)

search = driver.find_element(By.CLASS_NAME, 'gLFyf')
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
time.sleep(4)

search = driver.find_element(By.XPATH, "//*[contains(@class, 'LC20lb MBeuO DKV0Md')]").click()
time.sleep(4)


