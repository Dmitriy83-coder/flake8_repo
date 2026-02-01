def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    return year % 4 == 0

year_to_check = 2024
is_leap = is_year_leap(year_to_check)

print(f"Год {year_to_check}: {is_leap}")