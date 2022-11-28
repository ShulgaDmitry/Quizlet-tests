from pages.creation_folder_page import CreationFolderPage
from time import sleep


def test_creation_folder_button(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    assert creation.check_create_button() is True


def test_delete_folder(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.click_create_button()
    sleep(2)
    creation.delete_folder()
    sleep(2)
    assert creation.check_url_delete_folder()


def test_addition_modul(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.click_create_button()
    creation.addition_modul()
    sleep(2)
    assert creation.check_url_creation_modul()
    creation.close_banner()
    sleep(2)
    creation.open_profile()
    sleep(2)
    creation.delete_folder()
    sleep(2)
