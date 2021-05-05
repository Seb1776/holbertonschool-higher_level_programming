#!/usr/bin/env python3


def no_c(my_string):
    for c in my_string:
        if c is not None:
            current_c = ord(c)

            if current_c == 67 or current_c == 99:
                c = ''

            print(c, end='')
