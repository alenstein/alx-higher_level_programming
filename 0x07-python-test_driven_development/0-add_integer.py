#!/usr/bin/python3
"""
    Module for function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
        function add 2 integers

        Args:
        a: first integer.
        b: second integer.
    """
    if isinstance(a, int) or isinstance(b, int):
        pass
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    else:
        raise TypeError('a must be an integer or b must be an integer')
    return a + b
