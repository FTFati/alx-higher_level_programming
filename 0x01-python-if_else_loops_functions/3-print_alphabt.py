#!/usr/bin/python3
for char in range(97, 122):
    if char != 101 and char != 113:
        print("{}".format(chr(char)), end='')
