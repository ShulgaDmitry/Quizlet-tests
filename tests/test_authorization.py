from pages.authorization_page import AuthorizationPage
import allure


@allure.feature("Authorization")
@allure.story("Fault Log in")
def test_error_authorization(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    with allure.step("Open authorization page"):
        authorization.open_authorization_page()
    with allure.step("Enter error email"):
        authorization.enter_error_email()
    with allure.step("Enter error password"):
        authorization.enter_error_password()
    with allure.step("Click enter"):
        authorization.enter_next()
    with allure.step("Check that error message is enabled"):
        assert authorization.check_error_message()


@allure.feature("Authorization")
@allure.story("Log in")
def test_right_authorization(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    with allure.step("Open authorization page"):
        authorization.open_authorization_page()
    with allure.step("Enter right email"):
        authorization.enter_right_email()
    with allure.step("Enter right password"):
        authorization.enter_right_password()
    with allure.step("Click enter"):
        authorization.enter_next()
    with allure.step("Make sure the main page opens and the avatar appears"):
        assert authorization.check_avatar() is True


@allure.feature("Authorization")
@allure.story("Log out")
def test_log_out_account(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    with allure.step("Open authorization page"):
        authorization.open_authorization_page()
    with allure.step("Enter email"):
        authorization.enter_right_email()
    with allure.step("Enter password"):
        authorization.enter_right_password()
    with allure.step("Click enter"):
        authorization.enter_next()
    with allure.step("Make sure the main page opens and the avatar disappears"):
        assert authorization.log_out_account() is True


@allure.feature("Authorization")
@allure.story("Dark theme")
def test_dark_theme(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    with allure.step("Open authorization page"):
        authorization.open_authorization_page()
    with allure.step("Enter email"):
        authorization.enter_right_email()
    with allure.step("Enter password"):
        authorization.enter_right_password()
    with allure.step("Click enter"):
        authorization.enter_next()
    with allure.step("Make sure the main page in white color"):
        assert authorization.check_color_page() is True
    with allure.step("Choose dark theme"):
        authorization.change_theme()
    with allure.step("Make sure the main page change in dark color"):
        assert authorization.check_dark_color_page() is True
    authorization.change_theme()


@allure.feature("Authorization")
@allure.story("Subscription")
def test_subscription_page(chrome_driver):
    authorization = AuthorizationPage(chrome_driver)
    with allure.step("Open authorization page"):
        authorization.open_authorization_page()
    with allure.step("Enter email"):
        authorization.enter_right_email()
    with allure.step("Enter password"):
        authorization.enter_right_password()
    with allure.step("Click enter"):
        authorization.enter_next()
    with allure.step("Make sure the subscription page was opened"):
        assert authorization.check_subscription_page()
