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
    f"{date} May,2025",
    f"{picture}",
    f"{subject}",
    "Sports",
    f"{adress}",
    f"{state} {city}"
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
    driver.find_element(By.XPATH, f'//div[@aria-label="Choose Thursday, May {date}th, 2025"]').click()
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
    rows = driver.find_elements(By.XPATH, '//tbody//tr')
    list_labels = []
    list_values = []

    for row in rows:
        label = row.find_element(By.XPATH, './td[1]').text
        value = row.find_element(By.XPATH, './td[2]').text
        list_labels.append(label)
        list_values.append(value)

    actual_res = dict(zip(list_labels, list_values))

    assert actual_res["Student Name"] == expected_result[0],\
        f"Значение поля 'Student Name': ОР '{expected_result[0]}', ФР '{actual_res["Student Name"]}'"
    assert actual_res["Student Email"] == expected_result[1],\
        f"Значение поля 'Student Email': ОР '{expected_result[1]}', ФР '{actual_res["Student Email"]}'"
    assert actual_res["Gender"] == expected_result[2],\
        f"Значение поля 'Gender': ОР '{expected_result[2]}', ФР '{actual_res["Gender"]}'"
    assert actual_res["Mobile"] == expected_result[3],\
        f"Значение поля 'Mobile': ОР '{expected_result[3]}', ФР '{actual_res["Mobile"]}'"
    assert actual_res["Date of Birth"] == expected_result[4],\
        f"Значение поля 'Date of Birth': ОР '{expected_result[4]}', ФР '{actual_res["Date of Birth"]}'"
    assert actual_res["Picture"] == expected_result[5],\
        f"Значение поля 'Picture': ОР '{expected_result[5]}', ФР '{actual_res["Picture"]}'"
    assert actual_res["Hobbies"] == expected_result[7],\
        f"Значение поля 'Hobbies': ОР '{expected_result[7]}', ФР '{actual_res["Hobbies"]}'"
    assert actual_res["Address"] == expected_result[8],\
        f"Значение поля 'Address': ОР '{expected_result[8]}', ФР '{actual_res["Address"]}'"
    assert actual_res["State and City"] == expected_result[9],\
        f"Значение поля 'State and City': ОР '{expected_result[9]}', ФР '{actual_res["State and City"]}'"

    assert actual_res["Subjects"] == expected_result[6],\
        f"Значение поля 'Student Name': ОР '{expected_result[6]}', ФР '{actual_res["Subjects"]}'"

