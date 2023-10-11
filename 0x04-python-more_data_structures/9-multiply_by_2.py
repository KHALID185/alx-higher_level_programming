#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dct = a_dictionary.copy()
    ky = list(dct.keys())
    for items in ky:
        dct[items] *= 2
    return dct
