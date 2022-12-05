from pages.creation_modul_page import CreationModulPage


def test_error_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    assert creation.check_error_modul_message()


def test_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    assert creation.check_user_link() is True
    creation.delete_modul()


def test_creation_image_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.change_modul()
    creation.add_image()
    creation.click_create_button()
    assert creation.check_image() is True
    creation.delete_modul()


def test_pass_test(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.click_next_card()
    creation.delete_modul()


def test_selection_game(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.click_selection()
    creation.delete_modul()


def test_writing_memorization(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.click_memorization()
    creation.delete_modul()


def test_long_term_memorization_round_1(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.click_long_term_memorization_round_1()
    creation.delete_modul()


def test_long_term_memorization_round_2(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    creation.open_creation_modul_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_term_field_1()
    creation.choose_language_1()
    creation.enter_definition_field_1()
    creation.choose_language_2()
    creation.enter_term_field_2()
    creation.enter_definition_field_2()
    creation.click_create_button()
    creation.close_banner()
    creation.click_long_term_memorization_round_2()
    creation.delete_modul()
