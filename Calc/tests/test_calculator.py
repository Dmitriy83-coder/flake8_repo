import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    """Тесты для калькулятора"""
    
    def test_calculator_with_delay(self, driver):
        """
        Тест проверяет работу калькулятора с задержкой:
        1. Открыть страницу калькулятора
        2. Установить задержку 45 секунд
        3. Нажать кнопки 7, +, 8, =
        4. Проверить результат 15
        """
      
        calculator_page = CalculatorPage(driver)
        
        calculator_page.open()
        
        calculator_page.set_delay(45)
        
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        
        calculator_page.wait_for_result(15, timeout=60)
        
        result = calculator_page.get_result_text()
        assert result == "15", f"Expected result to be '15', but got '{result}'"
