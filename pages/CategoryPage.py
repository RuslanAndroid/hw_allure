from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CategoryPage(BasePage):
    LEFT_COLUMN = (By.CSS_SELECTOR, "#column-left")
    SIGN = (By.CSS_SELECTOR, "body > footer > div > p")
    PRODUCT_TREE = (By.CSS_SELECTOR, "#product-category > ul")
    CART = (By.CSS_SELECTOR, "#cart")
    ONE_ITEM = (By.CSS_SELECTOR, "#column-left > div.swiper-viewport")

    def verify_left_column(self):
        self._verify_element_presence(self.LEFT_COLUMN)

    def verify_sign(self):
        self._verify_element_presence(self.SIGN)

    def verify_product_tree(self):
        self._verify_element_presence(self.PRODUCT_TREE)

    def verify_cart(self):
        self._verify_element_presence(self.CART)

    def verify_one_item(self):
        self._verify_element_presence(self.ONE_ITEM)
