#!/usr/bin/python3
"""
    Module containing a function that returns the JSON
    representation of an object (string):
"""

import json


def to_json_string(my_obj):
    """
        definition for to_json_string function.

        Args:
        my_obj: object to be serialised to json format.
    """

    return (json.dumps(my_obj))
