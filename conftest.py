import allure
import pytest
import os
import logging

from allure_commons.types import AttachmentType
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from selenium import webdriver

from pages.CategoryPage import CategoryPage
from pages.ContactsPage import ContactsPage
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from pages.RegistrationPage import RegistrationPage

logging.basicConfig(level=logging.INFO, filename=os.path.dirname(os.path.abspath(__file__)) + "/logs/selenium.log")


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        logging.error(f'Oooops i got: {exception}')



def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://demo-opencart.ru/")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.29.222")
    parser.addoption("--bversion", action="store", default="90.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {}
    }

    options = webdriver.ChromeOptions()
    driver = EventFiringWebDriver(webdriver.Remote(options=options, command_executor=executor_url,
                                                   desired_capabilities=caps), MyListener())

    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished".format(test_name))

    request.addfinalizer(fin)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    return driver


@pytest.fixture
def main_page(browser):
    return MainPage(browser)


@pytest.fixture
def contacts_page(browser):
    return ContactsPage(browser)


@pytest.fixture
def product_page(browser):
    return ProductPage(browser)


@pytest.fixture
def category_page(browser):
    return CategoryPage(browser)


@pytest.fixture
def registration_page(browser):
    return RegistrationPage(browser)
