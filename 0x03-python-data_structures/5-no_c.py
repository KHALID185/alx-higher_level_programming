#!/usr/bin/python3
def no_c(my_string):
    after_rem = ""
    for st in range(len(my_string)):
        if (my_string[st] != 'c' and my_string[st] != 'C'):
            after_rem += my_string[st]
    return after_rem
