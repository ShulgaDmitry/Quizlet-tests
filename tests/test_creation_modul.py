from pages.creation_modul_page import CreationModulPage
import allure


@allure.feature("Creation modul")
@allure.story("Fault creation modul")
def test_error_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Check that error message is enabled"):
        assert creation.check_error_modul_message()


@allure.feature("Creation modul")
@allure.story("Creation modul")
def test_creation_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Check modul link"):
        assert creation.check_user_link() is True
    creation.delete_modul()


@allure.feature("Creation modul")
@allure.story("Update modul")
def test_creation_image_modul(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Click change button"):
        creation.change_modul()
    with allure.step("Add image"):
        creation.add_image()
    with allure.step("Click create button"):
        creation.click_create_button()
    with allure.step("Check that image is enabled"):
        assert creation.check_image() is True
    creation.delete_modul()


@allure.feature("Creation modul")
@allure.story("Knowledge test")
def test_pass_test(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    with allure.step("Banner with congratulations is enabled"):
        creation.close_banner()
    creation.click_next_card()
    creation.delete_modul()


@allure.feature("Creation modul")
@allure.story("Selection word game")
def test_selection_game(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Check that button after game is enabled"):
        creation.click_selection()
    creation.delete_modul()


@allure.feature("Creation modul")
@allure.story("Writing memorization test")
def test_writing_memorization(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Check that 2 words is enabled"):
        creation.click_memorization()
    creation.delete_modul()


def test_long_term_memorization_round_1(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Check that banner is enabled"):
        creation.click_long_term_memorization_round_1()
    creation.delete_modul()


def test_long_term_memorization_round_2(chrome_driver):
    creation = CreationModulPage(chrome_driver)
    with allure.step("Create modul"):
        creation.open_creation_modul_page()
    with allure.step("Enter name modul"):
        creation.enter_name_field()
    with allure.step("Enter description modul"):
        creation.enter_description_field()
    with allure.step("Enter first word"):
        creation.enter_term_field_1()
    with allure.step("Choose language of first word"):
        creation.choose_language_1()
    with allure.step("Enter second word"):
        creation.enter_definition_field_1()
    with allure.step("Choose language of second word"):
        creation.choose_language_2()
    with allure.step("Enter third word"):
        creation.enter_term_field_2()
    with allure.step("Enter fourth word"):
        creation.enter_definition_field_2()
    with allure.step("Click creation button"):
        creation.click_create_button()
    creation.close_banner()
    with allure.step("Cup image is enabled"):
        creation.click_long_term_memorization_round_2()
    creation.delete_modul()
