from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора"""
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTONS = (By.XPATH, "//span[text()='{}']")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        delay_field = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))
    
    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
    
    def get_result_text(self):
        screen = self.wait.until(
            EC.visibility_of_element_located(self.SCREEN)
        )
        return screen.text
    
    def wait_for_result(self, expected_result, timeout=60):
        self.wait.until(
            lambda driver: self.get_result_text() == str(expected_result),
            message=f"Result '{expected_result}' not appeared within {timeout} seconds"
        )
