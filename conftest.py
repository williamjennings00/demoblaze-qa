import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

TEST_PAGE_URL = "https://www.demoblaze.com/"

@pytest.fixture(scope="session")
def driver():
    """Headless Chrome WebDriver"""
    print("\n--- Starting Chrome WebDriver ---")

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # WebDriver manager downloads Chromedriver automatically
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(5)
    yield driver
    print("--- Quitting Chrome WebDriver ---")
    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    """Explicit wait helper."""
    return WebDriverWait(driver, 10)

@pytest.fixture(scope="session")
def page_url():
    return TEST_PAGE_URL
