from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH = (By.NAME, "q")
    FIRST_RESULT = (By.CSS_SELECTOR, "a")

    def search(self, term:str):
        self.type(self.SEARCH, term)
        from selenium.webdriver.common.keys import Keys
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def open_first_result(self):
        self.click(self.FIRST_RESULT)
