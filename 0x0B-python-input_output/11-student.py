#!/usr/bin/python3
'''JSON Serialization'''


class Student:
    '''Student Class'''

    def __init__(self, first_name, last_name, age):
        '''Class definition'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return a representation of the dictionary'''
        if attrs is None:
            return self.__dict__

        new = {}

        for key, value in self.__dict__.items():
            if key in attrs:
                new[key] = value

        return new

    def reload_from_json(self, json):
        '''JSON Deserialize'''
        self.__dict__.update(json)
