from pages.solution_experts_page import SolutionExpertsPage


def test_choose_solutions_experts(chrome_driver):
    solution = SolutionExpertsPage(chrome_driver)
    solution.open_solution_experts_page()
    assert solution.choose_solutions_experts()


def test_search_field(chrome_driver):
    solution = SolutionExpertsPage(chrome_driver)
    solution.open_solution_experts_page()
    solution.check_search_field()
