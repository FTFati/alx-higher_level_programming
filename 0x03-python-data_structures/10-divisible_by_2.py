#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) != 0:
        new = [num % 2 == 0 for num in my_list]
        return new
