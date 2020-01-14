#!/usr/bin/python3
"""
    matrix_divided
"""


def matrix_divided(matrix, div):
    """ matrix_divided """
    newmatrix = []
    newlsit = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for x in range(0, len(matrix)):
        if size is not len(matrix[x]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in matrix[x]:
            if (not isinstance(matrix[x], list)) or \
                 (not isinstance(y, (int, float))):
                raise TypeError("matrix must be a matri\
x (list of lists) of integers/floats")

            result = y / div
            newlsit.append(round(result, 2))
        newmatrix.append(newlsit[:])
        newlsit.clear()
    return newmatrix
