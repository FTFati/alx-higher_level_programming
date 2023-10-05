#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) == 2:
        print("{:d} ".format(len(argv) - 1) + "argument:")
        print("{:d} ".format(len(argv) - 1) + ": " + "{} ".format(argv[1]))
    elif len(argv) > 2:
        print("{:d} ".format(len(argv) - 1) + "arguments:")
        for i, arg in enumerate(argv[1:], start=1):
            print("{:d} ".format(i) + ": " + "{} ".format(arg))
    else:
        print("{:d} ".format(len(argv) - 1) + "arguments.")
