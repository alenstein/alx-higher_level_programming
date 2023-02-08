#!/usr/bin/python3
"""Module containing a function that checks if an object's class
    is a sub class of a specific class.
"""


def inherits_from(obj, a_class):
    """Definition for inherits_from, function checks if an object belongs to
        a specific sub class.

        Parameters:
        obj: the object whose sub class is to be checked.
        a_class: the specified sub class.

        Returns:
        True: if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class.
        False: if otherwise.
    """

    return (type(obj) != a_class) and isinstance(obj, a_class)
