#!/usr/bin/python3
"""definition for add_integer function """

def add_integer(a, b=98):
    """
    Function for adding 2 integers.
    Parameters:
        a: an int or float, first parameter.
        b: an int or float, second parameter.
    Returns:
        the sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:           
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
