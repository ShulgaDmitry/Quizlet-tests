from pages.expert_decision_page import ExpertDecisionPage
import allure


@allure.feature("Experts decision")
@allure.story("Exercises")
def test_choose_solutions_experts(chrome_driver):
    decision = ExpertDecisionPage(chrome_driver)
    with allure.step("Open solution experts page"):
        decision.open_solution_experts_page()
    with allure.step("Check opening exercises"):
        assert decision.choose_solutions_experts()


@allure.feature("Experts decision")
@allure.story("Search in solution experts")
def test_search_field(chrome_driver):
    decision = ExpertDecisionPage(chrome_driver)
    with allure.step("Open solution experts page"):
        decision.open_solution_experts_page()
    with allure.step("Check search"):
        decision.check_search_field(book="Advanced Engineering Mathematics")
