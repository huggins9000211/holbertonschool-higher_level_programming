#!/usr/bin/python3
"""File I/O"""


def append_write(filename="", text=""):
    """File I/O"""
    with open(filename, "a") as f:
        return f.write(text)
