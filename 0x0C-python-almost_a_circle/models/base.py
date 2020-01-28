#!/usr/bin/python3
""" Circle """
import json
import turtle
import csv


class Base:
    """ Circle """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Circle """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Circle """
        myTurtle = turtle.Turtle()

        for x in list_rectangles:
            myTurtle.speed(1)
            myTurtle.color("red", "black")
            myTurtle.begin_fill()
            myTurtle.forward(x.width)
            myTurtle.left(90)
            myTurtle.forward(x.height)
            myTurtle.left(90)
            myTurtle.forward(x.width)
            myTurtle.left(90)
            myTurtle.forward(x.height)
            myTurtle.end_fill()
            input("Press Enter to draw next rectangle")
            myTurtle.reset()

        for x in list_squares:
            myTurtle.speed(1)
            myTurtle.color("red", "black")
            myTurtle.begin_fill()
            myTurtle.forward(x.size)
            myTurtle.left(90)
            myTurtle.forward(x.size)
            myTurtle.left(90)
            myTurtle.forward(x.size)
            myTurtle.left(90)
            myTurtle.forward(x.size)
            myTurtle.end_fill()
            input("Press Enter to draw next square")
            myTurtle.reset()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open("{}.csv".format(cls.__name__), "w") as f:
            cavWriter = csv.writer(f)

    @classmethod
    def load_from_file_csv(cls):
        myList = []
        result = []
        with open("{}.csv".format(cls.__name__), 'r') as f:
            csvReader = csv.reader(f)
            if cls.__name__ == "Rectangle":
                for x in csvReader:
                    myList.append({
                        "id": x[0],
                        "width": x[1],
                        "height": x[2],
                        "x": x[3],
                        'y': x[4]
                    })
            else:
                for x in csvReader:
                    myList.append({
                        "id": x[0],
                        "size": x[1],
                        "x": x[2],
                        'y': x[3]
                    })
        for x in myList:
            result.append(cls.create(**x))
        return result

    @classmethod
    def save_to_file(cls, list_objs):
        """ Circle """
        myList = []
        for x in list_objs:
            myList.append(x.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as f:
            result = cls.to_json_string(myList)
            f.write(result)

    @classmethod
    def create(cls, **dictionary):
        """ Circle """
        if cls.__name__ == "Rectangle":
            newObj = cls(1, 1)
            newObj.update(**dictionary)
            return newObj
        else:
            newObj = cls(1)
            newObj.update(**dictionary)
            return newObj
    @classmethod
    def load_from_file(cls):
        """ Circle """
        myList = []
        try:
            with open("{}.json".format(cls.__name__)) as f:
                loadedString = f.read()
        except FileNotFoundError:
            return []
        pythonString = cls.from_json_string(loadedString)
        for x in pythonString:
            myList.append(cls.create(**x))
        return myList

    @staticmethod
    def from_json_string(json_string):
        """ Circle """
        if json_string is None:
            return []
        if json_string == "":
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Circle """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
