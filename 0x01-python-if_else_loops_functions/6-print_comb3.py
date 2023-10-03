#!/usr/bin/python3
for num in range(0, 10):
    for count in range(num + 1, 10):
        if num == 8 and count == 9:
            print("{}{}".format(num, count))
        else:
            print("{}{}".format(num, count), end=", ")
