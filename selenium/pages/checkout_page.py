from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    CART_COUNT = (By.ID, "cart-count")
    CHECKOUT_BTN = (By.ID, "checkout")
    ORDER_SUCCESS = (By.CSS_SELECTOR, ".order-success, .success")

    def proceed_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def is_success(self):
        return len(self.driver.find_elements(*self.ORDER_SUCCESS))>0
