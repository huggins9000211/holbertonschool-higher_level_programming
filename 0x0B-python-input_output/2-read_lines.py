#!/usr/bin/python3
"""File I/O"""
read_file = __import__('0-read_file').read_file


def read_lines(filename="", nb_lines=0):
    """File I/O"""
    if nb_lines <= 0:
        read_file(filename)
        return
    i = 0
    with open(filename, "r") as f:
        for line in f:
            print(line)
            i += 1
            if i is nb_lines:
                break
