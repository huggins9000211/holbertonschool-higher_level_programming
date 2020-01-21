#!/usr/bin/python3
"""File I/O"""


def write_file(filename="", text=""):
    """File I/O"""
    with open(filename, "w") as f:
        return f.write(text)
