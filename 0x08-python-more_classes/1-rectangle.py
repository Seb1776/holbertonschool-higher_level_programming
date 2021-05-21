#!/usr/bin/python3
'''Class Rectangle'''


class Rectangle:
    '''Class Rectangle'''
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

        if not isinstance(self.__height, int):
            raise TypeError('height must be integer')

        if not isinstance(self.__width, int):
            raise TypeError('width must be integer')

        if self.__width < 0:
            raise ValueError('width must be >= 0')

        if self.__height < 0:
            raise ValueError('height must be >= 0')

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        elif self.__width < 0:
            raise ValueError('width must be >= 0')

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        elif self.__height < 0:
            raise ValueError('height must be >= 0')
