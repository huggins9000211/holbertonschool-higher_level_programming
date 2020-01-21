#!/usr/bin/python3
"""File I/O"""
import json


def load_from_json_file(filename):
    """File I/O"""
    with open(filename, "r") as f:
        return json.load(f)
