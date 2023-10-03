#!/usr/bin/python3
itert = 0
for alph in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alph - itert)), end="")
    itert = 32 if itert == 0 else 0
