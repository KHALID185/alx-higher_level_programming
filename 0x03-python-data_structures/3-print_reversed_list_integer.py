#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    while num != 0:
        print("{:d}".format(my_list[num - 1]))
        num -= 1
