from selenium.common import NoSuchElementException
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


avatar = (By.XPATH, '//div[@id="TopNavigationReactTarget"]/header/div/div[2]/div[4]')
birth_date = (By.CSS_SELECTOR, 'select[aria-label="birth_day"]')
birth_month = (By.CSS_SELECTOR, 'select[aria-label="birth_month"]')
birth_year = (By.CSS_SELECTOR, 'select[aria-label="birth_year"]')
register_field_email = (By.CSS_SELECTOR, 'label[for="email"]')
register_field_name = (By.CSS_SELECTOR, 'label[for="username"]')
register_field_password = (By.CSS_SELECTOR, 'label[for="password1"]')
register_button = (By.XPATH, '//button[@class="UIButton UIButton--fill"]')
checkbox = (By.CSS_SELECTOR, 'input[name="TOS"]')
setting_button = (By.XPATH, '//div[@ data-overlay-container="true"]')
delete_button = (By.CSS_SELECTOR, 'a[href="/delete-account"]')
delete_field_password = (By.CLASS_NAME, 'UIInput-input')
continue_button = (By.CLASS_NAME, 'UIButton-wrapper')
delete_account_button = (By.CLASS_NAME, 'UIButton-wrapper')
checkbox_adult = (By.CSS_SELECTOR, 'input[name="is_parent"]')
checkbox_teacher = (By.CSS_SELECTOR, 'input[name="is_free_teacher"]')
return_main_page = (By.CSS_SELECTOR, 'a[href="/ru"]')


class RegistrationPage(HomePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_registration_page(self):
        self.open_page()
        self.click_registration_button()

    def reopen_page(self):
        WebDriverWait(self.chrome_driver, 5).\
            until(EC.url_to_be("https://quizlet.com/upgrade?source=signup&redir=https%3A%2F%2Fquizlet.com%2Fru"))
        self.open_page()

    def select_birth_date(self):
        select_date = Select(self.find_element(birth_date))
        select_date.select_by_value("16")

    def select_birth_month(self):
        select_month = Select(self.find_element(birth_month))
        select_month.select_by_value("5")

    def select_birth_year(self):
        select_year = Select(self.find_element(birth_year))
        select_year.select_by_visible_text("2002")

    def select_birth_minor_year(self):
        select_year = Select(self.find_element(birth_year))
        select_year.select_by_visible_text("2003")

    def enter_new_email(self):
        self.find_element(register_field_email).send_keys("aapbyw@mailto.plus")

    def enter_new_name(self):
        letters = string.ascii_letters
        name = "".join(random.sample(letters, 10))
        self.find_element(register_field_name).send_keys(name)

    def enter_new_password(self):
        self.find_element(register_field_password).send_keys("Abcd123456")

    def checkbox_true(self):
        self.find_element(checkbox).click()

    def checkbox_adult_true(self):
        adult_check = self.find_element(checkbox_adult)
        return adult_check.is_enabled()

    def checkbox_adult_absent(self):
        try:
            self.find_element(checkbox_adult).is_enabled()
        except NoSuchElementException:
            return True
        else:
            return False

    def checkbox_teacher_true(self):
        teacher_check = self.find_element(checkbox_teacher)
        return teacher_check.is_enabled()

    def checkbox_teacher_absent(self):
        try:
            self.find_element(checkbox_teacher).is_enabled()
        except NoSuchElementException:
            return True
        else:
            return False

    def check_button_register(self):
        WebDriverWait(self.chrome_driver, 5).until_not(EC.element_attribute_to_include(register_button, "disabled"))
        check_button = self.find_element(register_button)
        return check_button.is_enabled()

    def enter_register(self):
        WebDriverWait(self.chrome_driver, 5).until_not(EC.element_attribute_to_include(register_button, "disabled"))
        self.find_element(register_button).click()

    def check_avatar(self):
        WebDriverWait(self.chrome_driver, 5).until(EC.url_to_be("https://quizlet.com/latest"))
        avatar_logo = self.find_element(avatar)
        return avatar_logo.is_displayed()

    def setting_button(self):
        self.find_element(avatar).click()
        setting = self.find_element(setting_button)
        ActionChains(self.chrome_driver).click(setting).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ENTER).perform()

    def delete_account(self):
        self.window_scroll()
        self.find_element(delete_button).click()
        self.find_element(delete_field_password).send_keys("Abcd123456")
        self.find_element(continue_button).click()
        self.find_element(delete_account_button).click()

    def check_account_deletion(self):
        self.window_scroll()
        self.find_element(delete_button).click()
        self.find_element(delete_field_password).send_keys("Abcd123456")
        self.find_element(continue_button).click()
        self.find_element(delete_account_button).click()
        self.find_element(return_main_page).click()
        home_url = self.chrome_driver.current_url
        return "https://quizlet.com/ru" in home_url
