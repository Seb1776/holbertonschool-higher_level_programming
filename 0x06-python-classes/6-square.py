#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Class Square'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position    

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) is not 2 or 
                type(value[0]) is not int or value[0] < 0 or
                type(value[1]) is not int or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            print('\n' * self.__position[1], end='')

            for x in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
