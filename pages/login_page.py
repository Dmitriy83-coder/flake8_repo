"""
Page Object для страницы авторизации.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Страница авторизации.

    Локаторы:
        USERNAME_INPUT: Поле ввода логина
        PASSWORD_INPUT: Поле ввода пароля
        LOGIN_BUTTON: Кнопка входа
    """

    # Локаторы (тип: tuple[By, str])
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def open(self):
        """
        Открыть страницу авторизации.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        """
        Ввести логин.

        Args:
            username (str): Имя пользователя

        Returns:
            None
        """
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """
        Ввести пароль.

        Args:
            password (str): Пароль

        Returns:
            None
        """
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """
        Нажать кнопку входа.

        Returns:
            None
        """
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """
        Выполнить полную авторизацию.

        Args:
            username (str): Имя пользователя
            password (str): Пароль

        Returns:
            None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
