from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.home_page import HomePage


def test_home_page_loads(driver):
    home = HomePage(driver)
    home.driver.get("https://www.demoblaze.com/")
    assert home.is_loaded()
    print("test")
