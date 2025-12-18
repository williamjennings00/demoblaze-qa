from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time 



def test_home_page_loads(driver):
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    assert home.is_loaded()


def test_phone_category_render_correctly(driver):
    # List of phones to compare against
    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    
    home.select_category("Phones")
    
    home.wait_for_elements(home.PHONE_ITEMS,7)
    items = home.get_category_items()
    items.sort()
    list_of_phones.sort()
    try:
        assert items == list_of_phones, f"Lists do not match: {items} != {list_of_phones}"

        print("Success: Phone items match expected list.")

    except StaleElementReferenceException:
        print("Stale element reference exception encountered...")

def test_laptop_category_render_correctly(driver):
    # List of laptops to compare against
    list_of_laptops = [
        "Sony vaio i5", "Sony vaio i7", "MacBook air", "Dell i7 8gb", "2017 Dell 15.6 Inch", "MacBook Pro"
    ]
    
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    
    home.select_category("Laptops")
    
    home.wait_for_elements(home.LAPTOP_ITEMS,6)
    items = home.get_category_items()
    items.sort()
    list_of_laptops.sort()
    try:
        assert items == list_of_laptops, f"Lists do not match: {items} != {list_of_laptops}"

        print("Success: Laptop items match expected list.")

    except StaleElementReferenceException:
        print("Stale element reference exception encountered...")

def test_monitor_category_render_correctly(driver):
    # List of monitors to compare against
    list_of_monitors = [
        "Apple monitor 24", "ASUS Full HD"
    ]
    
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    
    home.select_category("Monitors")
    
    home.wait_for_elements(home.MONITOR_ITEMS,2)
    items = home.get_category_items()
    items.sort()
    list_of_monitors.sort()
    try:
        assert items == list_of_monitors, f"Lists do not match: {items} != {list_of_monitors}"

        print("Success: Monitor items match expected list.")

    except StaleElementReferenceException:
        print("Stale element reference exception encountered...")

def test_laptops_product_name_on_item_details_page(driver):

    list_of_laptops = [
        "Sony vaio i5", "Sony vaio i7", "MacBook air", "Dell i7 8gb", "2017 Dell 15.6 Inch", "MacBook Pro"
    ]
    home = HomePage(driver)
    for x in range(0,len(list_of_laptops)):
        home.navigate_to_laptop(list_of_laptops[x])
        product = home.get_product_name_on_info_page()
        assert list_of_laptops[x] == product, (
            f"[ASSERTION FAILED] Expected '{list_of_laptops[x]}' "
            f"but got '{product}' at index {x}"
        )

def test_phone_product_name_on_item_details_page(driver):

    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    home = HomePage(driver)
    for x in range(0,len(list_of_phones)):
        home.navigate_to_phone(list_of_phones[x])
        product = home.get_product_name_on_info_page()
        assert list_of_phones[x] == product, (
            f"[ASSERTION FAILED] Expected '{list_of_phones[x]}' "
            f"but got '{product}' at index {x}"
        )

def test_monitors_product_name_on_item_details_page(driver):

    list_of_monitors = [
        "Apple monitor 24", "ASUS Full HD"
    ]
    home = HomePage(driver)
    for x in range(0,len(list_of_monitors)):
        home.navigate_to_monitor(list_of_monitors[x])
        product = home.get_product_name_on_info_page()
        assert list_of_monitors[x] == product, (
            f"[ASSERTION FAILED] Expected '{list_of_monitors[x]}' "
            f"but got '{product}' at index {x}"
        )

def test_monitors_product_price_on_item_details_page(driver):

    list_of_monitors = [
        "Apple monitor 24", "ASUS Full HD"
    ]
    list_of_prices = [
        "$400 *includes tax", "$230 *includes tax"
    ]
    home = HomePage(driver)
    for x in range(0,len(list_of_monitors)):
        home.navigate_to_monitor(list_of_monitors[x])
        product_price = home.get_product_price_on_info_page()
        assert list_of_prices[x] == product_price, (
            f"[ASSERTION FAILED] Expected '{list_of_prices[x]}' "
            f"but got '{product_price}' at index {x}"
        )

def test_phones_product_price_on_item_details_page(driver):

    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    list_of_prices = [
        "$360 *includes tax",
        "$820 *includes tax",
        "$650 *includes tax",
        "$800 *includes tax",
        "$790 *includes tax",
        "$320 *includes tax",
        "$700 *includes tax"
    ]

    home = HomePage(driver)
    for x in range(0,len(list_of_phones)):
        home.navigate_to_phone(list_of_phones[x])
        product_price = home.get_product_price_on_info_page()
        assert list_of_prices[x] == product_price, (
            f"[ASSERTION FAILED] Expected '{list_of_prices[x]}' "
            f"but got '{product_price}' at index {x}"
        )



def test_laptops_product_price_on_item_details_page(driver):

    list_of_laptops = [
        "Sony vaio i5", "Sony vaio i7", "MacBook air", "Dell i7 8gb", "2017 Dell 15.6 Inch", "MacBook Pro"
    ]
    list_of_prices = [
        "$790 *includes tax", "$790 *includes tax", "$700 *includes tax",
        "$700 *includes tax", "$700 *includes tax", "$1100 *includes tax",
    ]

    home = HomePage(driver)
    for x in range(0,len(list_of_laptops)):
        home.navigate_to_laptop(list_of_laptops[x])
        product_price = home.get_product_price_on_info_page()
        assert list_of_prices[x] == product_price, (
            f"[ASSERTION FAILED] Expected '{list_of_prices[x]}' "
            f"but got '{product_price}' at index {x}"
        )

