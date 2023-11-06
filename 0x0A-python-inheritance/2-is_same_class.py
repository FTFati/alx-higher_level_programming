#!/usr/bin/python3
''' function that returns True if the object is
exactly an instance of the specified class'''


def is_kind_of_class(obj, a_class):
    '''Method that return True if an object is
    an instance of a class that inherited from'''

    return isinstance(obj, a_class)
