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


def test_purchase_form_fields_present(driver):
    cart = CartPage(driver)
    purchase = PurchasePage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")

    purchase.place_order()
    
    required_fields = [
        purchase.NAME_FIELD,
        purchase.COUNTRY_FIELD,
        purchase.CITY_FIELD,
        purchase.CREDIT_CARD_FIELD,
        purchase.MONTH_FIELD,
        purchase.YEAR_FIELD
    ]

    for field in required_fields:
        assert cart.is_visible(field), f"Field {field} is not visible"
    
    print("All required fields are present in the purchase form.")


def test_submit_empty_form(driver):
    cart = CartPage(driver)
    purchase = PurchasePage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")

    purchase.place_order()
    purchase.purchase_order() 
    purchase_alert = purchase.is_alert_present()
    assert purchase_alert.text == "Please fill out Name and Creditcard."

def test_submit_valid_form(driver):
    cart = CartPage(driver)
    purchase = PurchasePage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")
    purchase.place_order()
    required_fields = [
        purchase.NAME_FIELD,
        purchase.COUNTRY_FIELD,
        purchase.CITY_FIELD,
        purchase.CREDIT_CARD_FIELD,
        purchase.MONTH_FIELD,
        purchase.YEAR_FIELD
    ]
    purchase.wait_for_element(purchase.NAME_FIELD)
    for field in required_fields:
        input = purchase.find_element(field)
        input.send_keys("test")
    purchase.purchase_order() 
    assert purchase.check_if_pop_success_is_present()


def test_required_fields_have_required_attribute(driver):
    cart = CartPage(driver)
    purchase = PurchasePage(driver)
    cart.driver.get("https://www.demoblaze.com")

    product_name = "Samsung galaxy s6"
    cart.goto_product_page(product_name, driver)
    cart.add_product_to_cart()
    cart.driver.get("https://www.demoblaze.com/cart.html")
    purchase.place_order()
    required_fields = [
        purchase.NAME_FIELD,
        purchase.CREDIT_CARD_FIELD,
    ]
    purchase.wait_for_element(purchase.NAME_FIELD)
    for field in required_fields:
        input = purchase.find_element(field)
        input.send_keys("test")
    purchase.purchase_order() 
    assert purchase.check_if_pop_success_is_present()