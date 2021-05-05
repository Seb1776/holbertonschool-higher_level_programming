#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    listlen = len(my_list) - 1
    
    if listlen < 0:
        return None
    else:
        for i in range(listlen, -1, -1):
            print('{:d}'.format(my_list[i]))
