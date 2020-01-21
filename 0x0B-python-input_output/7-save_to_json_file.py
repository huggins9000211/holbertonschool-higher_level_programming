#!/usr/bin/python3
"""File I/O"""
import json


def save_to_json_file(my_obj, filename):
    """File I/O"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
