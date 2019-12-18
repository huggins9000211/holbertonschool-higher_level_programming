#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return None
    length = len(sentence)
    char = sentence[0]
    return length, char
