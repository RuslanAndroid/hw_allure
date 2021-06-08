from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ContactsPage(BasePage):
    CONTACTS = (By.CSS_SELECTOR, "#content > div.panel.panel-default")
    SHOPS_LIST = (By.CSS_SELECTOR, "#accordion")
    CONTACT_FORM = (By.CSS_SELECTOR, "#content > form > fieldset")
    SEND_MES_BTN = (By.CSS_SELECTOR, "#content > form > div")
    TITLE = (By.CSS_SELECTOR, "#content > h1")

    def verify_contacts(self):
        self._verify_element_presence(self.CONTACTS)

    def verify_shops_list(self):
        self._verify_element_presence(self.SHOPS_LIST)

    def verify_contact_form(self):
        self._verify_element_presence(self.CONTACT_FORM)

    def verify_send_message_btn(self):
        self._verify_element_presence(self.SEND_MES_BTN)

    def verify_title(self):
        self._verify_element_presence(self.TITLE)
