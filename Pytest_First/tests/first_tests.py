
'''--------19.2-------'''
import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_uncorrect(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_correct(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_correct(self):
        assert self.calc.adding(self, 2, 2) == 4