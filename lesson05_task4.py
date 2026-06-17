from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time

# Устанавливаем сервис для GeckoDriver
service = Service(GeckoDriverManager().install())

# Создаем экземпляр веб-драйвера Firefox
driver = webdriver.Firefox(service=service)

try:
    # Перейти на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    # Логинимся
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    # Паролимся
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # Нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ждем немного
    time.sleep(1)

    # Извлекаем текст зеленой плашки
    success_message = driver.find_element(By.ID, "flash")
    print(success_message.text)

finally:
    driver.quit()