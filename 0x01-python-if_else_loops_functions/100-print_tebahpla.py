#!/usr/bin/python3
capital = False
index = 122
tempStr = ''
while (index >= 97):
    if capital:
        tempStr = chr(index - 32)
        capital = False
    else:
        tempStr = chr(index)
        capital = True
    print(tempStr, end = '')
    index = index - 1
