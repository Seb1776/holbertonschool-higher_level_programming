#!/usr/bin/python3


def common_elements(set_1, set_2):
    lst_set_1 = set(set_1)
    intersect = lst_set_1.intersection(set_2)
    return intersect
