#!/usr/bin/python3
capital = False
index = 122
while (index >= 97):
    if capital:
        print(chr(index - 32), end="")
        capital = False
    else:
        print(chr(index), end="")
        capital = True
    index = index - 1
