#!/usr/bin/python3
'''Description'''


class BaseGeometry:
    '''
    Gemoetry Class

    Methods:

    area() -- Empty for now

    integer_validator(self, name, value) -- Validates a given integer
        with a given string [name]

        Args => self: Itself
                name: Name of the value
                value: Value of the data
    '''

    def area(self):
        '''Empty area method'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates an integer with a given name'''

        if type(value) != int:
            raise TypeError('{} must be integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
