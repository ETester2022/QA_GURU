from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import  os
from zipfile import ZipFile



@pytest.fixture()
def driver():
    """Фикстура для создания драйвера браузера."""

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture()
def create_archive():

    files = [
        "example.xlsx",
        "example.pdf",
        "example.csv"
    ]

    # Создаем архив и добавляем файлы
    with ZipFile("sources/archive.zip", 'w') as zf:
        for file in files:
            add_file = os.path.join('sources', file)
            zf.write(add_file, os.path.basename(add_file))
