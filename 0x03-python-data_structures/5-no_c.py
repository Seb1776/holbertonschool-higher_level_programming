#!/usr/bin/env python3


def no_c(my_string):
    i = 0
    res_text = my_string

    for c in my_string:
        if c is not None:
            current_c = ord(c)

            if current_c == 67 or current_c == 99:
                c = ''

            res_text[i] = chr(current_c)
            i += 1
    
    return res_text
