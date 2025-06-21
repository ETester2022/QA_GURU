
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_hw11.utils import attach


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
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    driver.set_window_size(1920, 1080)

    yield driver

    attach.add_screenshot(driver)
    attach.add_logs(driver)
    attach.add_html(driver)
    attach.add_video(driver)
    driver.quit()

# import pytest
# from selenium import webdriver
# from test_hw11.utils import attach
# from selenium.webdriver.chrome.options import Options as ChromeOptions

# @pytest.fixture()
# def browser():
#     """КРИВАЯ, НО РАБОЧАЯ Фикстура для создания драйвера браузера в Selenoid."""
#
#     chrome_options = ChromeOptions()  # Создаем экземпляр класса ChromeOptions!
#     chrome_options.set_capability("browserName", "chrome")
#     chrome_options.set_capability("browserVersion", "128.0")
#     chrome_options.set_capability("selenoid:options", {"enableVideo": True,
#                                                        "enableVNC": True,
#                                                        "enableLog": True})
#     chrome_options.set_capability("goog:loggingPrefs", "browser")
#
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=chrome_options)
#     driver.set_window_size(1920, 1080)
#     driver.implicitly_wait(10)
#
#     yield driver
#
#     attach.add_screenshot(driver)
#     attach.add_logs(driver)
#     attach.add_html(driver)
#     attach.add_video(driver)
#     driver.quit()
