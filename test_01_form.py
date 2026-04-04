import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()

    try:
        wait = WebDriverWait(driver, 10)

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        first_name = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
        first_name.send_keys("Иван")
        last_name = wait.until(EC.visibility_of_element_located((By.NAME, "last-name")))
        last_name.send_keys("Петров")
        address = wait.until(EC.visibility_of_element_located((By.NAME, "address")))
        address.send_keys("Ленина, 55-3")
        email = wait.until(EC.visibility_of_element_located((By.NAME, "e-mail")))
        email.send_keys("test@skypro.com")
        phone = wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
        phone.send_keys("+7985899998787")
        # Zip code оставляем пустым
        city = wait.until(EC.visibility_of_element_located((By.NAME, "city")))
        city.send_keys("Москва")
        country = wait.until(EC.visibility_of_element_located((By.NAME, "country")))
        country.send_keys("Россия")
        job = wait.until(EC.visibility_of_element_located((By.NAME, "job-position")))
        job.send_keys("QA")
        company = wait.until(EC.visibility_of_element_located((By.NAME, "company")))
        company.send_keys("SkyPro")


        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()


        wait.until(lambda driver: driver.find_element(By.NAME, "zip-code").get_attribute("class") != "")

        zip_code = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
        zip_class = zip_code.get_attribute("class")
        assert "alert-danger" in zip_class, f"Поле ZIP Code не подсвечено красным! Класс: {zip_class}"

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for name, expected_value in fields.items():
            field = wait.until(EC.presence_of_element_located((By.NAME, name)))

            actual_value = field.get_attribute("value")
            assert actual_value == expected_value, f"Значение для поля {name} не совпадает! Ожидалось: {expected_value}, Получено: {actual_value}"

            wait.until(lambda driver: "alert-success" in field.get_attribute("class"))
            field_class = field.get_attribute("class")
            assert "alert-success" in field_class, f"Поле {name} не подсвечено зеленым! Класс: {field_class}"

        print("Все поля заполнены корректно и прошли валидацию!")

    except Exception as e:
        print(f" Произошла ошибка: {e}")
        raise
    finally:
        driver.quit()
