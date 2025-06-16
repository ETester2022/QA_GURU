
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.implicitly_wait(10)
        self.driver.execute_script("document.body.style.zoom = '70%'")

    def fill_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(f"{first_name}")

    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID, "lastName").send_keys(f"{last_name}")

    def fill_email(self, user_email):
        self.driver.find_element(By.ID, "userEmail").send_keys(f"{user_email}")

    def select_gender_male(self):
        self.driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()

    def fill_mobile(self, phone):
        self.driver.find_element(By.ID, "userNumber").send_keys(f"{phone}")

    def select_date(self, date):
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        self.driver.find_element(By.XPATH, f'//div[contains(@aria-label, "{date}th")]').click()

    def fill_subject(self, subject):
        self.driver.find_element(By.ID, "subjectsInput").send_keys(f"{subject}")

    def select_hobbie_sports(self):
        self.driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()

    def add_picture(self, picture):
        file_path = os.path.abspath(f"{picture}")
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    def fill_current_address(self, adress):
        self.driver.find_element(By.ID, "currentAddress").send_keys(f"{adress}")

    def select_state(self, state):
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{state}"]').click()

    def select_city(self, city):
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{city}"]').click()

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()


    def should_have_header(self, header):
        # Ожидание появления модального окна
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="modal-content"]')
            )
        )
        # Проверка отображеня заголовка в модальном окне
        element = self.driver.find_element(By.CLASS_NAME, "modal-header")
        assert element.text == header

    def should_have_registered(self, expected_result):
        # Ожидание появления модального окна
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="modal-content"]')
            )
        )
        # Проверка от
        # Сравнение полученных и ожидаемых value в соответствии с их Label
        rows = self.driver.find_elements(By.XPATH, '//tbody//tr')
        list_labels = []
        list_values = []

        for row in rows:
            label = row.find_element(By.XPATH, './td[1]').text
            value = row.find_element(By.XPATH, './td[2]').text
            list_labels.append(label)
            list_values.append(value)

        actual_res = dict(zip(list_labels, list_values))

        assert actual_res["Student Name"] == expected_result[0], \
            f"Значение поля 'Student Name': ОР '{expected_result[0]}', ФР '{actual_res["Student Name"]}'"
        assert actual_res["Student Email"] == expected_result[1], \
            f"Значение поля 'Student Email': ОР '{expected_result[1]}', ФР '{actual_res["Student Email"]}'"
        assert actual_res["Gender"] == expected_result[2], \
            f"Значение поля 'Gender': ОР '{expected_result[2]}', ФР '{actual_res["Gender"]}'"
        assert actual_res["Mobile"] == expected_result[3], \
            f"Значение поля 'Mobile': ОР '{expected_result[3]}', ФР '{actual_res["Mobile"]}'"
        assert actual_res["Date of Birth"] == expected_result[4], \
            f"Значение поля 'Date of Birth': ОР '{expected_result[4]}', ФР '{actual_res["Date of Birth"]}'"
        assert actual_res["Picture"] == expected_result[5], \
            f"Значение поля 'Picture': ОР '{expected_result[5]}', ФР '{actual_res["Picture"]}'"
        assert actual_res["Hobbies"] == expected_result[7], \
            f"Значение поля 'Hobbies': ОР '{expected_result[7]}', ФР '{actual_res["Hobbies"]}'"
        assert actual_res["Address"] == expected_result[8], \
            f"Значение поля 'Address': ОР '{expected_result[8]}', ФР '{actual_res["Address"]}'"
        assert actual_res["State and City"] == expected_result[9], \
            f"Значение поля 'State and City': ОР '{expected_result[9]}', ФР '{actual_res["State and City"]}'"

        assert actual_res["Subjects"] == expected_result[6], \
            f"Значение поля 'Student Name': ОР '{expected_result[6]}', ФР '{actual_res["Subjects"]}'"

