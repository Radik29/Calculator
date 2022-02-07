import math
import re


def calculate(math_expr):
    math_expr = correct_factorial(math_expr)
    res = eval(math_expr)
    return int(res)


def correct_factorial(math_expr):
    new_math = re.sub(r"([0-9L]+)!", "math.factorial(\\1)", math_expr)

    if "!" in new_math:
        raise ValueError("Factorial operator must be used with numbers only")

    return new_math
