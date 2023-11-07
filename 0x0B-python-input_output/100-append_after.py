#!/usr/bin/python3
"""fct insert a line of a text in file"""


def append_after(filename="", search_string="", new_string=""):
    """append a line after a search string"""
    with open(filename, 'r', encoding="utf-8") as file:
        line = []
        while 1:
            ln = file.readline()
            if ln == "":
                break
            line.append(ln)
            if search_string in ln:
                line.append(new_string)
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(line)
