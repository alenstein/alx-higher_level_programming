#!/usr/bin/python

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(*args):
    """
    This function adds all arguments to a Python list, and
    then save them to a file.

    Parameters:
        *args: Variable length argument list.

    Returns:
        None.
    """
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    for arg in args:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
