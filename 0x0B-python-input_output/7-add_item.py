#!/usr/bin/python3
"""
    Module containing a script that adds all arguments to a Python list,
    and then save them to a file:
"""

import os
import json
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

lists_file = "add_item.json"
lists = []

if os.path.exists(lists_file) and os.path.getsize(lists_file) > 0:
    lists = load_from_json_file(lists_file)

if sys.argv:
    for item in sys.argv[1:]:
        lists.append(item)
save_to_json_file(lists, lists_file)
