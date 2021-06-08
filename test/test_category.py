
def test_left_column(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_left_column()


def test_sign(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_sign()


def test_products_tree(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_product_tree()


def test_cart(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_cart()


def test_one_item(main_page, category_page):
    main_page.click_category_tablets()
    category_page.verify_one_item()
