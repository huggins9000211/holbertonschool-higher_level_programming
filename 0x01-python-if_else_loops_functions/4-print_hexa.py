#!/usr/bin/python3
num = 0
while num < 99:
    hexString = hex(num)
    print("{} = {}".format(num, hexString))
    num = num + 1
