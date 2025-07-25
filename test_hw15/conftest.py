import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_hw12.utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
        "goog:loggingPrefs": {"browser": "ALL"}
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    url = os.getenv('URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}",
        options=options
    )
    driver.set_window_size(1920, 1080)

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)
    attach.add_video(driver)
    driver.quit()
