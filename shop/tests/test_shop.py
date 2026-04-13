import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    """Тесты для интернет-магазина"""

    def test_shop_checkout_total(self, driver):
        """
        Тест проверяет оформление заказа и итоговую сумму:
        1. Авторизоваться как standard_user
        2. Добавить 3 товара в корзину
        3. Перейти в корзину
        4. Нажать Checkout
        5. Заполнить форму данными
        6. Проверить итоговую сумму
        """
      
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

     
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        inventory_page.go_to_cart()

        cart_page.click_checkout()

        checkout_page.fill_checkout_form("Дмитрий", "Голдин", "197372")

        total_amount = checkout_page.get_total_amount()
      
        assert total_amount == "$58.29", f"Expected total to be '$58.29', but got '{total_amount}'"
