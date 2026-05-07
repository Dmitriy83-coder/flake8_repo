from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка авторизации")
    def is_logged_in(self) -> bool:
        """Проверить, авторизован ли пользователь (используется для информации)"""
        try:
            user_selectors = [
                "//*[contains(@class, 'user-menu')]",
                "//img[contains(@alt, 'avatar')]",
                "//a[contains(@href, '/profile/')]"
            ]
            for selector in user_selectors:
                if self.driver.find_elements(By.XPATH, selector):
                    return True
            return False
        except:
            return False
