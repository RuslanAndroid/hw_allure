import allure


@allure.feature("Main page")
@allure.title("Navigation Bar")
def test_menu(main_page):
    main_page.verify_navbar()


@allure.feature("Main page")
@allure.title("Banners")
def test_banners(main_page):
    main_page.verify_banners()


@allure.feature("Main page")
@allure.title("Carusel")
def test_carusel(main_page):
    main_page.verify_carusel()


@allure.feature("Main page")
@allure.title("Footer")
def test_footer(main_page):
    main_page.verify_footer()


@allure.feature("Main page")
@allure.title("Search")
@allure.severity(allure.severity_level.CRITICAL)
def test_search(main_page):
    main_page.verify_search()
