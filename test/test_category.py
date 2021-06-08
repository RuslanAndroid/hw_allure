import allure


@allure.feature("Category")
@allure.title("Left Column")
def test_left_column(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_left_column()


@allure.feature("Category")
@allure.title("Sign")
def test_sign(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_sign()


@allure.feature("Category")
@allure.title("Products Tree")
def test_products_tree(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_product_tree()


@allure.feature("Category")
@allure.title("Cart")
def test_cart(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_cart()


@allure.feature("Category")
@allure.title("One Item")
def test_one_item(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_one_item()
