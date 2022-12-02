from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


new_avatar = (By.CSS_SELECTOR, 'a[href="/settings/change-image/45"]')
old_avatar = (By.CSS_SELECTOR, 'a[href="/settings/change-image/16"]')
place_avatar = (By.CSS_SELECTOR, 'img[referrerpolicy="no-referrer"]')
language = (By.CSS_SELECTOR, 'select[name="localePreference"]')
change_button = (By.CLASS_NAME, 'UIButton-wrapper')
message = (By.XPATH, '//div[@class="UINotice UINotice--boxed UINotice--deprecated"]')
field_old_password = (By.CSS_SELECTOR, 'input[name="old_password"]')
field_new_password = (By.CSS_SELECTOR, 'input[name="new_password"]')
field_confirm_new_password = (By.CSS_SELECTOR, 'input[name="new_password_conf"]')
radiobutton = (By.CLASS_NAME, 'UIRadio')


class SettingPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_setting_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()
        authorization.click_setting()

    def open_setting_page_with_new_password(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.log_out_account()
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_new_password()
        authorization.enter_next()
        authorization.click_setting()

    def change_avatar(self):
        self.find_element(new_avatar).click()
        new = self.find_elements(place_avatar)
        sleep(2)
        new_image = new[0].get_attribute("src")
        return 'https://assets.quizlet.com/a/j/dist/app/i/animals/45.069bd0ea8329543.jpg' in new_image

    def return_avatar(self):
        self.find_element(old_avatar).click()
        new = self.find_elements(place_avatar)
        sleep(2)
        old_image = new[0].get_attribute("src")
        return 'https://assets.quizlet.com/a/j/dist/app/i/animals/16.a97172ddb231185.jpg' in old_image

    def change_language(self):
        choose_language = Select(self.find_element(language))
        choose_language.select_by_value("en-gb")
        change = self.find_elements(change_button)
        change[1].click()
        message_change = self.find_element(message)
        return message_change.is_enabled()

    def return_language(self):
        choose_language = Select(self.find_element(language))
        choose_language.select_by_value("ru")
        change = self.find_elements(change_button)
        change[1].click()
        message_change = self.find_element(message)
        return message_change.is_enabled()

    def change_password(self):
        self.find_element(field_old_password).send_keys("Abcd123456")
        self.find_element(field_new_password).send_keys("Abcd$123456")
        self.find_element(field_confirm_new_password).send_keys("Abcd$123456")
        change_password = self.find_elements(change_button)
        change_password[3].click()
        message_change = self.find_element(message)
        return message_change.is_enabled()

    def return_password(self):
        self.find_element(field_old_password).send_keys("Abcd$123456")
        self.find_element(field_new_password).send_keys("Abcd123456")
        self.find_element(field_confirm_new_password).send_keys("Abcd123456")
        change_password = self.find_elements(change_button)
        change_password[3].click()
        message_change = self.find_element(message)
        return message_change.is_enabled()

    def change_role(self):
        radiobutton_role = self.find_elements(radiobutton)
        radiobutton_role[0].click()
        change = self.find_elements(change_button)
        change[0].click()
        message_change = self.find_element(message)
        assert message_change.is_enabled()
        radiobutton_role = self.find_elements(radiobutton)
        radiobutton_role[1].click()
        change = self.find_elements(change_button)
        change[0].click()
        message_change = self.find_element(message)
        assert message_change.is_enabled()

