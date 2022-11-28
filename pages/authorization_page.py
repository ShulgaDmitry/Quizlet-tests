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
log_out_button = (By.XPATH, '//div[@ data-overlay-container="true"]')
create_button = (By.XPATH, '//*[@id="TopNavigationReactTarget"]/header/div/div[1]/div[2]/div[5]')
choose_button = (By.XPATH, '//div[@ data-overlay-container="true"]')
close_button = (By.XPATH, '//div[@aria-label="Закрыть диалоговое окно"]')


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
        log_out = self.find_element(log_out_button)
        ActionChains(self.chrome_driver).click(log_out).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ENTER).perform()
        try:
            self.find_element(avatar).is_displayed()
        except NoSuchElementException:
            return True
        else:
            return False

    def click_creation_modul(self):
        self.find_element(create_button).click()
        create = self.find_element(choose_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
        self.find_element(close_button).click()

    def click_creation_folder(self):
        self.find_element(create_button).click()
        create = self.find_element(choose_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ENTER).perform()

    def click_creation_course(self):
        self.find_element(create_button).click()
        create = self.find_element(choose_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
