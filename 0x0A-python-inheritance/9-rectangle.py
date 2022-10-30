#!/usr/bin/python3
"""Module containing a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition for class rectangle with instatiation
    """

    def __init__(self, width, height):
        """Initialises the rectangle object """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """return the rectangle description"""

        return "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                   self.__height)

    def area():
        """ method calculates the area of the rectangle """
        return self.__width * self.__height
