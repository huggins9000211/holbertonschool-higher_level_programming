#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arggs = sys.argv
    i = 0
    for x in range(1, len(arggs)):
        i = i + int(x)
    print(i)
