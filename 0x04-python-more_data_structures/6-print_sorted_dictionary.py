#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ky, values in sorted(a_dictionary.items()):
        print("{}: {}".format(ky, values))
