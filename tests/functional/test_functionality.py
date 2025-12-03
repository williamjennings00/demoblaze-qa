from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

def test_positive_admin(driver):
    driver.get("https://www.demoblaze.com/")