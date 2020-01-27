#!/usr/bin/python3
""" Circle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Circle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Circle """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Circle """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Circle """
        if len(args) == 0:
            for x, y in kwargs.items():
                setattr(self, x, y)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """ Circle """
        result = {}
        result["id"] = self.id
        result["size"] = self.size
        result["x"] = self.x
        result["y"] = self.y
        return result

    @property
    def size(self):
        """ Circle """
        return self.width

    @size.setter
    def size(self, value):
        """ Circle """
        self.width = value
        self.height = value
