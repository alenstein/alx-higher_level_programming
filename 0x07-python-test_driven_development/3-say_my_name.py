#!/usr/bin/python3
""" definition  for say_my_name function."""

def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name> <first
    parameters:
        first_name: string, first param
        last_name: string, second param
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

