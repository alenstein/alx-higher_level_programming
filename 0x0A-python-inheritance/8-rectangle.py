#!/usr/bin/python3
"""Module containing a class Rectangle that inherits
    from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Definition for sub class Rectangle """

    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
