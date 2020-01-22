#!/usr/bin/python3
"""MY list"""


class BaseGeometry():
    """Mylist claass"""

    def area(self):
        """test"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """test"""
        if not (type(value) is int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
