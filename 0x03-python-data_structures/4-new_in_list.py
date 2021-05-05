#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    newlist = my_list[:]
    listlen = len(newlist) - 1

    if idx < 0:
        return newlist

    elif idx > listlen:
        return newlist

    else:
        newlist[idx] = element
        return newlist
