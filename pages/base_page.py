from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.settings import UIConfig
import allure
import time


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, UIConfig.EXPLICIT_WAIT)
        self.implicit_wait = UIConfig.IMPLICIT_WAIT

    def open(self, url: str) -> None:
        """Открыть URL"""
        with allure.step(f"Открыть страницу: {url}"):
            self.driver.get(url)
            time.sleep(2)

    def find_element(self, locator: tuple):
        """Найти элемент с ожиданием"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            # Делаем скриншот при ошибке
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"element_not_found_{locator}",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    def find_elements(self, locator: tuple):
        """Найти все элементы"""
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple) -> None:
        """Кликнуть по элементу"""
        with allure.step(f"Кликнуть по элементу: {locator}"):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            element.click()

    def input_text(self, locator: tuple, text: str) -> None:
        """Ввести текст в поле"""
        with allure.step(f"Ввести текст: {text[:50]}..."):
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Получить текст элемента"""
        return self.find_element(locator).text

    def wait_for_url_contains(self, text: str) -> bool:
        """Ожидать URL содержит текст"""
        try:
            return self.wait.until(EC.url_contains(text))
        except TimeoutException:
            return False

    def handle_captcha_if_present(self) -> bool:
        """
        Обработка капчи (если появилась)
        Возвращает True если капча была обработана
        """
        try:
            # Проверяем наличие капчи по разным признакам
            captcha_selectors = [
                "//iframe[@title='reCAPTCHA']",
                "//div[@class='captcha']",
                "//*[contains(text(), 'робот')]",
                "//*[contains(text(), 'captcha')]"
            ]

            for selector in captcha_selectors:
                try:
                    captcha = self.driver.find_element(By.XPATH, selector)
                    if captcha:
                        allure.attach(
                            self.driver.get_screenshot_as_png(),
                            name="captcha_detected",
                            attachment_type=allure.attachment_type.PNG
                        )
                        print("Капча обнаружена! Пожалуйста, решите её вручную в течение 30 секунд...")
                        time.sleep(30)
                        return True
                except:
                    pass
            return False
        except:
            return False

    def wait_and_screenshot(self, seconds: int = 1, name: str = "debug"):
        """Сделать скриншот и подождать (для отладки)"""
        time.sleep(seconds)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

        def find_element_with_timeout(self, by, value, timeout=10):
            """Найти элемент с кастомным таймаутом"""
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
