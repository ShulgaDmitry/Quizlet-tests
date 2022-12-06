from selenium.common import NoSuchElementException
from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
solutions_experts = (By.CSS_SELECTOR, 'a[href="/explanations"]')
engineering = (By.CSS_SELECTOR, 'div[data-key="Инженерное дело"]')
choose_book = (By.CSS_SELECTOR, 'a[aria-label="Advanced Engineering Mathematics, 10th Edition"]')
chapter_1 = (By.CSS_SELECTOR, 'button[aria-label="Глава 1"]')
chapter_1_1 = (By.CSS_SELECTOR, 'button[aria-label="Раздел 1.1: Basic Concepts. Modeling"]')
all_steps_button = (By.CSS_SELECTOR, 'button[aria-label="Показать все шаги"]')
exercise = (By.CSS_SELECTOR, 'a[href="https://quizlet.com/explanations/textbook-solutions/'
                             'advanced-engineering-mathematics-10th-edition-9780470458365/'
                             'chapter-1-exercises-1-e41a24af-c7db-4502-a282-b71d7cfcd7bc"')


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
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        check_avatar = self.find_element(avatar)
        return check_avatar.is_displayed()

    def log_out_account(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
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
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(avatar).click()
        theme = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(theme).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))

    def check_color_page(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        check_header = self.find_element(header)
        check_color = check_header.value_of_css_property("background-color")
        return check_color == 'rgba(255, 255, 255, 1)'

    def check_dark_color_page(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        check_header = self.find_element(header)
        check_color = check_header.value_of_css_property("background-color")
        return check_color == 'rgba(10, 9, 45, 1)'

    def click_setting(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(avatar).click()
        setting = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(setting).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN). \
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).\
            perform()

    def click_solutions_experts(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(solutions_experts).click()

    def click_creation_modul(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.find_element(close_button).click()

    def click_creation_folder(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP).\
            send_keys(Keys.ENTER).perform()

    def click_creation_course(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be('https://quizlet.com/latest'))
        self.find_element(create_button).click()
        create = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(create).send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
