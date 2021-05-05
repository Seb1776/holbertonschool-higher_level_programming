#!/usr/bin/env python3


def no_c(my_string):
    lst = list(my_string)
    i = 0

    for c in lst:
        if c is 'c' or c is 'C':
            lst[i] = ''
        i += 1

    return "".join(lst)
