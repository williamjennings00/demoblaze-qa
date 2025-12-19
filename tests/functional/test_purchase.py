from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from page_objects.purchase_page import PurchasePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time 
import re



def test_purchase_modal_opens(driver):
    cart = CartPage(driver)
    purchase = PurchasePage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")

    purchase.place_order()
    assert purchase.check_if_modal_is_present()