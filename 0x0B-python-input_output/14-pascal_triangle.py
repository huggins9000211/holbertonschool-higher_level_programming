#!/usr/bin/python3
"""File I/O"""


def pascal_triangle(n):
    """File I/O"""
    endResult = []
    if n <= 0:
        return []
    for line in range(0, n):
        tempList = []
        for i in range(0, line + 1):
            tempList.append(binomialCoeff(line, i))
        endResult.append(tempList)
    return endResult


def binomialCoeff(n, k):
    """File I/O"""
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res
