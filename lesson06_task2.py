from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр браузера Firefox
driver = webdriver.Firefox()  # Убедитесь, что geckodriver в PATH

try:
    # Открываем страницу
    driver.get('http://uitestingplayground.com/textinput')

    # Находим поле ввода и вводим текст "SkyPro"
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    input_field.send_keys('SkyPro')

    # Находим синюю кнопку и нажимаем на нее
    blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    blue_button.click()

    # Изменяем текст кнопки на "SkyPro" с помощью JavaScript
    driver.execute_script("arguments[0].innerText = 'SkyPro';", blue_button)

    # Явное ожидание: ждем, пока текст кнопки станет видимым
    button_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary'))
    )

    # Получаем текст кнопки и выводим его в консоль
    print(button_text.text)

finally:
    # Закрываем браузер
    driver.quit()