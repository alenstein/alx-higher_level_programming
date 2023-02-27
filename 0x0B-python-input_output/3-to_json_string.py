#!/usr/bin/python3
""" Module containing definition for to_json_string function """

import json


def to_json_string(my_obj):
    """
    This function takes an object (string) and returns its JSON representation.

    Args:
        my_obj (string): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
