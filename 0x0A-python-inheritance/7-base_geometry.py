#!/usr/bin/python3
'''Description'''


class BaseGeometry:
    '''BaseGeometry Class'''

    def area(self):
        '''Empty Area Class'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''This method validates a given integer with a name'''

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
