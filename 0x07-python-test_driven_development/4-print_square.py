#!/usr/bin/python3
"""definition for print_square function"""

def print_square(size):
    """
    function that prints a square with the character #.

    parameters:
        size: int
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

