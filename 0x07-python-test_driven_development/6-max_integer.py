#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(my_list=None):
    """
    Function to find and return the max integer in a list of integers

    Parameters:
         my_list: (list) list of integers.

    Returns:
          None if list is empty.
          otherwise max integer in the list.
    """
    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        return None
    result = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > result:
            result = my_list[i]
        i += 1
    return result
