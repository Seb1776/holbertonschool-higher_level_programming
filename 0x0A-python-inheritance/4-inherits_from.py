#!/usr/bin/python3
'''Description'''


def inherits_from(obj, a_class):
    '''
    Returns true if the object is an instance of the inheritence class
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
