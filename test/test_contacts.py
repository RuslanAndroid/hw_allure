import allure


@allure.feature("Contacts")
@allure.title("Contacts")
def test_contacts(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_contacts()


@allure.feature("Contacts")
@allure.title("Shop List")
def test_shops_list(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_shops_list()


@allure.feature("Contacts")
@allure.title("Contact Form")
def test_contact_form(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_contact_form()


@allure.feature("Contacts")
@allure.title("Send Message")
def test_send_message_btn(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_send_message_btn()


@allure.feature("Contacts")
@allure.title("Title")
def test_page_title(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_title()
