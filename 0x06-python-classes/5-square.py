#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Class Square'''
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            for x in range(self.__size):
                print("{}".format("#" * self.__size))
