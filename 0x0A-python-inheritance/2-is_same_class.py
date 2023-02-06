#!/usr/bin/python3
"""Module containing a function that  checks if an object is
    Exact same object
"""


def is_same_class(obj, a_class):
    """definition for function that checks if an object is an instance of a
        specified class.

        Parameters:
        obj: object to be checked
        a_class: the class to compare with the object class

        Returns:
        True: if the object is exactly an instance of the specified class.
            Othewise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
