import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_configure(config):
    """Регистрация маркеров"""
    config.addinivalue_line("markers", "calculator: tests for calculator")
    config.addinivalue_line("markers", "shop: tests for online shop")


@pytest.fixture(scope="function")
def chrome_driver():
    """Фикстура для Chrome (калькулятор)"""
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver():
    """Фикстура для Firefox (магазин)"""
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()
