
import json
import logging

import allure
import requests
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


def open_cart(driver):
    driver.get("https://demowebshop.tricentis.com/cart")
    driver.implicitly_wait(10)

# pytest -m test_add_item -vv --alluredir=allure_results команда для запуска тестов
# allure serve allure_results/ команда для генерации отчета
@allure.title("Добавление товара в корзину")
@pytest.mark.test_add_item
@pytest.mark.parametrize("quantity, login, password", [
    (1, "login-auto@gmail.com", "autotest"),
    (3, "login-auto@gmail.com", "autotest"),
    (0, "login-auto@gmail.com", "autotest")
])
def test_add_item(driver, quantity, login, password):

    with allure.step("Login with API"):
        response = requests.post(url="https://demowebshop.tricentis.com/login",
                                  data={
                                      "Email": login,
                                      "Password": password,
                                      "RememberMe": False
                                      },
                                  allow_redirects=False)

        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)

    with allure.step("get auth cookie"):
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("add auth cookie"):
        open_cart(driver)
        driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    with allure.step("get quantity before"):
        open_cart(driver)
        quantity_before = driver.find_element(By.XPATH, "//td[@class='qty nobr']//input").get_attribute("value")

    with allure.step("add item to cart"):
        response = requests.post(url=f"https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/{quantity}",
                      data={
                          "addtocart_31.EnteredQuantity": f"{quantity}"
                           },
                      cookies={'NOPCOMMERCE.AUTH': cookie})

        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)

    with allure.step("open cart and get quantity items"):
        open_cart(driver)
        quantity_after = driver.find_element(By.XPATH, "//td[@class='qty nobr']//input").get_attribute("value")

    with allure.step("open cart and assert name, quantity items"):
        name = driver.find_element(By.XPATH, "//*[@class='product-name']")

        assert name.text == "14.1-inch Laptop"
        assert int(quantity_after) - int(quantity_before) == quantity
