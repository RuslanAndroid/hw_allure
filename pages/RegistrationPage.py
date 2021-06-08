from selenium.webdriver.common.by import By
import time
from pages.BasePage import BasePage


class RegistrationPage(BasePage):
    HINT = (By.CSS_SELECTOR, "#content > p")
    USER_DATA = (By.CSS_SELECTOR, "#account")
    CONFIRM_FORM = (By.CSS_SELECTOR, "#content > form > div")
    RIGHT_COLUMN = (By.CSS_SELECTOR, "#column-right")
    TITLE = (By.CSS_SELECTOR, "#content > h1")

    USER_NAME = (By.CSS_SELECTOR, "#input-firstname")
    USER_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    USER_EMAIL = (By.CSS_SELECTOR, "#input-email")
    USER_PHONE = (By.CSS_SELECTOR, "#input-telephone")
    USER_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    USER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    USER_AGREE_CHECKBOX = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(3)")
    REGISTRATION_ACCEPT_BUTTON = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    REGISTRATION_FINISH_TEXT = (By.CSS_SELECTOR, "#content > p:nth-child(2)")

    def verify_hint(self):
        self._verify_element_presence(self.HINT)

    def verify_user_data(self):
        self._verify_element_presence(self.USER_DATA)

    def verify_confirm_form(self):
        self._verify_element_presence(self.CONFIRM_FORM)

    def verify_right_column(self):
        self._verify_element_presence(self.RIGHT_COLUMN)

    def verify_page_title(self):
        self._verify_element_presence(self.TITLE)

    def register_user(self):
        # Чтобы тест сработал второй раз нужно уникальное значение пользователя
        cur_time = time.strftime("%Y%m%d%H%M%S")
        self._element(self.USER_NAME).send_keys('user' + cur_time)
        self._element(self.USER_LASTNAME).send_keys('user')
        self._element(self.USER_EMAIL).send_keys(f'user{cur_time}@mail.ru')
        self._element(self.USER_PHONE).send_keys('123456')
        self._element(self.USER_PASSWORD).send_keys('123456')
        self._element(self.USER_CONFIRM_PASSWORD).send_keys('123456')
        self.browser.find_element(*self.USER_AGREE_CHECKBOX).click()
        self.browser.find_element(*self.REGISTRATION_ACCEPT_BUTTON).click()
        self._verify_element_presence(self.REGISTRATION_FINISH_TEXT)
