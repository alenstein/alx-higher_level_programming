#!/usr/bin/python3
"""
Module containing a class Square that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Definition for Square class with instantiation and integer validation
    """

    def __init__(self, size):
        """
        Initialisation for a Square class object

        Parameters:
             size: a positive integer defining the sides of the square.
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        returns the calculated area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        pass
