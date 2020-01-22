#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""MY list"""


class Rectangle(BaseGeometry):
    """Mylist claass"""

    def __init__(self, width, height):
        """test"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """test"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """test"""
        return self.__width * self.__height
