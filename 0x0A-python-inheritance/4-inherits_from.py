#!/usr/bin/python3
'''function that returns True if the object is an
instance of a class that inherited
(directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''Method that return True if an object is
    an instance of a classthat inherited from'''

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
