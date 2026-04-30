"""
Базовый класс для всех Page Object.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс страницы.

    Attributes:
        driver (webdriver.Remote): Экземпляр драйвера
        wait (WebDriverWait): Объект для явного ожидания
    """

    def __init__(self, driver):
        """
        Инициализация базовой страницы.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """
        Клик по элементу.

        Args:
            locator (tuple): Локатор элемента (By, selector)

        Returns:
            None
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """
        Ввод текста в элемент.

        Args:
            locator (tuple): Локатор элемента (By, selector)
            text (str): Текст для ввода

        Returns:
            None
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Получение текста элемента.

        Args:
            locator (tuple): Локатор элемента (By, selector)

        Returns:
            str: Текст элемента
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
