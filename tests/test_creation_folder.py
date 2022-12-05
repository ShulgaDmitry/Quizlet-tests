from pages.creation_folder_page import CreationFolderPage


def test_creation_folder_button(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    creation.enter_name_field()
    creation.enter_description_field()
    assert creation.check_create_button() is True


def test_delete_folder(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.click_create_button()
    creation.delete_folder()
    assert creation.check_delete_folder()


def test_addition_modul(chrome_driver):
    creation = CreationFolderPage(chrome_driver)
    creation.open_creation_folder_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.click_create_button()
    creation.addition_modul()
    assert creation.check_url_creation_modul()
    creation.close_banner()
    creation.open_profile()
    creation.delete_folder()
