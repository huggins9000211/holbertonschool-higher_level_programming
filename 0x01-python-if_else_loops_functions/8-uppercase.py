#!/usr/bin/python3
def uppercase(c):
    for x in c:
        num = ord(c)
        if num  <= 97 and num >= 122:
            num = num - 32;
        result = chr(num)
        print(result)
