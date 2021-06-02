#!/usr/bin/python3
'''Description'''


def is_kind_of_class(obj, a_class):
    '''
    Return if the object is a class instance or a class inheritance,
    if is a clas instance returns True, otherwise returns False
    '''
    return isinstance(obj, a_class)
