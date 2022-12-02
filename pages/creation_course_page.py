from selenium.webdriver.support.select import Select
from pages.authorization_page import AuthorizationPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


name_field = (By.ID, 'CreateClassModal-class-name')
description_field = (By.CSS_SELECTOR, 'label[for="CreateClassModal-class-description"]')
education_field = (By.CSS_SELECTOR, 'input[aria-label="Введите название своего учебного заведения"]')
choose_educational_institution = (By.ID, 'react-autowhatever-1--item-0')
create_button = (By.CSS_SELECTOR, 'button[aria-label="Создать курс"]')
add_education = (By.CSS_SELECTOR, 'button[aria-label="+ Добавить"]')
country = (By.CSS_SELECTOR, 'select[class="d15dqdef"]')
city = (By.CSS_SELECTOR, 'input[aria-label="Город"]')
setting_button = (By.CLASS_NAME, 'MenuIconWithTooltip')
delete_button = (By.CSS_SELECTOR, 'svg[aria-label="delete"]')
confirm_delete_button = (By.CSS_SELECTOR, 'button[class="UIButton UIButton--alert UIButton--fill UIButton--hero"]')
close = (By.CLASS_NAME, 'r1lhaaik')


class CreationCoursePage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_creation_course_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()
        authorization.click_creation_course()

    def enter_name_field(self):
        self.find_element(name_field).send_keys("Test")

    def enter_description_field(self):
        self.find_element(description_field).send_keys("Testing")

    def enter_educational_institution(self):
        try:
            close_button = self.find_element(close)

        except NoSuchElementException:
            pass

        else:
            close_button.click()

        WebDriverWait(self.chrome_driver, 2).until(EC.element_to_be_clickable(education_field)).send_keys("БНТУ")

    def choose_education(self):
        education = self.find_elements(choose_educational_institution)
        education[0].click()

    def enter_new_educational_institution(self):
        try:
            close_button = self.find_element(close)

        except NoSuchElementException:
            pass

        else:
            close_button.click()

        WebDriverWait(self.chrome_driver, 2).until(EC.element_to_be_clickable(education_field)).send_keys("Test")
        self.window_scroll()
        self.find_element(add_education).click()
        select_country = self.find_elements(country)
        choose_country = Select(select_country[1])
        choose_country.select_by_value("by")
        self.find_element(city).send_keys("Minsk")

    def check_create_button(self):
        create = self.find_element(create_button)
        return create.is_enabled()

    def click_create_button(self):
        self.find_element(create_button).click()

    def delete_course(self):
        list_setting = self.find_elements(setting_button)
        ActionChains(self.chrome_driver).move_to_element(list_setting[3]).click(list_setting[3]).pause(1).perform()
        WebDriverWait(self.chrome_driver, 3).until(EC.element_to_be_clickable(delete_button)).click()
        self.find_element(confirm_delete_button).click()

    def check_url_delete_course(self):
        delete_url = self.chrome_driver.current_url
        return "https://quizlet.com/latest" in delete_url
