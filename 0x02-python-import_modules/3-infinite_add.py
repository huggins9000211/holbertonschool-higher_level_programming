#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arggs = sys.argv
    i = 0
    for x in range(1, len(arggs)):
        i = i + int(arggs[x])
    print(i)
