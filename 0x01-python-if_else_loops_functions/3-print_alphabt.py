#!/usr/bin/python3
for char in range(97, 122):
    if chr(char) is not 101 and chr(char) is not 113:
        print("{}".format(chr(char)), end='')
