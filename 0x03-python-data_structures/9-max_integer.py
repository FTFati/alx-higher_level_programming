#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        n_max = 0
        for num in my_list:
            if num > n_max:
                n_max = num
        return n_max
