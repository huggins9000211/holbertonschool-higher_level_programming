#!/usr/bin/python3
def uppercase(c):
    for x in c:
        num = ord(x)
        result = ""
        if num >= 97 and num <= 122:
            num = num - 32
            result = chr(num)
        else:
            result = chr(num)
        print("{}".format(result), end="")
    print("")
