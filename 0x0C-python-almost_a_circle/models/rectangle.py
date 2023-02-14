#!/usr/bn/python3
""" Module containing the definition for class Rectangle"""

from base import Base


class Rectangle(Base):
    """A class that represents a rectangle.

    Attributes:
        id (int): A unique identifier for the instance.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The horizontal position of the rectangle.
        y (int): The vertical position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The horizontal position of the rectangle.
                Defaults to 0.
            y (int, optional): The vertical position of the rectangle.
                Defaults to 0.
            id (int, optional): The unique identifier for the instance.
                Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Parameters:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be positive")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Parameters:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be positive")
        self.__height = value

    @property
    def x(self):
        """int: The horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position of the rectangle.

        Parameters:
            value (int): The new horizontal position of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not negative.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x cannot be negative")
        self.__x = value

    @property
    def y(self):
        """int: The vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle.

        Parameters:
            value (int): The new vertical position of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not negative.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y cannot be negative")
        self.__y = value
