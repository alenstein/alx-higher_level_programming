#!/usr/bin/python3
"""Module containing a class Rectangle that inherits
    from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Definition for sub class Rectangle """

    def __init__(self, width, height):
        """Initialiser for new objects
            Args:
            width: width of the new object.
            height: height of the new object.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
