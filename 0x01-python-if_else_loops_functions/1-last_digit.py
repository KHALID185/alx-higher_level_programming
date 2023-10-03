#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 10:
    l_n = number % 10
else:
    l_n = number % -10
print("Last digit of {:d} is {:d}".format(number, l_n), end=" ")
if l_n > 5:
    print("and is greater than 5")
elif l_n == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
