import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    def test_calculator_with_delay(self, chrome_driver):
        calculator_page = CalculatorPage(chrome_driver)
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        calculator_page.wait_for_result(15, timeout=60)
        result = calculator_page.get_result_text()
        assert result == "15", f"Expected '15', got '{result}'"
