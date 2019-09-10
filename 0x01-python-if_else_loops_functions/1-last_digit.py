#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numString = int(repr(number)[-1])
print("Last digit of {} is {}".format(number, numString), end=" ")
if numString > 5:
    print("and is greater than 5")
elif numString == 0:
    print("and is 0")
elif numString < 6 and numString != 0:
    print("and is less than 6 and not 0")
