"""
Unit tests for the calculator library
"""

import calculator
import pytest


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):

        with pytest.raises(ZeroDivisionError):
            calculator.divide(20, 0)

        assert 5.0 == calculator.divide(20, 4)
