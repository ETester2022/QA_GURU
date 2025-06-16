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

    def register(self, user):
        self.driver.find_element(By.ID, "firstName").send_keys(user.first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(user.last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(user.user_email)
        self.driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()
        self.driver.find_element(By.ID, "userNumber").send_keys(user.phone)
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        self.driver.find_element(By.XPATH, f'//div[contains(@aria-label, "{user.date}th")]').click()
        self.driver.find_element(By.ID, "subjectsInput").send_keys(user.subject)
        self.driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()
        file_path = os.path.abspath(user.picture)
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
        self.driver.find_element(By.ID, "currentAddress").send_keys(user.address)
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{user.state}"]').click()
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, f'//*[text()="{user.city}"]').click()
        self.driver.find_element(By.ID, "submit").click()

    def should_have_registered(self, user):
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

        assert f"{user.first_name} {user.last_name}" == actual_res["Student Name"], \
            f"Значение поля 'Student Name': ОР '{user.first_name} {user.last_name}', ФР '{actual_res['Student Name']}'"

        assert user.user_email == actual_res["Student Email"], \
            f"Значение поля 'Student Email': ОР '{user.user_email}', ФР '{actual_res['Student Email']}'"

        assert "Male" == actual_res["Gender"], \
            f"Значение поля 'Gender': ОР 'Male', ФР '{actual_res['Gender']}'"

        assert user.phone == actual_res["Mobile"], \
            f"Значение поля 'Mobile': ОР '{user.phone}', ФР '{actual_res['Mobile']}'"

        assert user.date in actual_res["Date of Birth"], \
            f"Значение поля 'Date of Birth': ОР '{user.date} June,2025', ФР '{actual_res['Date of Birth']}'"

        assert user.picture.split('/')[-1] == actual_res["Picture"], \
            f"Значение поля 'Picture': ОР '{user.picture.split('/')[-1]}', ФР '{actual_res['Picture']}'"

        assert "Sports" == actual_res["Hobbies"], \
            f"Значение поля 'Hobbies': ОР 'Sports', ФР '{actual_res['Hobbies']}'"

        assert user.address == actual_res["Address"], \
            f"Значение поля 'Address': ОР '{user.address}', ФР '{actual_res['Address']}'"

        assert f"{user.state} {user.city}" == actual_res["State and City"], \
            f"Значение поля 'State and City': ОР '{user.state} {user.city}', ФР '{actual_res['State and City']}'"

        assert user.subject == actual_res["Subjects"], \
            f"Значение поля 'Subjects': ОР '{user.subject}', ФР '{actual_res['Subjects']}'"

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
