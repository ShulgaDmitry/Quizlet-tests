from pages.creation_folder_page import CreationFolderPage
import allure


@allure.feature("Creation folder")
@allure.story("Button disabled until all data has been enter")
def test_creation_folder_button(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    with allure.step("Create folder"):
        creation.open_creation_folder_page()
    with allure.step("Enter name folder"):
        creation.enter_name_field()
    with allure.step("Enter description folder"):
        creation.enter_description_field()
    with allure.step("Check that button is enabled"):
        assert creation.check_create_button() is True


@allure.feature("Creation folder")
@allure.story("Delete folder")
def test_delete_folder(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    with allure.step("Create folder"):
        creation.open_creation_folder_page()
    with allure.step("Enter name folder"):
        creation.enter_name_field()
    with allure.step("Enter description folder"):
        creation.enter_description_field()
    with allure.step("Click create button"):
        creation.click_create_button()
    with allure.step("Delete folder"):
        creation.delete_folder()
    with allure.step("Check that banner is enabled"):
        assert creation.check_delete_folder()


@allure.feature("Creation folder")
@allure.story("Delete folder")
def test_addition_modul(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    with allure.step("Create folder"):
        creation.open_creation_folder_page()
    with allure.step("Enter name folder"):
        creation.enter_name_field()
    with allure.step("Enter description folder"):
        creation.enter_description_field()
    with allure.step("Click create button"):
        creation.click_create_button()
    with allure.step("Addition modul"):
        creation.addition_modul()
    with allure.step("Check url creation modul page"):
        assert creation.check_url_creation_modul()
    creation.close_banner()
    creation.open_profile()
    creation.delete_folder()
