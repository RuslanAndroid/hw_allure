from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class MainPage(BasePage):
    NAVBAR = (By.CLASS_NAME, "navbar")
    BANNERS = (By.CLASS_NAME, "swiper-viewport")
    CARUSEL = (By.CSS_SELECTOR, "#carousel0")
    FOOTER = (By.CSS_SELECTOR, "body > footer")
    SEARCH = (By.CSS_SELECTOR, "#search")
    CONTACTS = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(1) > a > i")
    PRODUCT_IPHONE = (By.CSS_SELECTOR, "#content > div.row > div:nth-child(2) > div > div.image > a > img")
    REGISTRATION = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
    REGISTRATION_DROPDOWN = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a")
    CATEGORY_TABLETS = (By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > "
                                         "li:nth-child(4) > a")

    def verify_navbar(self):
        self._verify_element_presence(self.NAVBAR)

    def verify_banners(self):
        self._verify_element_presence(self.BANNERS)

    def verify_carusel(self):
        self._verify_element_presence(self.CARUSEL)

    def verify_footer(self):
        self._verify_element_presence(self.FOOTER)

    def verify_search(self):
        self._verify_element_presence(self.SEARCH)

    def click_contacts(self):
        self.browser.find_element(*self.CONTACTS).click()

    def click_product_iphone(self):
        self.browser.find_element(*self.PRODUCT_IPHONE).click()

    def click_category_tablets(self):
        self.browser.find_element(*self.CATEGORY_TABLETS).click()

    def click_registration(self):
        self.browser.find_element(*self.REGISTRATION_DROPDOWN).click()
        self.browser.find_element(*self.REGISTRATION).click()
