from selenium.common import NoSuchElementException
from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


field_email = (By.CSS_SELECTOR, 'label[for="username"]')
field_password = (By.CSS_SELECTOR, 'label[for="password"]')
enter_button = (By.CLASS_NAME, 'UILoadingButton')
error_message = (By.CLASS_NAME, 'lvwq407')
avatar = (By.XPATH, '//div[@id="TopNavigationReactTarget"]/header/div/div[2]/div[4]')
setting_button = (By.XPATH, '//div[@ data-overlay-container="true"]')
create_button = (By.XPATH, '//*[@id="TopNavigationReactTarget"]/header/div/div[1]/div[2]/div[5]')
close_button = (By.XPATH, '//div[@aria-label="Закрыть диалоговое окно"]')
header = (By.XPATH, '//div[@id="TopNavigationReactTarget"]/header')
field_search = (By.XPATH, '//input[@id="GlobalSearchBar"]')
learn_modul = (By.CSS_SELECTOR, 'div[data-key="Учебные модули"]')
select_image = (By.CSS_SELECTOR, 'div[data-overlay-container="true"]')
image_symbol = (By.CLASS_NAME, 'AssemblyPillText')
name_modul = (By.CLASS_NAME, 'SetPreviewCard-title')


class AuthorizationPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_authorization_page(self):
        self.open_page()
        self.click_authorization_button()

    def enter_error_email(self):
        self.find_element(field_email).send_keys("Some_email@mail.com")

    def clear_email(self):
        self.find_element(field_email).send_keys(Keys.CONTROL + "a")
        self.find_element(field_email).send_keys(Keys.DELETE)

    def enter_right_email(self):
        self.find_element(field_email).send_keys("ekocm@mailto.plus")

    def enter_error_password(self):
        self.find_element(field_password).send_keys("1234")

    def clear_password(self):
        self.find_element(field_password).send_keys(Keys.CONTROL + "a")
        self.find_element(field_password).send_keys(Keys.DELETE)

    def enter_right_password(self):
        self.find_element(field_password).send_keys("Abcd123456")

    def enter_new_password(self):
        self.find_element(field_password).send_keys("Abcd$123456")

    def enter_next(self):
        self.find_element(enter_button).click()

    def check_error_message(self):
        message = self.find_element(error_message)
        return "ВЫ ВВЕЛИ НЕВЕРНЫЕ ДАННЫЕ ДЛЯ ВХОДА. ПОВТОРИТЕ ПОПЫТКУ." in message.text

    def check_avatar(self):
        check_avatar = self.find_element(avatar)
        return check_avatar.is_displayed()

    def log_out_account(self):
        self.find_element(avatar).click()
        log_out = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(log_out).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ENTER).perform()
        try:
            self.find_element(avatar).is_displayed()
        except NoSuchElementException:
            return True
        else:
            return False

    def change_theme(self):
        self.find_element(avatar).click()
        theme = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(theme).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def check_color_page(self):
        check_header = self.find_element(header)
        check_color = check_header.value_of_css_property("background-color")
        return check_color == 'rgba(255, 255, 255, 1)'

    def check_dark_color_page(self):
        check_header = self.find_element(header)
        check_color = check_header.value_of_css_property("background-color")
        return check_color == 'rgba(10, 9, 45, 1)'

    def click_setting(self):
        self.find_element(avatar).click()
        setting = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(setting).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN). \
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).\
            perform()

    def click_creation_modul(self):
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.find_element(close_button).click()

    def click_creation_folder(self):
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ENTER).perform()

    def click_creation_course(self):
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
