from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time 
import re


def test_add_single_product_to_cart(driver):
    cart = CartPage(driver)
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    home.navigate_to_phone("Samsung galaxy s6")
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")
    cart_product_title = cart.get_cart_item_titles()
    assert any("Samsung galaxy s6" in title for title in cart_product_title)
