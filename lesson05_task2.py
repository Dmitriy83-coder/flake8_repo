from selenium import webdriver
from selenium.webdriver.common.by import By  # Импорт By
import time

# Создаем экземпляр броузера
driver = webdriver.Chrome()  

try:
    # Открываем искомый сайт
    driver.get('http://uitestingplayground.com/dynamicid')

    # Находим синюю кнопку и клацаем на нее
    blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')  # Используем CSS
    blue_button.click()

    # Ждем результат клика
    time.sleep(3)

finally:
    # Закрываем броузер
    driver.quit()