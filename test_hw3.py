from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search_positive(driver):
    """Тест появления текста yashaka/selene: User-oriented Web UI browser tests in Python - GitHub"""
    driver.get("https://duckduckgo.com/")
    driver.implicitly_wait(10)
    input_text = 'yashaka/selene'
    driver.find_element(By.ID, 'searchbox_input').send_keys(f'{input_text}')
    driver.find_element(By.ID, 'searchbox_input').send_keys(Keys.RETURN)
    element = driver.find_element(By.XPATH, '//*[contains(text(), "yashaka/selene: User-oriented")]')

    assert element.text == f"{input_text}: User-oriented Web UI browser tests in Python - GitHub"

def test_search_negative(driver):
    """Тест появления текста ничего не найдено"""
    driver.get("https://duckduckgo.com/")
    driver.implicitly_wait(10)
    input_text = 'qwertyhnbv34'
    driver.find_element(By.ID, 'searchbox_input').send_keys(f'{input_text}')
    driver.find_element(By.ID, 'searchbox_input').send_keys(Keys.RETURN)
    element = driver.find_element(By.XPATH, '//span[text()="» ничего не найдено."]')

    assert element.text == f'По запросу «{input_text}» ничего не найдено.'