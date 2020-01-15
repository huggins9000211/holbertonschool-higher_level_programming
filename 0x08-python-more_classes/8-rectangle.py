#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height is 0) or (self.width is 0):
            return 0
        return self.height + self.width + self.height + self.width

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __str__(self):
        mystr = ''
        if (self.height is 0) or (self.width is 0):
            return ""
        for x in range(0, self.height):
            for y in range(0, self.width):
                mystr += str(self.print_symbol)
            if x != self.height - 1:
                mystr += '\n'
        return mystr
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
