
def test_hint(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_hint()


def test_user_data_form(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_user_data()


def test_confirm_form(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_confirm_form()


def test_right_column(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_right_column()


def test_page_title(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_page_title()


def test_register_user(main_page, registration_page):
    main_page.click_registration()
    registration_page.register_user()
