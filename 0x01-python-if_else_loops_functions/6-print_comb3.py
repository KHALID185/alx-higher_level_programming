#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num, 10):
    if num < num2:
        if num != 8 and num2 != 9:
            print("{:d}{:d}".format(num, num2), end=", ")
        else:
            print("{:d}{:d}".format(num, num2), end="\n")
