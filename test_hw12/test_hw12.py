import pytest
import allure
from allure_commons.types import Severity
from test_hw12.registration_student_page_hw12 import PegistrationStudentPage12


# pytest -m test_fill_registration_form_std -vv --clean-alluredir --alluredir=test_hw11/allure_results12
# allure serve test_hw12/allure_results12
@pytest.mark.test_fill_registration_form_std
@allure.tag("web")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.label('owner', 'tster: Evgeniy')
@allure.title("тест на отображение внесенных данных с декоратором @allure.step")
@allure.severity(Severity.CRITICAL)
def test_fill_registration_form_std(browser):

    text_header = "Thanks for submitting the form"
    first_name = "My firstName"
    last_name = "My lastName"
    user_email = "My@userEmail.ru"
    phone = "8999888776"
    date = "15"
    picture = "64.jpg"
    subject = "subjectsContainer"
    adress = "currentAddress"
    state = "NCR"
    city = "Delhi"

    expected_result = [
        f"{first_name} {last_name}",
        f"{user_email}",
        "Male",
        f"{phone}",
        f"{date} July,2025",
        f"{picture}",
        f"{subject}",
        "Sports",
        f"{adress}",
        f"{state} {city}"
    ]


    registration_student = PegistrationStudentPage12(browser)
    registration_student.open_main_page()
    registration_student.fill_first_name(first_name)
    registration_student.fill_last_name(last_name)
    registration_student.fill_user_email(user_email)
    registration_student.radio_btn_male()
    registration_student.fill_phone(phone)
    registration_student.select_date(date)
    registration_student.fill_subject(subject)
    registration_student.radio_btn_sports()
    registration_student.upload_picture(picture)
    registration_student.fill_adress(adress)
    registration_student.select_state(state)
    registration_student.select_city(city)
    registration_student.submit_btn()

    registration_student.should_be_header(text_header)
    registration_student.should_be_result(expected_result)


