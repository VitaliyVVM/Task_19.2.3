import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 20, 5) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 9, 1) == 8

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 7, 4) == 11