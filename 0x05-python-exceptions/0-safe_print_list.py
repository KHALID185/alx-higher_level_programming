#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        while j < x:
            print(my_list[j], end="")
            j += 1
        except IndexError:
            None
    print()
    return j
