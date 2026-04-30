"""
Page Object для главной страницы магазина.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Главная страница магазина (каталог товаров).

    Локаторы:
        CART_LINK: Ссылка на корзину
    """

    # Локаторы (тип: tuple[By, str])
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def _get_add_button_locator(self, item_name: str) -> tuple:
        """
        Получить локатор кнопки добавления товара по названию.

        Args:
            item_name (str): Название товара

        Returns:
            tuple: Локатор кнопки (By, str)
        """
        return (By.XPATH,
                f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")

    def add_item_to_cart(self, item_name: str):
        """
        Добавить товар в корзину по названию.

        Args:
            item_name (str): Название товара

        Returns:
            None
        """
        button_locator = self._get_add_button_locator(item_name)
        self.click(button_locator)

    def go_to_cart(self):
        """
        Перейти в корзину.

        Returns:
            None
        """
        self.click(self.CART_LINK)
