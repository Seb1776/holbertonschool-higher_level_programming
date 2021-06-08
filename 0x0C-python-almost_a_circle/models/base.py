#!/usr/bin/python3
'''Description Base Class'''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Method Constructor
        Define id attribute
        '''
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
