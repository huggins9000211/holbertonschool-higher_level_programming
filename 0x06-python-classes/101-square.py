#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if value[0] < 0 or value[1] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            else:
                self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        finally:
            if (not isinstance(value[0], int)) or (not isinstance(value[0], int)):
                raise TypeError("size must be an integer")

    def area(self):
        return self.size * self.size

    def my_print(self):
        for x in range(0, self.position[1]):
            print()
        for x in range(0, self.size):
            for x in range(0, self.position[0]):
                print(" ", end="")
            for x in range(0, self.size):
                print("#", end="")
            print()
        if self.size is 0:
            print()

    def __str__(self):
        for x1 in range(0, self.position[1]):
            print()
        for x2 in range(0, self.size):
            for y in range(0, self.position[0]):
                print(" ", end="")
            for y in range(0, self.size):
                print("#", end="")
            if not(x2 is self.size - 1):
                print()
        if self.size is 0:
            return ""
        return ""
