#!/usr/bin/python3
""" Circle """
from models.base import Base


class Rectangle(Base):
    """ Circle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Circle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """ Circle """
        result = {}
        result["id"] = self.id
        result["width"] = self.width
        result["height"] = self.height
        result["x"] = self.x
        result["y"] = self.y
        return result

    def __str__(self):
        """ Circle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """ Circle """
        return self.width * self.height

    def display(self):
        """ Circle """
        for x in range(0, self.y):
            print()
        for x in range(0, self.height):
            print(' ' * self.x, end='')
            for x in range(0, self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Circle """
        if len(args) == 0:
            for x, y in kwargs.items():
                setattr(self, x, y)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    @property
    def width(self):
        """ Circle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Circle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Circle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Circle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Circle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Circle """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Circle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Circle """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
