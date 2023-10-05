#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    addition = 0
    for number in range (len(sys.argv) - 1):
        addition += int(sys.argv[number + 1])
    print(addition)
