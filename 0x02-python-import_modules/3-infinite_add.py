#!/usr/bin/python3
import sys
argv = sys.argv
result = 0
count = 0
if __name__ == "__main__":
    for arg in sys.argv:
        if count != 0:
            result += int(arg)
        else:
            count += 1
    print("{:d}".format(result))
