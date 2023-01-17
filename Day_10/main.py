import math


class Calculator:

    def addition(value_a, value_b):
        return value_a + value_b

    def subtraction(value_a, value_b):
        return value_a - value_b

    def multiplication(value_a, value_b):
        return value_a * value_b

    def division(value_a, value_b):
        return value_a / value_b

    def exponentiation(value_a, value_b):

        return value_a ** value_b

    def square_root(value_a):
        return math.sqrt(value_a)


a = Calculator.square_root(150)
print(a)
