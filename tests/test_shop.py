import pytest
from pages.shop_login_page import LoginPage
from pages.shop_inventory_page import InventoryPage
from pages.shop_cart_page import CartPage
from pages.shop_checkout_page import CheckoutPage


class TestShop:
    def test_shop_checkout_total(self, firefox_driver):
        login_page = LoginPage(firefox_driver)
        inventory_page = InventoryPage(firefox_driver)
        cart_page = CartPage(firefox_driver)
        checkout_page = CheckoutPage(firefox_driver)
        
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_form("Дмитрий", "Голдин", "197372")
        
        total_amount = checkout_page.get_total_amount()
        assert total_amount == "$58.29", f"Expected '$58.29', got '{total_amount}'"
