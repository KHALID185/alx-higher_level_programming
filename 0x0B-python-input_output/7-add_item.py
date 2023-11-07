#!/usr/bin/python3
'''load, add and save file'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_lst = list(sys.argv[1:])

try:
    o_d = load_from_json_file('add_item.json')
except Exception:
    o_d = []

o_d.extend(arg_lst)
save_to_json_file(o_d, 'add_item.json')
