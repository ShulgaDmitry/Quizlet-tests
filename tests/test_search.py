from pages.search_page import SearchPage
from time import sleep


def test_search(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    sleep(2)
    search.check_search()
    sleep(2)


def test_filters_search(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    sleep(2)
    assert search.check_filter() is True
    sleep(2)


def test_additions_other_modul(chrome_driver):
    search = SearchPage(chrome_driver)
    search.open_search_page()
    sleep(2)
    assert search.additions_other_modul() is True
    search.delete_folder()

