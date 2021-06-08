
def test_buy_button(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_buy_button()


def test_logo(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_logo()


def test_desc_content(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_tab_content()


def test_rating(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_rating()


def test_change_language(main_page, product_page):
    main_page.click_product_iphone()
    product_page.verify_change_language()
