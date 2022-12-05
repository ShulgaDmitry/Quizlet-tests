from pages.authorization_page import AuthorizationPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


name_field = (By.ID, 'CreateFolderModal--name')
description_field = (By.CSS_SELECTOR, 'label[for="CreateFolderModal--description"]')
create_button = (By.CSS_SELECTOR, 'button[aria-label="Создать папку"]')
setting_button = (By.CLASS_NAME, 'MenuIconWithTooltip')
delete_button = (By.CSS_SELECTOR, 'svg[aria-label="delete"]')
confirm_delete_button = (By.CSS_SELECTOR, 'button[class="UIButton UIButton--alert UIButton--fill UIButton--hero"]')
add_modul = (By.CSS_SELECTOR, 'button[title="Добавить модули"]')
create_modul = (By.CSS_SELECTOR, 'a[aria-label="+ Создать новый модуль"]')
close_button = (By.CSS_SELECTOR, 'div[aria-label="Закрыть диалоговое окно"]')
avatar = (By.XPATH, '//div[@id="TopNavigationReactTarget"]/header/div/div[2]/div[4]')
profile_button = (By.XPATH, '//div[@ data-overlay-container="true"]')
folders_button = (By.CSS_SELECTOR, 'div[data-key="PROFILE_TABS.FOLDERS"]')
our_folder = (By.CSS_SELECTOR, 'a[aria-label="Test"]')
check_banner = (By.CSS_SELECTOR, 'img[alt="Нет папок в библиотеке"]')
main = (By.CSS_SELECTOR, 'a[href="/latest"]')


class CreationFolderPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_creation_folder_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()
        authorization.click_creation_folder()

    def enter_name_field(self):
        self.find_element(name_field).send_keys("Test")

    def enter_description_field(self):
        self.find_element(description_field).send_keys("Testing")

    def check_create_button(self):
        create = self.find_element(create_button)
        return create.is_enabled()

    def click_create_button(self):
        self.find_element(create_button).click()

    def delete_folder(self):
        list_setting = self.find_elements(setting_button)
        ActionChains(self.chrome_driver).move_to_element(list_setting[2]).click(list_setting[2]).pause(1).perform()
        choose_delete = WebDriverWait(self.chrome_driver, 3).until(EC.element_to_be_clickable(delete_button))
        choose_delete.click()
        self.find_element(confirm_delete_button).click()

    def check_delete_folder(self):
        WebDriverWait(self.chrome_driver, 3).until(EC.url_to_be("https://quizlet.com/latest"))
        self.find_element(avatar).click()
        profile = self.find_element(profile_button)
        ActionChains(self.chrome_driver).click(profile).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN). \
            send_keys(Keys.ENTER).perform()
        self.find_element(folders_button).click()
        banner = self.find_element(check_banner)
        return banner.is_enabled()

    def addition_modul(self):
        self.find_element(add_modul).click()
        self.find_element(create_modul).click()

    def check_url_creation_modul(self):
        creation_url = self.chrome_driver.current_url
        return 'https://quizlet.com/create-set' in creation_url

    def close_banner(self):
        self.find_element(close_button).click()

    def open_profile(self):
        self.find_element(main).click()
        WebDriverWait(self.chrome_driver, 3).until(EC.url_to_be("https://quizlet.com/latest"))
        self.find_element(avatar).click()
        profile = self.find_element(profile_button)
        ActionChains(self.chrome_driver).click(profile).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).\
            send_keys(Keys.ENTER).perform()
        self.find_element(folders_button).click()
        self.find_element(our_folder).click()


