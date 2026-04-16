from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name):
        """Добавить товар в корзину по названию"""
        add_button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button = self.wait.until(
            EC.element_to_be_clickable(add_button)
        )
        button.click()

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()
