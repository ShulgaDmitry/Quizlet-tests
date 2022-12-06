from pages.setting_page import SettingPage


def test_change_avatar(chrome_driver):
    setting = SettingPage(chrome_driver)
    setting.open_setting_page()
    assert setting.change_avatar() is True
    assert setting.return_avatar() is True


def test_change_language(chrome_driver):
    setting = SettingPage(chrome_driver)
    setting.open_setting_page()
    assert setting.change_language() is True
    assert setting.return_language() is True


def test_change_role(chrome_driver):
    setting = SettingPage(chrome_driver)
    setting.open_setting_page()
    setting.change_role()


def test_change_password(chrome_driver):
    setting = SettingPage(chrome_driver)
    setting.open_setting_page()
    assert setting.change_password() is True
    setting.open_setting_page_with_new_password()
    assert setting.return_password() is True

