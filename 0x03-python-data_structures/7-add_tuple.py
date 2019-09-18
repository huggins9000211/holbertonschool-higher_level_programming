#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = (0, 0)
    result[0] = tuple_a[0] + tuple_b[0]
    result[1] = tuple_a[1] + tuple_b[1]
    return(result)
