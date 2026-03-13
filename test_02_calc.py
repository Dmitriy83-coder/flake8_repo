import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit()

def test_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.send_keys("45")  

    button_7 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='7']"))
    )
    button_7.click()

    button_plus = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='+']"))
    )
    button_plus.click()

    button_8 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='8']"))
    )
    button_8.click()

    button_equals = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[value='=']"))
    )
    button_equals.click()

    result = WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )

    assert result.text == "15", f"Expected result to be '15', but got '{result.text}'"