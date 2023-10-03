#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{:d} is positive".format(number)) if number > 0 else print("{:d} is zero".format(number)) if number == 0 else print("{:d} is negative".format(number))
