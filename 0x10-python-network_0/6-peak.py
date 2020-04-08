#!/usr/bin/python3
""" hello """


def findPeakUtil(arr, low, high, n):
    mid = low + (high - low)/2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


def find_peak(list_of_integers):
    if list_of_integers:
        return list_of_integers[findPeakUtil(list_of_integers, 0, len(
            list_of_integers) - 1, len(list_of_integers))]
