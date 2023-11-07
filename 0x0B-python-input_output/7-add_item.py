#!/usr/bin/python3
"""load, add and save file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = list(sys.argv[1:])

try:
    data = load_from_json_file('add_item.json')
except Exception:
    data = []

data.extend(arguments)
save_to_json_file(data, 'add_item.json')
