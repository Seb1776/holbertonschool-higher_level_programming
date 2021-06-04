#!/usr/bin/python3
'''Read ext file'''


def read_file(filename=""):
    '''Call ext file, read and print'''
    with open(filename) as file:
        print(file.read(), end='')
