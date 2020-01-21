#!/usr/bin/python3
"""File I/O"""


def number_of_lines(filename=""):
    """File I/O"""
    i = 0
    with open(filename, "r") as f:
        for line in f:
            i += 1
    return(i)
