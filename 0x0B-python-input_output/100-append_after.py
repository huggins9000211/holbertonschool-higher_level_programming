#!/usr/bin/python3
"""File I/O"""
read_file = __import__('0-read_file').read_file


def append_after(filename="", search_string="", new_string=""):
    """File I/O"""
    indexesList = []
    i = 0
    with open(filename, "r") as f:
        allLines = f.readlines()
    for x in allLines:
        if search_string in x:
            indexesList.append(i + 1)
            i += 1
        i += 1
    for x in indexesList:
        allLines.insert(x, new_string)
    with open(filename, "w") as f:
        f.write("".join(allLines))
