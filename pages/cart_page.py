"""
Page Object для страницы корзины.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Страница корзины.

    Локаторы:
        CHECKOUT_BUTTON: Кнопка оформления заказа
    """

    # Локаторы (тип: tuple[By, str])
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def click_checkout(self):
        """
        Нажать кнопку Checkout.

        Returns:
            None
        """
        self.click(self.CHECKOUT_BUTTON)
