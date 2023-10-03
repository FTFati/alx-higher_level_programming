#!/usr/bin/python3
for char in [a for a in range(97, 122) if a != 101 and a != 113]:
    print(chr(char), end='')
