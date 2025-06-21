import numbers
from argparse import ArgumentError


class Calculator:
    def __init__(self, number1, number2)->None:
        pass

    @staticmethod
    def is_number(value):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def add(number1, number2):
        if not Calculator.is_number(number1) or not Calculator.is_number(number2):
            raise ArgumentError
        return number1 + number2

    @staticmethod
    def subtract(number1, number2):
        if not Calculator.is_number(number1) or not Calculator.is_number(number2):
            raise ArgumentError
        return number1 - number2

if __name__ == "__main__":
    print(Calculator.add(1, 2))