#!/usr/bin/python3
""" Module containing definition for class base"""


class Base:
    """
    The base class for all other classes in this project.

    The goal of this class is to manage the id attribute in all future classes
    and to avoid duplicating the same code and bugs.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the
            number of instances of the class that have been created.

        id (int): A public instance attribute that represents the unique
            identifier of each instance of the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Parameters:
            id (int, optional): The unique identifier for the instance.
                If not provided, a new identifier is generated based on the
                number of instances that have already been created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
