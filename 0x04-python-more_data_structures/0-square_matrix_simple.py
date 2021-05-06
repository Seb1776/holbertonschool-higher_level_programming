#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    res = []

    for x in matrix:
        r = list(map(lambda y: y * y, x))
        res.append(r)

    return res
