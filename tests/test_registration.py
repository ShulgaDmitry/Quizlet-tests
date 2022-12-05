from pages.registration_page import RegistrationPage


def test_registration_button(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    registration.open_registration_page()
    registration.select_birth_date()
    registration.select_birth_month()
    registration.select_birth_year()
    registration.enter_new_name()
    registration.enter_new_password()
    registration.enter_new_email()
    registration.checkbox_true()
    assert registration.check_button_register() is True


def test_age_checkbox(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    registration.open_registration_page()
    registration.select_birth_date()
    registration.select_birth_month()
    registration.select_birth_year()
    assert registration.checkbox_adult_true() is True
    assert registration.checkbox_teacher_true() is True
    registration.select_birth_minor_year()
    assert registration.checkbox_adult_absent() is True
    assert registration.checkbox_teacher_absent() is True


def test_registration(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    registration.open_registration_page()
    registration.select_birth_date()
    registration.select_birth_month()
    registration.select_birth_year()
    registration.enter_new_name()
    registration.enter_new_password()
    registration.enter_new_email()
    registration.checkbox_true()
    registration.enter_register()
    registration.reopen_page()
    assert registration.check_avatar() is True
    registration.setting_button()
    registration.delete_account()

