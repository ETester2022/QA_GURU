from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimpleRegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, main_section, sub_section):
        self.driver.get("https://demoqa.com/")
        self.driver.implicitly_wait(10)
        self.driver.execute_script("document.body.style.zoom = '70%'")
        section = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//h5[text()='{main_section}']"))
        )
        section.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".left-pannel"))
        )
        subitem = self.driver.find_element(By.XPATH, f"//span[text()='{sub_section}']")
        subitem.click()
        return self

