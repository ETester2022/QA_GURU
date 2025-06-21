import pytest
import allure
from allure_commons.types import Severity
from test_hw11.registration_student_page import PegistrationStudentPage


# pytest -m test_label_issue -vv --clean-alluredir --alluredir=test_hw11/allure_results11
# allure serve test_hw11/allure_results11
@pytest.mark.test_label_issue
@allure.tag("web")
@allure.link("https://github.com")
@allure.label('owner', 'tster: Evgeniy')
@allure.title("тест на проверку отображения Issue Шаги с декоратором @allure.step")
@allure.severity(Severity.CRITICAL)
def test_label_issue(browser):

    registration_student = PegistrationStudentPage(browser)
    registration_student.open_main_page()
    registration_student.open_issues_page(repo="eroshenkoam/allure-example")
    registration_student.is_displayed(number="199")

