#!/usr/bin/python3
"""using json create object"""
import json


def load_from_json_file(filename):
    """create object from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        cr = json.load(file)
    return cr
