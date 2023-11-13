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
        """serialization in csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [
                                [a.id, a.width, a.height, a.x, a.y]
                                for a in list_objs
                            ]
            else:
                list_objs = [
                                [a.id, a.size, a.x, a.y]
                                for a in list_objs
                            ]
        with open(
                    '{}.csv'.format(cls.__name__),
                    'w', newline='', encoding='utf-8'
                    ) as fl:
            writer = csv.writer(fl)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize in csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        lst = []
        with open(
                    '{}.csv'.format(cls.__name__),
                    'r', newline='', encoding='utf-8'
                    ) as fl:
            reader = csv.reader(fl)
            for ln in reader:
                ln = [int(b) for b in ln]
                if cls is Rectangle:
                    dct = {
                            "id": ln[0], "width": ln[1], "height": ln[2],
                            "x": ln[3], "y": ln[4]
                        }
                else:
                    dct = {
                            "id": ln[0], "size": ln[1],
                            "x": ln[2], "y": ln[3]
                        }
                    lst.append(cls.create(**dct))
        return lst

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
