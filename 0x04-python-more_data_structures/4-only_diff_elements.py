#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    lst_set_1 = set(set_1)
    differ = lst_set_1.symmetric_difference(set_2)
    return differ
