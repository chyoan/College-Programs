# Complex Calculator - Python
# by CodeChum Admin

# Implement the class called ComplexCalculator with the following details:
# Class - ComplexCalculator:
# Public Methods:
# get_square_root(number: int) -> float: Returns the square root of number as a floating-point number. If number is negative, it returns 0.
# get_factorial(number: int) -> int: Computes and returns the factorial of number as an integer. If number is negative, it returns 0.
# get_sum(number1: int, number2: int) -> float: Returns the sum of number1 and number2 as a floating-point number.
# get_product(number1: int, number2: int) -> float: Returns the product of number1 and number2 as a floating-point number.
# get_difference(number1: int, number2: int) -> float: Returns the difference between number1 and number2 as a floating-point number.
# get_quotient(number1: int, number2: int) -> float: Returns the quotient when number1 is divided by number2 as a floating-point number. In cases of infinite or invalid divisions (like division by zero), it returns 0.

class ComplexCalculator:
    def get_square_root(self, number: int):
        if number < 0:
            return 0
        else:
            return float(number ** 0.5)

    def get_factorial(self, number: int):
        factorial = 1
        if number < 0:
            return 0
        else:
            for i in range(1, number + 1):
                factorial *= i
        return factorial

    def get_sum(self, number1: int, number2: int):
        return float(number1 + number2)

    def get_product(self, number1: int, number2: int):
        return float(number1 * number2)

    def get_difference(self, number1: int, number2: int):
        return float(number1 - number2)

    def get_quotient(self, number1: int, number2: int):
        try:
            return float(number1 / number2)
        except ZeroDivisionError:
            return 0