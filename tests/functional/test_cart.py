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
    cart.goto_product_page("Samsung galaxy s6",driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")
    cart_product_title = cart.get_cart_item_titles()
    assert any("Samsung galaxy s6" in title for title in cart_product_title)

def test_add_multiple_products_to_cart(driver):
    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    cart = CartPage(driver)
    for x in range(0,len(list_of_phones)):
        cart.driver.get("https://www.demoblaze.com")
        cart.goto_product_page(list_of_phones[x],driver)
        cart.add_product_to_cart()
    
    cart.driver.get("https://www.demoblaze.com/cart.html")
    cart_product_title = cart.get_cart_item_titles()
    for phone in list_of_phones:
        assert any(phone in title for title in cart_product_title), f"'{phone}' not found in cart"

def test_remove_product_from_cart(driver):
    cart = CartPage(driver)
    cart.goto_product_page("Samsung galaxy s6",driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")
    cart.remove_product_from_cart()
    cart.wait_for_element_invisibility(cart.CART_PRODUCT_TITLE)
    cart_product_title = cart.get_cart_item_titles()
    assert not any("Samsung galaxy s6" in title for title in cart_product_title)

def test_cart_price_calculations(driver):
    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    cart = CartPage(driver)
    for x in range(0,len(list_of_phones)):
        cart.driver.get("https://www.demoblaze.com")
        cart.goto_product_page(list_of_phones[x],driver)
        cart.add_product_to_cart()
    
    cart.driver.get("https://www.demoblaze.com/cart.html")
    cart.is_visible(cart.CART_TOTAL)
    price_total = cart.get_price_total()
    assert price_total == '4440'

def test_cart_persistence(driver):
    cart = CartPage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()

    cart.driver.get("https://www.demoblaze.com")
    
    product_name2 = "Nokia lumia 1520"
    cart.goto_product_page(product_name2, driver)
    cart.add_product_to_cart()

    cart.driver.get("https://www.demoblaze.com/cart.html")

    cart_product_titles = cart.get_cart_item_titles()
    cart.is_visible(cart.CART_TOTAL) # used to make sure that cart has fully loaded. 
    assert any("Samsung galaxy s6" in title for title in cart_product_titles), "Samsung galaxy s6 is not in the cart"
    assert any("Nokia lumia 1520" in title for title in cart_product_titles), "Nokia lumia 1520 is not in the cart"

    print("Cart persistence test passed. Products are still in the cart.")
