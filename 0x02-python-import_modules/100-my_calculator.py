#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(sys.argv[1]
    b = int(sys.argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
