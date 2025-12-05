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
    items = home.get_phone_items()
    items.sort()
    list_of_phones.sort()
    try:
        assert items == list_of_phones, f"Lists do not match: {items} != {list_of_phones}"

        print("Success: Phone items match expected list.")

    except StaleElementReferenceException:
        print("Stale element reference exception encountered...")

