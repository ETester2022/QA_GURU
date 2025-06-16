from test_hw9.pages.registration_page import RegistrationPage



def test_fill_registration_form_student_hw9(driver):

    header="Thanks for submitting the form"
    first_name = "My firstName"
    last_name = "My lastName"
    user_email = "My@userEmail.ru"
    phone = "8999888776"
    date = "15"
    picture = "64.jpg"
    subject = "subjectsContainer"
    address = "currentAddress"
    state = "NCR"
    city = "Delhi"

    expected_result = [
    f"{first_name} {last_name}",
    f"{user_email}",
    "Male",
    f"{phone}",
    f"{date} June,2025",
    f"{picture}",
    f"{subject}",
    "Sports",
    f"{address}",
    f"{state} {city}"
    ]

    registration_page = RegistrationPage(driver)
    registration_page.open()
    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_email(user_email)
    registration_page.select_gender_male()
    registration_page.fill_mobile(phone)
    registration_page.select_date(date)
    registration_page.fill_subject(subject)
    registration_page.select_hobbie_sports()
    registration_page.add_picture(picture)
    registration_page.fill_current_address(address)
    registration_page.select_state(state)
    registration_page.select_city(city)
    registration_page.submit()

    registration_page.should_have_header(header)
    registration_page.should_have_registered(expected_result)

