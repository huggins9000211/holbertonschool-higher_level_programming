#!/usr/bin/python3
"""
    print square
"""


def print_square(size):
    """ print square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for x in range(0, size):
        print("#"*size)
    if size is 0:
        print()

