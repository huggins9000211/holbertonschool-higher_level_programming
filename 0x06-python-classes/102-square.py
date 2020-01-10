#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size * self.size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, y):
        return self.area() < y.area()

    def __le__(self, y):
        return self.area() <= y.area()

    def __eq__(self, y):
        return self.area() == y.area()

    def __ne__(self, y):
        return self.area() != y.area()

    def __gt__(self, y):
        return self.area() > y.area()

    def __ge__(self, y):
        return self.area() >= y.area()
