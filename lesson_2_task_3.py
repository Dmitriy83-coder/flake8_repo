import math
def square(side):
    """Возвращает площадь квадрата, округленную вверх, если сторона не целая."""
    area = side * side
    return math.ceil(area)
side_length = 4.3 
area_result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area_result}")