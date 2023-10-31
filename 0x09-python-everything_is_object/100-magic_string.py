#!/usr/bin/python3
'''function that returns a string “BestSchool”
n times the number of the iteration'''


def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
