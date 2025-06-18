from test_hw9.pages.registration_page import RegistrationPage
from test_hw9.users.user import User


def test_fill_registration_form_student_hw9(driver):

    yasha = User(
        first_name = "My firstName",
        last_name = "My lastName",
        user_email = "My@userEmail.ru",
        phone = "8999888776",
        date = "15",
        picture = "64.jpg",
        subject = "subjectsContainer",
        address = "currentAddress",
        state = "NCR",
        city = "Delhi"
    )

    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.register(yasha)
    registration_page.should_have_registered(yasha)