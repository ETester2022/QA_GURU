from test_hw9.pages.simple_registration_page import SimpleRegistrationPage
from test_hw9.pages.left_panel import LeftPanel


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.simple_registration = SimpleRegistrationPage(driver)
        self.left_panel = LeftPanel(driver)
