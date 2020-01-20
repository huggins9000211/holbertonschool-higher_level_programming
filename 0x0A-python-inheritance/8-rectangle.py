#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""MY list"""


class Rectangle(BaseGeometry):
    """Mylist claass"""

    def __init__(self, width, height):
        """test"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
