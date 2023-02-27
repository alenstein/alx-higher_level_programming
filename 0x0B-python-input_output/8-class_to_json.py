#!/usr/bin/python3
""" Module containing the definition for class_to_json function """


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
     (list, dictionary, string, integer and boolean) for JSON serialization of
     an object.

    Parameters:
    obj (object): An instance of a Class

    Returns:
    dict: A dictionary description with simple data structure
     (list, dictionary, string, integer and boolean) for JSON serialization of
      an object.
    """
    json_dict = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
