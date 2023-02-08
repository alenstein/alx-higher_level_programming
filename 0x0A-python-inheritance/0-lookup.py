#!/usr/bin/python3
"""
    Module with a  function that returns the list of available attributes,
    and methods of an object.
"""


def lookup(obj):
    """
        definition for def lookup(obj): method

        Args:
        obj: an object of any class to look into.
    """
    data = dir(obj)
    return data
