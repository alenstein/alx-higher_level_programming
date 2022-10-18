#!/usr/bin/python3
"""
    Module with  class for creating a rectangle.
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

    """
        Public instance method: area(self),
        that returns the rectangle area
    """
    def area(self):
        """ calculates the area of the rectangle """
        return self.__height * self.__width

    """
        Public instance method: perimeter(self),
        that returns the rectangle perimeter
    """
    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a represantation of  Rectangle instance,
        using the '#' character"""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for h in range(self.height):
            for w in range(self.width):
                rect_str += "#"
            rect_str += "\n"
        return rect_str[:-1]
