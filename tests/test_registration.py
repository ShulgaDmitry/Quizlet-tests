from pages.registration_page import RegistrationPage
from time import sleep


def test_registration_button(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    registration.open_registration_page()
    sleep(2)
    registration.select_birth_date()
    registration.select_birth_month()
    registration.select_birth_year()
    registration.enter_new_name()
    registration.enter_new_password()
    registration.enter_new_email()
    registration.checkbox_true()
    sleep(2)
    assert registration.check_button_register() is True
    sleep(3)


def test_age_checkbox(chrome_driver):
    registration = RegistrationPage(chrome_driver)
    registration.open_registration_page()
    sleep(2)
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
    sleep(2)
    registration.select_birth_date()
    registration.select_birth_month()
    registration.select_birth_year()
    registration.enter_new_name()
    registration.enter_new_password()
    registration.enter_new_email()
    registration.checkbox_true()
    sleep(2)
    registration.enter_register()
    sleep(3)
    registration.reopen_page()
    sleep(2)
    assert registration.check_avatar() is True
    registration.setting_button()
    registration.delete_account()
    sleep(2)
