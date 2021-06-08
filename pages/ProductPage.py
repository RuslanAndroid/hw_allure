from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):
    BUY_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    LOGO = (By.CSS_SELECTOR, "#logo")
    TAB_CONTENT = (By.CLASS_NAME, "tab-content")
    RATING = (By.CLASS_NAME, "rating")
    CHANGE_LANGUAGE = (By.CSS_SELECTOR, "#form-language > div > button")

    def verify_buy_button(self):
        self._verify_element_presence(self.BUY_BUTTON)

    def verify_logo(self):
        self._verify_element_presence(self.LOGO)

    def verify_tab_content(self):
        self._verify_element_presence(self.TAB_CONTENT)

    def verify_rating(self):
        self._verify_element_presence(self.RATING)

    def verify_change_language(self):
        self._verify_element_presence(self.CHANGE_LANGUAGE)
