#!/usr/bin/python3
if __name__ == "__main__":
    from calculation_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b , o = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
    if o == "+": print("{} + {} = {}".format(a, b, add(a, b)))
    elif o == "-": print("{} - {} = {}".format(a, b, sub(a, b)))
    elif o == "/": print("{} / {} = {}".format(a, b, div(a, b)))
    elif o == "*": print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
