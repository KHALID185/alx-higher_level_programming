#!/usr/bin/python3
for alph in range(ord('a'), ord('z') + 1):
    if alph != ord('e') and alph != ord('q'):
        print("{:c}".format(alph), end="")
