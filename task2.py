#Ссорина Анна сергеевна 44-22-119 Вариант 20

import unittest
import math

def calculate_expression(x):
    if isinstance(x, (int, float)):
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x)**2)
        else:
            return math.exp(x**3) * math.sin(3*x)
    else:
        raise ValueError("Введенное значение не является числом")

class TestCalculateExpression(unittest.TestCase):
    def test_negative_x(self):
        x = 0.3
        expected_result = math.sqrt(math.sin(x) + math.cos(x)**2)
        self.assertAlmostEqual(calculate_expression(x), expected_result)

    def test_positive_x(self):
        x = 0.7
        expected_result = math.exp(x**3) * math.sin(3*x)
        self.assertAlmostEqual(calculate_expression(x), expected_result)

    def test_non_numeric_input(self):
        x = 'abc'
        self.assertRaises(ValueError, calculate_expression, x)

if __name__ == '__main__':
    unittest.main()
