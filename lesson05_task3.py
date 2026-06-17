from selenium import webdriver
from selenium.webdriver.common.by import By  # Импорт By
import time

# Создаем экземпляр браузера Firefox
driver = webdriver.Firefox()  

try:
    driver.get('http://the-internet.herokuapp.com/inputs')

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, 'input')

    input_field.send_keys('Sky')

    time.sleep(2)

    # Очищаем поле ввода
    input_field.clear()

    input_field.send_keys('Pro')

    time.sleep(2)

finally:
    driver.quit()