from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time 
import re

def normalize_text(text):
    import re
    text = re.sub(r"\s+", " ", text).strip()  # collapse spaces/newlines
    return text


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

def test_laptops_product_description_on_item_details_page(driver):
    list_of_laptops = [
        "Sony vaio i5", "Sony vaio i7", "MacBook air",
        "Dell i7 8gb", "2017 Dell 15.6 Inch", "MacBook Pro"
    ]
    
    laptop_descriptions = [
        "Product description Sony is so confident that the VAIO S is a superior ultraportable laptop that the company proudly compares the notebook to Apple's 13-inch MacBook Pro. And in a lot of ways this notebook is better, thanks to a lighter weight.",
        "Product description REVIEW Sony is so confident that the VAIO S is a superior ultraportable laptop that the company proudly compares the notebook to Apple's 13-inch MacBook Pro. And in a lot of ways this notebook is better, thanks to a lighter weight, higher-resolution display, more storage space, and a Blu-ray drive.",
        "Product description 1.6GHz dual-core Intel Core i5 (Turbo Boost up to 2.7GHz) with 3MB shared L3 cache Configurable to 2.2GHz dual-core Intel Core i7 (Turbo Boost up to 3.2GHz) with 4MB shared L3 cache.",
        "Product description 6th Generation Intel Core i7-6500U Dual-Core Processor 2.5 GHz (max boost speed up to 3.1GHz) 4MB L3 Cache, 8GB DDR4 1600 MHz, 1TB 5400 RPM HDD15.6 in Full HD LED-backlit touchscreen with Truelife (1920 x 1080), 10-finger multi-touch support, Intel HD Graphics 520 with shared graphics memory",
        "Product description 7th Gen Intel Core i7-7500U mobile processor 2.70 GHz with Turbo Boost Technology up to 3.50 GHz, Intel HD Graphics 62015.6 inch Full HD IPS TrueLife LED-backlit touchscreen (1920 x 1080), 10-finger multi-touch support, 360° flip-and-fold design,8GB DDR4 2400 MHz Memory, 1TB 5400 RPM HDD, No optical drive, 3 in 1 card reader (SD SDHC SDXC)",
        "Product description Apple has introduced three new versions of its MacBook Pro line, including a 13-inch and 15-inch model with the Touch Bar, a thin, multi-touch strip display that sits above the MacBook Pro's keyboard."
    ]


    home = HomePage(driver)
    
    for x in range(len(list_of_laptops)):
        home.navigate_to_laptop(list_of_laptops[x])
        product_description = home.get_product_description_on_info_page()
        
        expected = normalize_text(laptop_descriptions[x])
        actual = normalize_text(product_description)
        
        assert expected == actual, (
            f"[ASSERTION FAILED] Expected '{expected}' "
            f"but got '{actual}' at index {x}"
        )
def test_phones_product_description_on_item_details_page(driver):
    list_of_phones = [
        "Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", 
        "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"
    ]
    
    phone_descriptions = [
        "Product description The Samsung Galaxy S6 is powered by 1.5GHz octa-core Samsung Exynos 7420 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage cannot be expanded.",
        "Product description The Nokia Lumia 1520 is powered by 2.2GHz quad-core Qualcomm Snapdragon 800 processor and it comes with 2GB of RAM.",
        "Product description The Motorola Google Nexus 6 is powered by 2.7GHz quad-core Qualcomm Snapdragon 805 processor and it comes with 3GB of RAM.",
        "Product description The Samsung Galaxy S7 is powered by 1.6GHz octa-core it comes with 4GB of RAM. The phone packs 32GB of internal storage that can be expanded up to 200GB via a microSD card.",
        "Product description It comes with 1GB of RAM. The phone packs 16GB of internal storage cannot be expanded. As far as the cameras are concerned, the Apple iPhone 6 packs a 8-megapixel primary camera on the rear and a 1.2-megapixel front shooter for selfies.",
        "Product description Sony Xperia Z5 Dual smartphone was launched in September 2015. The phone comes with a 5.20-inch touchscreen display with a resolution of 1080 pixels by 1920 pixels at a PPI of 424 pixels per inch.",
        "Product description The HTC One M9 is powered by 1.5GHz octa-core Qualcomm Snapdragon 810 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage that can be expanded up to 128GB via a microSD card."
    ]
    home = HomePage(driver)
    
    for x in range(len(list_of_phones)):
        home.navigate_to_phone(list_of_phones[x])
        product_description = home.get_product_description_on_info_page()
        
        expected = normalize_text(phone_descriptions[x])
        actual = normalize_text(product_description)
        
        assert expected == actual, (
            f"[ASSERTION FAILED] Expected '{expected}' "
            f"but got '{actual}' at index {x}"
        )