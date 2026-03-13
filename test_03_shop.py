import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Firefox() 
    yield driver
    driver.quit()

def test_shop(browser):
    browser.get("https://www.saucedemo.com/")

    username_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_input.send_keys("standard_user")

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()

    backpack_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Backpack']/following-sibling::button"))
    )
    backpack_button.click()

    t_shirt_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/following-sibling::button"))
    )
    t_shirt_button.click()

    onesie_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Sauce Labs Onesie']/following-sibling::button"))
    )
    onesie_button.click()

    cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link"))
    )
    cart_button.click()

    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_action.checkout_button"))
    )
    checkout_button.click()

    first_name_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name_input.send_keys("Иван")

    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys("Петров")

    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("12345")

    continue_button = browser.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button")
    continue_button.click()

    total_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )
    total_text = total_element.text
    total_amount = total_text.split()[-1] 

    assert total_amount == "$58.29", f"Expected total to be '$58.29', but got '{total_amount}'"