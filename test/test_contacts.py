
def test_contacts(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_contacts()


def test_shops_list(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_shops_list()


def test_contact_form(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_contact_form()


def test_send_message_btn(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_send_message_btn()


def test_page_title(main_page, contacts_page):
    main_page.click_contacts()
    contacts_page.verify_title()
