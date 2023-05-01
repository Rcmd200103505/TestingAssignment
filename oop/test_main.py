from selenium import webdriver
from oop.test_home_search import HomePage
from test_searching_item import SearchPage
from test_item import ItemPage
from test_home_item_added import HomeItemAddedPage
from test_basket import BasketPage

driver = webdriver.Chrome()
driver.get('https://shop.kz/')

def test_home():
    home_page = HomePage(driver)
    home_page.click_search()
    home_page.search("a4tech")
    assert driver.current_url != "http://www.google.com/"

search_page = SearchPage(driver)
search_page.click_item()

item_page = ItemPage(driver)
item_page.add_item()
item_page.go_basket()
item_page.go_home()

home_item_added_page = HomeItemAddedPage(driver)
home_item_added_page.click_basket()

basket_page = BasketPage(driver)
basket_page.click_delete_item()


