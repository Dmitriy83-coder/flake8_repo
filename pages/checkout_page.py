"""
Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Страница оформления заказа.

    Локаторы:
        FIRST_NAME_INPUT: Поле ввода имени
        LAST_NAME_INPUT: Поле ввода фамилии
        POSTAL_CODE_INPUT: Поле ввода почтового индекса
        CONTINUE_BUTTON: Кнопка продолжения
        TOTAL_LABEL: Метка с итоговой суммой
    """

    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name: str) -> None:
        """Ввести имя."""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Ввести фамилию."""
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Ввести почтовый индекс."""
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self) -> None:
        """Нажать кнопку Continue."""
        self.click(self.CONTINUE_BUTTON)

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполнить форму оформления заказа."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму.

        Returns:
            str: Итоговая сумма в формате "$XX.XX"
        """
        total_text = self.get_text(self.TOTAL_LABEL)
        # Извлекаем только сумму из текста "Total: $58.29"
        return total_text.replace("Total: ", "")
