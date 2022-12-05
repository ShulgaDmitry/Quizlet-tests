from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


engineering = (By.CSS_SELECTOR, 'div[data-key="Инженерное дело"]')
choose_book = (By.CSS_SELECTOR, 'a[aria-label="Advanced Engineering Mathematics, 10th Edition"]')
chapter_1 = (By.CSS_SELECTOR, 'button[aria-label="Глава 1"]')
chapter_1_1 = (By.CSS_SELECTOR, 'button[aria-label="Раздел 1.1: Basic Concepts. Modeling"]')
all_steps_button = (By.CSS_SELECTOR, 'button[aria-label="Показать все шаги"]')
search_field = (By.CSS_SELECTOR, 'input[placeholder="Поиск учебников, вопросов, ISBN"]')
title_book = (By.CLASS_NAME, 'TextbookCard-Title')
books = (By.CSS_SELECTOR, 'div[data-key="Учебники"]')
exercise = (By.CSS_SELECTOR, 'a[href="https://quizlet.com/explanations/textbook-solutions/'
                             'advanced-engineering-mathematics-10th-edition-9780470458365/'
                             'chapter-1-exercises-1-e41a24af-c7db-4502-a282-b71d7cfcd7bc"')


class SolutionExpertsPage(AuthorizationPage):
    def __init__(self, chrome_driver):
        super().__init__(chrome_driver)

    def open_solution_experts_page(self):
        authorization = AuthorizationPage(self.chrome_driver)
        authorization.open_authorization_page()
        authorization.enter_right_email()
        authorization.enter_right_password()
        authorization.enter_next()
        authorization.click_solutions_experts()

    def choose_solutions_experts(self):
        self.find_element(engineering).click()
        self.find_element(choose_book).click()
        self.find_element(chapter_1).click()
        self.find_element(chapter_1_1).click()
        self.find_element(exercise).click()
        all_steps = self.find_element(all_steps_button)
        return all_steps.is_enabled()

    def check_search_field(self):
        search = self.find_element(search_field)
        search.send_keys("Advanced Engineering Mathematics")
        search.send_keys(Keys.ENTER)
        self.find_element(books).click()
        titles = self.find_elements(title_book)
        list_title = []
        for title in titles:
            list_title.append(title.text)
        for each_title in list_title:
            assert "Advanced Engineering Mathematics" in each_title


