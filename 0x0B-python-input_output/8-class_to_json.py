#!/usr/bin/python3
'''JSON Serialization'''


def class_to_json(obj):
    '''Returns the description of a Dictionary in a simple structure'''
    return obj.__dict__
