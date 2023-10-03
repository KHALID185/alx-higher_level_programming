#!/usr/bin/python3
for alph in range(25, -1, -1):
    character = alph + ord('A')
    if alph % 2 ==1:
        character += 32
    print("{:c}".format(character), end=""
