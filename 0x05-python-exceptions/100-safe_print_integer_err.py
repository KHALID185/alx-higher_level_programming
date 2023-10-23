#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    bol = True
    try:
        print("{:d}".format(value))
    except Exception as exp:
        print("Exception:", exp, file=sys.stderr)
        bol = False
    return bol
