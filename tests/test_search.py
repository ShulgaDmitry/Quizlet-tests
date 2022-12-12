from pages.search_page import SearchPage
import allure


@allure.feature("Search field")
@allure.story("Search")
def test_search(chrome_driver):
    search = SearchPage(chrome_driver)
    with allure.step("Open main page"):
        search.open_search_page()
    with allure.step("Check search by word english "):
        search.check_search(search_phrase="English")


@allure.feature("Search field")
@allure.story("Search filters")
def test_filters_search(chrome_driver):
    search = SearchPage(chrome_driver)
    with allure.step("Open main page"):
        search.open_search_page()
    with allure.step("Check search by filter 'with image'"):
        assert search.check_filter(search_phrase="English") is True


@allure.feature("Search field")
@allure.story("Addition other modul")
def test_additions_other_modul(chrome_driver):
    search = SearchPage(chrome_driver)
    with allure.step("Open main page"):
        search.open_search_page()
    with allure.step("Check addition other modul in folder"):
        assert search.additions_other_modul(search_phrase="English", folder_name="Test") is True
    search.delete_folder()

