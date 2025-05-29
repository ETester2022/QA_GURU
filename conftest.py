from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    """Фикстура для создания драйвера браузера."""

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demoqa.com/automation-practice-form")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()