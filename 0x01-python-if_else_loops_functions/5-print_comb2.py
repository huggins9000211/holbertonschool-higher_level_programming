#!/usr/bin/python3
num = 0
while num < 100:
    numString = str(num).zfill(2)
    if num == 99:
        print("99")
    else:
        print("{}".format(numString), end=", ")
    num = num + 1
