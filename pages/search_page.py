from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


field_search = (By.XPATH, '//input[@id="GlobalSearchBar"]')
learn_modul = (By.CSS_SELECTOR, 'div[data-key="Учебные модули"]')
select_image = (By.CSS_SELECTOR, 'div[data-overlay-container="true"]')
image_symbol = (By.CLASS_NAME, 'AssemblyPillText')
name_modul = (By.CLASS_NAME, 'SetPreviewCard-title')
modul_card = (By.CLASS_NAME, 'SetPreviewCard-metadata')
add_button = (By.CSS_SELECTOR, 'button[aria-label="add"]')
choose_folder = (By.CSS_SELECTOR, 'div[data-key="folder"]')
click_create_folder = (By.CSS_SELECTOR, 'button[aria-label="+ Создать новую папку"]')
name_field = (By.ID, 'CreateFolderModal--name')
create_button = (By.CSS_SELECTOR, 'button[aria-label="Создать папку"]')
modul_card_folder = (By.CLASS_NAME, 'UISetCard')
setting_button = (By.CLASS_NAME, 'MenuIconWithTooltip')
delete_button = (By.CSS_SELECTOR, 'svg[aria-label="delete"]')
confirm_delete_button = (By.CSS_SELECTOR, 'button[class="UIButton UIButton--alert UIButton--fill UIButton--hero"]')


class SearchPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_search_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()

    def check_search(self):
        search = self.find_element(field_search)
        search.send_keys("English")
        search.send_keys(Keys.ENTER)
        self.find_element(learn_modul).click()
        names = self.find_elements(name_modul)
        list_name = []
        for name in names:
            list_name.append(name.text)
        for each_name in list_name:
            assert "English" or "ENGLISH" in each_name

    def check_filter(self):
        search = self.find_element(field_search)
        search.send_keys("English")
        search.send_keys(Keys.ENTER)
        self.find_element(learn_modul).click()
        type_modul = self.find_elements(select_image)
        ActionChains(self.chrome_driver).click(type_modul[5]).send_keys(Keys.ARROW_DOWN). \
            send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        images = self.find_elements(image_symbol)
        list_image = []
        for image in images:
            list_image.append(image.text)
        count = 0
        for each_image in list_image:
            if each_image == "Изображения":
                count += 1
        return count == 8

    def additions_other_modul(self):
        search = self.find_element(field_search)
        search.send_keys("English")
        search.send_keys(Keys.ENTER)
        self.find_element(learn_modul).click()
        modul = self.find_elements(modul_card)
        modul[0].click()
        self.find_element(add_button).click()
        self.find_element(choose_folder).click()
        self.find_element(click_create_folder).click()
        self.find_element(name_field).send_keys("Test")
        self.find_element(create_button).click()
        card = self.find_element(modul_card_folder)
        return card.is_enabled()

    def delete_folder(self):
        list_setting = self.find_elements(setting_button)
        ActionChains(self.chrome_driver).move_to_element(list_setting[3]).click(list_setting[3]).pause(1).perform()
        choose_delete = WebDriverWait(self.chrome_driver, 3).until(EC.element_to_be_clickable(delete_button))
        choose_delete.click()
        self.find_element(confirm_delete_button).click()
