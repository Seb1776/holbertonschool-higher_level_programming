#!/usr/bin/python3
'''Class Rectangle'''


class Rectangle:
    '''Class Rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return self.__width * self.__height

    def __str__(self):
        contain = ""
        if self.__width is 0 or self.__height is 0:
            return contain
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    contain += "#"
                contain += '\n'

            return contain[:-1]

    def __repr__(self):
        return ('Rectangle(' + str(self.width) + ', ' + str(self.height) + ')')

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
