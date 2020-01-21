#!/usr/bin/python3
"""File I/O"""


def read_file(filename=""):
    """File I/O"""
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')
