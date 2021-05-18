#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    y = 0

    try:
        for y in range(x):
            print('{:d}'.format(my_list[y]), end='')

        print()

        return(x)

    except (TypeError, IndexError):
        print()
        return (y)
