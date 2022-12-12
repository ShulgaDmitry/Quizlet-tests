from pages.registration_page import RegistrationPage
import allure


@allure.feature("Registration")
@allure.story("Registration button disabled until all data has been enter")
def test_registration_button(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    with allure.step("Open registration page"):
        registration.open_registration_page()
    with allure.step("Select birth date"):
        registration.select_birth_date()
    with allure.step("Select birth month"):
        registration.select_birth_month()
    with allure.step("Select birth year"):
        registration.select_birth_year()
    with allure.step("Enter name"):
        registration.enter_new_name()
    with allure.step("Enter password"):
        registration.enter_new_password(password="Abcd123456")
    with allure.step("Enter email"):
        registration.enter_new_email(email="aapbyw@mailto.plus")
    with allure.step("Choose checkbox agreement"):
        registration.checkbox_true()
    with allure.step("Check that button is enabled"):
        assert registration.check_button_register() is True


@allure.feature("Registration")
@allure.story("Registration button disabled until all data has been enter")
def test_age_checkbox(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    with allure.step("Open registration page"):
        registration.open_registration_page()
    with allure.step("Select birth date"):
        registration.select_birth_date()
    with allure.step("Select birth month"):
        registration.select_birth_month()
    with allure.step("Select birth year"):
        registration.select_birth_year()
    with allure.step("Check that checkbox adult is enabled"):
        assert registration.checkbox_adult_true() is True
    with allure.step("Check that checkbox teacher is enabled"):
        assert registration.checkbox_teacher_true() is True
    with allure.step("Choose birth year less than age adult person"):
        registration.select_birth_minor_year()
    with allure.step("Check that checkbox adult is disenabled"):
        assert registration.checkbox_adult_absent() is True
    with allure.step("Check that checkbox teacher is enabled"):
        assert registration.checkbox_teacher_absent() is True


@allure.feature("Registration")
@allure.story("Create account")
def test_registration(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    with allure.step("Open registration page"):
        registration.open_registration_page()
    with allure.step("Select birth date"):
        registration.select_birth_date()
    with allure.step("Select birth month"):
        registration.select_birth_month()
    with allure.step("Select birth year"):
        registration.select_birth_year()
    with allure.step("Enter name"):
        registration.enter_new_name()
    with allure.step("Enter password"):
        registration.enter_new_password(password="Abcd123456")
    with allure.step("Enter email"):
        registration.enter_new_email(email="aapbyw@mailto.plus")
    with allure.step("Choose checkbox agreement"):
        registration.checkbox_true()
    with allure.step("Enter button registration"):
        registration.enter_register()
    registration.reopen_page()
    with allure.step("Make sure the main page opens and the avatar appears"):
        assert registration.check_avatar() is True
    registration.setting_button()
    registration.delete_account()


@allure.feature("Registration")
@allure.story("Delete account")
def test_delete_account(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    with allure.step("Open registration page"):
        registration.open_registration_page()
    with allure.step("Select birth date"):
        registration.select_birth_date()
    with allure.step("Select birth month"):
        registration.select_birth_month()
    with allure.step("Select birth year"):
        registration.select_birth_year()
    with allure.step("Enter name"):
        registration.enter_new_name()
    with allure.step("Enter password"):
        registration.enter_new_password(password="Abcd123456")
    with allure.step("Enter email"):
        registration.enter_new_email(email="aapbyw@mailto.plus")
    with allure.step("Choose checkbox agreement"):
        registration.checkbox_true()
    with allure.step("Enter button registration"):
        registration.enter_register()
    registration.reopen_page()
    registration.setting_button()
    with allure.step("Make sure the main page opens and the avatar disappears"):
        assert registration.check_account_deletion()

