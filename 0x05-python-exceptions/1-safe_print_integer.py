#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
    except ValueError:
        None
    if value is int:
        return True
    return False
