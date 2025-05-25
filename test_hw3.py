from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search_link(driver):
    """Тест появления текста yashaka/selene: User-oriented Web UI browser tests in Python - GitHub"""
    driver.find_element(By.ID, 'searchbox_input').send_keys('yashaka/selene')
    driver.find_element(By.ID, 'searchbox_input').send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH,
                               '//*[text()="yashaka/selene: User-oriented Web UI browser tests in Python - GitHub"]')
    assert link is not None

def test_search_text(driver):
    """Тест появления текста рон-дон-дон"""
    driver.find_element(By.ID, 'searchbox_input').send_keys('yashaka/selene')
    driver.find_element(By.ID, 'searchbox_input').send_keys(Keys.RETURN)
    text = driver.find_element(By.XPATH, '//*[text()="рон-дон-дон"]')
    assert text is not None
