#!/usr/bin/python3
i = 0
i2 = 1
i3 = 1
while i < 9:
    while i2 <= 9:
        if (not(i2 == 9 and i == 8)):
            print("{}{}".format(i, i2), end=", ")
        i2 = i2 + 1
    i2 = i3 + 1
    i3 = i2
    i = i + 1
print("89")
