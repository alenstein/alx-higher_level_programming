#!/usr/bin/python3
"""Module containing a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition for class rectangle with instatiation
    """

    def __init__(self, width, height):
        BaseGeometry.__init__(self, width, height)

    def __str__(self):
        """return the rectangle description"""

        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.width, self.height)

    def area():
        """ method calculates the area of the rectangle """
        return self.__width * self.__height
