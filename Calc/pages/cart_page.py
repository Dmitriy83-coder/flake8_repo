from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины"""

    # Локаторы
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self):
        """Получить список названий товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        names = []
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            names.append(name)
        return names

    def get_cart_item_prices(self):
        """Получить список цен товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        prices = []
        for item in items:
            price = item.find_element(*self.ITEM_PRICE).text
            prices.append(price)
        return prices
