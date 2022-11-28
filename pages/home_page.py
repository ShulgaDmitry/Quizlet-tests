from pages.base_page import BasePage
from selenium.webdriver.common.by import By


registration_button = (By.CSS_SELECTOR, 'button[aria-label="Зарегистрироваться"]')
authorization_button = (By.CSS_SELECTOR, 'button[aria-label="Вход"]')


class HomePage(BasePage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_page(self):
        self.chrome_driver.get(self.base_url)

    def click_registration_button(self):
        self.find_element(registration_button).click()

    def click_authorization_button(self):
        self.find_element(authorization_button).click()

