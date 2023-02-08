#!/usr/bin/python3
"""Module containing a function that checks if a class is same as or
    or inherits from a particular class"""


def is_kind_of_class(obj, a_class):
    """definition for function  that returns True if the object
    is an instance of, or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Parameters:
    obj: the object to be checked.
    a_class: the class to be compared with.

    Returns:
    True: if the object is an instance of that specified class.
    False: if the object is not the same type as the specified class.
    """

    return isinstance(obj, a_class)
