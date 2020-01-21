#!/usr/bin/python3
"""File I/O"""


class Student():
    """File I/O"""

    def __init__(self, first_name, last_name, age):
        """File I/O"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """File I/O"""
        if checktype(attrs):
            myDict = {}
            for x in attrs:
                try:
                    temp = getattr(self, x)
                except Exception:
                    pass
                else:
                    myDict[x] = temp
            return (myDict)
        return (self.__dict__)
    
    def reload_from_json(self, json):
        """File I/O"""
        for x, y in json.items():
            setattr(self, x, y)


def checktype(obj):
    """File I/O"""
    return bool(obj) and all(isinstance(elem, str) for elem in obj)
