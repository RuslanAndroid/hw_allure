import allure


@allure.feature("Product")
@allure.title("Buy button")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_button(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_buy_button()


@allure.feature("Product")
@allure.title("Logo")
def test_logo(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_logo()


@allure.feature("Product")
@allure.title("Description Content")
def test_desc_content(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_tab_content()


@allure.feature("Product")
@allure.title("Rating")
def test_rating(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_rating()


@allure.feature("Product")
@allure.title("Change Language")
def test_change_language(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_change_language()
