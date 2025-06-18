"""Написать тест на проверку названия Issue в репозитории через Web-интерфейс.

Этот тест представить в трех вариантах:
1. Чистый Selene (без шагов)
2. Лямбда шаги через with allure.step
3. Шаги с декоратором @allure.step
4. Разметку тестов всеми аннотациями
В качестве ответа на задание приложите ссылку на свой репозиторий GitHub в поле ответа"""

import pytest
import allure
from allure_commons.types import Severity
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Команда запуска тестов только из hw10
pytest -m hw10 -vv --clean-alluredir --alluredir=allure_result_tests
"""
@pytest.mark.hw10
@allure.title("тест на проверку отображения Issue без шагов")
def test_label_issue_without_steps(driver):

    driver.get("https://github.com")
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//qbsearch-input").click()
    driver.find_element(By.ID, "query-builder-test").send_keys("eroshenkoam/allure-example")
    driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Issues']"))
    )
    driver.find_element(By.XPATH, "//span[text()='Issues']").click()
    try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[text()='#' and text()='199']")
            )
        )
        assert bool(element) is True
    except TimeoutException:
        raise AssertionError("Элемент не найден!")

@pytest.mark.hw10
@allure.title("тест на проверку отображения Issue Лямбда шаги через with allure.step")
def test_label_issue_with_steps(driver):

    with allure.step("Переход на главную страницу github"):
        driver.get("https://github.com")
        driver.implicitly_wait(10)

    with allure.step("Переход в раздел Issues"):
        driver.find_element(By.XPATH, "//qbsearch-input").click()
        driver.find_element(By.ID, "query-builder-test").send_keys("eroshenkoam/allure-example")
        driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Issues']"))
        )
        driver.find_element(By.XPATH, "//span[text()='Issues']").click()

    with allure.step("Проверка отображения Issue #199"):
        try:
            element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[text()='#' and text()='199']")
                )
            )
            assert bool(element) is True
        except TimeoutException:
            raise AssertionError("Элемент не найден!")

@pytest.mark.hw10
@allure.tag("web")
@allure.link("https://github.com")
@allure.label('owner', 'tster: Evgeniy')
@allure.title("тест на проверку отображения Issue Шаги с декоратором @allure.step")
@allure.severity(Severity.CRITICAL)
def test_label_issue_with_decorator_steps(driver):

    open_main_page(driver)
    open_issues_page(driver, repo="eroshenkoam/allure-example")
    is_displayed(driver, number="199")


@allure.step("Переход на главную страницу github")
def open_main_page(driver):
    driver.get("https://github.com")
    driver.implicitly_wait(10)

@allure.step("Переход в раздел Issues")
def open_issues_page(driver, repo):
    driver.find_element(By.XPATH, "//qbsearch-input").click()
    driver.find_element(By.ID, "query-builder-test").send_keys(repo)
    driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
    WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='Issues']"))
        )
    driver.find_element(By.XPATH, "//span[text()='Issues']").click()

@allure.step("Проверка отображения issue #199")
def is_displayed(driver, number):
    try:
        element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//*[text()='#' and text()='{number}']")
                )
            )
        assert bool(element) is True
    except TimeoutException:
        raise AssertionError("Элемент не найден!")
