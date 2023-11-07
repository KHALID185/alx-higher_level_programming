#!/usr/bin/python3
"""function return the JSON representation"""
import json


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str
