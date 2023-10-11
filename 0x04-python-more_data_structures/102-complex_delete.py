#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = list(a_dictionary.keys())[list(a_dictionary.values()).index(value)]))
    if a_dictionary["d"] == value:
        del a_dictionary["d"]
    return a_dictionary
