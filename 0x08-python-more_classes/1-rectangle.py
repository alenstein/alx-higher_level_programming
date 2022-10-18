#!/usr/bin/python3
"""
    Module with empty class for creating a rectangle.
"""


class Rectangle:
    """
        definition for class Rectangle
        Args:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property for getting width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width value """
        if isinstance(value, int):
            pass
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property for getting height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height value """
        if isinstance(value, int):
            pass
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
