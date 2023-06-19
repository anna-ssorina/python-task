#Ссорина Анна сергеевна 44-22-119 Вариант 20

import math

def calculate_expression(x):
    if isinstance(x, (int, float)):
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x)**2)
        else:
            return math.exp(x**3) * math.sin(3*x)
    else:
        raise ValueError("Введенное значение не является числом")

try:
    x = float(input("Введите значение x: "))
    result = calculate_expression(x)
    print(f"Результат вычисления: {result}")
except ValueError as ve:
    print(f"Ошибка: {ve}")
