#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arggs = sys.argv
    i = 1
    print("{} arguments:".format(len(arggs) - 1))
    for x in range(1, len(arggs)):
        print("{}: {}".format(i, arggs[x]))
        i += 1
