#!/usr/bin/python3
"""MY list"""


class MyList(list):
    """Mylist claass"""

    def print_sorted(self):
        """myList custom print"""
        copy = self[:]
        copy.sort()
        print(copy)
