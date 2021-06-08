
def test_menu(main_page):
    main_page.verify_navbar()


def test_banners(main_page):
    main_page.verify_banners()


def test_carusel(main_page):
    main_page.verify_carusel()


def test_footer(main_page):
    main_page.verify_footer()


def test_search(main_page):
    main_page.verify_search()
