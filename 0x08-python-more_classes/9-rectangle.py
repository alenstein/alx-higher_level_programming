#!/usr/bin/python3
"""
    Module with  class for creating a rectangle.
"""


class Rectangle:
    """
        definition for class Rectangle
        Public class attribute number_of_instances:
            - Initialized to 0
            - Incremented during each new instance instantiation
            - Decremented during each instance deletion
        Args:
        width: width of the rectangle
        height: height of the rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        __class__.number_of_instances += 1

    @property
    def width(self):
        """ get width value """
        return self.__width

    @width.setter
    def width(self, value):
        """
            sets width value
            Args:
            value: new width value to be set.
        """
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
        """ gets height value """
        return self.__height

    @height.setter
    def height(self, value):
        """
            sets height value
            Args:
            value: new height value to be set
        """
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
        """
            Returns a represantation of  Rectangle instance,
            using the '#' character.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect_str = ""
        for h in range(self.height):
            for w in range(self.width):
                rect_str += str(self.print_symbol)
            rect_str += "\n"
        return rect_str[:-1]

    def __repr__(self):
        """
           Returns a string representation of the rectangle,
           to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """"
            prints message when an instance of Rectangle is deleted
            decrements number_of_instances during each instance deletion.
        """
        __class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Returns the biggest rectangle based on the area

        Args:
            rect_1: first rectangle instance
            rect_2_: second rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
            Returns a new Ractangle instance with width == height == size

        Args:
            size: size for the new rectangle
        """
        return cls(size, size)
