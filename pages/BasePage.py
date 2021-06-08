from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            self.logger.info("Verify element presence: {}".format(locator))
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _click(self, locator: tuple):
        self.logger.info("Click element: {}".format(locator))
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self
