import pytest
from selenium.webdriver.common.by import By




@pytest.mark.parametrize('size_window', [(1920, 1080)])
def test_click_sign_in_desktop(driver, size_window):

    driver.get("https://github.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[contains(@class, "HeaderMenu-link--sign-in")]').click()



@pytest.mark.parametrize('size_window', [(414, 896)])
def test_click_sign_in_mobile(driver, size_window):

    driver.get("https://github.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[contains(@data-analytics-event, "click to Sign")]').click()