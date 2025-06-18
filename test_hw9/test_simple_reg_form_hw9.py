from test_hw9.application_manager import Application


def test_simple_registration_form(driver):

    app = Application(driver)

    app.left_panel.open_simple_registration_form()

