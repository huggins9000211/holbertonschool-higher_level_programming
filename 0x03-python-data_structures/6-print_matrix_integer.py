#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            if x:
                for y in x[:-1]:
                    print("{:d}".format(y), end=" ")
                print("{:d}".format(x[-1]))
            else:
                print("")
