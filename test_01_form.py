import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture
def test_fill_form():
    driver_path = r'C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe'
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)

    try:
        wait = WebDriverWait(driver, 10)
     
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        driver.find_element(By.NAME, "firstName").send_keys("Иван")
        driver.find_element(By.NAME, "lastName").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phoneNumber").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        zip_input = wait.until(EC.presence_of_element_located((By.NAME, "zip")))
        wait.until(lambda d: zip_input.get_attribute("style").find("border-color: rgb(255, 0, 0)") != -1)

        fields = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phoneNumber": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job": "QA",
            "company": "SkyPro"
        }
        
        for name, value in fields.items():
            elem = wait.until(EC.presence_of_element_located((By.NAME, name)))
            assert elem.get_attribute("value") == value
            border_color = elem.get_attribute("style").find("border-color: rgb(0, 128, 0)") != -1
            assert border_color, f"Поле {name} не подсвечено зеленым"

    finally:
        driver.quit()