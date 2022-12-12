from pages.creation_course_page import CreationCoursePage
import allure


@allure.feature("Creation course")
@allure.story("Button disabled until all data has been entered")
def test_creation_course_button(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    with allure.step("Open course page"):
        creation.open_creation_course_page()
    with allure.step("Enter name field"):
        creation.enter_name_field(name="Test")
    with allure.step("Enter description field"):
        creation.enter_description_field(description="Testing")
    with allure.step("Enter educational institution"):
        creation.enter_educational_institution(education="БНТУ")
    with allure.step("Choose institute"):
        creation.choose_education()
    with allure.step("Check that button is enabled"):
        assert creation.check_create_button() is True


@allure.feature("Creation course")
@allure.story("Addiction new institute")
def test_creation_educational_institution(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    with allure.step("Open course page"):
        creation.open_creation_course_page()
    with allure.step("Enter name field"):
        creation.enter_name_field(name="Test")
    with allure.step("Enter description field"):
        creation.enter_description_field(description="Testing")
    with allure.step("Create new educational institution"):
        creation.enter_new_educational_institution(new_education="Test")
    with allure.step("Check that button is enabled"):
        assert creation.check_create_button() is True


@allure.feature("Creation course")
@allure.story("Delete course")
def test_delete_course(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    with allure.step("Open course page"):
        creation.open_creation_course_page()
    with allure.step("Enter name field"):
        creation.enter_name_field(name="Test")
    with allure.step("Enter description field"):
        creation.enter_description_field(description="Testing")
    with allure.step("Enter educational institution"):
        creation.enter_educational_institution(education="БНТУ")
    with allure.step("Choose educational institution"):
        creation.choose_education()
    with allure.step("Click create button"):
        creation.click_create_button()
    with allure.step("Delete course"):
        creation.delete_course()
    with allure.step("Check that banner is enabled"):
        assert creation.check_delete_course()

