from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class PurchasePage(BasePage):
    PLACE_ORDER_BUTTON = (By.CLASS_NAME,"btn-success")
    PLACE_ORDER_CONTENT = (By.ID, "orderModal")
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CREDIT_CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[@onclick='purchaseOrder()']")
    PURCHASE_POPUP_SUCCESS = (By.CLASS_NAME, "sa-success")

    
    def place_order(self):
        place_order_button = self.find_element(self.PLACE_ORDER_BUTTON)
        place_order_button.click()

    
    def check_if_modal_is_present(self):
        return self.wait_until_visible(self.PLACE_ORDER_CONTENT)
    
    def purchase_order(self):
        purchase_button = self.find_element(self.PURCHASE_BUTTON)
        purchase_button.click()

    
    def check_if_pop_success_is_present(self):
       return self.wait_until_visible(self.PURCHASE_POPUP_SUCCESS)

