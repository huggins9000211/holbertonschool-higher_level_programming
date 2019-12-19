#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for list_item in matrix:
        result.append(list(map(lambda x: x ** 2, list_item)))
    return(result)
