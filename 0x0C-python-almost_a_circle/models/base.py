#!/usr/bin/python3
"""a classe base"""
import csv
import json


class Base:
    """insert attributes and methodes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize
        args: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string representation (serialization)"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            res = json.dumps(list_dictionaries)
            return res

    @staticmethod
    def from_json_string(json_string):
        """json string to dictionary"""
        if json_string is None or not json_string:
            return []
        else:
            res = json.loads(json_string)
            return res

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = [objt.to_dictionary() for objt in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as d:
            d.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """return instances with all attributes"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            temp = Rectangle(1, 1)
        elif cls is Square:
            temp = Square(1)
        else:
            temp = None
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """return list of instance"""
        from os import path
        f = "{}.json".format(cls.__name__)
        if not path.isfile(f):
            return []
        with open(f, "r", encoding="utf-8") as fl:
            return [
                    cls.create(**r_dic)
                    for r_dic in cls.from_json_string(fl.read())
                ]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialization to csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        f_n = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            lst_d = [0, 0, 0, 0, 0]
            lst_k = ['id', 'width', 'height', 'x', 'y']
        else:
            lst_d = ['0', '0', '0', '0']
            lst_k = ['id', 'size', 'x', 'y']

        res = []

        if not list_objs:
            pass
        else:
            for ob in list_objs:
                for ln in range(len(lst_k)):
                    lst_d[ln] = ob.to_dictionary()[lst_k[ln]]
                res.append(lst_d[:])

        with open(f_n, 'w') as fl:
            writer = csv.writer(fl)
            writer.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """deserialization of csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        import os.path
        f_n = "{}.csv".format(cls.__name__)

        if os.path.exists(f_n) is False:
            return []

        with open(f_n, 'r') as fl:
            reader = csv.reader(fl)
            l_csv = list(reader)

        if cls.__name__ == "Rectangle":
            l_k = ['id', 'width', 'height', 'x', 'y']
        else:
            l_k = ['id', 'size', 'x', 'y']

        res = []

        for items in l_csv:
            d_csv = {}
            for ln in enumerate(items):
                d_csv[l_k[ln[0]]] = int(ln[1])
            res.append(d_csv)

        l_i = []

        for items_1 in range(len(res)):
            l_i.append(cls.create(**res[items_1]))
        return l_i

    @staticmethod
    def draw(list_rectangles, list_squares):
        """open window and draw rectangle and square"""
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for j in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((j.x + t.pos()[0], j.y - t.pos()[1]))
            t.pensize(10)
            t.forward(j.width)
            t.left(90)
            t.forward(j.height)
            t.left(90)
            t.forward(j.width)
            t.left(90)
            t.forward(j.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
