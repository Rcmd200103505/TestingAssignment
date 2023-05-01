from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(4)

login = driver.find_element(By.ID, 'email')
login.send_keys("seitzhan213@gmail.com")


password = driver.find_element(By.ID, 'pass')
password.send_keys("12334567677")

time.sleep(4)

search = driver.find_element(By.XPATH, "//*[contains(@data-testid, 'royal_login_button')]").click()
time.sleep(4)