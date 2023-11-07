#!/usr/bin/python3
"""function return the pbject or data structure"""
import json


def from_json_string(my_str):
    """from json"""
    objt = json.loads(my_str)
    return objt
