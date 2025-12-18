from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):

    ADD_TO_CART = (By.CSS_SELECTOR, "a.btn.btn-success.btn-lg")
    CART_PRODUCT_TITLE = (By.XPATH, "//tr[contains(@class,'success')]")

    def add_product_to_cart(self):
        add_button = self.find_element(self.ADD_TO_CART)
        add_button.click()

    def get_cart_item_titles(self):
        cart_titles = self.find_elements(self.CART_PRODUCT_TITLE)
        return [title.text for title in cart_titles]
