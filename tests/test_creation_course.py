from pages.creation_course_page import CreationCoursePage
from time import sleep


def test_creation_course_button(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    creation.open_creation_course_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_educational_institution()
    creation.choose_education()
    assert creation.check_create_button() is True
    sleep(2)


def test_creation_educational_institution(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    creation.open_creation_course_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_new_educational_institution()
    assert creation.check_create_button() is True


def test_delete_course(chrome_driver):
    creation = CreationCoursePage(chrome_driver)
    creation.open_creation_course_page()
    creation.enter_name_field()
    creation.enter_description_field()
    creation.enter_educational_institution()
    creation.choose_education()
    creation.click_create_button()
    creation.delete_course()
    assert creation.check_delete_course()

