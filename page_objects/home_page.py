from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    CATEGORY_ITEMS = (By.CSS_SELECTOR, "a.list-group-item")
    NAV_BAR = (By.ID, "nava")
    PHONE_ITEMS = (By.CLASS_NAME, "hrefch")
    LAPTOP_ITEMS = (By.CLASS_NAME, "hrefch")
    MONITOR_ITEMS = (By.CLASS_NAME, "hrefch")
    PRODUCT_NAME_INFO_PAGE = (By.CLASS_NAME, "name")

    def get_category_items(self):
        items = self.find_elements(self.PHONE_ITEMS)
        return [element.text for element in items]
    
    def get_product_name_on_info_page(self):
        product_name = self.find_element(self.PRODUCT_NAME_INFO_PAGE)
        return product_name.text
    
    def select_category(self, category_name: str):
        items = self.find_elements(self.CATEGORY_ITEMS)

        for item in items:
            if item.text.strip().lower() == category_name.lower():
                item.click()
                return

        raise Exception(f"Category '{category_name}' not found.")

    def is_loaded(self) -> bool:
        """Check if the main banner is visible."""
        return self.is_visible(self.NAV_BAR)