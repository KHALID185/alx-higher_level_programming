#!/usr/bin/python3
"""using json create object"""
import json


def load_from_json_file(filename):
    """write object using json"""
    with open(filename, 'r', encoding='utf-8') as file:
        cr = json.load(file)
    return cr
