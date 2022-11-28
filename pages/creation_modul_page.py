from pages.authorization_page import AuthorizationPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


name_field = (By.XPATH, '//textarea[@tabindex="5"]')
description_field = (By.XPATH, '//textarea[@tabindex="6"]')
create_button = (By.CLASS_NAME, 'CreateSetHeader-infoButtonWrap')
error_message_modul = (By.CLASS_NAME, 'UINotice-message')
term_field = (By.XPATH, '//div[@tabindex="7"]')
card_field = (By.XPATH, '//div[@tabindex="7"]')
choose_language = (By.XPATH, '//button[@class="UILink is-Popover is-Tooltip UIOverlayTrigger-target"]')
english_button = (By.ID, 'react-select-2--option-1')
russian_button = (By.ID, 'react-select-3--option-12')
user_link = (By.CLASS_NAME, 'UserLink')
delete_button = (By.CSS_SELECTOR, 'div[data-overlay-container="true"]')
confirm_delete_button = (By.CLASS_NAME, 'UIButton-wrapper')
close_button = (By.CSS_SELECTOR, 'div[class="UIModalHeader-closeIconButton"]')
click_modul = (By.CSS_SELECTOR, 'div[data-testid="AssemblyTooltip--base"]')
image_button = (By.CLASS_NAME, 'ImageUploadComponent')
image = (By.CLASS_NAME, 'ImageCarousel-imageWrap')
check_image = (By.CLASS_NAME, 'ZoomableImage')


class CreationModulPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_creation_modul_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()
        authorization.click_creation_modul()

    def enter_name_field(self):
        self.find_element(name_field).send_keys("Test")

    def enter_description_field(self):
        self.find_element(description_field).send_keys("Testing")

    def click_create_button(self):
        self.find_element(create_button).click()

    def check_error_modul_message(self):
        message = self.find_element(error_message_modul)
        return "НЕОБХОДИМО КАК МИНИМУМ ДВЕ КАРТОЧКИ, ЯЗЫК ТЕРМИНА И ЯЗЫК ОПРЕДЕЛЕНИЯ, ЧТОБЫ СОХРАНИТЬ МОДУЛЬ." \
               in message.text

    def enter_term_field_1(self):
        term = self.find_elements(card_field)
        term[0].send_keys("Home")

    def enter_term_field_2(self):
        term = self.find_elements(card_field)
        term[2].send_keys("Job")

    def enter_definition_field_1(self):
        definition = self.find_elements(card_field)
        definition[1].send_keys("Дом")

    def enter_definition_field_2(self):
        definition = self.find_elements(card_field)
        definition[3].send_keys("Работа")

    def choose_language_1(self):
        self.find_element(choose_language).click()
        self.find_element(english_button).click()

    def choose_language_2(self):
        self.find_element(choose_language).click()
        self.find_element(russian_button).click()

    def close_banner(self):
        self.find_element(close_button).click()

    def check_user_link(self):
        link = self.find_element(user_link)
        return link.is_enabled()

    def delete_modul(self):
        delete = self.find_elements(delete_button)
        ActionChains(self.chrome_driver).click(delete[2]).send_keys(Keys.ARROW_UP). \
            send_keys(Keys.ENTER).perform()
        confirm = self.find_elements(confirm_delete_button)
        confirm[2].click()

    def change_modul(self):
        change_button = self.find_elements(click_modul)
        change_button[5].click()

    def add_image(self):
        add_image = self.find_element(image_button)
        add_image.click()
        choose_image = self.find_elements(image)
        choose_image[0].click()

    def check_image(self):
        special_image = self.find_element(check_image)
        return special_image.is_enabled()
