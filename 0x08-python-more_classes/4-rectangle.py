#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height is 0) or (self.width is 0):
            return 0
        return self.height + self.width + self.height + self.width

    def __str__(self):
        mylist = []
        if (self.height is 0) or (self.width is 0):
            return ""
        for x in range(0, self.height):
            mylist.append("#" * self.width)
            if x != self.height - 1:
                mylist.append("\n")
        return ''.join(mylist)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
