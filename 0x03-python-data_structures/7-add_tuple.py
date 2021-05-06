#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_tup_a = len(tuple_a)
    len_tup_b = len(tuple_b)

    if len_tup_a >= 2 and len_tup_b >= 2:
        res_tup = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    elif len_tup_a == 1 and len_tup_b == 1:
        res_tup = ((tuple_a[0] + tuple_b[0]), (0 + 0))
    elif len_tup_a <= 0 and len_tup_b <= 0:
        res_tup = (0, 0)
    else:
        if len_tup_a == 1:
            res_tup = ((tuple_a[0] + tuple_b[0]), (0 + tuple_b[1]))
        elif len_tup_b == 1:
            res_tup = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
        elif len_tup_a == 0:
            res_tup = ((0 + tuple_b[0]), (0 + tuple_b[1]))
        elif len_tup_b == 0:
            res_tup = ((tuple_a[0] + 0), (tuple_a[1] + 0))

    return res_tup
