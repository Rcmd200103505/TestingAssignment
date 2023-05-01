from selenium import webdriver
from oop.test_home_search import HomePage


driver = webdriver.Chrome()
driver.get('https://shop.kz/')

def test_home_page():
    home_page = HomePage(driver)
    home_page.click_search()
    home_page.search("a4tech")
    assert driver.current_url != "http://www.google.com/"