#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        garage = fct(*args)
        return garage
    except Exception as exp:
        print("Exception: {}".format(exp), file=sys.stderr)
        return None
