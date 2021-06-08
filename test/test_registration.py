import allure


@allure.feature("Registration")
@allure.title("Hint")
def test_hint(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_hint()


@allure.feature("Registration")
@allure.title("User Data Form")
def test_user_data_form(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_user_data()


@allure.feature("Registration")
@allure.title("Confirm Form")
def test_confirm_form(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_confirm_form()


@allure.feature("Registration")
@allure.title("Right Column")
def test_right_column(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_right_column()


@allure.feature("Registration")
@allure.title("Title")
def test_page_title(main_page, registration_page):
    main_page.click_registration()
    registration_page.verify_page_title()


@allure.feature("Registration")
@allure.title("Register User")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_user(main_page, registration_page):
    main_page.click_registration()
    registration_page.register_user()
