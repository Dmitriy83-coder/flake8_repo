from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox() 

try:
    driver.get('http://uitestingplayground.com/textinput')

    input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    input_field.send_keys('SkyPro')

    blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    blue_button.click()

    driver.execute_script("arguments[0].innerText = 'SkyPro';", blue_button)

    button_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary'))
    )

    print(button_text.text)

finally:
    driver.quit()
