from selenium.common import NoSuchElementException
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
error_password = (By. CLASS_NAME, 'lvwq407')


class SettingPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_setting_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email(right_email="ekocm@mailto.plus")
        authorization.enter_right_password(right_password="Abcd123456")
        authorization.enter_next()
        try:
            self.find_element(error_password).is_enabled()
        except NoSuchElementException:
            authorization.click_setting()
        else:
            authorization.clear_password()
            authorization.enter_new_password(new_password="Abcd$123456")
            authorization.enter_next()
            authorization.click_setting()
            self.find_element(field_old_password).send_keys("Abcd$123456")
            self.find_element(field_new_password).send_keys("Abcd123456")
            self.find_element(field_confirm_new_password).send_keys("Abcd123456")
            change_password = self.find_elements(change_button)
            change_password[3].click()

    def open_setting_page_with_new_password(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_page()
        authorization.log_out_account()
        WebDriverWait(self.chrome_driver, 5).until(EC.url_contains("https://quizlet.com/goodbye"))
        authorization.click_authorization_button()
        authorization.enter_right_email(right_email="ekocm@mailto.plus")
        authorization.enter_new_password(new_password="Abcd$123456")
        authorization.enter_next()
        authorization.click_setting()

    def change_avatar(self):
        self.find_element(new_avatar).click()
        WebDriverWait(self.chrome_driver, 5).until(EC.text_to_be_present_in_element_attribute(new_avatar, 'class',
                                                                                              'animal selected'))
        new = self.find_element(place_avatar)
        new_image = new.get_attribute("src")
        return 'https://assets.quizlet.com/a/j/dist/app/i/animals/45.069bd0ea8329543.jpg' in new_image

    def return_avatar(self):
        self.find_element(old_avatar).click()
        WebDriverWait(self.chrome_driver, 5).until(EC.text_to_be_present_in_element_attribute(old_avatar, 'class',
                                                                                              'animal selected'))
        new = self.find_elements(place_avatar)
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

    def change_password(self, old_password, new_password):
        self.find_element(field_old_password).send_keys(old_password)
        self.find_element(field_new_password).send_keys(new_password)
        self.find_element(field_confirm_new_password).send_keys(new_password)
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

