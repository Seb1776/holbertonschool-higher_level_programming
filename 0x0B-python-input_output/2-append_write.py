#!/usr/bin/python3
'''Appends string to end of file'''


def append_write(filename="", text=""):
    '''Appends string to the end of file'''
    with open(filename, 'a') as file:
        return file.write(text)
