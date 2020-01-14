#!/usr/bin/python3
"""
    text indentation
"""


def text_indentation(text):
    """ text indentation """
    justFound = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in range(0, len(text)):
        if text[x] in ['.', '?', ':']:
            print(text[x], end="\n\n")
            justFound = True
        else:
            if justFound and text[x] is ' ':
                pass
            else:
                justFound = False
                print(text[x], end="")
