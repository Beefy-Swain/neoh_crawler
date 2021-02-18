"""This module has mypy and pylint errors to test editor setup.

You should see the following problems from mypy and pylint.

Mypy:
Name 'math' is not defined
Argument 1 to "test_linting" has incompatible type "int"; expected "str"
Redundant cast to "int"

Pylint:
Undefined variable 'math'
Missing function or method docstring
Missing function or method docstring
Used builtin function 'filter'. Using a list comprehension can be clearer
"""
from typing import cast

Count = int


def example(x: Count):
    cast(int, x)


def test_linting(text: str):
    number = math.sqrt(100)
    print(text + str(number))


if __name__ == "__main__":
    test_linting(100)
    filter(lambda x: x == 1, [1, 1, 2])
