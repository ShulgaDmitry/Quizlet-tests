from pages.creation_modul_page import CreationModulPage
from time import sleep


def test_error_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.click_create_button()
    assert creation.check_error_modul_message()


def test_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    sleep(3)
    creation.close_banner()
    assert creation.check_user_link() is True
    sleep(2)
    creation.delete_modul()
    sleep(3)


def test_creation_image_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    sleep(3)
    creation.click_create_button()
    creation.close_banner()
    sleep(3)
    creation.change_modul()
    creation.add_image()
    creation.click_create_button()
    sleep(3)
    assert creation.check_image() is True
    creation.delete_modul()
    sleep(3)


def test_pass_test(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    sleep(2)
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    sleep(3)
    creation.click_create_button()
    creation.close_banner()
    sleep(3)
    creation.click_next_card()
    creation.delete_modul()
    sleep(3)

