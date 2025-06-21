
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PegistrationStudentPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на главную страницу github")
    def open_main_page(self):
        self.driver.get("https://github.com")
        self.driver.implicitly_wait(10)

    @allure.step("Переход в раздел Issues")
    def open_issues_page(self, repo):
        self.driver.find_element(By.XPATH, "//qbsearch-input").click()
        self.driver.find_element(By.ID, "query-builder-test").send_keys(repo)
        self.driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Issues']"))
            )
        self.driver.find_element(By.XPATH, "//span[text()='Issues']").click()

    @allure.step("Проверка отображения issue #199")
    def is_displayed(self, number):
        try:
            element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f"//*[text()='#' and text()='{number}']")
                    )
                )
            assert bool(element) is True
        except TimeoutException:
            raise AssertionError("Элемент не найден!")