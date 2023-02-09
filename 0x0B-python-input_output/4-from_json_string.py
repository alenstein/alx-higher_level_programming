#!/usr/bin/python3
""" Module containing definition for from_json_string """

import json


def from_json_string(my_str):
    """
    This function takes a JSON string and returns an object (Python data structure) represented by the JSON string.

    Parameters:
    my_str (str): The JSON string to be converted.

    Returns:
    obj (object): The object (Python data structure) represented by the JSON string.
    """
    obj = json.loads(my_str)
    return obj
