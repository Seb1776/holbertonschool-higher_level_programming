#!/usr/bin/python3
'''Description'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Calculates the Area of the square'''

    def __init__(self, size):
        '''Inheritance of Method'''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
