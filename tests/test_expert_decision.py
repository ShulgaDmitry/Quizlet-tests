from pages.expert_decision_page import ExpertDecisionPage


def test_choose_solutions_experts(chrome_driver):
    decision = ExpertDecisionPage(chrome_driver)
    decision.open_solution_experts_page()
    assert decision.choose_solutions_experts()


def test_search_field(chrome_driver):
    decision = ExpertDecisionPage(chrome_driver)
    decision.open_solution_experts_page()
    decision.check_search_field()
