#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arggs = sys.argv
    i = 1
    if len(arggs) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(arggs) - 1))
    for x in range(1, len(arggs)):
        print("{}: {}".format(i, arggs[x]))
        i += 1
