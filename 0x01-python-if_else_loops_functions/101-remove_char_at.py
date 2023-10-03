#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for k, m in enumerate(str):
        if k != n:
            str2 += m
        return str2
