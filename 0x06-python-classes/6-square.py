#!/usr/bin/python3
""" Module defines a class that defines a square."""


class Square:
    """
        Defines a square with a private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """gets position value """
        return self.__position

    @position.setter
    def position(self, position):
        """ setting position value in a tuple of size 2"""
        if isinstance(position, tuple) and len(position) == 2:
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """gets data """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size value """
        if isinstance(value, int):
            pass
        else:
            raise TypeError("size must be an integer!")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """
        Public instance method: def area(self):
        that returns the current square area.
    """
    def area(self):
        return self.size ** 2

    """
        Public instance method: def my_print(self):
        that prints in stdout the square with the character #.
    """
    def my_print(self):
        """ function prints a square in stdout """
        cols = self.__size
        rows = cols

        if cols == 0:
            print()

        for cols in range(rows):
            for i in range(self.__position[0]):
                print(" ", end="")
            for rows in range(self.__size):
                print("#", end="")
            print()
