#!/usr/bin/python3
""" Module containing the definition for class Rectangle"""

import sys
sys.path.append("/models/")

Base = __import__('base').Base


class Rectangle(Base):
    """A class that represents a rectangle.
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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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

    def area(self):
        """ returns the area of the rectangle object """
        return self.__width * self.__height

    def display(self):
        """
        displays a rectangle that  fits the dimensions x and y.
        """
        rectangle = self.__y * "\n"
        for i in range(self.__height):
            rectangle += (" " * self.__x)
            rectangle += ("#" * self.__width) + "\n"

        print(rectangle, end='')

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
