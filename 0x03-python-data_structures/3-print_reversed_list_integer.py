#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = len(my_list) - 1
    if not my_list:
        return None
    while rev >= 0:
        print("{:d}".format(my_list[rev]))
        rev -= 1
