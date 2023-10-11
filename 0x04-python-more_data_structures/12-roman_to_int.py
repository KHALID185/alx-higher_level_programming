#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n_r = 0
    c = 0
    for items in reversed(roman_string):
        n_r = d[items]
        c += n_r if c < n_r * 5 else -n_r
    return c
