

class LeftPanel:
    def __init__(self, driver):
        self.driver = driver

    def open_simple_registration_form(self):
        self.driver.get("https://demoqa.com/text-box")
        self.driver.implicitly_wait(10)
        self.driver.execute_script("document.body.style.zoom = '70%'")
