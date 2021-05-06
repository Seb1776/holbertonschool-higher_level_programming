#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    emp = ""

    for x in range(matrix_len):
        emp = ''
        for y in matrix[x]:
            print('{}{:d}'.format(emp, y), end='')
            emp = ' '
        print('')
