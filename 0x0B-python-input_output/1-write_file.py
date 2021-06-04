#!/usr/bin/python3
'''Write an ext file'''


def write_file(filename="", text=""):
    '''Writes to an ext file'''
    with open(filename, 'w') as file:
        return file.write(text)
