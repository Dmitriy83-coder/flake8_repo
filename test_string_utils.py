import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Тест", "Тест"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # Пустая строка
    (" ", " "),  # Строка с пробелом
    (None, None),  # None
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для функции trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Тест", "Тест"),
    ("hello world   ", "hello world"),
    ("   123   ", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # Пустая строка
    (" ", ""),  # Строка с пробелом
    (None, None),  # None
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для функции contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "Т", True),
    ("123", "1", True),
    ("04 апреля 2023", " ", True),  # Пробел как символ
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "X", False),  # Символ не найден
    ("", "A", False),  # Пустая строка
    (" ", "A", False),  # Строка с пробелом
    (None, "A", False),  # None
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# Тесты для функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "е", "Тст"),
    ("123", "2", "13"),
    ("04 апреля 2023", " ", "04апреля2023"),  # Удаление пробелов
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Тест", "X", "Тест"),  # Символ не найден
    ("", "", ""),  # Пустая строка и пустой символ
    (" ", "", " "),  # Строка с пробелом и пустой символ
    (None, "A", None),  # None
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected