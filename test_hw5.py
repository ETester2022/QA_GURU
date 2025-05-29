import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# pytest -m test_fill_registration_form_student -vv
@pytest.mark.test_fill_registration_form_student
def test_fill_registration_form_student(driver):
    """Заполнение формы студента"""
    driver.execute_script("document.body.style.zoom = '70%'")

    first_name = "My firstName"
    last_name = "My lastName"
    user_email = "My@userEmail.ru"
    phone = "89998887766"
    picture = "64.jpg"
    subject = "subjectsContainer"
    adress = "currentAddress"
    state = "NCR"
    city = "Delhi"

    labels = [
        "Student Name",
        "Student Email",
        "Gender",
        "Mobile",
        "Date of Birth",
        "Subjects",
        "Hobbies",
        "Picture",
        "Address",
        "State and City"
    ]

    expected_result = [
    f"{first_name} {last_name}",
    f"{user_email}",
    "Male",
    f"{phone}",
    "15",
    f"{picture}",
    f"{subject}",
    "Sports",
    f"{adress}",
    f"{state}",
    f"{city}"
    ]
    #Ввод Имени, Фамилии, Email
    driver.find_element(By.ID, "firstName").send_keys(f"{first_name}")
    driver.find_element(By.ID, "lastName").send_keys(f"{last_name}")
    driver.find_element(By.ID, "userEmail").send_keys(f"{user_email}")
    #Выбор пола
    driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()
    #Ввод номера телефона
    driver.find_element(By.ID, "userNumber").send_keys(f"{phone}")
    #Выбор даты
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.XPATH, '//div[@aria-label="Choose Thursday, May 15th, 2025"]').click()
    #Выбор предмета
    driver.find_element(By.ID, "subjectsInput").send_keys(f"{subject}")
    driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()
    #Загрузка фото
    file_path = os.path.abspath(f"{picture}")
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    #Выбор адреса
    driver.find_element(By.ID, "currentAddress").send_keys(f"{adress}")
    #Выбор штата
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, f'//*[text()="{state}"]').click()
    # Выбор города
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, f'//*[text()="{city}"]').click()
    #Клик Submit
    driver.find_element(By.ID, "submit").click()
    # Ожидание появления модального окна
    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="modal-content"]')
            )
        )
    #Проверка отображеня заголовка в модальном окне
    element = driver.find_element(By.CLASS_NAME, "modal-header")
    assert element.text == "Thanks for submitting the form"

    #Сравнение полученных и ожидаемых value в соответствии с их Label
    rows = driver.find_elements(By.XPATH, '//tbody//tr//td[1]')
    for row in rows:
        for label in labels:
            if label == row.text:
                actual_value = driver.find_element(By.XPATH, f'//tbody//tr/td[text()="{label}"]/following-sibling::td')
                for res in expected_result:
                    assert actual_value.text == res


