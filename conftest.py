import pytest
import os

from selenium import webdriver

from pages.CategoryPage import CategoryPage
from pages.ContactsPage import ContactsPage
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from pages.RegistrationPage import RegistrationPage

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://demo-opencart.ru/")
    parser.addoption("--tolerance", type=int, default=3)


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path=f"{DRIVERS}/chromedriver")

    request.addfinalizer(driver.quit)

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
