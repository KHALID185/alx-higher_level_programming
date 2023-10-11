#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del (list(a_dictionary.keys())[list(a_dictionary.values()).index(value)]))
    return a_dictionary
