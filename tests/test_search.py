from pages.search_page import SearchPage


def test_search(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    search.check_search()


def test_filters_search(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    assert search.check_filter() is True


def test_additions_other_modul(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    assert search.additions_other_modul() is True
    search.delete_folder()

