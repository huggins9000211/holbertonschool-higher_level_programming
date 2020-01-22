#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""MY list"""


class Square(Rectangle):
    """Mylist claass"""

    def __init__(self, size):
        """test"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """test"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """test"""
        return self.__size * self.__size
