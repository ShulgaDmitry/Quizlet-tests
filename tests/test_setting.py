from pages.setting_page import SettingPage
import allure


@allure.feature("Setting")
@allure.story("Change avatar")
def test_change_avatar(chrome_driver):
    setting = SettingPage(chrome_driver)
    with allure.step("Open main page"):
        setting.open_setting_page()
    with allure.step("Check that avatar changed"):
        assert setting.change_avatar() is True
    with allure.step("Check that avatar returned"):
        assert setting.return_avatar() is True


@allure.feature("Setting")
@allure.story("Change language")
def test_change_language(chrome_driver):
    setting = SettingPage(chrome_driver)
    with allure.step("Open main page"):
        setting.open_setting_page()
    with allure.step("Check that language changed"):
        assert setting.change_language() is True
    with allure.step("Check that language returned"):
        assert setting.return_language() is True


@allure.feature("Setting")
@allure.story("Change role")
def test_change_role(chrome_driver):
    setting = SettingPage(chrome_driver)
    with allure.step("Open main page"):
        setting.open_setting_page()
    with allure.step("Check that role changed and returned"):
        setting.change_role()


@allure.feature("Setting")
@allure.story("Change password")
def test_change_password(chrome_driver):
    setting = SettingPage(chrome_driver)
    with allure.step("Open main page"):
        setting.open_setting_page()
    with allure.step("Check that password changed"):
        assert setting.change_password(old_password="Abcd123456", new_password="Abcd$123456") is True
    with allure.step("Check log in with new password"):
        setting.open_setting_page_with_new_password()
    assert setting.return_password() is True

