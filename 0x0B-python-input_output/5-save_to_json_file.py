#!/usr/bin/python3
"""using json write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write object using json"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
