import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def chrome_driver():
    """Фикстура для Chrome"""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver():
    """Фикстура для Firefox"""
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
