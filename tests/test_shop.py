"""
Тесты для интернет-магазина Saucedemo.
"""
import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Корзина")
@allure.story("Оформление заказа")
@allure.tag("UI", "Saucedemo", "PageObject")
@allure.label("owner", "QA Team")
class TestShop:
    """Тестовый класс для проверки функциональности магазина."""

    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("""
        Тест проверяет полный сценарий оформления заказа:
        1. Авторизация пользователем standard_user
        2. Добавление трех товаров в корзину
        3. Оформление заказа с заполнением формы
        4. Проверка итоговой суммы (должна быть $58.29)
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop_checkout_total(self, driver):
        """
        Тест проверки итоговой суммы заказа.

        Args:
            driver: Фикстура WebDriver
        """
        # Создание объектов страниц
        with allure.step("Инициализация Page Object классов"):
            login_page = LoginPage(driver)
            inventory_page = InventoryPage(driver)
            cart_page = CartPage(driver)
            checkout_page = CheckoutPage(driver)

        # Открытие сайта и авторизация
        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Авторизация пользователем 'standard_user'"):
            login_page.login("standard_user", "secret_sauce")

        # Добавление товаров в корзину
        items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for item in items:
            with allure.step(f"Добавление товара '{item}' в корзину"):
                inventory_page.add_item_to_cart(item)

        # Переход в корзину
        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        # Шаг 5: Нажатие кнопки Checkout
        with allure.step("Нажатие кнопки 'Checkout'"):
            cart_page.click_checkout()

        # Шаг 6: Заполнение формы
        with allure.step("Заполнение формы данными покупателя"):
            checkout_page.fill_checkout_form("Дмитрий", "Голдин", "197372")

        # Шаг 7: Получение итоговой суммы
        with allure.step("Получение итоговой суммы заказа"):
            total_amount = checkout_page.get_total_amount()

        # Шаг 8: Проверка результата
        with allure.step(f"Проверка что итоговая сумма равна '$58.29', получено '{total_amount}'"):
            assert total_amount == "$58.29", \
                f"Expected total to be '$58.29', but got '{total_amount}'"

        with allure.step("Тест успешно завершен"):
            allure.attach(
                f"Итоговая сумма: {total_amount}",
                name="Результат проверки",
                attachment_type=allure.attachment_type.TEXT
            )
