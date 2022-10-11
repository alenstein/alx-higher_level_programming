#!/usr/bin/python3
"""Module with a class for definining a square with an integer size """


class Square:
    """
        Defines a square with a private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
    """

    def __init__(self, size=0):
        """ setting size value """
        if isinstance(size, int):
            pass
        else:
            raise TypeError("size must be an integer!")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """
        Public instance method: def area(self):
        that returns the current square area.
    """
    def area(self):
        return self.__size ** 2
