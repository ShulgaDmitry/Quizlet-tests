from pages.authorization_page import AuthorizationPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


name_field = (By.XPATH, '//textarea[@tabindex="5"]')
description_field = (By.XPATH, '//textarea[@tabindex="6"]')
create_button = (By.CLASS_NAME, 'CreateSetHeader-infoButtonWrap')
error_message_modul = (By.CLASS_NAME, 'UINotice-message')
term_field = (By.XPATH, '//div[@tabindex="7"]')
card_field = (By.XPATH, '//div[@tabindex="7"]')
choose_language = (By.XPATH, '//button[@class="UILink is-Popover is-Tooltip UIOverlayTrigger-target"]')
english_button = (By.XPATH, '//div[@id="react-select-2--option-1"]')
russian_button = (By.XPATH, '//div[@id="react-select-3--option-12"]')
user_link = (By.CLASS_NAME, 'UserLink')
delete_button = (By.CSS_SELECTOR, 'div[data-overlay-container="true"]')
confirm_delete_button = (By.CSS_SELECTOR, 'button[aria-label="Да, удалить модуль"]')
close_banner_button = (By.CSS_SELECTOR, 'div[aria-label="Закрыть диалоговое окно"]')
click_modul = (By.CSS_SELECTOR, 'div[data-testid="AssemblyTooltip--base"]')
image_button = (By.CLASS_NAME, 'ImageUploadComponent')
image = (By.CLASS_NAME, 'ImageCarousel-imageWrap')
check_image = (By.CLASS_NAME, 'ZoomableImage')
next_card = (By.CSS_SELECTOR, 'div[aria-label="Нажмите для изучения следующей карточки"]')
congratulation = (By.CLASS_NAME, 'hralq3g')
come_back = (By.CLASS_NAME, 'hideBelow--m')
select_button = (By.CSS_SELECTOR, 'svg[aria-label="режим подбора"]')
start_game = (By.CSS_SELECTOR, 'button[aria-label="Начать игру"]')
play_again = (By.CSS_SELECTOR, 'button[aria-label="Играть снова"]')
back = (By.CSS_SELECTOR, 'a[data-testid="UILink-anchor"]')
card_job_rus = (By.CSS_SELECTOR, 'div[aria-label="Работа"]')
card_job = (By.CSS_SELECTOR, 'div[aria-label="Job"]')
card_home_rus = (By.CSS_SELECTOR, 'div[aria-label="Дом"]')
card_home = (By.CSS_SELECTOR, 'div[aria-label="Home"]')
congratulatory_banner = (By.CLASS_NAME, 'UIModalBody')
memorize_button = (By.CSS_SELECTOR, 'svg[aria-label="режим заучивания"]')
test_button = (By.CSS_SELECTOR, 'svg[aria-label="режим тестирования"]')
english_answer = (By.CSS_SELECTOR, 'input[aria-label="Введите ответ (язык: Английский)"]')
answer_button = (By.CSS_SELECTOR, 'button[aria-label="Далее"]')
send_answer_button = (By.CSS_SELECTOR, 'button[aria-label="Отправить тест"]')
check = (By.CSS_SELECTOR, 'div[data-testid="primary-count"]')
control_word = (By.CSS_SELECTOR, 'div[style="display: block;"]')
continue_button = (By.CSS_SELECTOR, 'button[aria-label="Продолжить"]')
long_term_answer_home = (By.CSS_SELECTOR, 'div[aria-label="Home"]')
long_term_answer_job = (By.CSS_SELECTOR, 'div[aria-label="Job"]')
round_2 = (By.CSS_SELECTOR, 'button[aria-label="Перейти к раунду 2"]')
close = (By.CSS_SELECTOR, 'button[aria-label="Назад к модулю"]')
new_window = (By.CSS_SELECTOR, 'div[data-testid="lowKnowledge"]')
next_answer_button = (By.CSS_SELECTOR, 'button[aria-label="Ответить"]')
next_answer = (By.CSS_SELECTOR, 'input[aria-label="Введите ответ (язык: Английский)"]')
cup = (By.CLASS_NAME, 'imwizko')
bottom_banner = (By.CSS_SELECTOR, 'div[aria-live="polite"]')
close_test = (By.CSS_SELECTOR, 'button[aria-label="Назад"]')


class CreationModulPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_creation_modul_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email(right_email="ekocm@mailto.plus")
        authorization.enter_right_password(right_password="Abcd123456")
        authorization.enter_next()
        authorization.click_creation_modul()

    def enter_name_field(self, name):
        self.find_element(name_field).send_keys(name)

    def enter_description_field(self, description):
        self.find_element(description_field).send_keys(description)

    def click_create_button(self):
        self.find_element(create_button).click()
        WebDriverWait(self.chrome_driver, 3).until(EC.invisibility_of_element_located(create_button))

    def check_error_modul_message(self):
        self.find_element(create_button).click()
        message = self.find_element(error_message_modul)
        return "НЕОБХОДИМО КАК МИНИМУМ ДВЕ КАРТОЧКИ, ЯЗЫК ТЕРМИНА И ЯЗЫК ОПРЕДЕЛЕНИЯ, ЧТОБЫ СОХРАНИТЬ МОДУЛЬ." \
               in message.text

    def enter_term_field_1(self, first_word):
        term = self.find_elements(card_field)
        term[0].send_keys(first_word)

    def enter_term_field_2(self, third_word):
        term = self.find_elements(card_field)
        term[2].send_keys(third_word)

    def enter_definition_field_1(self, second_word):
        definition = self.find_elements(card_field)
        definition[1].send_keys(second_word)

    def enter_definition_field_2(self, fourth_word):
        definition = self.find_elements(card_field)
        definition[3].send_keys(fourth_word)

    def choose_language_1(self):
        self.find_element(choose_language).click()
        WebDriverWait(self.chrome_driver, 5).until(EC.presence_of_element_located(english_button)).click()

    def choose_language_2(self):
        self.find_element(choose_language).click()
        WebDriverWait(self.chrome_driver, 5).until(EC.presence_of_element_located(russian_button)).click()

    def close_banner(self):
        WebDriverWait(self.chrome_driver, 8).until(EC.element_to_be_clickable(close_banner_button)).click()

    def check_user_link(self):
        link = self.find_element(user_link)
        return link.is_enabled()

    def delete_modul(self):
        delete = self.find_elements(delete_button)
        ActionChains(self.chrome_driver).click(delete[2]).send_keys(Keys.ARROW_UP). \
            send_keys(Keys.ENTER).perform()
        yes_button = self.find_element(confirm_delete_button)
        yes_button.click()

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

    def click_next_card(self):
        self.find_element(next_card).click()
        self.find_element(next_card).click()
        congratulations = self.find_element(congratulation)
        assert "Поздравляем! Вы повторили все карточки." in congratulations.text
        self.find_element(come_back).click()

    def click_selection(self):
        self.find_element(select_button).click()
        self.find_element(start_game).click()
        left_home = self.find_element(card_home_rus)
        right_home = self.find_element(card_home)
        ActionChains(self.chrome_driver).pause(3).drag_and_drop(left_home, right_home).perform()
        left_job = self.find_element(card_job_rus)
        right_job = self.find_element(card_job)
        ActionChains(self.chrome_driver).drag_and_drop(left_job, right_job).perform()
        assert self.find_element(congratulatory_banner).is_enabled()
        self.find_element(play_again).click()
        WebDriverWait(self.chrome_driver, 3).until(EC.element_to_be_clickable(back)).click()

    def click_memorization(self):
        self.find_element(test_button).click()
        first_word = self.find_elements(control_word)
        if first_word[0].text == "Дом":
            first = self.find_elements(english_answer)
            first[0].send_keys("Home")
            self.find_element(answer_button).click()
            second = self.find_elements(english_answer)
            second[1].send_keys("Job")
            self.find_element(send_answer_button).click()
        else:
            second = self.find_elements(english_answer)
            second[0].send_keys("Job")
            self.find_element(answer_button).click()
            first = self.find_elements(english_answer)
            first[1].send_keys("Home")
            self.find_element(send_answer_button).click()

        WebDriverWait(self.chrome_driver, 5).until(EC.presence_of_element_located(check))
        checks = self.find_element(check)
        assert "2" == checks.text
        self.find_element(close_test).click()

    def click_long_term_memorization_round_1(self):
        self.find_element(memorize_button).click()
        #self.find_element(continue_button).click()
        # WebDriverWait(self.chrome_driver, 3).until(EC.presence_of_element_located(new_window))
        # self.find_element(continue_button).click()
        first_word = self.find_element(control_word)
        if first_word.text == "Дом":
            self.find_element(long_term_answer_home).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Работа"))
            self.find_element(long_term_answer_job).click()
        else:
            self.find_element(long_term_answer_job).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Дом"))
            self.find_element(long_term_answer_home).click()

        banner = self.find_element(bottom_banner)
        assert banner.is_enabled()
        self.find_element(close).click()

    def click_long_term_memorization_round_2(self):
        self.find_element(memorize_button).click()
        # self.find_element(continue_button).click()
        # WebDriverWait(self.chrome_driver, 3).until(EC.presence_of_element_located(new_window))
        # self.find_element(continue_button).click()
        first_word = self.find_element(control_word)
        if first_word.text == "Дом":
            self.find_element(long_term_answer_home).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Работа"))
            self.find_element(long_term_answer_job).click()
        else:
            self.find_element(long_term_answer_job).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Дом"))
            self.find_element(long_term_answer_home).click()

        next_round = self.find_elements(round_2)
        next_round[1].click()
        first_word = self.find_element(control_word)
        if first_word.text == "Дом":
            self.find_element(next_answer).send_keys("Home")
            self.find_element(next_answer_button).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Работа"))
            self.find_element(next_answer).send_keys("Job")
            self.find_element(next_answer_button).click()
        else:
            self.find_element(next_answer).send_keys("Job")
            self.find_element(next_answer_button).click()
            WebDriverWait(self.chrome_driver, 3).until(EC.text_to_be_present_in_element(control_word, "Дом"))
            self.find_element(next_answer).send_keys("Home")
            self.find_element(next_answer_button).click()

        cup_image = self.find_element(cup)
        assert cup_image.is_enabled()
        self.find_element(close).click()
