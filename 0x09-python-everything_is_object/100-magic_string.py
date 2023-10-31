#!/usr/bin/python3
def magic_string():
    magic_string.cnt = getattr(magic_string, 'cnt', 0) + 1
    return ", ".join(["BestSchool" for items in range(magic_string.cnt)])
