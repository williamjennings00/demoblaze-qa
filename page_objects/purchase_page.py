from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class PurchasePage(BasePage):
    PLACE_ORDER_BUTTON = (By.CLASS_NAME,"btn-success")
    PLACE_ORDER_CONTENT = (By.ID, "orderModal")


    def place_order(self):
        place_order_button = self.find_element(self.PLACE_ORDER_BUTTON)
        place_order_button.click()

    
    def check_if_modal_is_present(self):
        return self.wait_until_visible(self.PLACE_ORDER_CONTENT)

