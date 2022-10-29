#!/usr/bin/python3
"""Module containing an improved BaseGeometry class."""


class BaseGeometry:
    """based on 5-base_geometry.py,has a
       Public instance method: def area(self):
       Public instance method: def integer_validator(self, name, value):
    """

    def area(self):
        """a public instance that raises an Exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method for validating a value

        Parameters:
        name: name (string) for the value.
        value: the value to be validated.
        """
        if isinstance(name, str):
            pass
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
