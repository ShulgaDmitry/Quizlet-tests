from pages.authorization_page import AuthorizationPage
from time import sleep


def test_error_authorization(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    authorization.open_authorization_page()
    sleep(2)
    authorization.enter_error_email()
    authorization.enter_error_password()
    authorization.enter_next()
    sleep(2)
    assert authorization.check_error_message()


def test_right_authorization(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    authorization.open_authorization_page()
    sleep(2)
    authorization.enter_right_email()
    authorization.enter_right_password()
    authorization.enter_next()
    assert authorization.check_avatar() is True
    sleep(2)


def test_log_out_account(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    authorization.open_authorization_page()
    sleep(2)
    authorization.enter_right_email()
    authorization.enter_right_password()
    authorization.enter_next()
    assert authorization.log_out_account() is True


def test_dark_theme(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    authorization.open_authorization_page()
    sleep(2)
    authorization.enter_right_email()
    authorization.enter_right_password()
    authorization.enter_next()
    sleep(2)
    assert authorization.check_color_page() is True
    authorization.change_theme()
    sleep(2)
    assert authorization.check_dark_color_page() is True
    authorization.change_theme()
    sleep(2)
